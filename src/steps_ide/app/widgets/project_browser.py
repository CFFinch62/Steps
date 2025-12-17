"""Steps IDE - Project Browser Widget.

Displays the Steps project structure as a tree (DISPLAY-ONLY):
- Building (root)
  - Building file (.building)
  - Floors (folders)
    - Floor file (.floor)
    - Steps (.step files)

Note: This browser is for viewing project structure only.
To open files, use the File Browser (Ctrl+B).
"""

from textual.widgets import Tree, Static
from textual.containers import ScrollableContainer
from textual.widget import Widget
from textual.message import Message
from textual.binding import Binding
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List
import os


class StaticTree(Tree):
    """A Tree widget that is display-only - no expand/collapse on click."""

    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        """Override to prevent expand/collapse on click."""
        # Don't call super() to prevent default expand/collapse behavior
        pass


@dataclass
class StepInfo:
    """Information about a step file."""
    name: str
    path: str


@dataclass
class FloorInfo:
    """Information about a floor."""
    name: str
    floor_path: str
    steps: List[StepInfo]


@dataclass
class ProjectStructure:
    """Complete project structure."""
    name: str
    building_path: str
    floors: List[FloorInfo]


def load_project_structure(project_path: str) -> Optional[ProjectStructure]:
    """Load project structure from a directory.
    
    Expected structure:
    project_name/
        project_name.building
        floor1/
            floor1.floor
            step1.step
            step2.step
        floor2/
            floor2.floor
            ...
    """
    path = Path(project_path)
    if not path.is_dir():
        return None
    
    project_name = path.name
    building_file = path / f"{project_name}.building"
    
    if not building_file.exists():
        # Try to find any .building file
        building_files = list(path.glob("*.building"))
        if building_files:
            building_file = building_files[0]
            project_name = building_file.stem
        else:
            return None
    
    floors: List[FloorInfo] = []
    
    # Scan subdirectories for floors
    for item in sorted(path.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            floor_file = item / f"{item.name}.floor"
            if floor_file.exists():
                # Found a floor
                steps: List[StepInfo] = []
                for step_file in sorted(item.glob("*.step")):
                    steps.append(StepInfo(
                        name=step_file.stem,
                        path=str(step_file)
                    ))
                floors.append(FloorInfo(
                    name=item.name,
                    floor_path=str(floor_file),
                    steps=steps
                ))
    
    return ProjectStructure(
        name=project_name,
        building_path=str(building_file),
        floors=floors
    )


class ProjectBrowser(Widget):
    """Steps project browser - shows building/floor/step structure."""

    DEFAULT_CSS = """
    ProjectBrowser {
        width: 35;
        height: 100%;
        border-left: solid $primary;
        background: $surface;
    }

    ProjectBrowser.hidden {
        display: none;
    }

    ProjectBrowser #browser-header {
        dock: top;
        height: 1;
        background: $primary;
        color: $text;
        padding: 0 1;
    }

    ProjectBrowser #project-name {
        dock: top;
        height: 1;
        background: $surface-darken-1;
        color: $text-muted;
        padding: 0 1;
        text-style: italic;
    }

    ProjectBrowser #tree-container {
        height: 1fr;
        overflow-x: auto;
        overflow-y: auto;
    }

    ProjectBrowser Tree {
        width: auto;
        min-width: 100%;
        scrollbar-gutter: stable;
    }
    """

    BINDINGS = [
        Binding("r", "refresh", "Refresh", show=False),
    ]

    class StepSelected(Message):
        """Sent when a step file is selected."""
        def __init__(self, path: str, floor: str, step: str):
            super().__init__()
            self.path = path
            self.floor = floor
            self.step = step

    class FloorSelected(Message):
        """Sent when a floor definition is selected."""
        def __init__(self, path: str, floor: str):
            super().__init__()
            self.path = path
            self.floor = floor

    class BuildingSelected(Message):
        """Sent when the building file is selected."""
        def __init__(self, path: str):
            super().__init__()
            self.path = path

    def __init__(self, project_path: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.project_path = project_path
        self.project_structure: Optional[ProjectStructure] = None

    def compose(self):
        yield Static("🏢 Project", id="browser-header")
        yield Static("No project loaded", id="project-name")
        with ScrollableContainer(id="tree-container"):
            yield StaticTree("Project", id="project-tree")

    def on_mount(self) -> None:
        """Initialize tree when mounted."""
        tree = self.query_one("#project-tree", Tree)
        tree.show_root = True
        tree.root.set_label("No project loaded")
        if self.project_path:
            self.load_project(self.project_path)

    def load_project(self, path: str) -> bool:
        """Load a Steps project and build the tree."""
        self.project_path = path
        self.project_structure = load_project_structure(path)
        self._build_tree()
        return self.project_structure is not None

    def _build_tree(self) -> None:
        """Build the tree widget from project structure."""
        tree = self.query_one("#project-tree", Tree)
        tree.clear()
        name_label = self.query_one("#project-name", Static)

        if not self.project_structure:
            tree.root.set_label("No project loaded")
            name_label.update("No project loaded")
            return

        # Set root to building name
        project_name = self.project_structure.name
        tree.root.set_label(f"🏢 {project_name}")
        tree.root.data = {"type": "building", "path": self.project_structure.building_path}
        name_label.update(project_name)

        # Add building file
        tree.root.add_leaf(
            f"📄 {project_name}.building",
            data={"type": "building_file", "path": self.project_structure.building_path}
        )

        # Add floors
        for floor in self.project_structure.floors:
            floor_node = tree.root.add(
                f"📁 {floor.name}",
                data={"type": "floor", "name": floor.name}
            )

            # Add floor definition file
            floor_node.add_leaf(
                f"📋 {floor.name}.floor",
                data={"type": "floor_file", "path": floor.floor_path, "floor": floor.name}
            )

            # Add steps
            for step in floor.steps:
                floor_node.add_leaf(
                    f"📝 {step.name}.step",
                    data={"type": "step", "path": step.path, "floor": floor.name, "step": step.name}
                )

            floor_node.expand()

        tree.root.expand()

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        """Completely disable tree node selection - project browser is display-only."""
        # Stop the event from propagating to prevent any action
        event.stop()
        # Don't post any messages - the project browser is purely for display

    def action_refresh(self) -> None:
        """Refresh the project tree."""
        if self.project_path:
            self.load_project(self.project_path)

    def toggle(self) -> bool:
        """Toggle visibility."""
        self.toggle_class("hidden")
        return not self.has_class("hidden")

    def show(self) -> None:
        """Show the browser."""
        self.remove_class("hidden")

    def hide(self) -> None:
        """Hide the browser."""
        self.add_class("hidden")

    @property
    def is_visible(self) -> bool:
        """Check if visible."""
        return not self.has_class("hidden")

    def focus_tree(self) -> None:
        """Focus the tree for keyboard navigation."""
        tree = self.query_one("#project-tree", Tree)
        tree.focus()

