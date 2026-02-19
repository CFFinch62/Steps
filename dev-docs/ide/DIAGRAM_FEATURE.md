# Project Diagram Feature - Implementation Documentation

## Overview

The project diagram feature allows users to visualize the structure of their Steps programs as ASCII art diagrams directly within the IDE. This feature is available both from the command line and integrated into the IDE.

## User-Facing Features

### IDE Integration

**Access Methods:**
- **Keyboard Shortcut**: `Ctrl+D`
- **Menu**: View → Show Project Diagram

**Behavior:**
1. If a file is currently open, the IDE automatically detects the project by searching up the directory tree for a `.building` file
2. If no file is open, the IDE prompts the user to select a project folder
3. The diagram is displayed in a dedicated tab labeled "📊 {project_name} Diagram"
4. Only one diagram tab exists at a time - opening a new diagram reuses the existing tab

**DiagramViewer Features:**
- Read-only text display with monospace font
- Toolbar with "💾 Save Diagram As..." button to export diagrams
- Theme-aware styling that matches the IDE theme
- Font validation with warnings if the current font may not display diagrams correctly

### Command Line Usage

```bash
python -m steps.main diagram <path_to_project>
```

## Implementation Details

### Files Modified

1. **`src/steps_ide/app/editor.py`**
   - Added `DiagramViewer` class (QWidget-based viewer)
   - Added `validate_diagram_font()` utility function
   - Modified `EditorTabs.show_diagram()` to manage diagram tabs
   - Updated `set_theme()` and `refresh_settings()` to handle DiagramViewer widgets

2. **`src/steps_ide/app/main_window.py`**
   - Added "Show Project Diagram" menu item to View menu
   - Implemented `_show_diagram()` handler method

3. **`src/steps/diagram.py`**
   - Fixed emoji width handling (emojis take 2 character widths in monospace fonts)
   - Adjusted padding to ensure proper right-edge alignment

### Key Components

#### DiagramViewer Class

```python
class DiagramViewer(QWidget):
    """Read-only viewer for ASCII project diagrams"""
```

**Features:**
- Uses `QTextEdit` (not `QPlainTextEdit`) for better emoji rendering
- Disables line wrapping
- Tests multiple monospace fonts (Courier New, Courier, Consolas, Monaco)
- Provides save functionality via toolbar button
- Supports theme updates

#### Font Validation

```python
def validate_diagram_font(font: QFont) -> tuple[bool, str]:
    """Validate if a font is suitable for displaying ASCII diagrams"""
```

**Checks:**
- Verifies font is monospace using `QFontInfo.fixedPitch()`
- Tests Unicode box-drawing character support (┌, ─, │)
- Returns validation status and warning message

#### Diagram Tab Management

- Uses special key `"__diagram__"` in `EditorTabs.editors` dictionary
- Similar pattern to untitled files (`"__untitled_N__"`)
- Single tab policy: reuses existing diagram tab if present

### Project Detection Logic

1. **With open file**: Traverse up directory tree from current file's location
2. **Without open file**: Prompt user with `QFileDialog.getExistingDirectory()`
3. **Validation**: Verify selected folder contains a `.building` file

### Error Handling

- Font validation warnings (non-blocking)
- Project load errors with detailed messages
- Diagram generation exceptions with traceback

## Diagram Format

The diagrams use Unicode box-drawing characters and emojis:

**Characters:**
- Box drawing: `┌─┐│├┤└┘`
- Emojis: 🏢 (building), 📂 (floor), 🔷 (step), 📊 (diagram tab)
- Arrows: `▼` (flow direction)

**Structure:**
```
┌──────────────────────────────────────────────────┐
│ 🏢 BUILDING: project_name                        │
├──────────────────────────────────────────────────┤
│                                                  │
│  ┌────────────────────────────────────────────┐  │
│  │ 📂 FLOOR: floor_name                       │  │
│  ├────────────────────────────────────────────┤  │
│  │                                            │  │
│  │    ┌────────────────────────────────────┐  │  │
│  │    │ 🔷 step_name                       │  │  │
│  │    │   needs: param1, param2            │  │  │
│  │    │   returns: result                  │  │  │
│  │    └────────────────────────────────────┘  │  │
│  │                                            │  │
│  └────────────────────────────────────────────┘  │
│                                                  │
└──────────────────────────────────────────────────┘
```

## Font Recommendations

For best display results, recommend these monospace fonts:
- **Courier New** (best compatibility)
- **Courier**
- **Consolas**
- **Monaco**

## Testing

Test coverage includes:
- Font validation with various fonts
- Diagram generation from CLI
- IDE integration (manual testing)
- Theme switching with diagram tab open
- Multiple diagram generations (tab reuse)

## Future Enhancements

Potential improvements:
- Export to other formats (SVG, PNG)
- Interactive diagram (clickable elements to jump to code)
- Diagram customization options (colors, styles)
- Zoom controls for large projects

