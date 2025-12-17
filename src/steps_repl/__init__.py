"""Steps REPL - Interactive interpreter for learning Steps fundamentals.

The REPL is a teaching tool for learning basic programming concepts.
It supports variables, math, text, lists, tables, conditionals, and loops.

It does NOT support steps, floors, buildings, or call statements -
those are for the full Steps IDE.
"""

__version__ = "0.1.0"

from .repl import StepsREPL

__all__ = ["StepsREPL"]

