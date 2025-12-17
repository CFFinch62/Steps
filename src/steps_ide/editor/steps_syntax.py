"""Steps Language Syntax Highlighter for Textual.

This module provides regex-based syntax highlighting for Steps language files.
It creates a custom tree-sitter-like highlighting system that works with
Textual's TextArea widget.
"""

import re
from dataclasses import dataclass
from typing import List, Tuple, Optional
from rich.style import Style
from rich.text import Text


@dataclass
class HighlightToken:
    """A highlighted token with its position and style."""
    start: int
    end: int
    style: str  # Style name like 'keyword', 'string', etc.


# Steps language theme colors (similar to VS Code Dark+)
STEPS_THEME = {
    # Structure keywords - blue/purple
    'keyword.structure': Style(color='#569cd6', bold=True),  # building:, floor:, step:, riser:
    'keyword.clause': Style(color='#569cd6'),  # expects:, returns:, belongs to:
    
    # Control flow - magenta/purple
    'keyword.control': Style(color='#c586c0'),  # if, otherwise, while, repeat, for each
    
    # Variable/assignment keywords - blue
    'keyword': Style(color='#569cd6'),  # set, to, as, declare:, fixed, do:
    
    # Function keywords - yellow
    'keyword.function': Style(color='#dcdcaa'),  # call, with, return
    
    # Builtin functions - yellow
    'function.builtin': Style(color='#dcdcaa'),  # display, input
    
    # Types - green/teal
    'type': Style(color='#4ec9b0'),  # number, text, boolean, list, table
    
    # Literals
    'string': Style(color='#ce9178'),  # "text"
    'string.escape': Style(color='#d7ba7d'),  # \n, \t, etc.
    'number': Style(color='#b5cea8'),  # 42, 3.14
    'boolean': Style(color='#569cd6'),  # true, false
    'constant': Style(color='#569cd6'),  # nothing
    
    # Operators - white/light
    'operator': Style(color='#d4d4d4'),  # +, -, *, /
    'operator.word': Style(color='#569cd6'),  # and, or, not, is equal to, etc.
    
    # Comments - green
    'comment': Style(color='#6a9955', italic=True),
    
    # Identifiers
    'variable': Style(color='#9cdcfe'),  # variable names
    'function': Style(color='#dcdcaa'),  # function/step names
    'namespace': Style(color='#4ec9b0'),  # building/floor names
    
    # Punctuation
    'punctuation': Style(color='#d4d4d4'),  # :, ,, [, ], (, )
}


# Regex patterns for Steps syntax (order matters - more specific first)
STEPS_PATTERNS: List[Tuple[str, str]] = [
    # Block comments (note block: ... end note)
    (r'note block:.*?end note', 'comment'),
    
    # Line comments (note: ...)
    (r'note:.*$', 'comment'),
    
    # Strings (including escape sequences handled separately)
    (r'"(?:[^"\\]|\\.)*"', 'string'),
    
    # Structure keywords with colons
    (r'\bbuilding:', 'keyword.structure'),
    (r'\bfloor:', 'keyword.structure'),
    (r'\bstep:', 'keyword.structure'),
    (r'\briser:', 'keyword.structure'),
    
    # Clause keywords
    (r'\bbelongs to:', 'keyword.clause'),
    (r'\bexpects:', 'keyword.clause'),
    (r'\breturns:', 'keyword.clause'),
    (r'\bdeclare:', 'keyword'),
    (r'\bdo:', 'keyword'),
    (r'\battempt:', 'keyword.control'),
    (r'\bif unsuccessful:', 'keyword.control'),
    (r'\bthen continue:', 'keyword.control'),
    
    # Multi-word comparison operators (before single words)
    (r'\bis greater than or equal to\b', 'operator.word'),
    (r'\bis less than or equal to\b', 'operator.word'),
    (r'\bis not equal to\b', 'operator.word'),
    (r'\bis greater than\b', 'operator.word'),
    (r'\bis less than\b', 'operator.word'),
    (r'\bis equal to\b', 'operator.word'),
    
    # Multi-word keywords
    (r'\bstoring result in\b', 'keyword'),
    (r'\botherwise if\b', 'keyword.control'),
    (r'\bfor each\b', 'keyword.control'),
    (r'\blength of\b', 'operator.word'),
    (r'\badded to\b', 'operator.word'),
    (r'\bstarts with\b', 'operator.word'),
    (r'\bends with\b', 'operator.word'),
    (r'\bsplit by\b', 'operator.word'),
    (r'\bcharacter at\b', 'operator.word'),
    (r'\bis in\b', 'operator.word'),
    (r'\bend note\b', 'comment'),
    
    # Control flow keywords
    (r'\bif\b', 'keyword.control'),
    (r'\botherwise\b', 'keyword.control'),
    (r'\bwhile\b', 'keyword.control'),
    (r'\brepeat\b', 'keyword.control'),
    (r'\btimes\b', 'keyword.control'),
    (r'\bexit\b', 'keyword.control'),
    
    # Boolean operators
    (r'\band\b', 'operator.word'),
    (r'\bor\b', 'operator.word'),
    (r'\bnot\b', 'operator.word'),
    
    # Variable keywords
    (r'\bset\b', 'keyword'),
    (r'\bto\b', 'keyword'),
    (r'\bas\b', 'keyword'),
    (r'\bfixed\b', 'keyword'),
    (r'\bin\b', 'keyword'),
    (r'\bfrom\b', 'keyword'),
    
    # Function keywords
    (r'\bcall\b', 'keyword.function'),
    (r'\bwith\b', 'keyword'),
    (r'\breturn\b', 'keyword.function'),
    
    # Builtin functions
    (r'\bdisplay\b', 'function.builtin'),
    (r'\binput\b', 'function.builtin'),
    
    # List operations
    (r'\badd\b', 'keyword'),
    (r'\bremove\b', 'keyword'),
    (r'\bcontains\b', 'operator.word'),
    (r'\bequals\b', 'operator.word'),
    
    # Types
    (r'\bnumber\b', 'type'),
    (r'\btext\b', 'type'),
    (r'\bboolean\b', 'type'),
    (r'\blist\b', 'type'),
    (r'\btable\b', 'type'),
    
    # Literals
    (r'\btrue\b', 'boolean'),
    (r'\bfalse\b', 'boolean'),
    (r'\bnothing\b', 'constant'),
    (r'-?\b\d+\.?\d*\b', 'number'),
    
    # Math operators
    (r'[+\-*/]', 'operator'),
    
    # Punctuation
    (r'[:\[\](),]', 'punctuation'),
]

# Compile patterns
COMPILED_PATTERNS = [(re.compile(pattern, re.MULTILINE), style) for pattern, style in STEPS_PATTERNS]


def highlight_steps_code(text: str) -> Text:
    """Apply Steps syntax highlighting to text.

    Args:
        text: The source code to highlight

    Returns:
        A Rich Text object with syntax highlighting applied
    """
    # Find all matches with their positions
    matches: List[Tuple[int, int, str]] = []

    for pattern, style in COMPILED_PATTERNS:
        for match in pattern.finditer(text):
            matches.append((match.start(), match.end(), style))

    # Sort by start position, then by length (longer matches first)
    matches.sort(key=lambda x: (x[0], -(x[1] - x[0])))

    # Remove overlapping matches (keep first/longest)
    filtered_matches: List[Tuple[int, int, str]] = []
    last_end = 0

    for start, end, style in matches:
        if start >= last_end:
            filtered_matches.append((start, end, style))
            last_end = end

    # Build Rich Text with highlighting
    result = Text(text)

    for start, end, style_name in filtered_matches:
        if style_name in STEPS_THEME:
            result.stylize(STEPS_THEME[style_name], start, end)

    return result


def get_line_highlights(line: str, line_offset: int = 0) -> List[Tuple[int, int, Style]]:
    """Get highlight ranges for a single line.

    Args:
        line: The line of code to highlight
        line_offset: Character offset of this line in the full document

    Returns:
        List of (start, end, style) tuples for this line
    """
    highlights: List[Tuple[int, int, Style]] = []
    matches: List[Tuple[int, int, str]] = []

    for pattern, style in COMPILED_PATTERNS:
        for match in pattern.finditer(line):
            matches.append((match.start(), match.end(), style))

    # Sort and filter overlaps
    matches.sort(key=lambda x: (x[0], -(x[1] - x[0])))

    last_end = 0
    for start, end, style_name in matches:
        if start >= last_end:
            if style_name in STEPS_THEME:
                highlights.append((start + line_offset, end + line_offset, STEPS_THEME[style_name]))
            last_end = end

    return highlights


class StepsHighlighter:
    """Highlighter class for integration with text widgets."""

    def __init__(self):
        self.patterns = COMPILED_PATTERNS
        self.theme = STEPS_THEME

    def highlight(self, text: str) -> Text:
        """Highlight the given text and return a Rich Text object."""
        return highlight_steps_code(text)

    def get_style_for_token(self, token_type: str) -> Optional[Style]:
        """Get the Rich Style for a given token type."""
        return self.theme.get(token_type)

