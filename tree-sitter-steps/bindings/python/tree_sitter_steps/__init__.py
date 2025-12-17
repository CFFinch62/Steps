"""Tree-sitter bindings for the Steps programming language."""

from pathlib import Path

try:
    from tree_sitter_steps.binding import language
except ImportError:
    # Fallback if binding not built yet
    def language():
        """Return the tree-sitter Language object for Steps."""
        raise ImportError(
            "The tree-sitter-steps binding has not been built. "
            "Please run 'pip install -e .' in the tree-sitter-steps directory."
        )


def get_language():
    """Get the tree-sitter Language object for Steps.

    Returns:
        Language: The tree-sitter Language object for parsing Steps code.
    """
    from tree_sitter import Language
    return Language(language())


def get_queries_path():
    """Get the path to the queries directory.

    Returns:
        Path: Path to the directory containing highlight queries.
    """
    # Go up from tree_sitter_steps/__init__.py -> python -> bindings -> tree-sitter-steps root
    return Path(__file__).parent.parent.parent.parent / "queries"


def get_highlight_query():
    """Get the highlight query for Steps syntax highlighting.

    Returns:
        str: The tree-sitter highlight query content.
    """
    queries_path = get_queries_path()
    # Use the full highlight query for rich syntax highlighting
    highlight_file = queries_path / "highlights.scm"
    minimal_file = queries_path / "highlights_minimal.scm"

    # Use full query if it exists, otherwise fall back to minimal
    query_file = highlight_file if highlight_file.exists() else minimal_file

    if query_file.exists():
        return query_file.read_text(encoding="utf-8")
    else:
        raise FileNotFoundError(f"Highlight query not found at {query_file}")


__all__ = ["language", "get_language", "get_queries_path", "get_highlight_query"]
__version__ = "1.0.0"

