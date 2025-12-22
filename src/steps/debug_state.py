"""Debug State Data Structures for Steps Debugger.

This module defines data structures for capturing and communicating
debugger state, including variable snapshots, stack frames, and debug events.
"""

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Set


class DebugMode(Enum):
    """Debug execution modes."""
    STEP_INTO = "step_into"      # Pause at every statement
    STEP_OVER = "step_over"      # Pause at next statement, skip step internals
    STEP_OUT = "step_out"        # Pause after returning from current step
    RUN_TO_BREAKPOINT = "run"    # Run until breakpoint or end
    PAUSED = "paused"            # Execution paused, waiting for command


@dataclass
class VariableInfo:
    """Information about a single variable for debugger display.
    
    Attributes:
        name: Variable name
        value_type: Type name ("number", "text", "boolean", "list", "table", "nothing")
        value_repr: Human-readable string representation of value
        is_changed: True if value changed since last pause (for highlighting)
    """
    name: str
    value_type: str
    value_repr: str
    is_changed: bool = False


@dataclass
class StackFrame:
    """Information about a single call stack frame.
    
    Attributes:
        name: Step or riser name (or "building" for entry point)
        file: Source file path
        line: Current line number in that file
        local_variables: Variables local to this frame
    """
    name: str
    file: Path
    line: int
    local_variables: List[VariableInfo] = field(default_factory=list)


@dataclass  
class DebugSnapshot:
    """Complete snapshot of debugger state at a pause point.
    
    Attributes:
        current_file: File containing current execution point
        current_line: Line number of current execution point
        call_stack: List of stack frames (deepest first)
        global_variables: Variables in the building/global scope
    """
    current_file: Path
    current_line: int
    call_stack: List[StackFrame] = field(default_factory=list)
    global_variables: List[VariableInfo] = field(default_factory=list)


@dataclass
class DebugEvent:
    """Event emitted by debugger during execution.
    
    Attributes:
        event_type: Type of event:
            - 'paused': Execution paused at a statement
            - 'call': Entering a step or riser
            - 'return': Returning from a step or riser  
            - 'breakpoint': Hit a breakpoint
            - 'error': Runtime error occurred
            - 'finished': Program completed
        snapshot: Current state snapshot
        message: Optional message (for errors, etc.)
    """
    event_type: str
    snapshot: DebugSnapshot
    message: Optional[str] = None


@dataclass
class Breakpoint:
    """A breakpoint definition.
    
    Attributes:
        file: Source file path
        line: Line number (1-indexed)
        enabled: Whether breakpoint is active
        condition: Optional condition expression (future feature)
    """
    file: Path
    line: int
    enabled: bool = True
    condition: Optional[str] = None
    
    def __hash__(self):
        return hash((self.file, self.line))
    
    def __eq__(self, other):
        if isinstance(other, Breakpoint):
            return self.file == other.file and self.line == other.line
        return False


# Type alias for debug event callback
DebugEventCallback = Callable[[DebugEvent], None]
