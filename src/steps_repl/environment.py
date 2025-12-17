"""Simplified environment for REPL - single scope, no steps/floors."""

from pathlib import Path
from typing import Callable, Dict, List, Optional
from steps.types import StepsValue, StepsNothing
from steps.errors import StepsRuntimeError, ErrorCode, SourceLocation


class REPLEnvironment:
    """Single-scope environment for the REPL.

    Unlike the full interpreter environment, this has:
    - No floors or steps (can't define them in REPL)
    - No scope nesting (except temporary for if/loops)
    - No 'fixed' type enforcement
    - Variables created on first assignment
    """

    def __init__(self) -> None:
        self.variables: Dict[str, StepsValue] = {}
        self._temp_scopes: List[Dict[str, StepsValue]] = []
        # Required by Interpreter but not used in REPL
        self.steps: Dict[str, object] = {}
        self.floors: Dict[str, object] = {}
        self.call_stack: List[str] = []
        self.output_handler: Callable[[str], None] = print
        self.input_handler: Callable[[], str] = input
        self.current_step: Optional[str] = None
        self.current_floor: Optional[str] = None

    def get_variable(self, name: str, location: Optional[SourceLocation] = None) -> StepsValue:
        """Get a variable's value."""
        # Check temp scopes first (innermost to outermost)
        for scope in reversed(self._temp_scopes):
            if name in scope:
                return scope[name]

        # Check main scope
        if name in self.variables:
            return self.variables[name]

        # Special built-in: problem_message (defined but not used in REPL)
        if name == "problem_message":
            return StepsNothing()

        raise StepsRuntimeError(
            code=ErrorCode.E401,
            message=f"Variable '{name}' has not been defined.",
            file=Path("<repl>"),
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint=f"Try: set {name} to some_value"
        )
    
    def set(self, name: str, value: StepsValue) -> None:
        """Set a variable's value. Creates if doesn't exist."""
        # If in a temp scope, check there first
        if self._temp_scopes:
            # Check if it exists in temp scope
            for scope in reversed(self._temp_scopes):
                if name in scope:
                    scope[name] = value
                    return
            # Check if it exists in main scope
            if name in self.variables:
                self.variables[name] = value
                return
            # New variable - put in innermost temp scope
            self._temp_scopes[-1][name] = value
        else:
            # Not in temp scope - use main scope
            self.variables[name] = value
    
    def define(self, name: str, value: StepsValue, fixed: bool = False) -> None:
        """Define a variable (same as set in REPL - no fixed enforcement)."""
        self.set(name, value)
    
    def push_scope(self) -> None:
        """Push a temporary scope (for if/loop bodies)."""
        self._temp_scopes.append({})
    
    def pop_scope(self) -> None:
        """Pop a temporary scope."""
        if self._temp_scopes:
            self._temp_scopes.pop()
    
    def get_all_variables(self) -> Dict[str, StepsValue]:
        """Get all variables in main scope (for 'vars' command)."""
        return dict(self.variables)
    
    def clear(self) -> None:
        """Clear all variables."""
        self.variables.clear()
        self._temp_scopes.clear()
    
    # These methods exist to satisfy the interpreter interface but are no-ops in REPL
    
    def register_step(self, floor: str, step: object) -> None:
        """No-op in REPL - can't define steps."""
        pass
    
    def resolve_step(self, name: str, location: Optional[SourceLocation] = None) -> object:
        """No-op in REPL - can't call steps."""
        raise StepsRuntimeError(
            code=ErrorCode.E405,
            message=f"Cannot call step '{name}' in the REPL.",
            file=Path("<repl>"),
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="The REPL is for learning basics. Use the IDE to work with steps."
        )

    def push_call(self, name: str) -> None:
        """Push a call onto the call stack."""
        self.call_stack.append(name)
    
    def pop_call(self) -> None:
        """Pop a call from the call stack."""
        if self.call_stack:
            self.call_stack.pop()

    def set_variable(self, name: str, value: StepsValue, location: Optional[SourceLocation] = None) -> None:
        """Set a variable (wrapper for set method to match interpreter interface)."""
        self.set(name, value)

    def define_variable(self, name: str, value: StepsValue, fixed: bool = False,
                        location: Optional[SourceLocation] = None) -> None:
        """Define a variable (wrapper to match interpreter interface)."""
        self.define(name, value, fixed)

    def write_output(self, text: str) -> None:
        """Write output (display statement)."""
        self.output_handler(text)

    def read_input(self) -> str:
        """Read input from user."""
        return self.input_handler()

