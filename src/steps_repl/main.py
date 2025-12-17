#!/usr/bin/env python3
"""Steps REPL - Interactive interpreter for learning Steps fundamentals."""

from steps_repl.repl import StepsREPL


def main() -> None:
    """Run the Steps REPL."""
    repl = StepsREPL()
    repl.run()


if __name__ == "__main__":
    main()

