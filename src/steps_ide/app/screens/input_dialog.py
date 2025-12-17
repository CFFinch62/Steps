"""Input dialog for Steps program execution."""

from textual.screen import ModalScreen
from textual.widgets import Input, Label, Button
from textual.containers import Vertical, Horizontal
from textual.binding import Binding


class StepsInputDialog(ModalScreen[str]):
    """Modal dialog for getting input from user during Steps program execution."""

    DEFAULT_CSS = """
    StepsInputDialog {
        align: center middle;
    }

    StepsInputDialog > Vertical {
        width: 60;
        height: auto;
        background: $surface;
        border: thick $primary;
        padding: 1 2;
    }

    StepsInputDialog Label {
        width: 100%;
        content-align: center middle;
        margin-bottom: 1;
    }

    StepsInputDialog Input {
        width: 100%;
        margin-bottom: 1;
    }

    StepsInputDialog Horizontal {
        width: 100%;
        height: auto;
        align: center middle;
    }

    StepsInputDialog Button {
        margin: 0 1;
    }
    """

    BINDINGS = [
        Binding("escape", "cancel", "Cancel", show=False),
    ]

    def __init__(self, prompt: str = "Enter input:"):
        """Initialize the input dialog.
        
        Args:
            prompt: The prompt message to display to the user
        """
        super().__init__()
        self.prompt = prompt

    def compose(self):
        """Compose the dialog."""
        with Vertical():
            yield Label("Steps Program Input", id="dialog-title")
            yield Label(self.prompt, id="dialog-prompt")
            yield Input(placeholder="Enter value...", id="input-field")
            with Horizontal():
                yield Button("OK", variant="primary", id="ok-button")
                yield Button("Cancel", variant="default", id="cancel-button")

    def on_mount(self):
        """Focus the input field when dialog opens."""
        self.query_one("#input-field", Input).focus()

    def on_button_pressed(self, event: Button.Pressed):
        """Handle button presses."""
        if event.button.id == "ok-button":
            input_field = self.query_one("#input-field", Input)
            self.dismiss(input_field.value)
        elif event.button.id == "cancel-button":
            self.dismiss("")

    def on_input_submitted(self, event: Input.Submitted):
        """Handle Enter key in input field."""
        if event.input.id == "input-field":
            self.dismiss(event.value)

    def action_cancel(self):
        """Handle escape key."""
        self.dismiss("")

