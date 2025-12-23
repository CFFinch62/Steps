"""Debug Panel Widget for Steps IDE.

Provides the main debugging control interface including:
- Step controls (step into, step over, step out, continue, stop)
- Variables view (tree display of variables by scope)
- Call stack view (clickable list of stack frames)
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTabWidget,
    QToolButton, QSplitter, QLabel
)
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont

from steps.debug_state import DebugSnapshot


class DebugPanel(QWidget):
    """Debug controls and variable/stack display panel."""
    
    # Signals for debug actions
    step_into_clicked = pyqtSignal()
    step_over_clicked = pyqtSignal()
    step_out_clicked = pyqtSignal()
    continue_clicked = pyqtSignal()
    stop_clicked = pyqtSignal()
    
    # Signal for when user clicks a stack frame
    frame_selected = pyqtSignal(str, int)  # file, line
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
    
    def _setup_ui(self):
        """Set up the debug panel UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(4)
        
        # Status label
        self.status_label = QLabel("Ready to debug")
        self.status_label.setStyleSheet("color: #888; font-style: italic;")
        layout.addWidget(self.status_label)
        
        # Toolbar with debug buttons
        toolbar = QHBoxLayout()
        toolbar.setSpacing(2)
        
        self.continue_btn = self._make_button("▶", "Continue (F5)", "#4CAF50")
        self.continue_btn.clicked.connect(self.continue_clicked.emit)
        toolbar.addWidget(self.continue_btn)
        
        self.step_into_btn = self._make_button("↓", "Step Into (F11)", "#2196F3")
        self.step_into_btn.clicked.connect(self.step_into_clicked.emit)
        toolbar.addWidget(self.step_into_btn)
        
        self.step_over_btn = self._make_button("→", "Step Over (F10)", "#2196F3")
        self.step_over_btn.clicked.connect(self.step_over_clicked.emit)
        toolbar.addWidget(self.step_over_btn)
        
        self.step_out_btn = self._make_button("↑", "Step Out (Shift+F11)", "#2196F3")
        self.step_out_btn.clicked.connect(self.step_out_clicked.emit)
        toolbar.addWidget(self.step_out_btn)
        
        toolbar.addSpacing(10)
        
        self.stop_btn = self._make_button("■", "Stop (Shift+F5)", "#f44336")
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
        
        # Forward frame selection signal
        self.call_stack_view.frame_selected.connect(self.frame_selected.emit)
        
        self.tabs.addTab(self.variables_view, "Variables")
        self.tabs.addTab(self.call_stack_view, "Call Stack")
        
        layout.addWidget(self.tabs)
        
        # Start with controls disabled
        self._set_controls_enabled(False)
    
    def _make_button(self, text: str, tooltip: str, color: str = None) -> QToolButton:
        """Create a styled debug button."""
        btn = QToolButton()
        btn.setText(text)
        btn.setToolTip(tooltip)
        btn.setMinimumSize(32, 32)
        btn.setFont(QFont("", 14))
        
        # Only set the text color, let the theme handle background
        if color:
            btn.setStyleSheet(f"QToolButton {{ color: {color}; }}")
        
        return btn
    
    def _set_controls_enabled(self, enabled: bool):
        """Enable or disable step controls."""
        self.continue_btn.setEnabled(enabled)
        self.step_into_btn.setEnabled(enabled)
        self.step_over_btn.setEnabled(enabled)
        self.step_out_btn.setEnabled(enabled)
        self.stop_btn.setEnabled(enabled)
    
    def set_debugging_active(self, active: bool):
        """Set whether debugging is currently active."""
        self._set_controls_enabled(active)
        if active:
            self.status_label.setText("Debugging...")
            self.status_label.setStyleSheet("color: #4CAF50; font-weight: bold;")
        else:
            self.status_label.setText("Ready to debug")
            self.status_label.setStyleSheet("color: #888; font-style: italic;")
            self.variables_view.clear()
            self.call_stack_view.clear()
    
    def set_paused(self, paused: bool, location_text: str = ""):
        """Update UI for paused/running state."""
        if paused:
            self.status_label.setText(f"Paused at {location_text}")
            self.status_label.setStyleSheet("color: #FFC107; font-weight: bold;")
        else:
            self.status_label.setText("Running...")
            self.status_label.setStyleSheet("color: #4CAF50;")
    
    def update_from_snapshot(self, snapshot: DebugSnapshot):
        """Update displays from a debug snapshot."""
        # Update status
        location_text = f"{snapshot.current_file.name}:{snapshot.current_line}"
        self.set_paused(True, location_text)
        
        # Update variable view
        self.variables_view.update_from_snapshot(snapshot)
        
        # Update call stack view
        self.call_stack_view.update_from_snapshot(snapshot)
