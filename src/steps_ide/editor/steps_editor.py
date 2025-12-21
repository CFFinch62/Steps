"""Steps Editor - Editor with Steps language awareness.

Extends OnlyCodeEditor with:
- Steps file extension detection (.building, .floor, .step)
- Steps syntax highlighting (when available)
- Validation integration
"""

from pathlib import Path
from typing import Optional, List
from textual.message import Message

from steps_ide.editor.editor_widget import OnlyCodeEditor
from steps_ide.editor.register_steps_language import register_steps_language, get_steps_language_name


# Steps-specific file extensions
STEPS_EXTENSIONS = {
    ".building": "steps",
    ".floor": "steps",
    ".step": "steps",
}


class StepsEditor(OnlyCodeEditor):
    """Editor with Steps language awareness."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Track if this is a Steps file
        self._is_steps_file = False
        self._steps_file_type: Optional[str] = None  # "building", "floor", "step"

        # Register the Steps language for syntax highlighting
        self._steps_language_registered = register_steps_language(self)

    def detect_language(self, path: str) -> Optional[str]:
        """Detect language from file path.

        Steps files get "steps" language if registered, otherwise None.
        Other files use the parent class detection.
        """
        p = Path(path)
        ext = p.suffix.lower()

        # Check for Steps files first
        if ext in STEPS_EXTENSIONS:
            self._is_steps_file = True
            self._steps_file_type = ext[1:]  # Remove the dot
            # Return "steps" if the language was successfully registered
            return get_steps_language_name()

        # Fall back to parent implementation
        self._is_steps_file = False
        self._steps_file_type = None
        return super().detect_language(path)

    def set_language_from_path(self, path: str) -> None:
        """Set the editor language based on file path."""
        language = self.detect_language(path)
        if language:
            self.language = language
        else:
            self.language = None

    @property
    def is_steps_file(self) -> bool:
        """Check if the current file is a Steps file."""
        return self._is_steps_file

    @property
    def steps_file_type(self) -> Optional[str]:
        """Get the type of Steps file (building, floor, step, or None)."""
        return self._steps_file_type

    def validate_steps(self) -> List[dict]:
        """Validate current content as Steps code.
        
        Returns a list of error dictionaries with keys:
        - line: int (1-based line number)
        - message: str
        - hint: Optional[str]
        
        Returns empty list if content is valid or not a Steps file.
        """
        if not self._is_steps_file:
            return []
        
        errors = []
        try:
            # Import here to avoid circular dependency
            from steps.parser import parse_building, parse_floor, parse_step

            # Determine which parser to use based on file type
            file_type = self._steps_file_type or "step"
            file_path = Path("current." + file_type)

            # Parse based on file type
            if file_type == "building":
                parse_result = parse_building(self.text, file_path)
            elif file_type == "floor":
                parse_result = parse_floor(self.text, file_path)
            else:  # step
                parse_result = parse_step(self.text, file_path)

            # Convert parse errors to editor format
            for error in parse_result.errors:
                errors.append({
                    "line": error.line or 1,
                    "message": error.message,
                    "hint": error.hint,
                })

        except ImportError:
            # Steps interpreter not available
            pass
        except Exception as e:
            # Other errors
            errors.append({
                "line": 1,
                "message": str(e),
                "hint": None,
            })

        return errors

    def get_steps_context(self) -> Optional[dict]:
        """Get context information for the current cursor position.
        
        Returns a dictionary with:
        - current_step: str or None
        - current_floor: str or None
        - in_definition: bool
        
        This can be used for context-aware features.
        """
        if not self._is_steps_file:
            return None
        
        # Basic context detection - look for enclosing step/floor definitions
        cursor_row = self.cursor_location[0]
        context = {
            "current_step": None,
            "current_floor": None,
            "in_definition": False,
        }
        
        # Scan backwards from cursor to find enclosing definitions
        for row in range(cursor_row, -1, -1):
            line = self.document.get_line(row).strip()
            if line.startswith("step:"):
                context["current_step"] = line[5:].strip()
                context["in_definition"] = True
                break
            elif line.startswith("floor:"):
                context["current_floor"] = line[6:].strip()
                context["in_definition"] = True
                break
            elif line.startswith("building:"):
                context["in_definition"] = True
                break
        
        return context

    class RunRequested(Message):
        """Message sent when run (F5) is requested."""
        pass
    
    class CheckRequested(Message):
        """Message sent when check (F6) is requested."""
        pass
        
    class SaveRequested(Message):
        """Message sent when save (Ctrl+S) is requested."""
        pass
        
    class OpenRequested(Message):
        """Message sent when open (Ctrl+O) is requested."""
        pass
        
    class NewFileRequested(Message):
        """Message sent when new file (Ctrl+T) is requested."""
        pass
        
    class CloseBufferRequested(Message):
        """Message sent when close buffer (Ctrl+W) is requested."""
        pass
        
    class NextBufferRequested(Message):
        """Message sent when next buffer is requested."""
        pass
        
    class PrevBufferRequested(Message):
        """Message sent when previous buffer is requested."""
        pass

    BINDINGS = [
        ("f5", "run", "Run"),
        ("f6", "check", "Check"),
        ("ctrl+s", "save", "Save"),
        ("ctrl+o", "open", "Open"),
        ("ctrl+t", "new_file", "New Tab"),
        ("ctrl+w", "close_buffer", "Close"),
        ("ctrl+pagedown", "next_buffer", "Next Tab"),
        ("ctrl+pageup", "prev_buffer", "Prev Tab"),
        # F7/F8 as fallback
        ("f8", "next_buffer", "Next Tab"),
        ("f7", "prev_buffer", "Prev Tab"),
    ]

    def action_run(self): self.post_message(self.RunRequested())
    def action_check(self): self.post_message(self.CheckRequested())
    def action_save(self): self.post_message(self.SaveRequested())
    def action_open(self): self.post_message(self.OpenRequested())
    def action_new_file(self): self.post_message(self.NewFileRequested())
    def action_close_buffer(self): self.post_message(self.CloseBufferRequested())
    def action_next_buffer(self): self.post_message(self.NextBufferRequested())
    def action_prev_buffer(self): self.post_message(self.PrevBufferRequested())


