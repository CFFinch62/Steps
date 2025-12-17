"""Integration tests for the Steps CLI."""

import subprocess
import sys
from pathlib import Path

import pytest


class TestCLI:
    """Test the Steps CLI commands."""
    
    def run_cli(self, *args: str) -> subprocess.CompletedProcess:
        """Run the Steps CLI with the given arguments."""
        return subprocess.run(
            [sys.executable, "-m", "steps.main", *args],
            capture_output=True,
            text=True,
            timeout=30
        )
    
    def test_help(self) -> None:
        """Test that --help works."""
        result = self.run_cli("--help")
        assert result.returncode == 0
        assert "Steps Programming Language" in result.stdout
        assert "run" in result.stdout
        assert "check" in result.stdout
        assert "repl" in result.stdout
        assert "diagram" in result.stdout
    
    def test_run_help(self) -> None:
        """Test that run --help works."""
        result = self.run_cli("run", "--help")
        assert result.returncode == 0
        assert "path" in result.stdout.lower()

    def test_check_help(self) -> None:
        """Test that check --help works."""
        result = self.run_cli("check", "--help")
        assert result.returncode == 0
        assert "path" in result.stdout.lower()

    def test_check_nonexistent_path(self) -> None:
        """Test check with nonexistent path."""
        result = self.run_cli("check", "/nonexistent/path")
        assert result.returncode == 1
        # Error message goes to stderr
        assert "not found" in result.stderr.lower() or "error" in result.stderr.lower() or "not exist" in result.stderr.lower()
    
    def test_run_nonexistent_path(self) -> None:
        """Test run with nonexistent path."""
        result = self.run_cli("run", "/nonexistent/path")
        assert result.returncode == 1


class TestREPL:
    """Test the Steps REPL."""
    
    def run_repl(self, input_text: str) -> subprocess.CompletedProcess:
        """Run the REPL with the given input."""
        return subprocess.run(
            [sys.executable, "-m", "steps_repl.main"],
            input=input_text,
            capture_output=True,
            text=True,
            timeout=30
        )
    
    def test_repl_starts(self) -> None:
        """Test that the REPL starts and exits cleanly."""
        result = self.run_repl("exit\n")
        assert result.returncode == 0
        assert "Steps REPL" in result.stdout
        assert "Goodbye!" in result.stdout
    
    def test_repl_help(self) -> None:
        """Test the help command."""
        result = self.run_repl("help\nexit\n")
        assert result.returncode == 0
        assert "Steps REPL Commands" in result.stdout
        assert "help" in result.stdout
        assert "exit" in result.stdout
        assert "vars" in result.stdout
    
    def test_repl_set_and_display(self) -> None:
        """Test setting and displaying a variable."""
        result = self.run_repl("set x to 42\ndisplay x\nexit\n")
        assert result.returncode == 0
        assert "42" in result.stdout
    
    def test_repl_arithmetic(self) -> None:
        """Test arithmetic operations."""
        result = self.run_repl("set x to 10\nset y to 5\ndisplay x + y\nexit\n")
        assert result.returncode == 0
        assert "15" in result.stdout
    
    def test_repl_vars_command(self) -> None:
        """Test the vars command."""
        result = self.run_repl("set x to 42\nvars\nexit\n")
        assert result.returncode == 0
        assert "x" in result.stdout
        assert "42" in result.stdout
    
    def test_repl_reset_command(self) -> None:
        """Test the reset command."""
        result = self.run_repl("set x to 42\nreset\nvars\nexit\n")
        assert result.returncode == 0
        # After reset, vars should show no variables
        lines = result.stdout.split("\n")
        # Find the line after "reset" and "vars"
        found_no_vars = False
        for i, line in enumerate(lines):
            if "No variables defined" in line:
                found_no_vars = True
                break
        assert found_no_vars, "Expected 'No variables defined' after reset"
    
    def test_repl_text_operations(self) -> None:
        """Test text operations."""
        result = self.run_repl('set name to "Steps"\ndisplay "Hello " added to name\nexit\n')
        assert result.returncode == 0
        assert "Hello Steps" in result.stdout
    
    def test_repl_list_operations(self) -> None:
        """Test list operations."""
        result = self.run_repl("set nums to [1, 2, 3]\nadd 4 to nums\ndisplay nums\nexit\n")
        assert result.returncode == 0
        # Should show the list with 4 elements
        assert "4" in result.stdout
    
    def test_repl_error_handling(self) -> None:
        """Test that errors are handled gracefully."""
        result = self.run_repl("display undefined_var\nexit\n")
        assert result.returncode == 0  # REPL should not crash
        assert "Error" in result.stdout or "error" in result.stdout
    
    def test_repl_quit_alias(self) -> None:
        """Test that 'quit' works as an alias for 'exit'."""
        result = self.run_repl("quit\n")
        assert result.returncode == 0
        assert "Goodbye!" in result.stdout

