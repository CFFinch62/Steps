"""The main REPL loop."""

from pathlib import Path
from typing import Dict, List, Optional, Any

from steps.lexer import Lexer
from steps.parser import Parser
from steps.interpreter import Interpreter
from steps.errors import StepsError, LexerError, ParseError, StepsRuntimeError
from steps.types import StepsValue, StepsNumber, StepsText, StepsList, StepsTable, StepsNothing

from .environment import REPLEnvironment
from .commands import handle_command, is_command


class StepsREPL:
    """Interactive Steps interpreter for learning fundamentals."""
    
    VERSION = "0.1.0"
    
    def __init__(self) -> None:
        self.environment = REPLEnvironment()
        self.interpreter = Interpreter(self.environment)  # type: ignore
        self.multiline_buffer: List[str] = []
        self.in_multiline = False
        self.indent_level = 0
    
    def run(self) -> None:
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
    
    def _print_banner(self) -> None:
        """Print welcome message."""
        print(f"Steps REPL v{self.VERSION}")
        print("Type 'help' for commands, 'exit' to quit.")
        print()
    
    def _get_input(self) -> Optional[str]:
        """Get input with appropriate prompt."""
        prompt = "... " if self.in_multiline else ">>> "
        try:
            return input(prompt)
        except EOFError:
            return None
    
    def _needs_continuation(self, line: str) -> bool:
        """Check if line needs continuation (opens a block)."""
        stripped = line.strip()
        # Lines that start block constructs need continuation
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
    
    def _execute(self, source: str) -> None:
        """Execute a piece of Steps code."""
        if not source.strip():
            return

        try:
            # Lex
            lexer = Lexer(source, Path("<repl>"))
            tokens = lexer.tokenize()

            # Parse as statements (not full step/building)
            parser = Parser(tokens, Path("<repl>"))
            statements = parser.parse_repl_statements()

            # Execute each statement
            for stmt in statements:
                self.interpreter.execute_statement(stmt)

        except (LexerError, ParseError, StepsRuntimeError) as e:
            self._print_error(e)
        except StepsError as e:
            self._print_error(e)
    
    def _is_display_statement(self, stmt: Any) -> bool:
        """Check if statement is a display statement."""
        from steps.ast_nodes import DisplayStatement
        return isinstance(stmt, DisplayStatement)
    
    def _format_value(self, value: StepsValue) -> str:
        """Format a value for display."""
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
        elif isinstance(value, StepsNumber):
            return str(value.value)
        else:
            # For other types, try to get value attribute
            if hasattr(value, 'value'):
                return str(value.value)
            return str(value)
    
    def _print_error(self, error: StepsError) -> None:
        """Print an error message in a helpful way."""
        print(f"Error: {error.message}")
        if error.hint:
            print(f"Hint: {error.hint}")

    def reset(self) -> None:
        """Reset the environment (clear all variables)."""
        self.environment = REPLEnvironment()
        self.interpreter = Interpreter(self.environment)  # type: ignore
        self.multiline_buffer = []
        self.in_multiline = False

    def get_variables(self) -> Dict[str, StepsValue]:
        """Get all defined variables."""
        return self.environment.get_all_variables()

