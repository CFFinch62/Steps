"""Random number operations."""

import random as _random
from typing import Optional

from ..types import StepsValue, StepsNumber, StepsList
from ..errors import StepsTypeError, StepsRuntimeError, ErrorCode, SourceLocation


def random_int(
    min_val: StepsValue,
    max_val: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Generate a random integer between min and max (inclusive)."""
    if not isinstance(min_val, StepsNumber) or not isinstance(max_val, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"random_int requires two numbers, got {min_val.type_name()} and {max_val.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use: call random_int with 1, 100"
        )
    
    min_i = int(min_val.value)
    max_i = int(max_val.value)
    
    if min_i > max_i:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"random_int: minimum ({min_i}) cannot be greater than maximum ({max_i}).",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Swap the values: call random_int with smaller, larger"
        )
    
    return StepsNumber(float(_random.randint(min_i, max_i)))


def random_choice(
    lst: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsValue:
    """Pick a random element from a list."""
    if not isinstance(lst, StepsList):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"random_choice requires a list, got {lst.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use: call random_choice with my_list"
        )
    
    if lst.length() == 0:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message="random_choice: cannot pick from an empty list.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Make sure the list has at least one element."
        )
    
    return _random.choice(lst.elements)
