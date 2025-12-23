"""Text operations including new string handling functions."""

from typing import Optional

from ..types import (
    StepsValue, StepsNumber, StepsText, StepsBoolean, StepsList,
    StepsTable
)
from ..errors import StepsTypeError, StepsRuntimeError, ErrorCode, SourceLocation


def text_concatenate(
    left: StepsValue, 
    right: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsText:
    """Concatenate two text values."""
    # Convert both to text
    left_text = left.as_text()
    right_text = right.as_text()
    return left_text.added_to(right_text)


def text_split(
    text: StepsValue, 
    delimiter: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsList:
    """Split text by delimiter."""
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot split {text.type_name()}, only text can be split.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Make sure the value you're splitting is text."
        )
    
    delim_str = delimiter.as_text().value
    return text.split_by(delim_str)


def text_length(
    value: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Get length of text or collection."""
    if isinstance(value, StepsText):
        return StepsNumber(float(value.length()))
    elif isinstance(value, StepsList):
        return StepsNumber(float(value.length()))
    elif isinstance(value, StepsTable):
        return StepsNumber(float(value.length()))
    else:
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot get length of {value.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="'length of' works with text, lists, and tables."
        )


def text_character_at(
    text: StepsValue,
    index: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsText:
    """Get character at index in text."""
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot get character from {text.type_name()}, only from text.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="'character at' only works with text values."
        )
    
    if not isinstance(index, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Character index must be a number, not {index.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use a number for the index, like 'character at 0 of text'."
        )
    
    idx = int(index.value)
    try:
        return text.character_at(idx)
    except IndexError:
        raise StepsRuntimeError(
            code=ErrorCode.E405,
            message=f"Character index {idx} is out of bounds for text of length {text.length()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint=f"Valid indices are 0 to {text.length() - 1}."
        )


def text_contains(
    text: StepsValue, 
    substring: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsBoolean:
    """Check if text contains substring."""
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot check if {text.type_name()} contains something.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="'contains' works with text values."
        )
    
    substr = substring.as_text().value
    return text.contains(substr)


def text_starts_with(
    text: StepsValue, 
    prefix: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsBoolean:
    """Check if text starts with prefix."""
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot check if {text.type_name()} starts with something.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="'starts with' works with text values."
        )
    
    pref = prefix.as_text().value
    return text.starts_with(pref)


def text_ends_with(
    text: StepsValue, 
    suffix: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsBoolean:
    """Check if text ends with suffix."""
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot check if {text.type_name()} ends with something.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="'ends with' works with text values."
        )
    
    suf = suffix.as_text().value
    return text.ends_with(suf)


# =============================================================================
# New String Functions
# =============================================================================

def text_slice(
    text: StepsValue,
    start: StepsValue,
    end: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsText:
    """Extract a substring from start to end index.
    
    Args:
        text: The text to slice
        start: Starting index (inclusive, 0-based)
        end: Ending index (exclusive)
        
    Returns:
        The substring from start to end
    """
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot slice {text.type_name()}, only text can be sliced.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use: call slice with my_text, 0, 5"
        )
    
    if not isinstance(start, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Start index must be a number, got {start.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use numbers for slice indices."
        )
    
    if not isinstance(end, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"End index must be a number, got {end.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use numbers for slice indices."
        )
    
    start_idx = int(start.value)
    end_idx = int(end.value)
    
    # Python handles out-of-bounds slicing gracefully
    return StepsText(text.value[start_idx:end_idx])


def text_lowercase(
    text: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsText:
    """Convert text to lowercase."""
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot convert {text.type_name()} to lowercase, only text.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use: call lowercase with my_text"
        )
    
    return StepsText(text.value.lower())


def text_uppercase(
    text: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsText:
    """Convert text to uppercase."""
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot convert {text.type_name()} to uppercase, only text.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use: call uppercase with my_text"
        )
    
    return StepsText(text.value.upper())


def text_trim(
    text: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsText:
    """Remove leading and trailing whitespace from text."""
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot trim {text.type_name()}, only text.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use: call trim with my_text"
        )
    
    return StepsText(text.value.strip())


def text_index_of(
    text: StepsValue,
    search: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Find the index of a substring in text.
    
    Returns -1 if not found.
    """
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot search in {text.type_name()}, only in text.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use: call index_of with my_text, search_term"
        )
    
    search_str = search.as_text().value
    return StepsNumber(float(text.value.find(search_str)))


def text_replace(
    text: StepsValue,
    old: StepsValue,
    new: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsText:
    """Replace all occurrences of 'old' with 'new' in text."""
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot replace in {text.type_name()}, only in text.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use: call replace with my_text, old_text, new_text"
        )
    
    old_str = old.as_text().value
    new_str = new.as_text().value
    return StepsText(text.value.replace(old_str, new_str))


def text_characters(
    text: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsList:
    """Convert text to a list of individual characters.
    
    This allows iterating over a string letter by letter:
        call characters with my_text storing result in char_list
        repeat for each char in char_list
            display char
    """
    if not isinstance(text, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot get characters from {text.type_name()}, only from text.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use: call characters with my_text"
        )
    
    # Convert each character to a StepsText and put in a list
    char_list = [StepsText(c) for c in text.value]
    return StepsList(char_list)

