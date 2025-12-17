"""Steps Builtins - Built-in Operations and Functions.

This module provides built-in operations that are used by the interpreter
to implement Steps language features.
"""

from typing import List, Optional

from .types import (
    StepsValue, StepsNumber, StepsText, StepsBoolean, 
    StepsList, StepsTable, StepsNothing, make_value
)
from .errors import StepsRuntimeError, StepsTypeError, SourceLocation, ErrorCode


# =============================================================================
# Type Checking Operations
# =============================================================================


def _validate_type(
    value: StepsValue, 
    expected_type: type, 
    op_name: str, 
    location: Optional[SourceLocation] = None
) -> None:
    """Validate that a value is of the expected type."""
    if not isinstance(value, expected_type):
        # Map class to nice name
        type_map = {
            StepsNumber: "number",
            StepsText: "text",
            StepsBoolean: "boolean",
            StepsList: "list",
            StepsTable: "table",
            StepsNothing: "nothing"
        }
        expected_name = type_map.get(expected_type, expected_type.__name__)
        
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"'{op_name}' requires a {expected_name}, but got a {value.type_name()}.",
            file=location.file if location else Path("<unknown>"),
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint=f"Ensure the value passed to '{op_name}' is a {expected_name}."
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


# =============================================================================
# Type Conversion Operations
# =============================================================================

def convert_to_number(
    value: StepsValue, 
    location: Optional[SourceLocation] = None
) -> StepsNumber:
    """Convert a value to a number.
    
    Raises:
        StepsTypeError: If conversion fails
    """
    try:
        return value.as_number()
    except ValueError as e:
        raise StepsTypeError(
            code=ErrorCode.E301,
            message=f"Cannot convert {value.type_name()} value to number.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint=f"The value '{value.display_string()}' cannot be interpreted as a number."
        )


def convert_to_text(value: StepsValue) -> StepsText:
    """Convert a value to text."""
    return value.as_text()


def uppercase(text: StepsValue) -> StepsText:
    """Convert text to uppercase."""
    _validate_type(text, StepsText, "uppercase")
    return StepsText(text.value.upper())


def format_number_string(value: StepsValue, places: StepsValue) -> StepsText:
    """Format a number with specific decimal places."""
    _validate_type(value, StepsNumber, "format number")
    _validate_type(places, StepsNumber, "format number decimal places")
    
    try:
        places_int = int(places.value)
        if places_int < 0:
            raise ValueError("Decimal places cannot be negative")
            
        formatted = f"{value.value:.{places_int}f}"
        return StepsText(formatted)
    except ValueError as e:
        # Should catch conversion errors or negative places
        raise StepsRuntimeError(
            code=ErrorCode.E304, # Using Generic Runtime Error for now
            message=f"Invalid decimal places: {e}",
            file=Path("builtins"),
            line=0,
            column=0
        )



def convert_to_boolean(value: StepsValue) -> StepsBoolean:
    """Convert a value to a boolean."""
    return value.as_boolean()


# =============================================================================
# Arithmetic Operations
# =============================================================================

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
            hint="The '+' operator works with numbers. Use 'added to' for text concatenation."
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
            hint="The '-' operator only works with numbers."
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
            hint="The '*' operator only works with numbers."
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
            hint="The '/' operator only works with numbers."
        )
    
    if right.value == 0:
        raise StepsRuntimeError(
            code=ErrorCode.E404,
            message="Cannot divide by zero.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check that your divisor is not zero before dividing."
        )
    
    return left / right


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
            hint="The unary '-' operator only works with numbers."
        )
    return -value


# =============================================================================
# Comparison Operations
# =============================================================================

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


# =============================================================================
# Boolean Operations
# =============================================================================

def boolean_and(left: StepsValue, right: StepsValue) -> StepsBoolean:
    """Logical AND of two values."""
    return StepsBoolean(left.is_truthy() and right.is_truthy())


def boolean_or(left: StepsValue, right: StepsValue) -> StepsBoolean:
    """Logical OR of two values."""
    return StepsBoolean(left.is_truthy() or right.is_truthy())


def boolean_not(value: StepsValue) -> StepsBoolean:
    """Logical NOT of a value."""
    return StepsBoolean(not value.is_truthy())


# =============================================================================
# Text Operations
# =============================================================================

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
# List Operations
# =============================================================================

def list_add(
    lst: StepsValue, 
    item: StepsValue,
    location: Optional[SourceLocation] = None
) -> None:
    """Add an item to a list (mutates the list)."""
    if not isinstance(lst, StepsList):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot add to {lst.type_name()}, only to lists.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Make sure you're adding to a list variable."
        )
    lst.add(item)


def list_remove(
    lst: StepsValue, 
    item: StepsValue,
    location: Optional[SourceLocation] = None
) -> bool:
    """Remove an item from a list (mutates the list). Returns True if found."""
    if not isinstance(lst, StepsList):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot remove from {lst.type_name()}, only from lists.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Make sure you're removing from a list variable."
        )
    return lst.remove(item)


def list_get(
    lst: StepsValue, 
    index: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsValue:
    """Get item at index from list."""
    if not isinstance(lst, StepsList):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot index into {lst.type_name()}, only into lists or tables.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use square brackets only with lists and tables."
        )
    
    if not isinstance(index, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"List index must be a number, not {index.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use a number for list indices, like 'my_list[0]'."
        )
    
    idx = int(index.value)
    try:
        return lst.get(idx)
    except IndexError:
        raise StepsRuntimeError(
            code=ErrorCode.E405,
            message=f"List index {idx} is out of bounds for list of length {lst.length()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint=f"Valid indices are 0 to {lst.length() - 1}."
        )


def list_contains(
    collection: StepsValue, 
    item: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsBoolean:
    """Check if item is in collection (list)."""
    if isinstance(collection, StepsList):
        return collection.contains(item)
    elif isinstance(collection, StepsText):
        # For text, check substring
        substr = item.as_text().value
        return collection.contains(substr)
    else:
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot check if something is in {collection.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="'is in' works with lists and text."
        )


# =============================================================================
# Table Operations
# =============================================================================

def table_get(
    table: StepsValue, 
    key: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsValue:
    """Get value for key from table."""
    if not isinstance(table, StepsTable):
        # Could be list access
        if isinstance(table, StepsList):
            return list_get(table, key, location)
        
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot access {table.type_name()} with a key.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use square brackets with tables (using text keys) or lists (using number indices)."
        )
    
    key_str = key.as_text().value
    try:
        return table.get(key_str)
    except KeyError as e:
        raise StepsRuntimeError(
            code=ErrorCode.E406,
            message=f"Key '{key_str}' not found in table.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint=f"Available keys: {', '.join(table.pairs.keys()) if table.pairs else '(empty table)'}"
        )


def table_set(
    container: StepsValue, 
    key: StepsValue, 
    value: StepsValue,
    location: Optional[SourceLocation] = None
) -> None:
    """Set value for key in table or index in list (mutates the container)."""
    # Handle list assignment
    if isinstance(container, StepsList):
        if not isinstance(key, StepsNumber):
            raise StepsTypeError(
                code=ErrorCode.E302,
                message=f"List index must be a number, got {key.type_name()}.",
                file=location.file if location else None,
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint="Use a number like 0, 1, 2 to access list elements."
            )
        
        index = int(key.value)
        if index < 0 or index >= len(container.elements):
            raise StepsRuntimeError(
                code=ErrorCode.E304,
                message=f"List index {index} out of range. List has {len(container.elements)} element(s).",
                file=location.file if location else None,
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint=f"Valid indices are 0 to {len(container.elements) - 1}."
            )
        
        container.elements[index] = value
        return
    
    # Handle table assignment
    if isinstance(container, StepsTable):
        key_str = key.as_text().value
        container.set(key_str, value)
        return
    
    raise StepsTypeError(
        code=ErrorCode.E302,
        message=f"Cannot set index on {container.type_name()}, only on lists and tables.",
        file=location.file if location else None,
        line=location.line if location else 0,
        column=location.column if location else 0,
        hint="Use square brackets to set values only on lists and tables."
    )



def table_has_key(
    table: StepsValue, 
    key: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsBoolean:
    """Check if table has a key."""
    if not isinstance(table, StepsTable):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"Cannot check keys on {table.type_name()}, only on tables.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use 'has key' only with tables."
        )
    
    key_str = key.as_text().value
    return table.has_key(key_str)


# =============================================================================
# Random Number Operations
# =============================================================================

import random as _random

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


# =============================================================================
# File I/O Operations
# =============================================================================

import csv as _csv
from io import StringIO as _StringIO

def read_file(
    path: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsText:
    """Read entire contents of a text file."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"read_file requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call read_file with "myfile.txt"'
        )
    
    try:
        with open(path.value, 'r', encoding='utf-8') as f:
            return StepsText(f.read())
    except FileNotFoundError:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"File not found: '{path.value}'",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check that the file path is correct."
        )
    except IOError as e:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Could not read file '{path.value}': {e}",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check file permissions."
        )


def write_file(
    path: StepsValue,
    content: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNothing:
    """Write content to a text file (overwrites existing)."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"write_file requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call write_file with "myfile.txt", content'
        )
    
    text_content = content.as_text().value
    
    try:
        with open(path.value, 'w', encoding='utf-8') as f:
            f.write(text_content)
        return StepsNothing()
    except IOError as e:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Could not write to file '{path.value}': {e}",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check file permissions and path."
        )


def append_file(
    path: StepsValue,
    content: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNothing:
    """Append content to a text file."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"append_file requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call append_file with "myfile.txt", content'
        )
    
    text_content = content.as_text().value
    
    try:
        with open(path.value, 'a', encoding='utf-8') as f:
            f.write(text_content)
        return StepsNothing()
    except IOError as e:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Could not append to file '{path.value}': {e}",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check file permissions and path."
        )


def file_exists(
    path: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsBoolean:
    """Check if a file exists."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"file_exists requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call file_exists with "myfile.txt"'
        )
    
    import os
    return StepsBoolean(os.path.isfile(path.value))


def read_csv(
    path: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsList:
    """Read a CSV file and return a list of tables (each row is a table)."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"read_csv requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call read_csv with "data.csv"'
        )
    
    try:
        with open(path.value, 'r', encoding='utf-8', newline='') as f:
            reader = _csv.DictReader(f)
            rows = []
            for row in reader:
                # Convert each row (dict) to a StepsTable
                table = StepsTable({k: StepsText(v) for k, v in row.items()})
                rows.append(table)
            return StepsList(rows)
    except FileNotFoundError:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"CSV file not found: '{path.value}'",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check that the file path is correct."
        )
    except _csv.Error as e:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"CSV parsing error in '{path.value}': {e}",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check the CSV file format."
        )


def write_csv(
    path: StepsValue,
    data: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNothing:
    """Write a list of tables to a CSV file."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"write_csv requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call write_csv with "output.csv", data_list'
        )
    
    if not isinstance(data, StepsList):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"write_csv requires a list of tables, got {data.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Data must be a list of tables."
        )
    
    if data.length() == 0:
        # Write empty file
        try:
            with open(path.value, 'w', encoding='utf-8', newline='') as f:
                pass
            return StepsNothing()
        except IOError as e:
            raise StepsRuntimeError(
                code=ErrorCode.E407,
                message=f"Could not write CSV file '{path.value}': {e}",
                file=location.file if location else None,
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint="Check file permissions and path."
            )
    
    # Get headers from first row
    first_row = data.elements[0]
    if not isinstance(first_row, StepsTable):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message="write_csv: each element must be a table.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Each row should be a table with key-value pairs."
        )
    
    headers = list(first_row.pairs.keys())
    
    try:
        with open(path.value, 'w', encoding='utf-8', newline='') as f:
            writer = _csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for row in data.elements:
                if isinstance(row, StepsTable):
                    row_dict = {k: v.as_text().value for k, v in row.pairs.items()}
                    writer.writerow(row_dict)
        return StepsNothing()
    except IOError as e:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Could not write CSV file '{path.value}': {e}",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check file permissions and path."
        )


# =============================================================================
# Native Functions Registry
# =============================================================================
# These functions can be called directly from Steps stdlib via the interpreter.
# The interpreter checks this registry before looking for user-defined steps.

NATIVE_FUNCTIONS = {
    # Random functions
    "random_int": {
        "function": random_int,
        "params": ["min_val", "max_val"],
    },
    "random_choice": {
        "function": random_choice,
        "params": ["lst"],
    },
    # File I/O functions
    "read_file": {
        "function": read_file,
        "params": ["path"],
    },
    "write_file": {
        "function": write_file,
        "params": ["path", "content"],
    },
    "append_file": {
        "function": append_file,
        "params": ["path", "content"],
    },
    "file_exists": {
        "function": file_exists,
        "params": ["path"],
    },
    # CSV functions
    "read_csv": {
        "function": read_csv,
        "params": ["path"],
    },
    "write_csv": {
        "function": write_csv,
        "params": ["path", "data"],
    },
}
