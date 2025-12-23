"""Arithmetic operations."""

from typing import Optional

from ..types import StepsValue, StepsNumber
from ..errors import StepsTypeError, StepsRuntimeError, ErrorCode, SourceLocation


def add_numbers(
    left: StepsValue, 
    right: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Add two numbers."""
    if not isinstance(left, StepsNumber) or not isinstance(right, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot add {left.type_name()} and {right.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use 'added to' for text concatenation, or convert values to numbers."
        )
    return left + right


def subtract_numbers(
    left: StepsValue, 
    right: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Subtract two numbers."""
    if not isinstance(left, StepsNumber) or not isinstance(right, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot subtract {right.type_name()} from {left.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Subtraction only works with numbers."
        )
    return left - right


def multiply_numbers(
    left: StepsValue, 
    right: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Multiply two numbers."""
    if not isinstance(left, StepsNumber) or not isinstance(right, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot multiply {left.type_name()} and {right.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Multiplication only works with numbers."
        )
    return left * right


def divide_numbers(
    left: StepsValue, 
    right: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Divide two numbers."""
    if not isinstance(left, StepsNumber) or not isinstance(right, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot divide {left.type_name()} by {right.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Division only works with numbers."
        )
    
    if right.value == 0:
        raise StepsRuntimeError(
            code=ErrorCode.E304,
            message="Cannot divide by zero.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check that the divisor is not zero before dividing."
        )
    
    return left / right


def modulo_numbers(
    left: StepsValue, 
    right: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Compute modulo (remainder) of two numbers."""
    if not isinstance(left, StepsNumber) or not isinstance(right, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot compute modulo of {left.type_name()} and {right.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Modulo only works with numbers."
        )
    
    if right.value == 0:
        raise StepsRuntimeError(
            code=ErrorCode.E304,
            message="Cannot compute modulo with zero.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check that the divisor is not zero before using modulo."
        )
    
    return left % right


def negate_number(
    value: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Negate a number."""
    if not isinstance(value, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot negate {value.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Negation only works with numbers."
        )
    return -value
