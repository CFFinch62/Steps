"""Native Functions Registry.

These functions can be called directly from Steps code via the interpreter.
The interpreter checks this registry before looking for user-defined steps.
"""

from .random import random_int, random_choice
from .io import read_file, write_file, append_file, file_exists, read_csv, write_csv
from .text import (
    text_slice, text_lowercase, text_uppercase, text_trim,
    text_index_of, text_replace, text_characters
)
from .tui import (
    tui_box, tui_line, tui_banner, tui_center_text,
    tui_pad_text, tui_progress_bar
)

NATIVE_FUNCTIONS = {
    # Random functions
    "random_int": {
        "function": random_int,
        "params": ["min_val", "max_val"],
    },
    "random_choice": {
        "function": random_choice,
        "params": ["lst"],
    },
    # File I/O functions
    "read_file": {
        "function": read_file,
        "params": ["path"],
    },
    "write_file": {
        "function": write_file,
        "params": ["path", "content"],
    },
    "append_file": {
        "function": append_file,
        "params": ["path", "content"],
    },
    "file_exists": {
        "function": file_exists,
        "params": ["path"],
    },
    # CSV functions
    "read_csv": {
        "function": read_csv,
        "params": ["path"],
    },
    "write_csv": {
        "function": write_csv,
        "params": ["path", "data"],
    },
    # String functions
    "slice": {
        "function": text_slice,
        "params": ["text", "start", "end"],
    },
    "lowercase": {
        "function": text_lowercase,
        "params": ["text"],
    },
    "uppercase": {
        "function": text_uppercase,
        "params": ["text"],
    },
    "trim": {
        "function": text_trim,
        "params": ["text"],
    },
    "index_of": {
        "function": text_index_of,
        "params": ["text", "search"],
    },
    "replace": {
        "function": text_replace,
        "params": ["text", "old", "new"],
    },
    "characters": {
        "function": text_characters,
        "params": ["text"],
    },
    # TUI functions
    "box": {
        "function": tui_box,
        "params": ["content", "width"],
    },
    "line": {
        "function": tui_line,
        "params": ["width", "style"],
    },
    "banner": {
        "function": tui_banner,
        "params": ["title", "width"],
    },
    "center_text": {
        "function": tui_center_text,
        "params": ["text", "width"],
    },
    "pad_text": {
        "function": tui_pad_text,
        "params": ["text", "width", "align"],
    },
    "progress_bar": {
        "function": tui_progress_bar,
        "params": ["current", "total", "width"],
    },
}

