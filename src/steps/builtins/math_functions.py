"""Advanced math functions: power, roots, trig, and logarithms."""

import math
from typing import Optional

from ..types import StepsValue, StepsNumber
from ..errors import StepsTypeError, StepsRuntimeError, ErrorCode, SourceLocation


def _require_number(value: StepsValue, fn_name: str, location: Optional[SourceLocation] = None) -> None:
    """Validate that value is a StepsNumber."""
    if not isinstance(value, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"'{fn_name}' requires a number, got {value.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint=f"Make sure you pass a number to '{fn_name}'."
        )


# ---------------------------------------------------------------------------
# Power / root
# ---------------------------------------------------------------------------

def math_square(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return n squared (n²)."""
    _require_number(n, "sqr", location)
    return StepsNumber(n.value ** 2)


def math_sqrt(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the square root of n."""
    _require_number(n, "sqrt", location)
    if n.value < 0:
        raise StepsRuntimeError(
            code=ErrorCode.E304,
            message=f"Cannot take the square root of a negative number ({n.value}).",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Square root is only defined for zero and positive numbers."
        )
    return StepsNumber(math.sqrt(n.value))


def math_pow(base: StepsValue, exp: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return base raised to the power of exp."""
    _require_number(base, "pow", location)
    _require_number(exp, "pow", location)
    return StepsNumber(math.pow(base.value, exp.value))


def math_pi(location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the mathematical constant π (≈ 3.14159)."""
    return StepsNumber(math.pi)


# ---------------------------------------------------------------------------
# Trigonometry  (angles in radians)
# ---------------------------------------------------------------------------

def math_sin(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the sine of n (radians)."""
    _require_number(n, "sin", location)
    return StepsNumber(math.sin(n.value))


def math_cos(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the cosine of n (radians)."""
    _require_number(n, "cos", location)
    return StepsNumber(math.cos(n.value))


def math_tan(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the tangent of n (radians)."""
    _require_number(n, "tan", location)
    return StepsNumber(math.tan(n.value))


def math_asin(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the arcsine of n in radians. Input must be between -1 and 1."""
    _require_number(n, "asin", location)
    if not (-1.0 <= n.value <= 1.0):
        raise StepsRuntimeError(
            code=ErrorCode.E304,
            message=f"'asin' input must be between -1 and 1, got {n.value}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Arcsine is only defined for values in the range [-1, 1]."
        )
    return StepsNumber(math.asin(n.value))


def math_acos(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the arccosine of n in radians. Input must be between -1 and 1."""
    _require_number(n, "acos", location)
    if not (-1.0 <= n.value <= 1.0):
        raise StepsRuntimeError(
            code=ErrorCode.E304,
            message=f"'acos' input must be between -1 and 1, got {n.value}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Arccosine is only defined for values in the range [-1, 1]."
        )
    return StepsNumber(math.acos(n.value))


def math_atan(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the arctangent of n in radians."""
    _require_number(n, "atan", location)
    return StepsNumber(math.atan(n.value))


def math_atan2(y: StepsValue, x: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the angle in radians between the positive x-axis and the point (x, y)."""
    _require_number(y, "atan2", location)
    _require_number(x, "atan2", location)
    return StepsNumber(math.atan2(y.value, x.value))


def math_degrees(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Convert radians to degrees."""
    _require_number(n, "degrees", location)
    return StepsNumber(math.degrees(n.value))


def math_radians(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Convert degrees to radians."""
    _require_number(n, "radians", location)
    return StepsNumber(math.radians(n.value))


# ---------------------------------------------------------------------------
# Logarithms and exponentials
# ---------------------------------------------------------------------------

def _require_positive(n: StepsValue, fn_name: str, location: Optional[SourceLocation] = None) -> None:
    """Validate that value is a positive number (for log functions)."""
    if n.value <= 0:
        raise StepsRuntimeError(
            code=ErrorCode.E304,
            message=f"'{fn_name}' requires a positive number, got {n.value}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Logarithms are only defined for positive numbers."
        )


def math_log(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the natural logarithm (base e) of n."""
    _require_number(n, "log", location)
    _require_positive(n, "log", location)
    return StepsNumber(math.log(n.value))


def math_log10(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the base-10 logarithm of n."""
    _require_number(n, "log10", location)
    _require_positive(n, "log10", location)
    return StepsNumber(math.log10(n.value))


def math_log2(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the base-2 logarithm of n."""
    _require_number(n, "log2", location)
    _require_positive(n, "log2", location)
    return StepsNumber(math.log2(n.value))


def math_exp(n: StepsValue, location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return e raised to the power of n."""
    _require_number(n, "exp", location)
    return StepsNumber(math.exp(n.value))

