"""Main screen for Steps IDE."""

import os
from textual.screen import Screen
from textual.widgets import Header, Footer
from textual.containers import Horizontal, Vertical
from textual.binding import Binding
from pathlib import Path
from steps_ide.editor.steps_editor import StepsEditor
from steps_ide.editor.buffer_manager import BufferManager, Buffer
from steps_ide.app.widgets.status_bar import StatusBar
from steps_ide.app.widgets.tab_bar import TabBar, TabInfo
from steps_ide.app.widgets.file_browser import FileBrowser
from steps_ide.app.widgets.project_browser import ProjectBrowser
from steps_ide.app.widgets.terminal_panel import TerminalPanel
from steps_ide.app.screens.file_dialogs import OpenFileDialog, SaveFileDialog, ConfirmCloseDialog
from steps_ide.app.screens.project_dialogs import (
    NewProjectDialog, NewFloorDialog, NewStepDialog,
    create_project, create_floor, create_step
)
from steps_ide.app.screens.input_dialog import StepsInputDialog
from steps_ide.shared.config.session import SessionManager
import asyncio
from typing import Optional
import queue
import threading


class MainScreen(Screen):
    """The main screen of the application."""

    DEFAULT_CSS = """
    MainScreen {
        layout: vertical;
    }

    MainScreen #workspace {
        height: 1fr;
    }

    MainScreen #main-container {
        height: 1fr;
    }

    MainScreen #editor-container {
        width: 1fr;
    }
    """

    BINDINGS = [
        Binding("ctrl+o", "open_file", "Open", priority=True),
        Binding("ctrl+s", "save_file", "Save", priority=True),
        Binding("ctrl+t", "new_file", "New Tab", priority=True),
        Binding("ctrl+w", "close_buffer", "Close", priority=True),
        Binding("ctrl+b", "toggle_file_browser", "Browser", priority=True),
        Binding("f4", "toggle_project_browser", "Project", priority=True),
        Binding("ctrl+j", "toggle_terminal", "Terminal", priority=True),
        # Steps interpreter commands
        Binding("f5", "run_steps", "Run", priority=True),
        Binding("f6", "check_steps", "Check", priority=True),
        # Project operations (hidden from footer, accessible via command palette)
        Binding("ctrl+shift+n", "new_project", "New Project", show=False, priority=True),
        Binding("escape", "focus_editor", "Focus Editor", show=False, priority=True),
        # Tab navigation: ctrl+pagedown/pageup are standard in many editors
        Binding("ctrl+pagedown", "next_buffer", "Next Tab", show=False, priority=True),
        Binding("ctrl+pageup", "prev_buffer", "Prev Tab", show=False, priority=True),
        # F7/F8 as fallback for next/prev tab
        Binding("f8", "next_buffer", "Next Tab", show=False, priority=True),
        Binding("f7", "prev_buffer", "Prev Tab", show=False, priority=True),
        Binding("alt+1", "buffer_1", "Tab 1", show=False, priority=True),
        Binding("alt+2", "buffer_2", "Tab 2", show=False, priority=True),
        Binding("alt+3", "buffer_3", "Tab 3", show=False, priority=True),
        Binding("alt+4", "buffer_4", "Tab 4", show=False, priority=True),
        Binding("alt+5", "buffer_5", "Tab 5", show=False, priority=True),
        Binding("alt+6", "buffer_6", "Tab 6", show=False, priority=True),
        Binding("alt+7", "buffer_7", "Tab 7", show=False, priority=True),
        Binding("alt+8", "buffer_8", "Tab 8", show=False, priority=True),
        Binding("alt+9", "buffer_9", "Tab 9", show=False, priority=True),
        Binding("ctrl+q", "quit", "Quit", priority=True),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buffer_manager = BufferManager()
        self.session_manager = SessionManager()
        self._loading_buffer = True  # Start True to prevent marking as modified during initial setup

    def compose(self):
        yield Header()
        # Start file browser at the 'project' directory in the Steps project folder
        # This assumes the IDE is run from the Steps project root
        start_path = os.path.join(os.getcwd(), "projects")
        # Fall back to current directory if projects folder doesn't exist
        if not os.path.isdir(start_path):
            start_path = os.getcwd()
        with Vertical(id="workspace"):
            with Horizontal(id="main-container"):
                # File browser for general file access (toggle with Ctrl+B) - LEFT side
                yield FileBrowser(path=start_path, id="file-browser", classes="hidden")
                with Vertical(id="editor-container"):
                    yield TabBar(id="tab-bar")
                    yield StepsEditor(id="editor")
                # Project browser for Steps projects (toggle with F4) - RIGHT side
                yield ProjectBrowser(id="project-browser", classes="hidden")
            yield TerminalPanel(id="terminal-panel", classes="hidden")
            yield StatusBar(id="status-bar")
        yield Footer()

    def on_mount(self):
        # Try to restore session, or create initial buffer
        self._restore_session()
        if self.buffer_manager.buffer_count == 0:
            self._create_new_buffer()
        self.query_one(StepsEditor).focus()

        # Auto-detect and load Steps project from current directory
        self._auto_load_project()
        # Delay enabling change detection until after Textual finishes setup
        # Use set_timer to ensure this runs after all call_after_refresh callbacks
        self.set_timer(0.1, self._enable_change_detection)

    def _enable_change_detection(self):
        """Enable change detection after initial setup is complete."""
        self._loading_buffer = False
        # Reset any modified flags that may have been set during setup
        tab_bar = self.query_one(TabBar)
        for buffer in self.buffer_manager.get_all_buffers():
            if not buffer.path and buffer.content == "":
                # New empty buffer should not be marked as modified
                buffer.is_modified = False
                tab_bar.set_modified(buffer.id, False)

    def _create_new_buffer(self) -> Buffer:
        """Create a new buffer and add tab."""
        # Save current buffer content BEFORE creating new buffer
        self._save_current_buffer_state()

        buffer = self.buffer_manager.create_buffer()
        tab_bar = self.query_one(TabBar)
        tab_bar.add_tab(TabInfo(
            id=buffer.id,
            name=buffer.name,
            path=buffer.path,
            is_modified=buffer.is_modified,
        ))
        self._switch_to_buffer(buffer)
        return buffer

    def _save_current_buffer_state(self) -> None:
        """Save the current editor state to the active buffer."""
        current = self.buffer_manager.active_buffer
        if current:
            editor = self.query_one(StepsEditor)
            current.content = editor.text
            current.cursor_position = editor.selection.end

    def _switch_to_buffer(self, buffer: Buffer) -> None:
        """Switch editor to show the given buffer."""
        editor = self.query_one(StepsEditor)

        # Save current buffer state
        current = self.buffer_manager.active_buffer
        if current and current.id != buffer.id:
            current.content = editor.text
            current.cursor_position = editor.selection.end

        # Load new buffer - set flag to prevent marking as modified
        self._loading_buffer = True
        self.buffer_manager.set_active(buffer.id)
        editor.text = buffer.content
        # Set language from path if available, otherwise use buffer's language
        if buffer.path:
            editor.set_language_from_path(buffer.path)
        else:
            editor.language = buffer.language

        # Update UI
        tab_bar = self.query_one(TabBar)
        tab_bar.set_active(buffer.id)

        # Detect line ending from content
        line_ending = "CRLF" if "\r\n" in buffer.content else "LF"

        self.update_status_bar(
            path=str(buffer.path) if buffer.path else buffer.name,
            modified=buffer.is_modified,
            encoding="UTF-8",
            line_ending=line_ending
        )

        # Delay re-enabling change detection until after events are processed
        # Use set_timer to ensure this runs after all async TextArea events
        def finish_switch():
            self._loading_buffer = False
            # Ensure the buffer's modified state is correct in the UI
            tab_bar.set_modified(buffer.id, buffer.is_modified)
        self.set_timer(0.05, finish_switch)

    def action_new_file(self):
        self._create_new_buffer()

    def action_open_file(self):
        def open_file_callback(path: str | None):
            if path:
                # Save current buffer state BEFORE opening new file
                self._save_current_buffer_state()

                buffer = self.buffer_manager.open_file(path)
                if buffer:
                    tab_bar = self.query_one(TabBar)
                    # Check if tab already exists
                    if buffer.id not in tab_bar.get_tab_ids():
                        tab_bar.add_tab(TabInfo(
                            id=buffer.id,
                            name=buffer.name,
                            path=buffer.path,
                            is_modified=buffer.is_modified,
                        ))
                    self._switch_to_buffer(buffer)
                    self.notify(f"Opened {path}")
                else:
                    self.notify(f"Failed to open {path}", severity="error")

        self.app.push_screen(OpenFileDialog(), open_file_callback)

    def action_save_file(self):
        buffer = self.buffer_manager.active_buffer
        if not buffer:
            return

        if buffer.path:
            self._save_buffer(buffer, buffer.path)
        else:
            self.action_save_as()

    def action_save_as(self):
        def save_file_callback(path: str | None):
            if path:
                buffer = self.buffer_manager.active_buffer
                if buffer:
                    self._save_buffer(buffer, path)

        self.app.push_screen(SaveFileDialog(), save_file_callback)

    def _save_buffer(self, buffer: Buffer, path: str) -> None:
        """Save buffer to file."""
        editor = self.query_one(StepsEditor)
        buffer.content = editor.text

        if editor.save_file(path):
            buffer.path = path
            buffer.name = Path(path).name
            buffer.is_modified = False

            tab_bar = self.query_one(TabBar)
            tab_bar.update_tab_name(buffer.id, buffer.name, buffer.path)
            tab_bar.set_modified(buffer.id, False)
            self.update_status_bar(path=path, modified=False)
            self.notify(f"Saved {path}")

            # Refresh project browser if a Steps file was saved
            self._refresh_project_browser_if_steps_file(path)
        else:
            self.notify(f"Failed to save {path}", severity="error")

    def _refresh_project_browser_if_steps_file(self, path: str) -> None:
        """Refresh project browser if a .building, .floor, or .step file was saved."""
        if path.endswith(('.building', '.floor', '.step')):
            project_browser = self.query_one(ProjectBrowser)
            if project_browser.project_path:
                project_browser.load_project(project_browser.project_path)

    def action_close_buffer(self):
        buffer = self.buffer_manager.active_buffer
        if not buffer:
            return

        if buffer.is_modified:
            # Show confirmation dialog for unsaved changes
            def handle_close_response(response: str | None):
                if response == "save":
                    # Save then close
                    if buffer.path:
                        self._save_buffer(buffer, buffer.path)
                        self._do_close_buffer(buffer.id)
                    else:
                        # Need to save as first
                        def save_then_close(path: str | None):
                            if path:
                                self._save_buffer(buffer, path)
                                self._do_close_buffer(buffer.id)
                        self.app.push_screen(SaveFileDialog(), save_then_close)
                elif response == "discard":
                    # Close without saving
                    self._do_close_buffer(buffer.id)
                # "cancel" or None - do nothing

            self.app.push_screen(
                ConfirmCloseDialog(buffer.name),
                handle_close_response
            )
        else:
            self._do_close_buffer(buffer.id)

    def _do_close_buffer(self, buffer_id: str):
        """Actually close a buffer (after confirmation if needed)."""
        tab_bar = self.query_one(TabBar)
        tab_bar.remove_tab(buffer_id)
        self.buffer_manager.close_buffer(buffer_id)

        # Switch to another buffer or create new one
        if self.buffer_manager.active_buffer:
            self._switch_to_buffer(self.buffer_manager.active_buffer)
        else:
            self._create_new_buffer()


    def action_next_buffer(self):
        """Switch to next buffer."""
        next_id = self.buffer_manager.get_next_buffer_id()
        if next_id:
            self._save_current_buffer_state()
            buffer = self.buffer_manager.get_buffer(next_id)
            if buffer:
                self._switch_to_buffer(buffer)

    def action_prev_buffer(self):
        """Switch to previous buffer."""
        prev_id = self.buffer_manager.get_prev_buffer_id()
        if prev_id:
            self._save_current_buffer_state()
            buffer = self.buffer_manager.get_buffer(prev_id)
            if buffer:
                self._switch_to_buffer(buffer)

    def _jump_to_buffer(self, index: int):
        """Jump to buffer by index (0-based)."""
        buffer_id = self.buffer_manager.get_buffer_by_index(index)
        if buffer_id:
            self._save_current_buffer_state()
            buffer = self.buffer_manager.get_buffer(buffer_id)
            if buffer:
                self._switch_to_buffer(buffer)

    def action_buffer_1(self): self._jump_to_buffer(0)
    def action_buffer_2(self): self._jump_to_buffer(1)
    def action_buffer_3(self): self._jump_to_buffer(2)
    def action_buffer_4(self): self._jump_to_buffer(3)
    def action_buffer_5(self): self._jump_to_buffer(4)
    def action_buffer_6(self): self._jump_to_buffer(5)
    def action_buffer_7(self): self._jump_to_buffer(6)
    def action_buffer_8(self): self._jump_to_buffer(7)
    def action_buffer_9(self): self._jump_to_buffer(8)

    def action_quit(self):
        # Check for unsaved changes
        unsaved = [b for b in self.buffer_manager.get_all_buffers() if b.is_modified]
        if unsaved:
            self.notify(f"{len(unsaved)} unsaved buffer(s). Save before quitting.", severity="warning")
            return
        # Save session before quitting
        self._save_session()
        self.app.exit()

    def update_status_bar(
        self,
        path: str = None,
        modified: bool = None,
        encoding: str = None,
        line_ending: str = None
    ):
        status_bar = self.query_one(StatusBar)
        if path is not None:
            status_bar.file_path = path
        if modified is not None:
            status_bar.is_modified = modified
        if encoding is not None:
            status_bar.encoding = encoding
        if line_ending is not None:
            status_bar.line_ending = line_ending

    def on_text_area_changed(self, event):
        """Handle text changes - mark buffer as modified."""
        # Skip if we're loading a buffer (programmatic text change)
        if self._loading_buffer:
            return

        buffer = self.buffer_manager.active_buffer
        if buffer:
            buffer.is_modified = True
            tab_bar = self.query_one(TabBar)
            tab_bar.set_modified(buffer.id, True)
            self.update_status_bar(modified=True)

    def on_text_area_selection_changed(self, event):
        """Handle cursor movement."""
        status_bar = self.query_one(StatusBar)
        status_bar.cursor_position = event.selection.end

    def on_tab_bar_tab_selected(self, event: TabBar.TabSelected):
        """Handle tab selection from tab bar."""
        self._save_current_buffer_state()
        buffer = self.buffer_manager.get_buffer(event.tab_id)
        if buffer:
            self._switch_to_buffer(buffer)

    def _restore_session(self) -> None:
        """Restore the previous session (open files)."""
        session = self.session_manager.load_session()
        if not session or not session.open_files:
            return

        tab_bar = self.query_one(TabBar)
        active_buffer = None

        for i, file_path_str in enumerate(session.open_files):
            file_path = Path(file_path_str)
            if file_path.exists():
                buffer = self.buffer_manager.open_file(str(file_path))
                if buffer:
                    tab_bar.add_tab(TabInfo(
                        id=buffer.id,
                        name=buffer.name,
                        path=buffer.path,
                        is_modified=buffer.is_modified,
                    ))
                    # Track which buffer to activate
                    if i == session.active_tab_index:
                        active_buffer = buffer

        # Activate the correct buffer
        if active_buffer:
            self._switch_to_buffer(active_buffer)
        elif self.buffer_manager.buffer_count > 0:
            first = self.buffer_manager.get_all_buffers()[0]
            self._switch_to_buffer(first)

    def _save_session(self) -> None:
        """Save current session (open files) for restoration."""
        # Collect file paths from buffers that have paths (not Untitled)
        open_files = []
        active_index = 0
        buffers = self.buffer_manager.get_all_buffers()
        active_buffer = self.buffer_manager.active_buffer

        for i, buffer in enumerate(buffers):
            if buffer.path:
                open_files.append(str(buffer.path))
                if active_buffer and buffer.id == active_buffer.id:
                    active_index = len(open_files) - 1

        self.session_manager.save_session(open_files, active_index)

    def action_focus_editor(self):
        """Return focus to the editor."""
        self.query_one(StepsEditor).focus()

    def action_toggle_file_browser(self):
        """Toggle the file browser panel, or focus it if visible but not focused."""
        file_browser = self.query_one(FileBrowser)

        if file_browser.is_visible:
            # Check if file browser tree already has focus
            focused = self.app.focused
            tree = file_browser.query_one("#file-tree")
            if focused == tree:
                # Already focused on tree - hide it
                file_browser.hide()
                self.query_one(StepsEditor).focus()
            else:
                # Visible but not focused - focus the tree
                file_browser.focus_tree()
        else:
            # Not visible - show and focus
            file_browser.show()
            file_browser.focus_tree()

    def action_toggle_project_browser(self):
        """Toggle the project browser panel."""
        project_browser = self.query_one(ProjectBrowser)

        if project_browser.is_visible:
            focused = self.app.focused
            tree = project_browser.query_one("#project-tree")
            if focused == tree:
                project_browser.hide()
                self.query_one(StepsEditor).focus()
            else:
                project_browser.focus_tree()
        else:
            # Refresh project when showing browser
            if project_browser.project_path:
                project_browser.load_project(project_browser.project_path)
            project_browser.show()
            project_browser.focus_tree()

    def load_project(self, project_path: str) -> bool:
        """Load a Steps project into the project browser."""
        project_browser = self.query_one(ProjectBrowser)
        result = project_browser.load_project(project_path)
        if result:
            project_browser.show()
            # Open the building file by default
            if project_browser.project_structure:
                self._open_file(project_browser.project_structure.building_path)
        return result

    def _auto_load_project(self) -> None:
        """Auto-detect and load a Steps project from the current directory."""
        cwd = os.getcwd()
        # Check if current directory contains a .building file
        from pathlib import Path
        path = Path(cwd)
        building_files = list(path.glob("*.building"))
        if building_files:
            # Found a Steps project - load it silently (don't show browser automatically)
            project_browser = self.query_one(ProjectBrowser)
            project_browser.load_project(cwd)

    # Project browser is now display-only - no file selection handlers needed
    # Users should use the file browser to open files

    def _get_project_path(self) -> str | None:
        """Get the project path from the current file or project browser."""
        # First check if project browser has a loaded project
        project_browser = self.query_one(ProjectBrowser)
        if project_browser.project_structure:
            return os.path.dirname(project_browser.project_structure.building_path)

        # Otherwise, try to find project from current file
        buffer = self.buffer_manager.active_buffer
        if buffer and buffer.path:
            # Look for .building file in parent directories
            path = Path(buffer.path)
            for parent in [path.parent] + list(path.parents):
                building_files = list(parent.glob("*.building"))
                if building_files:
                    return str(parent)

        return None

    def action_run_steps(self):
        """Run the current Steps project (F5)."""
        project_path = self._get_project_path()
        if not project_path:
            self.notify("No Steps project found. Open a .building file or load a project.", severity="warning")
            return

        # Show terminal and run the project
        terminal = self.query_one(TerminalPanel)
        terminal.show()

        # Run the Steps interpreter (async)
        asyncio.create_task(self._run_steps_command(project_path, check_only=False))

    def action_check_steps(self):
        """Check the current Steps project for errors (F6)."""
        project_path = self._get_project_path()
        if not project_path:
            self.notify("No Steps project found. Open a .building file or load a project.", severity="warning")
            return

        # Show terminal and check the project
        terminal = self.query_one(TerminalPanel)
        terminal.show()

        # Run the Steps checker (async)
        asyncio.create_task(self._run_steps_command(project_path, check_only=True))

    async def _run_steps_command(self, project_path: str, check_only: bool = False):
        """Run or check a Steps project and display output in terminal."""
        terminal = self.query_one(TerminalPanel)

        try:
            from steps.loader import load_project
            from steps.interpreter import run_building
            from steps.errors import StepsError

            # Load the entire project (building + floors + steps)
            terminal.write_output(f"{'Checking' if check_only else 'Running'}: {Path(project_path).name}\n")
            terminal.write_output("-" * 40 + "\n")

            building, env, errors = load_project(Path(project_path))

            if errors:
                # Show loading errors
                for error in errors:
                    terminal.write_output(error.format() + "\n")
                return

            if building is None:
                terminal.write_output("Error: No building found in project.\n")
                return

            if check_only:
                terminal.write_output("✓ No syntax errors found.\n")
            else:
                # Run the interpreter with the loaded environment
                # Track the last output message for input prompts
                last_output = [""]

                # Override output handler to capture output
                def capture_output(message: str):
                    last_output[0] = message
                    terminal.write_output(message + "\n")

                env.output_handler = capture_output

                # Create separate queues for input requests and responses
                request_queue: queue.Queue = queue.Queue()
                response_queue: queue.Queue = queue.Queue()

                # Override input handler to request input via queue
                def handle_input() -> str:
                    # Put a request in the request queue
                    request_queue.put(last_output[0])
                    # Wait for the response in the response queue
                    return response_queue.get()

                env.input_handler = handle_input

                # Run the interpreter in a background thread
                result_holder = [None]
                error_holder = [None]

                def run_interpreter():
                    try:
                        result_holder[0] = run_building(building, env)
                    except Exception as e:
                        error_holder[0] = e

                interpreter_thread = threading.Thread(target=run_interpreter, daemon=True)
                interpreter_thread.start()

                # Process input requests from the queue
                while interpreter_thread.is_alive():
                    try:
                        # Check if there's an input request (non-blocking)
                        prompt = request_queue.get(timeout=0.1)

                        # Create a future to wait for the dialog result
                        input_future = asyncio.Future()

                        def on_input_received(user_input: str):
                            # Put the user's input in the response queue
                            response_queue.put(user_input)
                            input_future.set_result(user_input)

                        # Show input dialog with callback
                        self.app.push_screen(
                            StepsInputDialog(prompt if prompt else "Enter input:"),
                            on_input_received
                        )

                        # Wait for the dialog to be dismissed
                        await input_future

                    except queue.Empty:
                        # No input request yet, keep waiting
                        await asyncio.sleep(0.1)

                # Wait for thread to complete
                interpreter_thread.join(timeout=1.0)

                # Check for errors
                if error_holder[0]:
                    raise error_holder[0]

                result = result_holder[0]

                terminal.write_output("-" * 40 + "\n")

                if result and result.success:
                    terminal.write_output("✓ Execution complete.\n")
                elif result and result.error:
                    terminal.write_output(result.error.format() + "\n")

        except ImportError as e:
            terminal.write_output(f"Error: Steps interpreter not available: {e}\n")
        except Exception as e:
            terminal.write_output(f"Unexpected error: {str(e)}\n")
            import traceback
            error_trace = traceback.format_exc()
            terminal.write_output(error_trace)

            # Also write to a log file for easier viewing
            try:
                with open("steps_ide_error.log", "w") as f:
                    f.write("Steps IDE Error Log\n")
                    f.write("=" * 50 + "\n\n")
                    f.write(f"Error: {str(e)}\n\n")
                    f.write("Full Traceback:\n")
                    f.write(error_trace)
                terminal.write_output("\n[Error details written to steps_ide_error.log]\n")
            except:
                pass

    def action_new_project(self):
        """Show dialog to create a new Steps project."""
        def handle_result(result: dict | None):
            if result:
                try:
                    project_path = create_project(
                        result["name"],
                        result["location"],
                        result["description"]
                    )
                    # Load the new project in the project browser
                    self.load_project(project_path)
                    self.notify(f"Created project: {result['name']}")
                except Exception as e:
                    self.notify(f"Error creating project: {e}", severity="error")

        self.app.push_screen(NewProjectDialog(os.getcwd()), handle_result)

    def action_new_floor(self):
        """Show dialog to create a new floor in the current project."""
        project_path = self._get_project_path()
        if not project_path:
            self.notify("No project loaded. Create or open a project first.", severity="warning")
            return

        def handle_result(result: dict | None):
            if result:
                try:
                    floor_path = create_floor(result["name"], result["project_path"])
                    # Reload the project browser
                    project_browser = self.query_one(ProjectBrowser)
                    project_browser.load_project(project_path)
                    # Open the new floor file
                    floor_file = os.path.join(floor_path, f"{result['name']}.floor")
                    self._open_file(floor_file)
                    self.notify(f"Created floor: {result['name']}")
                except Exception as e:
                    self.notify(f"Error creating floor: {e}", severity="error")

        self.app.push_screen(NewFloorDialog(project_path), handle_result)

    def action_new_step(self):
        """Show dialog to create a new step in the current floor."""
        # Try to determine the current floor from the active file
        buffer = self.buffer_manager.active_buffer
        floor_path = None

        if buffer and buffer.path:
            path = Path(buffer.path)
            # Check if we're in a floor directory
            if path.suffix == ".floor":
                floor_path = str(path.parent)
            elif path.suffix == ".step":
                floor_path = str(path.parent)
            else:
                # Look for .floor file in parent
                for f in path.parent.glob("*.floor"):
                    floor_path = str(path.parent)
                    break

        if not floor_path:
            self.notify("No floor selected. Open a floor file first.", severity="warning")
            return

        def handle_result(result: dict | None):
            if result:
                try:
                    step_file = create_step(result["name"], result["floor_path"])
                    # Reload the project browser
                    project_path = self._get_project_path()
                    if project_path:
                        project_browser = self.query_one(ProjectBrowser)
                        project_browser.load_project(project_path)
                    # Open the new step file
                    self._open_file(step_file)
                    self.notify(f"Created step: {result['name']}")
                except Exception as e:
                    self.notify(f"Error creating step: {e}", severity="error")

        self.app.push_screen(NewStepDialog(floor_path), handle_result)

    def action_toggle_terminal(self):
        """Toggle the terminal panel, or focus it if visible but not focused."""
        terminal = self.query_one(TerminalPanel)

        if terminal.is_visible:
            # Check if terminal already has focus
            focused = self.app.focused
            terminal_has_focus = False
            if focused:
                try:
                    terminal_has_focus = terminal in focused.ancestors_with_self
                except Exception:
                    pass

            if terminal_has_focus:
                # Terminal is focused - hide it and return to editor
                terminal.hide()
                self.query_one(StepsEditor).focus()
            else:
                # Terminal is visible but not focused - just focus it
                terminal.focus_input()
        else:
            # Terminal is hidden - show it and focus
            terminal.show()
            terminal.focus_input()

    def on_key(self, event):
        """Handle global key events."""
        # Escape in terminal returns focus to editor
        if event.key == "escape":
            terminal = self.query_one(TerminalPanel)
            if terminal.is_visible:
                # Check if focus is in terminal
                try:
                    focused = self.app.focused
                    if focused and terminal in focused.ancestors_with_self:
                        self.query_one(StepsEditor).focus()
                        event.prevent_default()
                        event.stop()
                except Exception:
                    pass

    def on_file_browser_file_selected(self, event: FileBrowser.FileSelected):
        """Handle file selection from file browser."""
        path = event.path

        # If it's a .building file, load the project
        if path.endswith('.building'):
            project_dir = os.path.dirname(path)
            project_browser = self.query_one(ProjectBrowser)
            if project_browser.load_project(project_dir):
                project_browser.show()
                self.notify(f"Loaded project: {os.path.basename(project_dir)}")
            # Also open the building file in editor

        # Check if file is already open
        existing = self.buffer_manager.get_buffer_by_path(path)
        if existing:
            self._save_current_buffer_state()
            buffer = self.buffer_manager.get_buffer(existing)
            if buffer:
                self._switch_to_buffer(buffer)
        else:
            # Open new file
            buffer = self.buffer_manager.open_file(path)
            if buffer:
                tab_bar = self.query_one(TabBar)
                if buffer.id not in tab_bar.get_tab_ids():
                    tab_bar.add_tab(TabInfo(
                        id=buffer.id,
                        name=buffer.name,
                        path=buffer.path,
                        is_modified=buffer.is_modified,
                    ))
                self._switch_to_buffer(buffer)
        # Return focus to editor
        self.query_one(StepsEditor).focus()
