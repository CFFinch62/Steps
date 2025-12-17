# Only Code Editor - File Browser Widget
from textual.widgets import DirectoryTree, Static, Input, Button, Label
from textual.containers import Vertical, ScrollableContainer, Horizontal
from textual.widget import Widget
from textual.reactive import reactive
from textual.message import Message
from textual.binding import Binding
from textual.screen import ModalScreen
from pathlib import Path
from typing import Iterable
import os
import shutil


class NewFolderDialog(ModalScreen[str]):
    """Dialog to create a new folder."""

    DEFAULT_CSS = """
    NewFolderDialog {
        align: center middle;
    }
    #dialog-container {
        width: 50;
        height: auto;
        border: solid $accent;
        background: $surface;
        padding: 1 2;
    }
    #message {
        margin: 1 0;
    }
    #folder-input {
        margin: 1 0;
    }
    #buttons {
        height: auto;
        align: center middle;
        margin-top: 1;
    }
    Button {
        margin: 0 1;
    }
    """

    def __init__(self, parent_path: str):
        super().__init__()
        self.parent_path = parent_path

    def compose(self):
        with Vertical(id="dialog-container"):
            yield Label(f"Create new folder in:", id="message")
            yield Label(self.parent_path, id="path-display")
            yield Input(placeholder="Folder name", id="folder-input")
            with Horizontal(id="buttons"):
                yield Button("Cancel", variant="default", id="cancel")
                yield Button("Create", variant="primary", id="create")

    def on_mount(self):
        self.query_one(Input).focus()

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "cancel":
            self.dismiss(None)
        elif event.button.id == "create":
            folder_name = self.query_one(Input).value.strip()
            if folder_name:
                self.dismiss(folder_name)


class DeleteFolderDialog(ModalScreen[bool]):
    """Dialog to confirm folder deletion."""

    DEFAULT_CSS = """
    DeleteFolderDialog {
        align: center middle;
    }
    #dialog-container {
        width: 60;
        height: auto;
        border: solid $accent;
        background: $surface;
        padding: 1 2;
    }
    #message {
        margin: 1 0;
        text-align: center;
    }
    #warning {
        margin: 1 0;
        text-align: center;
        color: $warning;
    }
    #buttons {
        height: auto;
        align: center middle;
        margin-top: 1;
    }
    Button {
        margin: 0 1;
    }
    """

    def __init__(self, folder_path: str):
        super().__init__()
        self.folder_path = folder_path

    def compose(self):
        with Vertical(id="dialog-container"):
            yield Label(f"Delete folder?", id="message")
            yield Label(self.folder_path, id="path-display")
            yield Label("⚠️  This action cannot be undone!", id="warning")
            with Horizontal(id="buttons"):
                yield Button("Cancel", variant="default", id="cancel")
                yield Button("Delete", variant="error", id="delete")

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "cancel":
            self.dismiss(False)
        elif event.button.id == "delete":
            self.dismiss(True)


class FilteredDirectoryTree(DirectoryTree):
    """DirectoryTree that hides hidden files (starting with .)"""

    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        """Filter out hidden files and directories."""
        return [p for p in paths if not p.name.startswith(".")]


class FileBrowser(Widget):
    """File browser panel with directory tree."""

    DEFAULT_CSS = """
    FileBrowser {
        width: 35;
        height: 100%;
        border-right: solid $primary;
        background: $surface;
    }

    FileBrowser.hidden {
        display: none;
    }

    FileBrowser #browser-header {
        dock: top;
        height: 1;
        background: $primary;
        color: $text;
        padding: 0 1;
    }

    FileBrowser #browser-path {
        dock: top;
        height: 1;
        background: $surface-darken-1;
        color: $text-muted;
        padding: 0 1;
        text-style: italic;
    }

    FileBrowser #tree-container {
        height: 1fr;
        overflow-x: auto;
        overflow-y: auto;
    }

    FileBrowser DirectoryTree {
        width: auto;
        min-width: 100%;
        scrollbar-gutter: stable;
    }
    """

    BINDINGS = [
        Binding("r", "refresh", "Refresh", show=False),
        Binding("n", "new_folder", "New Folder", show=False),
        Binding("delete", "delete_folder", "Delete", show=False),
    ]

    class FileSelected(Message):
        """Message sent when a file is selected."""
        def __init__(self, path: str):
            super().__init__()
            self.path = path

    class DirectoryChanged(Message):
        """Message sent when directory changes."""
        def __init__(self, path: str):
            super().__init__()
            self.path = path

    current_path = reactive("")

    def __init__(self, path: str | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Default to home directory if no path specified
        if path is None:
            path = str(Path.home())
        self.root_path = os.path.abspath(path)

    def compose(self):
        yield Static("📁 Files", id="browser-header")
        yield Static(self._get_short_path(), id="browser-path")
        with ScrollableContainer(id="tree-container"):
            yield FilteredDirectoryTree(self.root_path, id="file-tree")

    def _get_short_path(self) -> str:
        """Get shortened path for display (replace home with ~)."""
        path = self.root_path
        home = str(Path.home())
        if path.startswith(home):
            path = "~" + path[len(home):]
        # Truncate if too long
        if len(path) > 32:
            path = "..." + path[-29:]
        return path

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected):
        """Handle file selection - open in editor."""
        self.post_message(self.FileSelected(str(event.path)))

    def toggle(self):
        """Toggle visibility of the file browser."""
        self.toggle_class("hidden")
        return not self.has_class("hidden")

    def show(self):
        """Show the file browser."""
        self.remove_class("hidden")

    def hide(self):
        """Hide the file browser."""
        self.add_class("hidden")

    def focus_tree(self):
        """Focus the directory tree for keyboard navigation."""
        tree = self.query_one(FilteredDirectoryTree)
        tree.focus()

    @property
    def is_visible(self) -> bool:
        """Check if file browser is visible."""
        return not self.has_class("hidden")

    def set_root(self, path: str) -> None:
        """Change the root directory of the file browser."""
        self.root_path = os.path.abspath(path)
        # Update the path display
        path_label = self.query_one("#browser-path", Static)
        path_label.update(self._get_short_path())
        # Update the directory tree path (reactive property handles the rest)
        tree = self.query_one(FilteredDirectoryTree)
        tree.path = self.root_path

    def _get_current_directory(self) -> str:
        """Get the currently selected directory in the tree."""
        tree = self.query_one(FilteredDirectoryTree)
        if tree.cursor_node:
            cursor_path = Path(str(tree.cursor_node.data.path))
            if cursor_path.is_dir():
                return str(cursor_path)
            else:
                # If it's a file, return its parent directory
                return str(cursor_path.parent)
        # Fall back to root path
        return self.root_path

    def action_new_folder(self) -> None:
        """Create a new folder in the current directory."""
        parent_dir = self._get_current_directory()

        def handle_result(folder_name: str | None):
            if folder_name:
                new_folder_path = os.path.join(parent_dir, folder_name)
                try:
                    os.makedirs(new_folder_path, exist_ok=False)
                    # Refresh the tree to show the new folder
                    tree = self.query_one(FilteredDirectoryTree)
                    tree.reload()
                    self.app.notify(f"Created folder: {folder_name}")
                except FileExistsError:
                    self.app.notify(f"Folder already exists: {folder_name}", severity="error")
                except Exception as e:
                    self.app.notify(f"Error creating folder: {e}", severity="error")

        self.app.push_screen(NewFolderDialog(parent_dir), handle_result)

    def action_delete_folder(self) -> None:
        """Delete the currently selected folder."""
        tree = self.query_one(FilteredDirectoryTree)
        if not tree.cursor_node:
            self.app.notify("No folder selected", severity="warning")
            return

        cursor_path = Path(str(tree.cursor_node.data.path))

        # Only allow deleting directories
        if not cursor_path.is_dir():
            self.app.notify("Please select a folder to delete", severity="warning")
            return

        # Don't allow deleting the root path
        if str(cursor_path) == self.root_path:
            self.app.notify("Cannot delete the root directory", severity="error")
            return

        def handle_result(confirmed: bool):
            if confirmed:
                try:
                    shutil.rmtree(cursor_path)
                    # Refresh the tree
                    tree = self.query_one(FilteredDirectoryTree)
                    tree.reload()
                    self.app.notify(f"Deleted folder: {cursor_path.name}")
                except Exception as e:
                    self.app.notify(f"Error deleting folder: {e}", severity="error")

        self.app.push_screen(DeleteFolderDialog(str(cursor_path)), handle_result)

    def action_refresh(self) -> None:
        """Refresh the directory tree."""
        tree = self.query_one(FilteredDirectoryTree)
        tree.reload()

