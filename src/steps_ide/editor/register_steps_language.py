"""Register the Steps language with Textual's TextArea for syntax highlighting.

This module handles the integration of the tree-sitter Steps parser with
Textual's TextArea widget to enable proper syntax highlighting for Steps files.
"""

from typing import Optional
from textual.widgets import TextArea

# Flag to track if registration has been attempted
_registration_attempted = False
_registration_successful = False
_registration_error: Optional[str] = None


def register_steps_language(text_area: TextArea) -> bool:
    """Register the Steps language with a TextArea instance.
    
    This function attempts to load the tree-sitter Steps parser and
    register it with the given TextArea widget. It handles import errors
    gracefully and caches the result to avoid repeated attempts.
    
    Args:
        text_area: The TextArea widget to register the language with.
        
    Returns:
        bool: True if registration was successful, False otherwise.
    """
    global _registration_attempted, _registration_successful, _registration_error
    
    # If we've already tried and failed, don't try again
    if _registration_attempted and not _registration_successful:
        return False
    
    # If we've already succeeded, just return True
    if _registration_successful:
        return True
    
    _registration_attempted = True
    
    try:
        # Import the tree-sitter Steps bindings
        import tree_sitter_steps

        # Get the language object (already wrapped in Language class)
        language = tree_sitter_steps.get_language()

        # Get the highlight query
        highlight_query = tree_sitter_steps.get_highlight_query()

        # Register the language with the TextArea
        text_area.register_language(
            name="steps",
            language=language,
            highlight_query=highlight_query
        )

        _registration_successful = True
        return True
        
    except ImportError as e:
        _registration_error = f"Failed to import tree-sitter-steps: {e}"
        return False
    except FileNotFoundError as e:
        _registration_error = f"Highlight query not found: {e}"
        return False
    except Exception as e:
        _registration_error = f"Unexpected error during registration: {e}"
        return False


def is_steps_language_available() -> bool:
    """Check if the Steps language is available for syntax highlighting.
    
    Returns:
        bool: True if the language has been successfully registered.
    """
    return _registration_successful


def get_registration_error() -> Optional[str]:
    """Get the error message from the last registration attempt.
    
    Returns:
        Optional[str]: The error message, or None if no error occurred.
    """
    return _registration_error


def get_steps_language_name() -> str:
    """Get the language name to use for Steps files.
    
    Returns:
        str: "steps" if available, None otherwise to fall back to plain text.
    """
    return "steps" if _registration_successful else None

