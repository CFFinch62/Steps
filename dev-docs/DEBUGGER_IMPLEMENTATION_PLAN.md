# Stepping Debugger Implementation Plan for Steps IDE

A stepping debugger with variable tracking and display, inspired by Thonny IDE's pedagogical approach.

## Overview

The debugger will enable step-by-step execution of Steps programs with:
- **Step Into** - Execute one statement, entering function calls
- **Step Over** - Execute one statement, skipping over function internals
- **Step Out** - Complete current step/riser and return to caller
- **Breakpoints** - Pause at specific lines
- **Variable Display** - Real-time view of all variables by scope
- **Call Stack View** - Visual representation of step/riser call hierarchy

## Implementation Phases Checklist

### Phase 1: Core Debugger Engine ✅
- [x] Create `src/steps/debugger.py` with `DebugInterpreter` class
- [x] Add debug modes (step-into, step-over, step-out, run-to-breakpoint)
- [x] Create `DebugEvent` data structure for debugger events
- [x] Add breakpoint management (set, clear, list)

### Phase 2: Variable Tracking ✅
- [x] Extend `Environment` with variable change tracking
- [x] Create `VariableSnapshot` class for capturing state
- [x] Add call stack inspection methods

### Phase 3: IDE Debug UI
- [x] Create `DebugPanel` widget for debug controls
- [x] Create `VariablesView` widget for variable display
- [x] Create `CallStackView` widget
- [x] Add line highlighting in editor for current execution point

### Phase 4: Integration
- [x] Add debug commands to IDE menu and toolbar
- [x] Connect debug events to UI updates
- [x] Implement input handling during debug sessions

### Phase 5: Testing & Documentation
- [x] Add unit tests for debugger
- [ ] Add integration tests for debug UI
- [ ] Create debug mode documentation

---

## Design Decision: Execution Model

**Chosen approach: In-process debugging with threading**

Two approaches were considered:
1. **In-process debugging** (chosen): Run interpreter directly in IDE with callbacks. Simpler, full control, Thonny-like responsiveness.
2. **Subprocess debugging**: Run interpreter in separate process with IPC. More complex but isolates crashes.

The existing REPL already uses direct `Interpreter` calls, so in-process debugging is consistent with the codebase patterns.

---

## Proposed Changes

### Phase 1: Core Debugger Engine

#### [NEW] `src/steps/debugger.py`

The core debug interpreter extending `Interpreter` with stepping capabilities.

```python
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Callable, Dict, Set, Tuple, List, Any
import threading

from .interpreter import Interpreter
from .environment import Environment
from .errors import SourceLocation

@dataclass
class DebugEvent:
    """Event emitted during debugging."""
    event_type: str  # 'step', 'breakpoint', 'call', 'return', 'error'
    location: SourceLocation
    variables: Dict[str, Any]
    call_stack: List[str]

class DebugMode(Enum):
    STEP_INTO = "step_into"
    STEP_OVER = "step_over"  
    STEP_OUT = "step_out"
    RUN_TO_BREAKPOINT = "run"
    PAUSED = "paused"

class DebugInterpreter(Interpreter):
    """Interpreter with debugging capabilities."""
    
    def __init__(self, environment, on_debug_event: Callable[[DebugEvent], None]):
        super().__init__(environment)
        self.breakpoints: Set[Tuple[Path, int]] = set()
        self.debug_mode = DebugMode.PAUSED
        self._step_depth = 0  # For step-over logic
        self._on_debug_event = on_debug_event
        self._pause_event = threading.Event()
    
    def execute_statement(self, stmt):
        """Override to add debugging hooks."""
        # Check breakpoint or step condition
        if self._should_pause(stmt):
            self._emit_event('step', stmt.location)
            self._wait_for_resume()
        super().execute_statement(stmt)
    
    def call_step(self, step_name, arguments, location):
        """Override to track call stack depth."""
        self._step_depth += 1
        self._emit_event('call', location)
        result = super().call_step(step_name, arguments, location)
        self._step_depth -= 1
        self._emit_event('return', location)
        return result
    
    def _should_pause(self, stmt) -> bool:
        """Determine if execution should pause."""
        loc = stmt.location
        
        # Check breakpoints
        if (loc.file, loc.line) in self.breakpoints:
            return True
        
        # Check debug mode
        if self.debug_mode == DebugMode.STEP_INTO:
            return True
        elif self.debug_mode == DebugMode.STEP_OVER:
            return self._step_depth <= self._step_over_depth
        elif self.debug_mode == DebugMode.STEP_OUT:
            return self._step_depth < self._step_out_depth
        
        return False
    
    def _emit_event(self, event_type: str, location: SourceLocation):
        """Emit debug event to callback."""
        event = DebugEvent(
            event_type=event_type,
            location=location,
            variables=self.environment.get_all_variables_by_scope(),
            call_stack=self.environment.get_call_stack_info()
        )
        self._on_debug_event(event)
    
    def _wait_for_resume(self):
        """Block until resume signal."""
        self._pause_event.clear()
        self._pause_event.wait()
    
    def resume(self):
        """Resume execution."""
        self._pause_event.set()
    
    def set_mode(self, mode: DebugMode):
        """Set debug mode."""
        self.debug_mode = mode
        if mode == DebugMode.STEP_OVER:
            self._step_over_depth = self._step_depth
        elif mode == DebugMode.STEP_OUT:
            self._step_out_depth = self._step_depth
    
    def add_breakpoint(self, file: Path, line: int):
        """Add a breakpoint."""
        self.breakpoints.add((file, line))
    
    def remove_breakpoint(self, file: Path, line: int):
        """Remove a breakpoint."""
        self.breakpoints.discard((file, line))
    
    def stop(self):
        """Stop debugging."""
        self._running = False
        self._pause_event.set()  # Unblock if waiting
```

---

#### [MODIFY] `src/steps/interpreter.py`

Add hook points for subclass override (minimal changes).

```diff
 def execute_statement(self, stmt: StatementNode) -> None:
     """Execute a statement."""
+    self._pre_statement_hook(stmt)
     if isinstance(stmt, DisplayStatement):
         self._exec_display(stmt)
     # ... existing dispatch ...

+def _pre_statement_hook(self, stmt: StatementNode) -> None:
+    """Hook for debugger subclass. Override in DebugInterpreter."""
+    pass
```

---

### Phase 2: Variable Tracking

#### [NEW] `src/steps/debug_state.py`

Data structures for debug state snapshots.

```python
from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass
class VariableInfo:
    name: str
    value_type: str  # "number", "text", "boolean", "list", "table"
    value_repr: str  # Human-readable value
    is_changed: bool = False  # Highlight recently changed

@dataclass
class StackFrame:
    name: str  # Step or riser name
    file: Path
    line: int
    local_variables: List[VariableInfo]

@dataclass
class DebugSnapshot:
    current_file: Path
    current_line: int
    call_stack: List[StackFrame]
    global_variables: List[VariableInfo]
```

---

#### [MODIFY] `src/steps/environment.py`

Add methods for debugger introspection.

```diff
 class Environment:
+    def get_all_variables_by_scope(self) -> List[Dict[str, Tuple[str, Any]]]:
+        """Return variables organized by scope for debugger display."""
+        result = []
+        for scope in self._scope_stack:
+            scope_vars = {}
+            for name, value in scope.variables.items():
+                scope_vars[name] = (type(value).__name__, self._format_value(value))
+            result.append(scope_vars)
+        return result
+    
+    def get_call_stack_info(self) -> List[Dict[str, Any]]:
+        """Return structured call stack for debugger."""
+        return [
+            {'name': frame.name, 'file': str(frame.file), 'line': frame.line}
+            for frame in self._call_stack
+        ]
+    
+    def _format_value(self, value) -> str:
+        """Format value for debugger display."""
+        if hasattr(value, 'value'):
+            return str(value.value)
+        return str(value)
```

---

### Phase 3: IDE Debug UI

#### [NEW] `src/steps_ide/app/debug_panel.py`

Main debug control panel with toolbar buttons and views.

```python
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QTabWidget, QToolButton
)
from PyQt6.QtCore import pyqtSignal

class DebugPanel(QWidget):
    """Debug controls and variable/stack display."""
    
    step_into_clicked = pyqtSignal()
    step_over_clicked = pyqtSignal()
    step_out_clicked = pyqtSignal()
    continue_clicked = pyqtSignal()
    stop_clicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
    
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)
        
        # Toolbar with debug buttons
        toolbar = QHBoxLayout()
        
        self.continue_btn = self._make_button("▶", "Continue (F5)")
        self.continue_btn.clicked.connect(self.continue_clicked.emit)
        toolbar.addWidget(self.continue_btn)
        
        self.step_into_btn = self._make_button("⮕", "Step Into (F11)")
        self.step_into_btn.clicked.connect(self.step_into_clicked.emit)
        toolbar.addWidget(self.step_into_btn)
        
        self.step_over_btn = self._make_button("⮛", "Step Over (F10)")
        self.step_over_btn.clicked.connect(self.step_over_clicked.emit)
        toolbar.addWidget(self.step_over_btn)
        
        self.step_out_btn = self._make_button("⮝", "Step Out (Shift+F11)")
        self.step_out_btn.clicked.connect(self.step_out_clicked.emit)
        toolbar.addWidget(self.step_out_btn)
        
        self.stop_btn = self._make_button("■", "Stop (Shift+F5)")
        self.stop_btn.clicked.connect(self.stop_clicked.emit)
        toolbar.addWidget(self.stop_btn)
        
        toolbar.addStretch()
        layout.addLayout(toolbar)
        
        # Tab widget for Variables and Call Stack
        self.tabs = QTabWidget()
        
        from .widgets.variables_view import VariablesTreeView
        from .widgets.call_stack_view import CallStackListView
        
        self.variables_view = VariablesTreeView()
        self.call_stack_view = CallStackListView()
        
        self.tabs.addTab(self.variables_view, "Variables")
        self.tabs.addTab(self.call_stack_view, "Call Stack")
        
        layout.addWidget(self.tabs)
    
    def _make_button(self, text: str, tooltip: str) -> QToolButton:
        btn = QToolButton()
        btn.setText(text)
        btn.setToolTip(tooltip)
        btn.setMinimumSize(32, 32)
        return btn
    
    def set_enabled(self, enabled: bool):
        """Enable/disable debug controls."""
        self.continue_btn.setEnabled(enabled)
        self.step_into_btn.setEnabled(enabled)
        self.step_over_btn.setEnabled(enabled)
        self.step_out_btn.setEnabled(enabled)
        self.stop_btn.setEnabled(enabled)
```

---

#### [NEW] `src/steps_ide/app/widgets/variables_view.py`

Tree view for variables organized by scope.

```python
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt6.QtGui import QColor

class VariablesTreeView(QTreeWidget):
    """Display variables organized by scope."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHeaderLabels(["Name", "Value", "Type"])
        self.setColumnCount(3)
        self.setAlternatingRowColors(True)
        self.setColumnWidth(0, 120)
        self.setColumnWidth(1, 150)
    
    def update_variables(self, snapshot):
        """Update display from debug snapshot."""
        self.clear()
        
        # Global scope
        if snapshot.global_variables:
            global_item = QTreeWidgetItem(["Globals", "", ""])
            global_item.setExpanded(True)
            for var in snapshot.global_variables:
                item = QTreeWidgetItem([var.name, var.value_repr, var.value_type])
                if var.is_changed:
                    for col in range(3):
                        item.setBackground(col, QColor("#fff3cd"))
                global_item.addChild(item)
            self.addTopLevelItem(global_item)
        
        # Each stack frame's locals
        for frame in reversed(snapshot.call_stack):
            frame_item = QTreeWidgetItem([f"🗂 {frame.name}", "", ""])
            frame_item.setExpanded(True)
            for var in frame.local_variables:
                item = QTreeWidgetItem([var.name, var.value_repr, var.value_type])
                if var.is_changed:
                    for col in range(3):
                        item.setBackground(col, QColor("#fff3cd"))
                frame_item.addChild(item)
            self.addTopLevelItem(frame_item)
```

---

#### [NEW] `src/steps_ide/app/widgets/call_stack_view.py`

List view showing call stack frames.

```python
from PyQt6.QtWidgets import QListWidget, QListWidgetItem
from PyQt6.QtCore import pyqtSignal, Qt

class CallStackListView(QListWidget):
    """Display call stack as clickable list."""
    
    frame_selected = pyqtSignal(str, int)  # file, line
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.itemClicked.connect(self._on_item_clicked)
    
    def update_stack(self, call_stack):
        """Update from call stack."""
        self.clear()
        for frame in reversed(call_stack):
            text = f"{frame.name} at {frame.file.name}:{frame.line}"
            item = QListWidgetItem(text)
            item.setData(Qt.ItemDataRole.UserRole, (str(frame.file), frame.line))
            self.addItem(item)
    
    def _on_item_clicked(self, item):
        data = item.data(Qt.ItemDataRole.UserRole)
        if data:
            file, line = data
            self.frame_selected.emit(file, line)
```

---

#### [NEW] `src/steps_ide/app/debug_thread.py`

Threading support for running debugger without blocking UI.

```python
from pathlib import Path
from PyQt6.QtCore import QThread, pyqtSignal

class DebugThread(QThread):
    """Run debugger in background thread."""
    
    debug_event = pyqtSignal(object)  # DebugEvent
    finished_signal = pyqtSignal(bool, str)  # success, message
    
    def __init__(self, filepath: str, parent=None):
        super().__init__(parent)
        self.filepath = filepath
        self._debugger = None
        self._running = True
    
    def run(self):
        """Execute program with debugging."""
        try:
            from steps.loader import load_project
            from steps.debugger import DebugInterpreter
            from steps.environment import Environment
            
            project = load_project(Path(self.filepath).parent)
            env = Environment()
            
            def emit_event(event):
                self.debug_event.emit(event)
            
            self._debugger = DebugInterpreter(env, emit_event)
            result = self._debugger.run_building(project.building)
            
            self.finished_signal.emit(result.success, "")
        except Exception as e:
            self.finished_signal.emit(False, str(e))
    
    def step_into(self):
        if self._debugger:
            from steps.debugger import DebugMode
            self._debugger.set_mode(DebugMode.STEP_INTO)
            self._debugger.resume()
    
    def step_over(self):
        if self._debugger:
            from steps.debugger import DebugMode
            self._debugger.set_mode(DebugMode.STEP_OVER)
            self._debugger.resume()
    
    def step_out(self):
        if self._debugger:
            from steps.debugger import DebugMode
            self._debugger.set_mode(DebugMode.STEP_OUT)
            self._debugger.resume()
    
    def continue_run(self):
        if self._debugger:
            from steps.debugger import DebugMode
            self._debugger.set_mode(DebugMode.RUN_TO_BREAKPOINT)
            self._debugger.resume()
    
    def stop(self):
        self._running = False
        if self._debugger:
            self._debugger.stop()
```

---

#### [MODIFY] `src/steps_ide/app/editor.py`

Add debug line highlighting and breakpoint margin.

```diff
 class StepsCodeEditor(QPlainTextEdit):
+    breakpoint_toggled = pyqtSignal(int)  # line number
+    
+    def __init__(self, ...):
+        ...
+        self._current_debug_line = -1
+        self._breakpoints: Set[int] = set()
+    
+    def highlight_debug_line(self, line: int):
+        """Highlight the current execution line."""
+        self._current_debug_line = line
+        self._update_extra_selections()
+    
+    def clear_debug_highlight(self):
+        """Clear debug highlighting."""
+        self._current_debug_line = -1
+        self._update_extra_selections()
+    
+    def toggle_breakpoint(self, line: int):
+        """Toggle breakpoint on line."""
+        if line in self._breakpoints:
+            self._breakpoints.remove(line)
+        else:
+            self._breakpoints.add(line)
+        self.breakpoint_toggled.emit(line)
+        self.viewport().update()
+    
+    def get_breakpoints(self) -> Set[int]:
+        """Get all breakpoint line numbers."""
+        return self._breakpoints.copy()
+    
+    # In line number area paint event, add:
+    # - Red circles for breakpoints  
+    # - Yellow arrow for current debug line
```

---

#### [MODIFY] `src/steps_ide/app/main_window.py`

Add debug panel and menu items.

```diff
 class StepsIDEMainWindow(QMainWindow):
     def __init__(self, ...):
         ...
+        self.debug_panel = None
+        self._debug_session = None
+        self._debug_thread = None
     
     def _setup_ui(self):
         ...
+        # Add debug panel dock
+        from .debug_panel import DebugPanel
+        self.debug_panel = DebugPanel()
+        self.debug_dock = QDockWidget("Debug", self)
+        self.debug_dock.setWidget(self.debug_panel)
+        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.debug_dock)
+        self.debug_dock.hide()
+        
+        # Connect debug signals
+        self.debug_panel.step_into_clicked.connect(self._step_into)
+        self.debug_panel.step_over_clicked.connect(self._step_over)
+        self.debug_panel.step_out_clicked.connect(self._step_out)
+        self.debug_panel.continue_clicked.connect(self._continue_debug)
+        self.debug_panel.stop_clicked.connect(self._stop_debug)
     
     def _setup_menus(self):
         ...
+        # Debug menu
+        debug_menu = menubar.addMenu("&Debug")
+        debug_menu.addAction("Start Debugging", self._start_debug, "F5")
+        debug_menu.addAction("Step Into", self._step_into, "F11")
+        debug_menu.addAction("Step Over", self._step_over, "F10")
+        debug_menu.addAction("Step Out", self._step_out, "Shift+F11")
+        debug_menu.addSeparator()
+        debug_menu.addAction("Toggle Breakpoint", self._toggle_breakpoint, "F9")
+        debug_menu.addSeparator()
+        debug_menu.addAction("Stop Debugging", self._stop_debug, "Shift+F5")
+    
+    def _start_debug(self):
+        """Start debugging current project."""
+        filepath = self.editor_tabs.get_current_filepath()
+        if not filepath:
+            self.statusbar.showMessage("No file to debug", 3000)
+            return
+        
+        self.debug_dock.show()
+        self.debug_panel.set_enabled(True)
+        
+        from .debug_thread import DebugThread
+        self._debug_thread = DebugThread(filepath, self)
+        self._debug_thread.debug_event.connect(self._on_debug_event)
+        self._debug_thread.finished_signal.connect(self._on_debug_finished)
+        self._debug_thread.start()
+    
+    def _on_debug_event(self, event):
+        """Handle debug events from interpreter."""
+        # Highlight current line
+        self.editor_tabs.highlight_debug_line(str(event.location.file), event.location.line)
+        # Update variable display
+        self.debug_panel.variables_view.update_variables(event.snapshot)
+        self.debug_panel.call_stack_view.update_stack(event.call_stack)
+    
+    def _step_into(self):
+        if self._debug_thread:
+            self._debug_thread.step_into()
+    
+    def _step_over(self):
+        if self._debug_thread:
+            self._debug_thread.step_over()
+    
+    def _step_out(self):
+        if self._debug_thread:
+            self._debug_thread.step_out()
+    
+    def _continue_debug(self):
+        if self._debug_thread:
+            self._debug_thread.continue_run()
+    
+    def _stop_debug(self):
+        if self._debug_thread:
+            self._debug_thread.stop()
+            self._debug_thread = None
+        self.debug_dock.hide()
+        self.editor_tabs.clear_debug_highlight()
+    
+    def _toggle_breakpoint(self):
+        editor = self.editor_tabs.current_editor()
+        if editor:
+            cursor = editor.textCursor()
+            line = cursor.blockNumber() + 1
+            editor.toggle_breakpoint(line)
+    
+    def _on_debug_finished(self, success: bool, message: str):
+        self._stop_debug()
+        if not success and message:
+            self.statusbar.showMessage(f"Debug error: {message}", 5000)
```

---

## Verification Plan

### Automated Tests

Run existing tests to ensure no regressions:

```bash
cd /home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps
python -m pytest tests/ -v
```

Run new debugger tests:

```bash
python -m pytest tests/unit/test_debugger.py -v
```

### Manual Verification

1. **Basic Stepping Test**:
   - Launch IDE: `python -m steps_ide`
   - Open the `projects/hello_world/` project
   - Press F9 on line 2 to set a breakpoint
   - Press F5 to start debugging
   - Verify: Debug panel appears, execution pauses at breakpoint
   - Press F11 (Step Into) multiple times
   - Verify: Yellow arrow moves line by line

2. **Variable Display Test**:
   - Open `projects/price_calculator/` project
   - Start debugging with F5
   - Step through the program
   - Verify: Variables panel shows `price`, `quantity`, etc. with updating values

3. **Call Stack Test**:
   - In `price_calculator`, step into `calculate_subtotal` step
   - Verify: Call Stack panel shows both `price_calculator` (building) and `calculate_subtotal` (step)
   - Click on `price_calculator` in call stack
   - Verify: Editor jumps to calling location

---

## Files Summary

| File | Action | Purpose |
|------|--------|---------|
| `src/steps/debugger.py` | NEW | Core `DebugInterpreter` class |
| `src/steps/debug_state.py` | NEW | Data structures for debug snapshots |
| `src/steps/interpreter.py` | MODIFY | Add hook points for debugging |
| `src/steps/environment.py` | MODIFY | Add introspection methods |
| `src/steps_ide/app/debug_panel.py` | NEW | Debug controls widget |
| `src/steps_ide/app/widgets/variables_view.py` | NEW | Variable tree display |
| `src/steps_ide/app/widgets/call_stack_view.py` | NEW | Call stack display |
| `src/steps_ide/app/debug_thread.py` | NEW | Threading for background debugging |
| `src/steps_ide/app/editor.py` | MODIFY | Breakpoint/line highlighting |
| `src/steps_ide/app/main_window.py` | MODIFY | Debug menu and integration |
| `tests/unit/test_debugger.py` | NEW | Debugger unit tests |

---

## Implementation Order

1. **Core Engine First**: `debugger.py`, `debug_state.py`, interpreter hooks
2. **Environment Support**: Variable introspection methods
3. **UI Components**: Debug panel, variable view, call stack view (can develop independently)  
4. **Integration**: Connect UI to debugger via threading
5. **Testing**: Unit tests and manual verification

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| F5 | Start Debugging / Continue |
| Shift+F5 | Stop Debugging |
| F9 | Toggle Breakpoint |
| F10 | Step Over |
| F11 | Step Into |
| Shift+F11 | Step Out |
