"""Call Stack List View Widget for Steps IDE Debugger.

Displays the call stack as a clickable list where clicking
a frame navigates to that location in the editor.
"""

from PyQt6.QtWidgets import QListWidget, QListWidgetItem
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QColor, QIcon

from steps.debug_state import DebugSnapshot, StackFrame


class CallStackListView(QListWidget):
    """List view displaying the call stack."""
    
    # Emitted when user clicks a stack frame
    frame_selected = pyqtSignal(str, int)  # file path, line number
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.itemClicked.connect(self._on_item_clicked)
        
        # Use object name for any theme-specific styling
        self.setObjectName("callStackList")
    
    def update_from_snapshot(self, snapshot: DebugSnapshot):
        """Update display from debug snapshot."""
        self.clear()
        
        # Add current location at top (if not in a step)
        if not snapshot.call_stack:
            item = QListWidgetItem(
                f"▶ {snapshot.current_file.name}:{snapshot.current_line}"
            )
            item.setData(Qt.ItemDataRole.UserRole, (str(snapshot.current_file), snapshot.current_line))
            item.setForeground(QColor("#FFC107"))
            self.addItem(item)
        
        # Add stack frames (most recent first)
        for i, frame in enumerate(reversed(snapshot.call_stack)):
            is_top = (i == 0)
            prefix = "▶ " if is_top else "  "
            
            text = f"{prefix}{frame.name} at {frame.file.name}:{frame.line}"
            item = QListWidgetItem(text)
            item.setData(Qt.ItemDataRole.UserRole, (str(frame.file), frame.line))
            
            if is_top:
                item.setForeground(QColor("#FFC107"))  # Yellow for current
            
            self.addItem(item)
    
    def _on_item_clicked(self, item: QListWidgetItem):
        """Handle item click - emit frame selected signal."""
        data = item.data(Qt.ItemDataRole.UserRole)
        if data:
            file_path, line = data
            self.frame_selected.emit(file_path, line)
