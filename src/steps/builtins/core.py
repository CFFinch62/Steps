"""Core utilities and type checking operations."""

from typing import Optional

from ..types import (
    StepsValue, StepsNumber, StepsText, StepsBoolean,
    StepsList, StepsTable, StepsNothing
)
from ..errors import StepsTypeError, ErrorCode, SourceLocation


def _validate_type(
    value: StepsValue, 
    expected_type: type, 
    op_name: str, 
    location: Optional[SourceLocation] = None
) -> None:
    """Validate that a value is of the expected type.
    
    Args:
        value: The value to check
        expected_type: The expected Steps type
        op_name: Name of the operation (for error messages)
        location: Source location for error reporting
        
    Raises:
        StepsTypeError: If the value is not of the expected type
    """
    if not isinstance(value, expected_type):
        expected_name = {
            StepsNumber: "number",
            StepsText: "text",
            StepsBoolean: "boolean",
            StepsList: "list",
            StepsTable: "table",
        }.get(expected_type, expected_type.__name__)
        
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"'{op_name}' requires a {expected_name}, but got {value.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint=f"Make sure you're using a {expected_name} value."
        )


def type_of(value: StepsValue) -> str:
    """Get the type name of a Steps value."""
    return value.type_name()


def is_number(value: StepsValue) -> bool:
    """Check if value is a number."""
    return isinstance(value, StepsNumber)


def is_text(value: StepsValue) -> bool:
    """Check if value is text."""
    return isinstance(value, StepsText)


def is_boolean(value: StepsValue) -> bool:
    """Check if value is a boolean."""
    return isinstance(value, StepsBoolean)


def is_list(value: StepsValue) -> bool:
    """Check if value is a list."""
    return isinstance(value, StepsList)


def is_table(value: StepsValue) -> bool:
    """Check if value is a table."""
    return isinstance(value, StepsTable)


def is_nothing(value: StepsValue) -> bool:
    """Check if value is nothing."""
    return isinstance(value, StepsNothing)
