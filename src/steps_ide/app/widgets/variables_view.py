"""Variables Tree View Widget for Steps IDE Debugger.

Displays variables organized by scope in a tree structure with:
- Globals at root level
- Each stack frame's local variables
- Value change highlighting
"""

from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt6.QtGui import QColor, QBrush
from PyQt6.QtCore import Qt

from steps.debug_state import DebugSnapshot, VariableInfo


class VariablesTreeView(QTreeWidget):
    """Tree view displaying variables organized by scope."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHeaderLabels(["Name", "Value", "Type"])
        self.setColumnCount(3)
        self.setAlternatingRowColors(True)
        self.setIndentation(16)
        
        # Set column widths
        self.setColumnWidth(0, 120)
        self.setColumnWidth(1, 180)
        self.setColumnWidth(2, 70)
        
        # Use object name for any theme-specific styling
        self.setObjectName("variablesTree")
    
    def update_from_snapshot(self, snapshot: DebugSnapshot):
        """Update display from debug snapshot."""
        self.clear()
        
        # Global scope variables
        if snapshot.global_variables:
            global_item = QTreeWidgetItem(["🌐 Globals", "", ""])
            self.addTopLevelItem(global_item)  # Add to tree FIRST
            self._add_variables(global_item, snapshot.global_variables)
            global_item.setExpanded(True)  # Expand AFTER children added
        
        # Each stack frame's local variables (deepest first)
        for frame in reversed(snapshot.call_stack):
            if frame.local_variables:
                frame_item = QTreeWidgetItem([f"📦 {frame.name}", "", ""])
                self.addTopLevelItem(frame_item)  # Add to tree FIRST
                self._add_variables(frame_item, frame.local_variables)
                frame_item.setExpanded(True)  # Expand AFTER children added
    
    def _add_variables(self, parent_item: QTreeWidgetItem, variables: list):
        """Add variable items to a parent item."""
        default_color = QColor("#d4d4d4")  # Light gray text
        
        for var in variables:
            # Create item with parent directly
            item = QTreeWidgetItem(parent_item)
            item.setText(0, var.name)
            item.setText(1, var.value_repr)
            item.setText(2, var.value_type)
            
            # Set explicit text colors for visibility
            item.setForeground(0, QBrush(default_color))  # Name column
            item.setForeground(2, QBrush(default_color))  # Type column
            
            # Highlight changed values with visible colors
            if var.is_changed:
                changed_bg = QColor("#2d5a27")  # Dark green background
                changed_fg = QColor("#90EE90")  # Light green text
                for col in range(3):
                    item.setBackground(col, QBrush(changed_bg))
                    item.setForeground(col, QBrush(changed_fg))
            else:
                # Color-code value by type
                type_color = self._get_type_color(var.value_type)
                item.setForeground(1, QBrush(type_color))
    
    def _get_type_color(self, value_type: str) -> QColor:
        """Get display color for a value type."""
        colors = {
            "number": QColor("#b5cea8"),    # Green-ish
            "text": QColor("#ce9178"),       # Orange-ish
            "boolean": QColor("#569cd6"),    # Blue
            "list": QColor("#dcdcaa"),       # Yellow
            "table": QColor("#c586c0"),      # Purple
            "nothing": QColor("#808080"),    # Gray
        }
        return colors.get(value_type, QColor("#d4d4d4"))
