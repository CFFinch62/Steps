"""List and table collection operations."""

from typing import Optional

from ..types import (
    StepsValue, StepsNumber, StepsText, StepsBoolean,
    StepsList, StepsTable
)
from ..errors import StepsTypeError, StepsRuntimeError, ErrorCode, SourceLocation


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


def list_create(
    size: StepsValue,
    value: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsList:
    """Create a list of a given size filled with a single value.

    This is a native builtin so the allocation happens at C speed inside
    Python rather than through thousands of interpreted loop iterations.

    Args:
        size:  Number of elements (must be a non-negative number)
        value: The value to fill every slot with

    Returns:
        A new StepsList with *size* copies of *value*
    """
    if not isinstance(size, StepsNumber):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"create_list size must be a number, got {size.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Use: call create_list with 100, true storing result in my_list"
        )

    n = int(size.value)
    if n < 0:
        raise StepsRuntimeError(
            code=ErrorCode.E301,
            message=f"create_list size must be >= 0, got {n}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Size must be a non-negative number."
        )

    # Python list multiplication is a C-level operation — this is the whole point.
    return StepsList([value] * n)


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
