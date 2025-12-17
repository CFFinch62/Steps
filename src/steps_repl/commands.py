"""Built-in REPL commands."""

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .repl import StepsREPL


def is_command(line: str) -> bool:
    """Check if line is a REPL command (not Steps code)."""
    commands = ['help', 'exit', 'quit', 'clear', 'vars', 'reset']
    return line.strip().lower() in commands


def handle_command(line: str, repl: "StepsREPL") -> Optional[str]:
    """Handle a REPL command. Returns 'exit' to quit."""
    cmd = line.strip().lower()
    
    if cmd in ('exit', 'quit'):
        return 'exit'
    
    elif cmd == 'help':
        print_help()
    
    elif cmd == 'clear':
        # Clear screen (ANSI escape)
        print("\033[2J\033[H", end="")
    
    elif cmd == 'vars':
        print_variables(repl)
    
    elif cmd == 'reset':
        repl.reset()
        print("Environment cleared.")
    
    return None


def print_help() -> None:
    """Print help message."""
    print("""
Steps REPL Commands:
  help   - Show this help message
  exit   - Exit the REPL (also: quit)
  clear  - Clear the screen
  vars   - Show all defined variables
  reset  - Clear all variables and start fresh

Steps Basics:
  set x to 42              - Create/assign variable
  display x                - Output a value
  set y to x + 10          - Math operations
  set name to "Steps"      - Text values
  display "Hi " added to name  - Text concatenation
  
  if x is greater than 10  - Conditionals
      display "big"        (indent with spaces, blank line to end)
  
  repeat 3 times           - Loops
      display "hello"      (indent with spaces, blank line to end)

  set nums to [1, 2, 3]    - Lists
  add 4 to nums
  
  set person to ["name": "Jo", "age": 30]  - Tables
  display person["name"]
""")


def print_variables(repl: "StepsREPL") -> None:
    """Print all defined variables."""
    variables = repl.get_variables()
    if not variables:
        print("No variables defined.")
        return
    
    print("Variables:")
    for name, value in variables.items():
        formatted = repl._format_value(value)
        type_name = type(value).__name__.replace("Steps", "").lower()
        print(f"  {name} = {formatted} ({type_name})")

