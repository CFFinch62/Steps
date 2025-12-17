# Steps IDE Specification

## Overview

The Steps IDE evolves from Only Code to provide a complete development environment for Steps programs. The key insight: **the file system IS the program structure**. The project browser doesn't just show files - it shows the building, floors, and steps that make up the program.

## Philosophy

From Only Code we inherit:
- "Only code already" - Get to work fast
- "It's only code" - No clutter, pure focus
- Terminal-native - Keyboard-first, runs anywhere
- Resource-light - Fast startup, low memory

For Steps we add:
- **Structure is visible** - The project browser shows building → floors → steps
- **Flow is visible** - Diagram view shows program flow
- **One file, one intent** - Each step is a separate file, enforced
- **Educational errors** - Every error teaches

## Architecture

### Evolved from Only Code

```
steps_ide/
├── steps_ide/
│   ├── __init__.py
│   ├── main.py                     # Entry point
│   ├── app/
│   │   ├── application.py          # StepsIDEApp (extends OnlyCodeApp)
│   │   └── screens/
│   │       ├── main_screen.py      # Main editing screen
│   │       ├── project_dialogs.py  # New/Open project
│   │       └── diagram_screen.py   # Flow diagram view
│   ├── editor/
│   │   ├── steps_editor.py         # Steps-aware editor (extends OnlyCodeEditor)
│   │   ├── buffer_manager.py       # Project-aware buffers
│   │   └── steps_highlighter.py    # Steps syntax highlighting
│   ├── panels/
│   │   ├── project_browser.py      # Building/Floor/Step tree (replaces FileBrowser)
│   │   ├── terminal_panel.py       # Reuse from Only Code
│   │   ├── output_panel.py         # Interpreter output
│   │   └── diagram_panel.py        # Visual flow diagram
│   ├── interpreter/                # The Steps interpreter
│   │   ├── lexer.py
│   │   ├── parser.py
│   │   ├── ast_nodes.py
│   │   ├── interpreter.py
│   │   ├── environment.py
│   │   ├── types.py
│   │   ├── builtins.py
│   │   ├── loader.py
│   │   └── errors.py
│   └── shared/
│       └── config/                 # Steps-specific config
├── tests/
└── pyproject.toml
```

### Key Differences from Only Code

| Only Code | Steps IDE |
|-----------|-----------|
| FileBrowser (general files) | ProjectBrowser (building/floor/step structure) |
| Any file type | Only .building, .floor, .step files |
| Generic syntax highlighting | Steps-specific highlighting |
| No execution | Integrated interpreter |
| File tabs | Step tabs (grouped by floor) |

## Project Browser

The ProjectBrowser replaces FileBrowser with a Steps-aware tree:

```
┌─ Project Browser ──────────────────────┐
│ 🏢 price_calculator                    │
│   📄 price_calculator.building         │
│   📁 calculations                      │
│     📋 calculations.floor              │
│     📝 calc_from_price_and_margin.step │
│     📝 calc_from_price_and_cost.step   │
│     📝 calc_from_margin_and_cost.step  │
│   📁 user_interaction                  │
│     📋 user_interaction.floor          │
│     📝 display_menu.step               │
│     📝 get_number_input.step           │
│     📝 route_calculation.step          │
└────────────────────────────────────────┘
```

### Icons

| Icon | Meaning |
|------|---------|
| 🏢 | Building (project root) |
| 📁 | Floor folder |
| 📋 | Floor definition file |
| 📝 | Step file |
| 📄 | Building file |

### Project Browser Behavior

- Opening a `.step` file opens it in the editor
- Opening a `.floor` file shows the floor's steps
- Opening the `.building` file shows the main program
- Right-click context menu:
  - New Step (in current floor)
  - New Floor
  - Rename
  - Delete
- Floors are collapsible

### Project Browser Widget

```python
class ProjectBrowser(Widget):
    """Steps project browser - shows building/floor/step structure."""
    
    class StepSelected(Message):
        """Sent when a step is selected for editing."""
        def __init__(self, path: str, floor: str, step: str):
            self.path = path
            self.floor = floor
            self.step = step
    
    class FloorSelected(Message):
        """Sent when a floor definition is selected."""
        def __init__(self, path: str, floor: str):
            self.path = path
            self.floor = floor
    
    class BuildingSelected(Message):
        """Sent when the building file is selected."""
        def __init__(self, path: str):
            self.path = path
    
    def __init__(self, project_path: str | None = None):
        self.project_path = project_path
        self.project_structure = None  # Loaded from interpreter.loader
    
    def load_project(self, path: str):
        """Load a Steps project and build the tree."""
        # Use the interpreter's loader to discover structure
        from steps_ide.interpreter.loader import load_project_structure
        self.project_structure = load_project_structure(path)
        self._build_tree()
    
    def _build_tree(self):
        """Build the tree widget from project structure."""
        # Creates nodes for building, floors, steps
        pass
    
    def action_new_step(self):
        """Create a new step in the currently selected floor."""
        pass
    
    def action_new_floor(self):
        """Create a new floor in the project."""
        pass
```

## Main Screen Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Steps IDE - price_calculator                                      [─][□][×] │
├─────────────────────────────────────────────────────────────────────────┤
│ calculations/calc_from_price_and_margin.step │ display_menu.step │ + │
├──────────────────────┬──────────────────────────────────────────────────┤
│ 🏢 price_calculator  │ step: calc_from_price_and_margin                │
│   📄 price_calc...   │     belongs to: calculations                    │
│   📁 calculations    │     expects: nothing                            │
│     📋 calculations  │     returns: results as table                   │
│     📝 calc_from_... │                                                 │
│     📝 calc_from_... │     declare:                                    │
│   📁 user_interac... │         price as number fixed                   │
│     📋 user_inter... │         margin as number fixed                  │
│     📝 display_me... │         profit as number                        │
│     📝 get_number... │                                                 │
│                      │     do:                                         │
│                      │         call get_number_input with "Price: "... │
│                      │                                                 │
├──────────────────────┴──────────────────────────────────────────────────┤
│ 📟 Terminal                                                             │
│ $ steps run .                                                           │
│ Console Price Calculator                                                │
│ Enter Price: _                                                          │
├─────────────────────────────────────────────────────────────────────────┤
│ calc_from_price_and_margin.step │ Ln 12, Col 8 │ Steps │ UTF-8         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Layout Components

1. **Header** - App title, project name
2. **Tab Bar** - Open files, grouped by floor
3. **Project Browser** (left) - Building/floor/step tree
4. **Editor** (center) - Steps code editor
5. **Terminal Panel** (bottom) - Run programs, see output
6. **Status Bar** - File info, position, language

## Steps-Aware Editor

The editor extends OnlyCodeEditor with Steps-specific features:

```python
class StepsEditor(OnlyCodeEditor):
    """Editor with Steps language awareness."""
    
    def __init__(self):
        super().__init__()
        self.language = "steps"  # Custom Steps syntax highlighting
    
    def validate_on_save(self, path: str) -> list[StepsError]:
        """Validate Steps syntax before saving."""
        from steps_ide.interpreter.parser import parse_step
        errors = parse_step(self.text, Path(path))
        return errors
    
    def get_step_structure(self) -> dict:
        """Extract structure for outline view."""
        # Returns: { name, belongs_to, expects, returns, risers }
        pass
```

### Syntax Highlighting

Steps needs custom syntax highlighting for:
- Keywords: `step`, `floor`, `building`, `riser`, `belongs to`, etc.
- Multi-word keywords: `storing result in`, `is greater than`, etc.
- Types: `number`, `text`, `boolean`, `list`, `table`
- Comments: `note:` and `note block:`

## Terminal Integration

The terminal panel is reused from Only Code with Steps-specific commands:

```
$ steps run .
Console Price Calculator
...

$ steps check .
✓ Project structure valid
✓ All steps parse correctly
✓ All step references resolve

$ steps diagram .
[Opens diagram view]
```

## Flow Diagram Panel

A new panel showing program flow:

```
┌─ Flow Diagram ──────────────────────────────────────────┐
│                                                         │
│  ┌─────────────────────┐                               │
│  │ price_calculator    │                               │
│  │ (building)          │                               │
│  └──────────┬──────────┘                               │
│             │                                           │
│             ▼                                           │
│  ┌─────────────────────┐                               │
│  │ display_menu        │                               │
│  └──────────┬──────────┘                               │
│             │                                           │
│             ▼                                           │
│  ┌─────────────────────┐                               │
│  │ route_calculation   │                               │
│  └──────────┬──────────┘                               │
│             │                                           │
│    ┌────────┼────────┐                                 │
│    ▼        ▼        ▼                                 │
│  ┌───┐   ┌───┐   ┌───┐                                │
│  │ 1 │   │ 2 │   │...│  (9 calculation steps)         │
│  └───┘   └───┘   └───┘                                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

Implementation uses ASCII art initially, could upgrade to graphical later.

## Keybindings

### Inherited from Only Code

| Key | Action |
|-----|--------|
| Ctrl+O | Open file |
| Ctrl+S | Save file |
| Ctrl+T | New tab |
| Ctrl+W | Close tab |
| Ctrl+B | Toggle project browser |
| Ctrl+J | Toggle terminal |
| Ctrl+P | Command palette |
| Escape | Focus editor |

### Steps-Specific

| Key | Action |
|-----|--------|
| F5 | Run project |
| F6 | Check project (validate) |
| F7 | Show flow diagram |
| Ctrl+N | New step (in current floor) |
| Ctrl+Shift+N | New floor |
| Ctrl+Shift+F | New project |

## Project Operations

### New Project

Creates the folder structure:

```
project_name/
├── project_name.building
└── main/
    └── main.floor
```

With starter content:

**project_name.building:**
```
building: project_name

    note: Your program starts here
    
    exit
```

**main/main.floor:**
```
floor: main

    note: Add your steps here
```

### New Floor

1. Prompts for floor name
2. Creates `floor_name/` directory
3. Creates `floor_name/floor_name.floor` with template
4. Refreshes project browser

### New Step

1. Prompts for step name
2. Determines current floor from selection or prompts
3. Creates `floor_name/step_name.step` with template:

```
step: step_name
    belongs to: floor_name
    expects: nothing
    returns: nothing

    do:
        note: Add your code here
```

4. Opens the new file in editor
5. Refreshes project browser

## Integration with Interpreter

The IDE integrates tightly with the Steps interpreter:

### Real-time Validation

As you type, the IDE:
1. Parses the current file
2. Shows syntax errors in the editor (squiggly lines)
3. Updates the outline view

### Project Validation

On save or explicit check:
1. Validates entire project structure
2. Checks all step references resolve
3. Reports errors in output panel

### Execution

Run button or F5:
1. Saves all modified files
2. Runs `steps run .` in terminal
3. Shows output in terminal panel
4. Highlights errors with links to source

## Configuration

Stored in `~/.config/steps/`:

```
~/.config/steps/
├── settings.json       # IDE settings
├── keybindings.json    # Custom keybindings
└── session.json        # Last open project, files
```

### settings.json

```json
{
    "editor": {
        "indent_width": 4,
        "show_line_numbers": true,
        "theme": "vscode_dark"
    },
    "project_browser": {
        "show_hidden": false,
        "sort_floors_alphabetically": true
    },
    "terminal": {
        "default_height": 12
    }
}
```

## Implementation Plan

### Phase 1: Core IDE Shell

1. Fork/copy Only Code as base
2. Rename to Steps IDE
3. Replace FileBrowser with ProjectBrowser (structure-aware)
4. Add Steps syntax highlighting
5. Basic project open/navigate

### Phase 2: Interpreter Integration

1. Integrate interpreter as library
2. Add validation on save
3. Add "Run" command
4. Show output in terminal panel

### Phase 3: Project Operations

1. New Project wizard
2. New Floor command
3. New Step command (with template)
4. Rename/delete with refactoring

### Phase 4: Flow Diagram

1. ASCII-art diagram generation
2. Diagram panel
3. Click-to-navigate from diagram

### Phase 5: Polish

1. Educational error display
2. Outline view (step structure)
3. Go to definition
4. Find all references

## Reuse from Only Code

| Component | Reuse Strategy |
|-----------|----------------|
| `application.py` | Extend `OnlyCodeApp` → `StepsIDEApp` |
| `main_screen.py` | Modify layout, replace file browser |
| `editor_widget.py` | Extend for Steps highlighting |
| `buffer_manager.py` | Add project awareness |
| `terminal_panel.py` | Reuse as-is |
| `tab_bar.py` | Reuse as-is |
| `status_bar.py` | Add Steps-specific info |
| `file_dialogs.py` | Adapt for project operations |
| Config loading | Reuse pattern, new config location |

## Success Criteria

1. **Project structure visible** - Browser shows building/floor/step hierarchy
2. **One step per file** - Enforced by IDE, no workarounds
3. **Real-time validation** - Errors shown as you type
4. **Integrated execution** - Run and see output without leaving IDE
5. **Flow visualization** - Diagram shows program structure
6. **Educational errors** - Every error teaches how to fix it
7. **Keyboard-first** - Everything accessible without mouse
