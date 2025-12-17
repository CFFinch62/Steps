"""Unit Tests for Steps Error System.

Tests for error formatting, templates, and educational error messages.
"""

import pytest
from pathlib import Path

from steps.errors import (
    SourceLocation, ErrorCode, StepsError, LexerError, ParseError,
    StepsRuntimeError, StepsTypeError, make_error,
    undefined_variable_error, undefined_step_error, division_by_zero_error,
    type_mismatch_error
)


class TestSourceLocation:
    """Tests for SourceLocation dataclass."""
    
    def test_basic_location(self):
        loc = SourceLocation(
            file=Path("test.step"),
            line=5,
            column=10
        )
        assert loc.file == Path("test.step")
        assert loc.line == 5
        assert loc.column == 10
    
    def test_str_simple(self):
        loc = SourceLocation(file=Path("test.step"), line=5, column=10)
        assert str(loc) == "test.step:5:10"
    
    def test_str_with_end(self):
        loc = SourceLocation(
            file=Path("test.step"),
            line=5,
            column=10,
            end_line=7,
            end_column=15
        )
        assert str(loc) == "test.step:5:10-7:15"


class TestStepsError:
    """Tests for base error class."""
    
    def test_basic_error(self):
        error = StepsError(
            code="E101",
            message="Something went wrong"
        )
        assert error.code == "E101"
        assert error.message == "Something went wrong"
    
    def test_error_with_location(self):
        error = StepsError(
            code="E101",
            message="Something went wrong",
            file=Path("test.step"),
            line=5,
            column=10
        )
        formatted = error.format()
        assert "E101" in formatted
        assert "test.step" in formatted
        assert "line 5" in formatted
        assert "column 10" in formatted
    
    def test_error_with_hint(self):
        error = StepsError(
            code="E101",
            message="Something went wrong",
            hint="Try doing X instead"
        )
        formatted = error.format()
        assert "Hint:" in formatted
        assert "Try doing X instead" in formatted
    
    def test_error_with_context(self):
        error = StepsError(
            code="E101",
            message="Something went wrong",
            file=Path("test.step"),
            line=2,
            column=5,
            context_lines=["line 1", "line 2 with error", "line 3"]
        )
        formatted = error.format()
        assert "line 2 with error" in formatted
    
    def test_from_location(self):
        loc = SourceLocation(file=Path("test.step"), line=5, column=10)
        error = StepsError.from_location(
            code="E101",
            message="Test error",
            location=loc,
            hint="Test hint"
        )
        assert error.file == Path("test.step")
        assert error.line == 5
        assert error.column == 10
        assert error.hint == "Test hint"


class TestErrorSubclasses:
    """Tests for specialized error classes."""
    
    def test_lexer_error(self):
        error = LexerError(code="E101", message="Bad character")
        assert isinstance(error, StepsError)
    
    def test_parse_error(self):
        error = ParseError(code="E201", message="Unexpected token")
        assert isinstance(error, StepsError)
    
    def test_runtime_error(self):
        error = StepsRuntimeError(code="E401", message="Undefined variable")
        assert isinstance(error, StepsError)
    
    def test_type_error(self):
        error = StepsTypeError(code="E301", message="Type mismatch")
        assert isinstance(error, StepsError)


class TestMakeError:
    """Tests for template-based error creation."""
    
    def test_undefined_variable_error(self):
        loc = SourceLocation(file=Path("test.step"), line=5, column=10)
        error = undefined_variable_error("my_var", loc)
        
        assert error.code == ErrorCode.E401
        assert "my_var" in error.message
        assert "not been defined" in error.message
    
    def test_undefined_step_error(self):
        loc = SourceLocation(file=Path("test.step"), line=5, column=10)
        error = undefined_step_error(
            "say_helo",
            loc,
            suggestion="say_hello",
            available="say_hello, greet_user"
        )
        
        assert error.code == ErrorCode.E402
        assert "say_helo" in error.message
        assert "say_hello" in error.hint
    
    def test_division_by_zero_error(self):
        loc = SourceLocation(file=Path("test.step"), line=5, column=10)
        error = division_by_zero_error("divisor", loc)

        assert error.code == ErrorCode.E404
        assert "divide by zero" in error.message.lower()
    
    def test_type_mismatch_error(self):
        loc = SourceLocation(file=Path("test.step"), line=5, column=10)
        error = type_mismatch_error("count", "number", "text", loc)
        
        assert error.code == ErrorCode.E301
        assert "count" in error.message
        assert "number" in error.message
        assert "text" in error.message
    
    def test_make_error_unknown_code(self):
        loc = SourceLocation(file=Path("test.step"), line=1, column=1)
        error = make_error("UNKNOWN", loc)
        
        assert error.code == "UNKNOWN"
        assert "Unknown error" in error.message


class TestErrorCodes:
    """Tests for error code constants."""
    
    def test_structure_errors(self):
        assert ErrorCode.E001 == "E001"
        assert ErrorCode.E002 == "E002"
        assert ErrorCode.E003 == "E003"
        assert ErrorCode.E004 == "E004"
    
    def test_lexer_errors(self):
        assert ErrorCode.E101 == "E101"
        assert ErrorCode.E102 == "E102"
        assert ErrorCode.E103 == "E103"
        assert ErrorCode.E104 == "E104"
        assert ErrorCode.E105 == "E105"
    
    def test_parser_errors(self):
        assert ErrorCode.E201 == "E201"
        assert ErrorCode.E206 == "E206"
    
    def test_runtime_errors(self):
        assert ErrorCode.E401 == "E401"
        assert ErrorCode.E403 == "E403"
