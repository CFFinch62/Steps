"""List aggregate math operations (min, max, sum for numeric lists)."""

from typing import Optional

from ..types import StepsValue, StepsNumber, StepsList
from ..errors import StepsTypeError, StepsRuntimeError, ErrorCode, SourceLocation


def _validate_numeric_list(lst: StepsValue, fn_name: str, location: Optional[SourceLocation] = None) -> list:
    """Validate that value is a non-empty list of numbers and return Python float list."""
    if not isinstance(lst, StepsList):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"'{fn_name}' requires a list, got {lst.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint=f"Pass a list of numbers to '{fn_name}', e.g. call {fn_name} with [1, 2, 3]"
        )

    if lst.length() == 0:
        raise StepsRuntimeError(
            code=ErrorCode.E405,
            message=f"'{fn_name}' cannot operate on an empty list.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Make sure the list has at least one number in it."
        )

    numbers = []
    for i, elem in enumerate(lst.elements):
        if not isinstance(elem, StepsNumber):
            raise StepsTypeError(
                code=ErrorCode.E302,
                message=f"'{fn_name}' requires a list of numbers, but item at index {i} is a {elem.type_name()}.",
                file=location.file if location else None,
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint="All items in the list must be numbers."
            )
        numbers.append(elem.value)

    return numbers


def list_min(
    lst: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Return the smallest number in a numeric list."""
    numbers = _validate_numeric_list(lst, "list_min", location)
    return StepsNumber(min(numbers))


def list_max(
    lst: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Return the largest number in a numeric list."""
    numbers = _validate_numeric_list(lst, "list_max", location)
    return StepsNumber(max(numbers))


def list_sum(
    lst: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Return the sum of all numbers in a numeric list."""
    numbers = _validate_numeric_list(lst, "list_sum", location)
    return StepsNumber(sum(numbers))

