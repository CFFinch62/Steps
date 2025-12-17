"""Project operation dialogs for Steps IDE.

Provides dialogs for:
- Creating new Steps projects
- Creating new floors
- Creating new steps
"""

from textual.screen import ModalScreen
from textual.widgets import Input, Button, Label, DirectoryTree
from textual.containers import Vertical, Horizontal
from pathlib import Path
import os


class NewProjectDialog(ModalScreen[dict | None]):
    """Dialog for creating a new Steps project."""

    DEFAULT_CSS = """
    NewProjectDialog {
        align: center middle;
    }
    #dialog-container {
        width: 60%;
        height: auto;
        max-height: 80%;
        border: solid $accent;
        background: $surface;
        padding: 1 2;
    }
    .dialog-title {
        text-style: bold;
        margin-bottom: 1;
    }
    .field-label {
        margin-top: 1;
    }
    Input {
        margin-bottom: 1;
    }
    #location-tree {
        height: 10;
        border: solid $secondary;
        margin-bottom: 1;
    }
    #buttons {
        height: auto;
        align: right middle;
        margin-top: 1;
    }
    Button {
        margin-left: 1;
    }
    """

    def __init__(self, initial_path: str | None = None):
        super().__init__()
        self.initial_path = initial_path or str(Path.home())

    def compose(self):
        with Vertical(id="dialog-container"):
            yield Label("New Steps Project", classes="dialog-title")
            yield Label("Project Name:", classes="field-label")
            yield Input(placeholder="my_project", id="project-name")
            yield Label("Location:", classes="field-label")
            yield DirectoryTree(self.initial_path, id="location-tree")
            yield Label("Description (optional):", classes="field-label")
            yield Input(placeholder="A Steps project", id="project-description")
            with Horizontal(id="buttons"):
                yield Button("Cancel", variant="error", id="cancel")
                yield Button("Create", variant="primary", id="create")

    def on_mount(self):
        self.query_one("#project-name", Input).focus()

    def on_directory_tree_directory_selected(self, event: DirectoryTree.DirectorySelected):
        """Track selected directory."""
        self.selected_dir = str(event.path)

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "cancel":
            self.dismiss(None)
        elif event.button.id == "create":
            name = self.query_one("#project-name", Input).value.strip()
            if not name:
                self.notify("Please enter a project name", severity="warning")
                return
            
            location = getattr(self, 'selected_dir', self.initial_path)
            description = self.query_one("#project-description", Input).value.strip()
            
            self.dismiss({
                "name": name,
                "location": location,
                "description": description or f"A Steps project: {name}",
            })


class NewFloorDialog(ModalScreen[dict | None]):
    """Dialog for creating a new floor in a Steps project."""

    DEFAULT_CSS = """
    NewFloorDialog {
        align: center middle;
    }
    #dialog-container {
        width: 50%;
        height: auto;
        border: solid $accent;
        background: $surface;
        padding: 1 2;
    }
    .dialog-title {
        text-style: bold;
        margin-bottom: 1;
    }
    .field-label {
        margin-top: 1;
    }
    Input {
        margin-bottom: 1;
    }
    #buttons {
        height: auto;
        align: right middle;
        margin-top: 1;
    }
    Button {
        margin-left: 1;
    }
    """

    def __init__(self, project_path: str):
        super().__init__()
        self.project_path = project_path

    def compose(self):
        with Vertical(id="dialog-container"):
            yield Label("New Floor", classes="dialog-title")
            yield Label(f"Project: {os.path.basename(self.project_path)}", classes="field-label")
            yield Label("Floor Name:", classes="field-label")
            yield Input(placeholder="calculations", id="floor-name")
            with Horizontal(id="buttons"):
                yield Button("Cancel", variant="error", id="cancel")
                yield Button("Create", variant="primary", id="create")

    def on_mount(self):
        self.query_one("#floor-name", Input).focus()

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "cancel":
            self.dismiss(None)
        elif event.button.id == "create":
            name = self.query_one("#floor-name", Input).value.strip()
            if not name:
                self.notify("Please enter a floor name", severity="warning")
                return
            self.dismiss({"name": name, "project_path": self.project_path})


class NewStepDialog(ModalScreen[dict | None]):
    """Dialog for creating a new step in a floor."""

    DEFAULT_CSS = """
    NewStepDialog {
        align: center middle;
    }
    #dialog-container {
        width: 50%;
        height: auto;
        border: solid $accent;
        background: $surface;
        padding: 1 2;
    }
    .dialog-title {
        text-style: bold;
        margin-bottom: 1;
    }
    .field-label {
        margin-top: 1;
    }
    Input {
        margin-bottom: 1;
    }
    #buttons {
        height: auto;
        align: right middle;
        margin-top: 1;
    }
    Button {
        margin-left: 1;
    }
    """

    def __init__(self, floor_path: str):
        super().__init__()
        self.floor_path = floor_path
        self.floor_name = os.path.basename(floor_path)

    def compose(self):
        with Vertical(id="dialog-container"):
            yield Label("New Step", classes="dialog-title")
            yield Label(f"Floor: {self.floor_name}", classes="field-label")
            yield Label("Step Name:", classes="field-label")
            yield Input(placeholder="calculate_total", id="step-name")
            with Horizontal(id="buttons"):
                yield Button("Cancel", variant="error", id="cancel")
                yield Button("Create", variant="primary", id="create")

    def on_mount(self):
        self.query_one("#step-name", Input).focus()

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "cancel":
            self.dismiss(None)
        elif event.button.id == "create":
            name = self.query_one("#step-name", Input).value.strip()
            if not name:
                self.notify("Please enter a step name", severity="warning")
                return
            self.dismiss({"name": name, "floor_path": self.floor_path})


def create_project(name: str, location: str, description: str) -> str:
    """Create a new Steps project structure.

    Args:
        name: Project name
        location: Parent directory for the project
        description: Project description

    Returns:
        Path to the created project directory
    """
    project_dir = os.path.join(location, name)
    os.makedirs(project_dir, exist_ok=True)

    # Create the building file
    building_file = os.path.join(project_dir, f"{name}.building")
    building_content = f'''building: {name}
    description: "{description}"
'''
    with open(building_file, 'w') as f:
        f.write(building_content)

    return project_dir


def create_floor(name: str, project_path: str) -> str:
    """Create a new floor in a Steps project.

    Args:
        name: Floor name
        project_path: Path to the project directory

    Returns:
        Path to the created floor directory
    """
    floor_dir = os.path.join(project_path, name)
    os.makedirs(floor_dir, exist_ok=True)

    # Create the floor file
    floor_file = os.path.join(floor_dir, f"{name}.floor")
    floor_content = f'''floor: {name}
'''
    with open(floor_file, 'w') as f:
        f.write(floor_content)

    return floor_dir


def create_step(name: str, floor_path: str) -> str:
    """Create a new step in a floor.

    Args:
        name: Step name
        floor_path: Path to the floor directory

    Returns:
        Path to the created step file
    """
    step_file = os.path.join(floor_path, f"{name}.step")
    step_content = f'''step: {name}
    -- Add your step logic here
'''
    with open(step_file, 'w') as f:
        f.write(step_content)

    return step_file

