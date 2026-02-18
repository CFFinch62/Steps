"""Date and time built-in functions.

Provides:
  time()          — current Unix timestamp (float seconds since epoch)
  date()          — today's date as "YYYY-MM-DD" text
  date_diff()     — days between two ISO date strings (date2 - date1)
"""

import time as _time
from datetime import date as _date
from typing import Optional

from ..types import StepsValue, StepsNumber, StepsText
from ..errors import StepsTypeError, StepsRuntimeError, ErrorCode, SourceLocation


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _require_date_text(
    value: StepsValue,
    param_name: str,
    fn_name: str,
    location: Optional[SourceLocation] = None,
) -> _date:
    """Validate a StepsText ISO date string and return a Python date object."""
    if not isinstance(value, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"'{fn_name}' requires a text date for '{param_name}', got {value.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint=f"Pass a date string in YYYY-MM-DD format, e.g. \"2024-06-15\".",
        )
    try:
        return _date.fromisoformat(value.value)
    except ValueError:
        raise StepsRuntimeError(
            code=ErrorCode.E304,
            message=f"'{fn_name}': '{value.value}' is not a valid date (expected YYYY-MM-DD).",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Dates must be in ISO format, e.g. \"2024-06-15\".",
        )


# ---------------------------------------------------------------------------
# Public functions
# ---------------------------------------------------------------------------

def time_now(location: Optional[SourceLocation] = None) -> StepsNumber:
    """Return the current Unix timestamp as a floating-point number.

    The value is seconds since the Unix epoch (1970-01-01 00:00:00 UTC),
    with sub-second precision suitable for performance timing.

    Example:
        call time storing result in start
        # ... code to measure ...
        call time storing result in finish
        set elapsed to finish - start
        display elapsed
    """
    return StepsNumber(_time.time())


def date_today(location: Optional[SourceLocation] = None) -> StepsText:
    """Return today's date as a text string in ISO format (YYYY-MM-DD).

    Example:
        call date storing result in today
        display today        # e.g. "2026-02-18"
    """
    return StepsText(_date.today().isoformat())


def date_diff(
    date1: StepsValue,
    date2: StepsValue,
    location: Optional[SourceLocation] = None,
) -> StepsNumber:
    """Return the number of days between two ISO date strings (date2 - date1).

    Result is positive when date2 is after date1, negative when before.

    Example:
        call date_diff with "2026-01-01", "2026-12-31" storing result in days
        display days        # 364
    """
    d1 = _require_date_text(date1, "date1", "date_diff", location)
    d2 = _require_date_text(date2, "date2", "date_diff", location)
    return StepsNumber(float((d2 - d1).days))

