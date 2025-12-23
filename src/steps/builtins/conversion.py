"""Type conversion operations."""

from typing import Optional

from ..types import (
    StepsValue, StepsNumber, StepsText, StepsBoolean
)
from ..errors import StepsTypeError, ErrorCode, SourceLocation


def convert_to_number(
    value: StepsValue, 
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Convert a value to a number.
    
    Raises:
        StepsTypeError: If conversion fails
    """
    if isinstance(value, StepsNumber):
        return value
    elif isinstance(value, StepsText):
        try:
            return StepsNumber(float(value.value))
        except ValueError:
            raise StepsTypeError(
                code=ErrorCode.E302,
                message=f"Cannot convert text '{value.value}' to a number.",
                file=location.file if location else None,
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint="Text must contain a valid number like '42' or '3.14'."
            )
    elif isinstance(value, StepsBoolean):
        return StepsNumber(1.0 if value.value else 0.0)
    else:
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot convert {value.type_name()} to a number.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Only text, numbers, and booleans can be converted to numbers."
        )


def convert_to_text(value: StepsValue) -> StepsText:
    """Convert a value to text."""
    return value.as_text()


def convert_to_boolean(value: StepsValue) -> StepsBoolean:
    """Convert a value to a boolean."""
    return StepsBoolean(value.is_truthy())


def format_number_string(value: StepsValue, places: StepsValue) -> StepsText:
    """Format a number with specific decimal places."""
    if not isinstance(value, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot format {value.type_name()} as decimal, expected a number.",
            file=None,
            line=0,
            column=0,
            hint="Use 'as decimal' only with number values."
        )
    
    if not isinstance(places, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Decimal places must be a number, got {places.type_name()}.",
            file=None,
            line=0,
            column=0,
            hint="Use a number like 2 for 'as decimal(2)'."
        )
    
    decimal_places = int(places.value)
    if decimal_places < 0:
        decimal_places = 0
    
    formatted = f"{value.value:.{decimal_places}f}"
    return StepsText(formatted)
