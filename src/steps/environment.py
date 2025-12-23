"""Steps Environment - Scope and Registry Management.

The environment manages:
- Variable scopes (lexical scoping with a scope stack)
- Step registry (all defined steps)
- Floor registry (step organization)
- Current execution context
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING

from .types import StepsValue, StepsNothing
from .errors import StepsRuntimeError, SourceLocation, ErrorCode


@dataclass
class StepDefinition:
    """A registered step definition."""
    name: str
    belongs_to: str
    parameters: List[str]
    returns: Optional[str]
    body: Any  # List[StatementNode] - avoiding circular import
    risers: Dict[str, "RiserDefinition"] = field(default_factory=dict)
    file_path: Optional[Path] = None


@dataclass
class RiserDefinition:
    """A private helper function within a step."""
    name: str
    parameters: List[str]
    returns: Optional[str]
    declarations: Any  # List[DeclarationNode]
    body: Any  # List[StatementNode]


@dataclass
class FloorDefinition:
    """A registered floor definition."""
    name: str
    steps: List[str]
    file_path: Optional[Path] = None


class Scope:
    """A single scope containing variable bindings."""
    
    def __init__(self, parent: Optional["Scope"] = None):
        self.variables: Dict[str, StepsValue] = {}
        self.fixed_variables: set[str] = set()  # Variables that can't be reassigned
        self.parent = parent
    
    def get(self, name: str) -> Optional[StepsValue]:
        """Get a variable value, checking parent scopes."""
        if name in self.variables:
            return self.variables[name]
        if self.parent:
            return self.parent.get(name)
        return None
    
    def set(self, name: str, value: StepsValue, is_fixed: bool = False) -> None:
        """Set a variable in this scope."""
        self.variables[name] = value
        if is_fixed:
            self.fixed_variables.add(name)
    
    def is_fixed(self, name: str) -> bool:
        """Check if a variable is fixed (can't be reassigned)."""
        if name in self.fixed_variables:
            return True
        if self.parent:
            return self.parent.is_fixed(name)
        return False
    
    def exists_locally(self, name: str) -> bool:
        """Check if variable exists in this scope only (not parent)."""
        return name in self.variables
    
    def exists(self, name: str) -> bool:
        """Check if variable exists in this or any parent scope."""
        if name in self.variables:
            return True
        if self.parent:
            return self.parent.exists(name)
        return False


class Environment:
    """Runtime environment for Steps interpreter.
    
    Manages:
    - Scope stack for variable bindings
    - Step registry for defined steps
    - Floor registry for step organization
    - Execution context (current step, floor, etc.)
    """
    
    def __init__(self) -> None:
        """Initialize an empty environment."""
        self.scope_stack: List[Scope] = [Scope()]  # Global scope
        self.steps: Dict[str, StepDefinition] = {}
        self.floors: Dict[str, FloorDefinition] = {}
        self.building_name: str = ""
        
        # Execution context
        self.current_step: Optional[str] = None
        self.current_floor: Optional[str] = None
        # Call stack tracks (name, location) pairs for debugger
        self._call_stack_entries: List[tuple] = []  # List of (name, SourceLocation)
        
        # Input/output handlers (can be overridden for testing)
        self.input_handler: Callable[[], str] = input
        self.output_handler: Callable[[str], None] = lambda msg: print(msg, end='')
    
    # =========================================================================
    # Debugger Introspection Methods
    # =========================================================================
    
    def get_scope_variables(self, scope_index: int) -> Dict[str, Any]:
        """Get variables from a specific scope for debugger display.
        
        Args:
            scope_index: Index of scope (0 = global/building scope)
            
        Returns:
            Dictionary of variable name -> value
        """
        if scope_index < 0 or scope_index >= len(self.scope_stack):
            return {}
        
        scope = self.scope_stack[scope_index]
        return dict(scope.variables)
    
    def get_all_scope_variables(self) -> List[Dict[str, Any]]:
        """Get all variables organized by scope for debugger.
        
        Returns:
            List of scope dictionaries, index 0 is global scope
        """
        result = []
        for scope in self.scope_stack:
            result.append(dict(scope.variables))
        return result
    
    def get_call_stack(self) -> List[tuple]:
        """Get the call stack for debugger display.
        
        Returns:
            List of (step_name, SourceLocation) tuples
        """
        return list(self._call_stack_entries)
    
    @property
    def call_stack(self) -> List[str]:
        """Get call stack as list of names (backwards compatibility)."""
        return [name for name, _ in self._call_stack_entries]


    
    # =========================================================================
    # Scope Management
    # =========================================================================
    
    @property
    def current_scope(self) -> Scope:
        """Get the current (innermost) scope."""
        return self.scope_stack[-1]
    
    def push_scope(self) -> None:
        """Create a new scope (e.g., entering a block)."""
        new_scope = Scope(parent=self.current_scope)
        self.scope_stack.append(new_scope)
    
    def pop_scope(self) -> None:
        """Remove the current scope (e.g., leaving a block)."""
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()
    
    def get_variable(self, name: str, location: Optional[SourceLocation] = None) -> StepsValue:
        """Get a variable value from the current scope chain.
        
        Args:
            name: Variable name
            location: Source location for error messages
        
        Returns:
            The variable's value
        
        Raises:
            StepsRuntimeError: If variable doesn't exist
        """
        value = self.current_scope.get(name)
        if value is None:
            # Check if maybe it's a misspelling
            similar = self._find_similar_names(name)
            hint = ""
            if similar:
                hint = f"Did you mean '{similar[0]}'?"
            
            raise StepsRuntimeError(
                code=ErrorCode.E401,
                message=f"Variable '{name}' has not been defined yet.",
                file=location.file if location else Path("<unknown>"),
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint=hint or "Make sure to use 'set' to define variables before using them."
            )
        return value
    
    def set_variable(
        self, 
        name: str, 
        value: StepsValue, 
        location: Optional[SourceLocation] = None,
        is_declaration: bool = False,
        is_fixed: bool = False
    ) -> None:
        """Set a variable value.
        
        Args:
            name: Variable name
            value: Value to assign
            location: Source location for error messages
            is_declaration: Whether this is a new declaration
            is_fixed: Whether the variable should be immutable
        
        Raises:
            StepsRuntimeError: If trying to reassign a fixed variable
        """
        # Check if trying to reassign a fixed variable
        if not is_declaration and self.current_scope.is_fixed(name):
            raise StepsRuntimeError(
                code=ErrorCode.E403,
                message=f"Cannot change '{name}' because it was declared as 'fixed'.",
                file=location.file if location else Path("<unknown>"),
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint="Fixed variables cannot be reassigned after their initial value is set."
            )
        
        self.current_scope.set(name, value, is_fixed)
    
    def declare_variable(
        self,
        name: str,
        type_name: str,
        is_fixed: bool = False,
        location: Optional[SourceLocation] = None
    ) -> None:
        """Declare a variable with a default value based on type.
        
        Args:
            name: Variable name
            type_name: Type name (number, text, boolean, list, table)
            is_fixed: Whether the variable is immutable
            location: Source location for error messages
        """
        from .types import StepsNumber, StepsText, StepsBoolean, StepsList, StepsTable
        
        default_values = {
            "number": StepsNumber(0.0),
            "text": StepsText(""),
            "boolean": StepsBoolean(False),
            "list": StepsList([]),
            "table": StepsTable({}),
        }
        
        value = default_values.get(type_name, StepsNothing())
        self.current_scope.set(name, value, is_fixed)
    
    def _find_similar_names(self, name: str, max_results: int = 3) -> List[str]:
        """Find variable names similar to the given name (for suggestions)."""
        # Collect all variable names from scope chain
        all_names: set[str] = set()
        scope: Optional[Scope] = self.current_scope
        while scope is not None:
            all_names.update(scope.variables.keys())
            scope = scope.parent
        
        # Simple similarity: starts with same letter or contains the name
        similar = []
        for n in all_names:
            if n.lower().startswith(name[0].lower()) or name.lower() in n.lower():
                similar.append(n)
        
        return similar[:max_results]
    
    # =========================================================================
    # Step Registry
    # =========================================================================
    
    def register_step(self, step: StepDefinition) -> None:
        """Register a step definition."""
        self.steps[step.name] = step
    
    def get_step(self, name: str, location: Optional[SourceLocation] = None) -> StepDefinition:
        """Get a step definition by name.
        
        Raises:
            StepsRuntimeError: If step doesn't exist
        """
        if name not in self.steps:
            available = list(self.steps.keys())[:5]
            hint = ""
            if available:
                hint = f"Available steps: {', '.join(available)}"
            
            raise StepsRuntimeError(
                code=ErrorCode.E402,
                message=f"Step '{name}' has not been defined.",
                file=location.file if location else Path("<unknown>"),
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint=hint or "Make sure the step is defined and belongs to a floor in this building."
            )
        return self.steps[name]
    
    def step_exists(self, name: str) -> bool:
        """Check if a step is registered."""
        return name in self.steps
    
    # =========================================================================
    # Floor Registry
    # =========================================================================
    
    def register_floor(self, floor: FloorDefinition) -> None:
        """Register a floor definition."""
        self.floors[floor.name] = floor
    
    def get_floor(self, name: str) -> Optional[FloorDefinition]:
        """Get a floor definition by name."""
        return self.floors.get(name)
    
    # =========================================================================
    # Execution Context
    # =========================================================================
    
    def enter_step(self, step_name: str, location: Optional[SourceLocation] = None) -> None:
        """Mark entering a step (for call stack tracking).
        
        Args:
            step_name: Name of the step being entered
            location: Source location of the call (for debugger)
        """
        self._call_stack_entries.append((step_name, location))
        self.current_step = step_name
    
    def exit_step(self) -> None:
        """Mark exiting a step."""
        if self._call_stack_entries:
            self._call_stack_entries.pop()
        self.current_step = self._call_stack_entries[-1][0] if self._call_stack_entries else None
    
    def is_recursive(self, step_name: str, max_depth: int = 100) -> bool:
        """Check if calling step_name would create excessive recursion."""
        count = sum(1 for name, _ in self._call_stack_entries if name == step_name)
        return count >= max_depth
    
    def get_call_stack_string(self) -> str:
        """Get a formatted call stack for error messages."""
        if not self._call_stack_entries:
            return "(at top level)"
        return " → ".join(name for name, _ in self._call_stack_entries)
    
    # =========================================================================
    # I/O Operations
    # =========================================================================
    
    def read_input(self) -> str:
        """Read input from the user."""
        return self.input_handler()
    
    def write_output(self, message: str) -> None:
        """Write output to the user."""
        self.output_handler(message)
    
    # =========================================================================
    # Context Managers
    # =========================================================================
    
    def step_context(self, step_name: str, location: Optional[SourceLocation] = None) -> "StepContext":
        """Context manager for step execution.
        
        Args:
            step_name: Name of the step being entered
            location: Source location of the call (for debugger call stack)
        """
        return StepContext(self, step_name, location)


class StepContext:
    """Context manager for step execution scope."""

    def __init__(self, env: Environment, name: str, location: Optional[SourceLocation] = None) -> None:
        self.env = env
        self.name = name
        self.location = location

    def __enter__(self) -> "StepContext":
        self.env.push_scope()
        self.env.enter_step(self.name, self.location)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.env.exit_step()
        self.env.pop_scope()
