"""Comparison and boolean operations."""

from typing import Optional

from ..types import StepsValue, StepsNumber, StepsBoolean
from ..errors import StepsTypeError, ErrorCode, SourceLocation


def equals(left: StepsValue, right: StepsValue) -> StepsBoolean:
    """Check if two values are equal."""
    return StepsBoolean(left == right)


def not_equals(left: StepsValue, right: StepsValue) -> StepsBoolean:
    """Check if two values are not equal."""
    return StepsBoolean(left != right)


def less_than(
    left: StepsValue, 
    right: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsBoolean:
    """Check if left < right (numbers only)."""
    if not isinstance(left, StepsNumber) or not isinstance(right, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot compare {left.type_name()} and {right.type_name()} with 'is less than'.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Numeric comparisons only work with numbers."
        )
    return StepsBoolean(left < right)


def greater_than(
    left: StepsValue, 
    right: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsBoolean:
    """Check if left > right (numbers only)."""
    if not isinstance(left, StepsNumber) or not isinstance(right, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot compare {left.type_name()} and {right.type_name()} with 'is greater than'.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Numeric comparisons only work with numbers."
        )
    return StepsBoolean(left > right)


def less_than_or_equal(
    left: StepsValue, 
    right: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsBoolean:
    """Check if left <= right (numbers only)."""
    if not isinstance(left, StepsNumber) or not isinstance(right, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot compare {left.type_name()} and {right.type_name()} with 'is less than or equal to'.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Numeric comparisons only work with numbers."
        )
    return StepsBoolean(left <= right)


def greater_than_or_equal(
    left: StepsValue, 
    right: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsBoolean:
    """Check if left >= right (numbers only)."""
    if not isinstance(left, StepsNumber) or not isinstance(right, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot compare {left.type_name()} and {right.type_name()} with 'is greater than or equal to'.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Numeric comparisons only work with numbers."
        )
    return StepsBoolean(left >= right)


def boolean_and(left: StepsValue, right: StepsValue) -> StepsBoolean:
    """Logical AND of two values."""
    return StepsBoolean(left.is_truthy() and right.is_truthy())


def boolean_or(left: StepsValue, right: StepsValue) -> StepsBoolean:
    """Logical OR of two values."""
    return StepsBoolean(left.is_truthy() or right.is_truthy())


def boolean_not(value: StepsValue) -> StepsBoolean:
    """Logical NOT of a value."""
    return StepsBoolean(not value.is_truthy())
