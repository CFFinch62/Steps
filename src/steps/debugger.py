"""Steps Debugger - Stepping Debugger for Steps Programs.

This module provides the DebugInterpreter class which extends the standard
Interpreter with debugging capabilities including:
- Step-into, step-over, step-out execution
- Breakpoint support
- Variable state snapshots
- Call stack tracking
"""

import threading
from pathlib import Path
from typing import Callable, Dict, List, Optional, Set, Any

from .interpreter import Interpreter, ExecutionResult
from .environment import Environment
from .errors import SourceLocation, StepsError
from .types import StepsValue, StepsNumber, StepsText, StepsBoolean, StepsList, StepsTable, StepsNothing
from .ast_nodes import StatementNode, BuildingNode

from .debug_state import (
    DebugMode, DebugEvent, DebugSnapshot, DebugEventCallback,
    VariableInfo, StackFrame, Breakpoint
)


class DebugInterpreter(Interpreter):
    """Interpreter with debugging capabilities.
    
    Extends the standard Interpreter to add:
    - Pausing at statements based on debug mode
    - Breakpoint checking
    - State snapshot generation
    - Threading support for IDE integration
    
    Usage:
        def on_event(event: DebugEvent):
            print(f"Paused at {event.snapshot.current_file}:{event.snapshot.current_line}")
        
        debugger = DebugInterpreter(Environment(), on_event)
        debugger.set_mode(DebugMode.STEP_INTO)
        result = debugger.run_building(building_ast)
    """
    
    def __init__(
        self, 
        environment: Optional[Environment] = None,
        on_debug_event: Optional[DebugEventCallback] = None
    ):
        """Initialize the debug interpreter.
        
        Args:
            environment: Optional pre-configured environment
            on_debug_event: Callback for debug events (required for debugging)
        """
        super().__init__(environment)
        
        self._on_debug_event = on_debug_event or (lambda e: None)
        self._debug_mode = DebugMode.PAUSED
        self._breakpoints: Set[Breakpoint] = set()
        
        # Depth tracking for step-over/step-out
        self._call_depth = 0
        self._step_over_depth = 0
        self._step_out_depth = 0
        
        # Threading support
        self._pause_event = threading.Event()
        self._stop_requested = False
        self._is_running = False
        
        # Track previous variable values for change detection
        self._previous_vars: Dict[str, str] = {}
        
        # Current location tracking
        self._current_location: Optional[SourceLocation] = None
    
    # =========================================================================
    # Debug Mode Control
    # =========================================================================
    
    def set_mode(self, mode: DebugMode) -> None:
        """Set the debug execution mode.
        
        Args:
            mode: The debug mode to use
        """
        self._debug_mode = mode
        
        if mode == DebugMode.STEP_OVER:
            self._step_over_depth = self._call_depth
        elif mode == DebugMode.STEP_OUT:
            self._step_out_depth = self._call_depth
    
    def get_mode(self) -> DebugMode:
        """Get the current debug mode."""
        return self._debug_mode
    
    def resume(self) -> None:
        """Resume execution after a pause."""
        self._pause_event.set()
    
    def stop(self) -> None:
        """Request stop of execution."""
        self._stop_requested = True
        self._pause_event.set()  # Unblock if waiting
    
    def is_running(self) -> bool:
        """Check if debugger is currently executing."""
        return self._is_running
    
    # =========================================================================
    # Breakpoint Management
    # =========================================================================
    
    def add_breakpoint(self, file: Path, line: int) -> None:
        """Add a breakpoint.
        
        Args:
            file: Source file path
            line: Line number (1-indexed)
        """
        bp = Breakpoint(file=file, line=line)
        self._breakpoints.add(bp)
    
    def remove_breakpoint(self, file: Path, line: int) -> None:
        """Remove a breakpoint.
        
        Args:
            file: Source file path  
            line: Line number
        """
        bp = Breakpoint(file=file, line=line)
        self._breakpoints.discard(bp)
    
    def clear_breakpoints(self) -> None:
        """Remove all breakpoints."""
        self._breakpoints.clear()
    
    def get_breakpoints(self) -> List[Breakpoint]:
        """Get all breakpoints."""
        return list(self._breakpoints)
    
    def has_breakpoint(self, file: Path, line: int) -> bool:
        """Check if there's a breakpoint at the given location."""
        for bp in self._breakpoints:
            if bp.file == file and bp.line == line and bp.enabled:
                return True
        return False
    
    # =========================================================================
    # Execution Override
    # =========================================================================
    
    def run_building(self, building: BuildingNode) -> ExecutionResult:
        """Execute a building with debugging support.
        
        Overrides parent to add debugging hooks.
        """
        self._is_running = True
        self._stop_requested = False
        self._call_depth = 0
        
        try:
            return super().run_building(building)
        finally:
            self._is_running = False
            # Emit finished event
            self._emit_event('finished')
    
    def execute_statement(self, stmt: StatementNode) -> None:
        """Execute a statement with debugging hooks.
        
        Overrides parent to add pause/breakpoint checking.
        """
        if self._stop_requested:
            return
        
        # Update current location
        self._current_location = stmt.location
        
        # Check if we should pause
        if self._should_pause(stmt):
            self._emit_event('paused')
            self._wait_for_resume()
            
            if self._stop_requested:
                return
        
        # Execute the statement
        super().execute_statement(stmt)
    
    def call_step(
        self, 
        step_name: str, 
        arguments: List[StepsValue],
        location: Optional[SourceLocation] = None
    ) -> StepsValue:
        """Call a step with debugging hooks.
        
        Overrides parent to track call depth.
        """
        if self._stop_requested:
            return StepsNothing()
        
        self._call_depth += 1
        self._emit_event('call')
        
        try:
            result = super().call_step(step_name, arguments, location)
            return result
        finally:
            self._call_depth -= 1
            self._emit_event('return')
    
    # =========================================================================
    # Internal Debug Logic
    # =========================================================================
    
    def _should_pause(self, stmt: StatementNode) -> bool:
        """Determine if execution should pause at this statement.
        
        Args:
            stmt: The statement about to execute
            
        Returns:
            True if should pause, False to continue
        """
        loc = stmt.location
        
        # Always check breakpoints first
        if self.has_breakpoint(loc.file, loc.line):
            return True
        
        # Check based on debug mode
        if self._debug_mode == DebugMode.STEP_INTO:
            return True
            
        elif self._debug_mode == DebugMode.STEP_OVER:
            # Pause only if at same or lower call depth
            return self._call_depth <= self._step_over_depth
            
        elif self._debug_mode == DebugMode.STEP_OUT:
            # Pause only if at lower call depth (returned from step)
            return self._call_depth < self._step_out_depth
            
        elif self._debug_mode == DebugMode.RUN_TO_BREAKPOINT:
            # Only breakpoints cause pause (already checked above)
            return False
            
        elif self._debug_mode == DebugMode.PAUSED:
            # Already paused mode, wait for mode change
            return True
        
        return False
    
    def _wait_for_resume(self) -> None:
        """Block until resume() or stop() is called."""
        self._pause_event.clear()
        self._pause_event.wait()
    
    def _emit_event(self, event_type: str, message: Optional[str] = None) -> None:
        """Emit a debug event to the callback.
        
        Args:
            event_type: Type of event ('paused', 'call', 'return', 'finished', 'error')
            message: Optional message
        """
        snapshot = self._create_snapshot()
        event = DebugEvent(
            event_type=event_type,
            snapshot=snapshot,
            message=message
        )
        self._on_debug_event(event)
    
    def _create_snapshot(self) -> DebugSnapshot:
        """Create a snapshot of current debugger state.
        
        Returns:
            DebugSnapshot with current variables and call stack
        """
        # Get current location
        if self._current_location:
            current_file = self._current_location.file
            current_line = self._current_location.line
        else:
            current_file = Path("<unknown>")
            current_line = 0
        
        # Build call stack from environment
        call_stack = self._build_call_stack()
        
        # Get global (building-level) variables
        global_vars = self._get_scope_variables(0)
        
        return DebugSnapshot(
            current_file=current_file,
            current_line=current_line,
            call_stack=call_stack,
            global_variables=global_vars
        )
    
    def _build_call_stack(self) -> List[StackFrame]:
        """Build the call stack from environment state.
        
        Returns:
            List of StackFrame objects (deepest first)
        """
        frames = []
        
        # Get call stack info from environment
        stack_info = self.env.get_call_stack()
        
        for i, (name, location) in enumerate(stack_info):
            # Get local variables for this frame
            # Scope index aligns with call stack depth
            scope_idx = i + 1  # +1 because 0 is global scope
            local_vars = self._get_scope_variables(scope_idx)
            
            frame = StackFrame(
                name=name,
                file=location.file if location else Path("<unknown>"),
                line=location.line if location else 0,
                local_variables=local_vars
            )
            frames.append(frame)
        
        return frames
    
    def _get_scope_variables(self, scope_index: int) -> List[VariableInfo]:
        """Get variables from a specific scope.
        
        Args:
            scope_index: Index of scope (0 = global)
            
        Returns:
            List of VariableInfo for variables in that scope
        """
        try:
            scope_vars = self.env.get_scope_variables(scope_index)
        except (IndexError, AttributeError):
            return []
        
        result = []
        for name, value in scope_vars.items():
            type_name = self._get_type_name(value)
            value_repr = self._format_value(value)
            
            # Check if value changed
            key = f"{scope_index}:{name}"
            is_changed = self._previous_vars.get(key) != value_repr
            self._previous_vars[key] = value_repr
            
            result.append(VariableInfo(
                name=name,
                value_type=type_name,
                value_repr=value_repr,
                is_changed=is_changed
            ))
        
        return result
    
    def _get_type_name(self, value: StepsValue) -> str:
        """Get the Steps type name for a value."""
        if isinstance(value, StepsNumber):
            return "number"
        elif isinstance(value, StepsText):
            return "text"
        elif isinstance(value, StepsBoolean):
            return "boolean"
        elif isinstance(value, StepsList):
            return "list"
        elif isinstance(value, StepsTable):
            return "table"
        elif isinstance(value, StepsNothing):
            return "nothing"
        else:
            return "unknown"
    
    def _format_value(self, value: StepsValue) -> str:
        """Format a value for debugger display."""
        if isinstance(value, StepsNothing):
            return "nothing"
        elif isinstance(value, StepsText):
            # Show strings in quotes
            return f'"{value.value}"'
        elif isinstance(value, StepsBoolean):
            return "true" if value.value else "false"
        elif isinstance(value, StepsNumber):
            # Format nicely (no trailing .0 for integers)
            if value.value == int(value.value):
                return str(int(value.value))
            return str(value.value)
        elif isinstance(value, StepsList):
            if len(value.elements) <= 5:
                items = ", ".join(self._format_value(v) for v in value.elements)
                return f"[{items}]"
            else:
                items = ", ".join(self._format_value(v) for v in value.elements[:3])
                return f"[{items}, ... ({len(value.elements)} items)]"
        elif isinstance(value, StepsTable):
            if len(value.pairs) <= 3:
                pairs = ", ".join(
                    f'"{k}": {self._format_value(v)}' 
                    for k, v in value.pairs.items()
                )
                return f"[{pairs}]"
            else:
                pairs = ", ".join(
                    f'"{k}": {self._format_value(v)}' 
                    for k, v in list(value.pairs.items())[:2]
                )
                return f"[{pairs}, ... ({len(value.pairs)} entries)]"
        else:
            return str(value)
