# CHANGELOG - Phase 6: Steps IDE

## Overview
Phase 6 implements the Steps IDE, a full-featured development environment for the Steps programming language. The IDE is evolved from the Only Code TUI editor, adapted for Steps project development.

## Files Created

### Core IDE Package (`src/steps_ide/`)
- Copied from `Only_Code/onlycode/` with all imports renamed from `onlycode` → `steps_ide`
- `StepsIDEApp` replaces `OnlyCodeApp` as the main application class

### New Files
- `src/steps_ide/app/widgets/project_browser.py` - Steps project browser widget
- `src/steps_ide/editor/steps_editor.py` - Steps-aware editor extension
- `src/steps_ide/app/screens/project_dialogs.py` - Project operation dialogs

## Files Modified

### `src/steps_ide/app/application.py`
- Renamed class to `StepsIDEApp`
- Added command palette entries for Steps operations:
  - Steps: New Project
  - Steps: New Floor
  - Steps: New Step
  - Steps: Run Project (F5)
  - Steps: Check Syntax (F6)

### `src/steps_ide/app/screens/main_screen.py`
- Added ProjectBrowser widget to compose()
- Added keybindings:
  - `Ctrl+Shift+P` - Toggle project browser
  - `F5` - Run Steps project
  - `F6` - Check Steps syntax
  - `Ctrl+Shift+N` - New project
- Added action methods:
  - `action_toggle_project_browser()`
  - `action_run_steps()`
  - `action_check_steps()`
  - `action_new_project()`
  - `action_new_floor()`
  - `action_new_step()`
- Added message handlers for ProjectBrowser events

### `src/steps_ide/app/widgets/terminal_panel.py`
- Added `write_output()` method for programmatic output
- Added `clear_output()` method

### `src/steps_ide/editor/buffer_manager.py`
- Added Steps file extensions to language map:
  - `.building` → Python (for syntax highlighting)
  - `.floor` → Python
  - `.step` → Python

### `src/steps_ide/editor/__init__.py`
- Added export for `StepsEditor`

## Features Implemented

### Phase 6.1: Core IDE Shell ✅
- Copied Only Code to `src/steps_ide/`
- Renamed all imports and classes
- Verified IDE launches correctly

### Phase 6.2: Project Browser ✅
- `ProjectBrowser` widget with tree visualization
- `ProjectStructure`, `FloorInfo`, `StepInfo` dataclasses
- `load_project_structure()` function
- Messages: `StepSelected`, `FloorSelected`, `BuildingSelected`
- Toggle with `Ctrl+Shift+P`

### Phase 6.3: Steps Editor ✅
- `StepsEditor` class extending `OnlyCodeEditor`
- Steps file detection (`.building`, `.floor`, `.step`)
- Validation integration with Steps lexer/parser
- `get_steps_context()` for context-aware features

### Phase 6.4: Interpreter Integration ✅
- F5 (Run) and F6 (Check) keybindings
- Project path detection from file or project browser
- Output to terminal panel with error formatting
- Uses existing `src/steps/` interpreter modules

### Phase 6.5: Project Operations ✅
- `NewProjectDialog` - Create new Steps project
- `NewFloorDialog` - Create new floor in project
- `NewStepDialog` - Create new step in floor
- Helper functions: `create_project()`, `create_floor()`, `create_step()`
- Command palette integration

### Phase 6.6: Output Panel & Polish ✅
- Terminal panel serves as output panel
- Command palette entries for all Steps operations
- Educational error display with hints

## Usage

### Launch the IDE
```bash
python -m steps_ide.main
```

### Keyboard Shortcuts
| Key | Action |
|-----|--------|
| Ctrl+O | Open file |
| Ctrl+S | Save file |
| Ctrl+B | Toggle file browser |
| Ctrl+Shift+P | Toggle project browser |
| Ctrl+J | Toggle terminal |
| F5 | Run Steps project |
| F6 | Check Steps syntax |
| Ctrl+Shift+N | New project |
| Ctrl+P | Command palette |

### Command Palette (Ctrl+P)
- Steps: New Project
- Steps: New Floor
- Steps: New Step
- Steps: Run Project (F5)
- Steps: Check Syntax (F6)

## Test Results
- All 364 tests pass
- IDE launches and runs correctly
- Project operations create valid Steps files

## Dependencies
- textual (TUI framework)
- watchfiles (file watching)
- Existing Steps interpreter (`src/steps/`)

## Next Steps
Phase 7: Packaging & Documentation
- Update README.md
- Create USER_GUIDE.md
- Package for PyPI

