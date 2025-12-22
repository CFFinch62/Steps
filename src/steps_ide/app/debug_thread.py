"""Debug Thread for Steps IDE.

Runs the Steps debugger in a separate thread to keep the UI responsive.
Handles communication between the UI (Main Window) and the DebugInterpreter.
"""

from pathlib import Path
import threading
from typing import Optional, Dict, Set
from PyQt6.QtCore import QThread, pyqtSignal, QObject

from steps.debug_state import DebugEvent, DebugMode
from steps.debugger import DebugInterpreter
from steps.environment import Environment
from steps.loader import load_project
from steps.ast_nodes import BuildingNode
from steps.errors import StepsError


class DebugThread(QThread):
    """Background thread for running the debugger."""
    
    # Signals
    debug_event = pyqtSignal(object)  # Emits DebugEvent
    finished_signal = pyqtSignal(bool, str)  # success, error_message
    output_signal = pyqtSignal(str)  # Emits output text
    input_request_signal = pyqtSignal(str)  # Emits prompt text
    
    def __init__(self, filepath: str, breakpoints: Dict[str, Set[int]], parent=None):
        """Initialize debug thread.
        
        Args:
            filepath: Path to the file/project to debug
            breakpoints: Initial breakpoints dict {filepath: {lines}}
            parent: Qt parent object
        """
        super().__init__(parent)
        self.filepath = Path(filepath)
        self.initial_breakpoints = breakpoints
        self._debugger: Optional[DebugInterpreter] = None
        self._is_running = False
        self._input_event = threading.Event() # Added for input handling
        self._input_response = "" # Added for input handling
        
    def run(self):
        """Execute the program with debugging."""
        self._is_running = True
        
        try:
            # 1. Load the project
            # Assuming filepath is inside a project, load from parent dir
            project_dir = self.filepath.parent
            building, env, errors = load_project(project_dir)
            
            if errors:
                error_msg = "\n".join(str(e) for e in errors)
                raise StepsError(f"Project load failed:\n{error_msg}")
            
            if not building:
                raise StepsError("No building definition found in project.")

            # 2. Environment is already setup by load_project
            # Redirect output and input
            env.output_handler = self.output_signal.emit
            env.input_handler = self._handle_input # Added for input handling
            
            # 3. Setup Debugger
            def on_event(event: DebugEvent):
                # This callback runs in the debug thread
                self.debug_event.emit(event)
            
            self._debugger = DebugInterpreter(env, on_event)
            
            # 4. Set Initial Breakpoints
            for path_str, lines in self.initial_breakpoints.items():
                path = Path(path_str)
                for line in lines:
                    self._debugger.add_breakpoint(path, line)
            
            # 5. Start Execution
            # Start in STEP_INTO mode to pause at start, or RUN to run to first breakpoint
            # Thonny usually pauses at start. Let's start with STEP_INTO so user sees entry.
            self._debugger.set_mode(DebugMode.STEP_INTO)
            
            result = self._debugger.run_building(building)
            
            self.finished_signal.emit(result.success, str(result.error) if result.error else "")
            
        except Exception as e:
            self.finished_signal.emit(False, str(e))
        finally:
            self._is_running = False
            self._debugger = None

    # Public slots for UI control
    
    def step_into(self):
        """Command debugger to step into."""
        if self._debugger:
            self._debugger.set_mode(DebugMode.STEP_INTO)
            self._debugger.resume()
    
    def step_over(self):
        """Command debugger to step over."""
        if self._debugger:
            self._debugger.set_mode(DebugMode.STEP_OVER)
            self._debugger.resume()
    
    def step_out(self):
        """Command debugger to step out."""
        if self._debugger:
            self._debugger.set_mode(DebugMode.STEP_OUT)
            self._debugger.resume()
    
    def continue_run(self):
        """Command debugger to continue execution."""
        if self._debugger:
            self._debugger.set_mode(DebugMode.RUN_TO_BREAKPOINT)
            self._debugger.resume()
    
    def stop(self):
        """Command debugger to stop."""
        self._running = False # Flag for loop
        self._input_event.set() # Unblock input wait if any
        if self._debugger:
            self._debugger.stop()
        # Thread will exit naturally after stop() unblocks run() loop
    
    def update_breakpoints(self, filepath: str, breakpoints: Set[int]):
        """Update breakpoints for a file during execution."""
        if not self._debugger:
            return
            
        path = Path(filepath)
        # Clear existing for this file (inefficient but safe)
        # Better: calculate diff. For now, simple approach.
        # Actually DebugInterpreter doesn't have "clear file breakpoints".
        # Let's iterate and remove unmatched, add new.
        
        # This is tricky because accessing specific file breakpoints in DebugInterpreter might need API
        # Implementation: for now just add all. 
        # TODO: Add remove_breakpoint logic if needed for runtime toggle.
        # Ideally DebugInterpreter should expose a way to manage easier.
        pass
        
    def add_breakpoint(self, filepath: str, line: int):
        """Add a dynamic breakpoint."""
        if self._debugger:
            self._debugger.add_breakpoint(Path(filepath), line)
            
    def remove_breakpoint(self, filepath: str, line: int):
        """Remove a dynamic breakpoint."""
        if self._debugger:
            self._debugger.remove_breakpoint(Path(filepath), line)

    def _handle_input(self, prompt: str = "") -> str:
        """Handle input request from environment."""
        self._input_event.clear()
        self.input_request_signal.emit(prompt)
        # Block until input is provided
        self._input_event.wait()
        return self._input_response

    def provide_input(self, text: str):
        """Provide input to the running program."""
        self._input_response = text
        self._input_event.set()
