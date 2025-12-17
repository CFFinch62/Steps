# Steps REPL - Implementation Guide

## Overview

The REPL is a **standalone component** - it does NOT use Only Code as a base. It's a simple interactive interpreter loop that reuses the Steps interpreter core but has its own minimal interface.

## Architecture

```
steps_repl/
├── __init__.py
├── main.py              # Entry point
├── repl.py              # REPL loop
├── environment.py       # Simplified single-scope environment
└── commands.py          # Built-in REPL commands (help, vars, etc.)
```

The REPL imports from the main Steps interpreter:
```
from steps.lexer import Lexer
from steps.parser import Parser  
from steps.interpreter import Interpreter
from steps.types import StepsValue
from steps.errors import StepsError
```

## Implementation

### main.py

```python
#!/usr/bin/env python3
"""Steps REPL - Interactive interpreter for learning Steps fundamentals."""

from steps_repl.repl import StepsREPL


def main():
    repl = StepsREPL()
    repl.run()


if __name__ == "__main__":
    main()
```

### repl.py

```python
"""The main REPL loop."""

import sys
from pathlib import Path

from steps.lexer import Lexer
from steps.parser import Parser
from steps.interpreter import Interpreter
from steps.errors import StepsError, LexerError, ParseError, RuntimeError

from steps_repl.environment import REPLEnvironment
from steps_repl.commands import handle_command, is_command


class StepsREPL:
    """Interactive Steps interpreter for learning fundamentals."""
    
    VERSION = "0.1.0"
    
    def __init__(self):
        self.environment = REPLEnvironment()
        self.interpreter = Interpreter(self.environment)
        self.multiline_buffer = []
        self.in_multiline = False
        self.indent_level = 0
    
    def run(self):
        """Main REPL loop."""
        self._print_banner()
        
        while True:
            try:
                line = self._get_input()
                
                if line is None:  # EOF (Ctrl+D)
                    print("\nGoodbye!")
                    break
                
                # Handle REPL commands
                if is_command(line) and not self.in_multiline:
                    result = handle_command(line, self)
                    if result == "exit":
                        print("Goodbye!")
                        break
                    continue
                
                # Handle multiline input
                if self._needs_continuation(line):
                    self.multiline_buffer.append(line)
                    self.in_multiline = True
                    continue
                
                if self.in_multiline:
                    if line.strip() == "":
                        # Empty line ends multiline input
                        full_input = "\n".join(self.multiline_buffer)
                        self.multiline_buffer = []
                        self.in_multiline = False
                        self._execute(full_input)
                    else:
                        self.multiline_buffer.append(line)
                else:
                    self._execute(line)
                    
            except KeyboardInterrupt:
                print("\n(Use 'exit' to quit)")
                self.multiline_buffer = []
                self.in_multiline = False
            except Exception as e:
                print(f"Internal error: {e}")
    
    def _print_banner(self):
        """Print welcome message."""
        print(f"Steps REPL v{self.VERSION}")
        print("Type 'help' for commands, 'exit' to quit.")
        print()
    
    def _get_input(self) -> str | None:
        """Get input with appropriate prompt."""
        prompt = "... " if self.in_multiline else ">>> "
        try:
            return input(prompt)
        except EOFError:
            return None
    
    def _needs_continuation(self, line: str) -> bool:
        """Check if line needs continuation (opens a block)."""
        stripped = line.strip()
        # Lines ending with block openers need continuation
        block_openers = [
            "if ", "otherwise if ", "otherwise",
            "repeat ", 
            "attempt:",
            "if unsuccessful:",
            "then continue:"
        ]
        for opener in block_openers:
            if stripped.startswith(opener) or stripped == opener.rstrip(":"):
                return True
        return False
    
    def _execute(self, source: str):
        """Execute a piece of Steps code."""
        if not source.strip():
            return
        
        try:
            # Wrap in a minimal structure for parsing
            wrapped = self._wrap_for_parsing(source)
            
            # Lex
            lexer = Lexer(wrapped, Path("<repl>"))
            tokens = lexer.tokenize()
            
            # Parse as statements (not full step/building)
            parser = Parser(tokens, "repl")
            statements = parser.parse_repl_statements()
            
            # Execute
            for stmt in statements:
                result = self.interpreter.visit(stmt)
                # If statement returns a value and isn't display, show it
                if result is not None and not self._is_display_statement(stmt):
                    print(self._format_value(result))
                    
        except LexerError as e:
            self._print_error(e)
        except ParseError as e:
            self._print_error(e)
        except RuntimeError as e:
            self._print_error(e)
        except StepsError as e:
            self._print_error(e)
    
    def _wrap_for_parsing(self, source: str) -> str:
        """Wrap REPL input for the parser.
        
        The parser expects proper indentation. REPL input
        needs to be wrapped appropriately.
        """
        # For simple statements, no wrapping needed
        # For blocks (if/repeat), they come pre-indented from multiline input
        return source
    
    def _is_display_statement(self, stmt) -> bool:
        """Check if statement is a display statement."""
        from steps.ast_nodes import DisplayStatement
        return isinstance(stmt, DisplayStatement)
    
    def _format_value(self, value) -> str:
        """Format a value for display."""
        from steps.types import StepsText, StepsList, StepsTable, StepsNothing
        
        if isinstance(value, StepsNothing):
            return ""
        elif isinstance(value, StepsText):
            return value.value  # Don't quote strings in output
        elif isinstance(value, StepsList):
            items = ", ".join(self._format_value(v) for v in value.elements)
            return f"[{items}]"
        elif isinstance(value, StepsTable):
            pairs = ", ".join(
                f'"{k}": {self._format_value(v)}' 
                for k, v in value.pairs.items()
            )
            return f"[{pairs}]"
        else:
            return str(value.value)
    
    def _print_error(self, error: StepsError):
        """Print an error message in a helpful way."""
        print(f"Error: {error.message}")
        if hasattr(error, 'hint') and error.hint:
            print(f"Hint: {error.hint}")
    
    def reset(self):
        """Reset the environment (clear all variables)."""
        self.environment = REPLEnvironment()
        self.interpreter = Interpreter(self.environment)
        self.multiline_buffer = []
        self.in_multiline = False
    
    def get_variables(self) -> dict:
        """Get all defined variables."""
        return self.environment.get_all_variables()
```

### environment.py

```python
"""Simplified environment for REPL - single scope, no steps/floors."""

from steps.types import StepsValue, StepsNothing


class REPLEnvironment:
    """Single-scope environment for the REPL.
    
    Unlike the full interpreter environment, this has:
    - No floors or steps (can't define them in REPL)
    - No scope nesting (except temporary for if/loops)
    - No 'fixed' type enforcement
    - Variables created on first assignment
    """
    
    def __init__(self):
        self.variables: dict[str, StepsValue] = {}
        self._temp_scopes: list[dict[str, StepsValue]] = []
    
    def get(self, name: str) -> StepsValue:
        """Get a variable's value."""
        # Check temp scopes first (innermost to outermost)
        for scope in reversed(self._temp_scopes):
            if name in scope:
                return scope[name]
        
        # Check main scope
        if name in self.variables:
            return self.variables[name]
        
        # Special built-in: problem_message (not used in REPL but defined)
        if name == "problem_message":
            return StepsNothing()
        
        from steps.errors import RuntimeError
        raise RuntimeError(
            message=f"Variable '{name}' has not been defined.",
            hint=f"Try: set {name} to some_value",
            line=0,
            column=0
        )
    
    def set(self, name: str, value: StepsValue):
        """Set a variable's value. Creates if doesn't exist."""
        # If in a temp scope, set there
        if self._temp_scopes:
            # Check if it exists in temp scope
            for scope in reversed(self._temp_scopes):
                if name in scope:
                    scope[name] = value
                    return
            # Check if it exists in main scope
            if name in self.variables:
                self.variables[name] = value
                return
            # New variable - put in innermost temp scope
            self._temp_scopes[-1][name] = value
        else:
            # Not in temp scope - use main scope
            self.variables[name] = value
    
    def define(self, name: str, value: StepsValue, fixed: bool = False):
        """Define a variable (same as set in REPL - no fixed enforcement)."""
        self.set(name, value)
    
    def push_scope(self):
        """Push a temporary scope (for if/loop bodies)."""
        self._temp_scopes.append({})
    
    def pop_scope(self):
        """Pop a temporary scope."""
        if self._temp_scopes:
            self._temp_scopes.pop()
    
    def get_all_variables(self) -> dict[str, StepsValue]:
        """Get all variables in main scope (for 'vars' command)."""
        return dict(self.variables)
    
    def clear(self):
        """Clear all variables."""
        self.variables.clear()
        self._temp_scopes.clear()
    
    # These methods exist to satisfy the interpreter interface but are no-ops in REPL
    
    def register_step(self, floor: str, step):
        """No-op in REPL - can't define steps."""
        pass
    
    def resolve_step(self, name: str):
        """No-op in REPL - can't call steps."""
        from steps.errors import RuntimeError
        raise RuntimeError(
            message=f"Cannot call step '{name}' in the REPL.",
            hint="The REPL is for learning basics. Use the IDE to work with steps.",
            line=0,
            column=0
        )
```

### commands.py

```python
"""Built-in REPL commands."""


def is_command(line: str) -> bool:
    """Check if line is a REPL command (not Steps code)."""
    commands = ['help', 'exit', 'quit', 'clear', 'vars', 'reset']
    return line.strip().lower() in commands


def handle_command(line: str, repl) -> str | None:
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


def print_help():
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


def print_variables(repl):
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
```

## Parser Addition

The main Steps parser needs a `parse_repl_statements()` method to handle REPL input:

```python
# Add to steps/parser.py

def parse_repl_statements(self) -> list[StatementNode]:
    """Parse REPL input as a list of statements.
    
    Unlike parsing a full step/building, this:
    - Doesn't expect step/floor/building declarations
    - Parses raw statements directly
    - Handles multiline blocks (if/repeat)
    """
    statements = []
    
    while not self.match(TokenType.EOF):
        if self.match(TokenType.NEWLINE):
            self.advance()
            continue
        
        stmt = self.parse_statement()
        if stmt:
            statements.append(stmt)
    
    return statements
```

## Integration with CLI

The REPL is invoked via the Steps CLI:

```bash
# Start REPL
steps repl

# Or directly
python -m steps_repl
```

In `steps/main.py`:

```python
def main():
    parser = argparse.ArgumentParser(description="Steps Programming Language")
    subparsers = parser.add_subparsers(dest="command")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run a Steps project")
    run_parser.add_argument("path", help="Path to project directory")
    
    # Check command
    check_parser = subparsers.add_parser("check", help="Validate a Steps project")
    check_parser.add_argument("path", help="Path to project directory")
    
    # REPL command
    repl_parser = subparsers.add_parser("repl", help="Start interactive REPL")
    
    args = parser.parse_args()
    
    if args.command == "repl":
        from steps_repl.repl import StepsREPL
        repl = StepsREPL()
        repl.run()
    elif args.command == "run":
        run_project(args.path)
    elif args.command == "check":
        check_project(args.path)
    else:
        parser.print_help()
```

## What the REPL Does NOT Include

To keep it simple and focused on teaching fundamentals:

- No readline/history library (could add later)
- No syntax highlighting in input
- No tab completion
- No file loading
- No step/floor/building definitions
- No `call` statements
- No `attempt`/`if unsuccessful` (simplifies error handling)
- No `declare` blocks (variables created on first `set`)
- No `fixed` type enforcement

These omissions are intentional - the REPL is for learning basics, not for real development.

## Example Session

```
$ steps repl
Steps REPL v0.1.0
Type 'help' for commands, 'exit' to quit.

>>> set x to 42
>>> display x
42
>>> set y to x * 2
>>> y
84
>>> set name to "Steps"
>>> display "Hello, " added to name
Hello, Steps
>>> if x is greater than 10
...     display "big number"
... 
big number
>>> vars
Variables:
  x = 42 (number)
  y = 84 (number)
  name = Steps (text)
>>> reset
Environment cleared.
>>> vars
No variables defined.
>>> exit
Goodbye!
```
