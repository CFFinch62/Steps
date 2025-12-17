"""Steps Type System.

This module implements the runtime value types for the Steps language:
- StepsNumber: Numeric values (integers and decimals)
- StepsText: String values
- StepsBoolean: True/false values
- StepsList: Ordered collections
- StepsTable: Key-value mappings
- StepsNothing: Represents the absence of a value
"""

from dataclasses import dataclass, field
from typing import Any, Dict, Iterator, List, Optional, Union
from abc import ABC, abstractmethod


class StepsValue(ABC):
    """Base class for all Steps runtime values.
    
    All Steps values must implement methods for type conversion,
    truthiness, and string representation.
    """
    
    @abstractmethod
    def python_value(self) -> Any:
        """Return the underlying Python value."""
        pass
    
    @abstractmethod
    def type_name(self) -> str:
        """Return the Steps type name."""
        pass
    
    @abstractmethod
    def is_truthy(self) -> bool:
        """Return whether this value is truthy in boolean context."""
        pass
    
    @abstractmethod
    def display_string(self) -> str:
        """Return string representation for display."""
        pass
    
    def as_number(self) -> "StepsNumber":
        """Convert this value to a StepsNumber.
        
        Raises:
            ValueError: If conversion is not possible
        """
        raise ValueError(f"Cannot convert {self.type_name()} to number")
    
    def as_text(self) -> "StepsText":
        """Convert this value to a StepsText."""
        return StepsText(self.display_string())
    
    def as_boolean(self) -> "StepsBoolean":
        """Convert this value to a StepsBoolean."""
        return StepsBoolean(self.is_truthy())
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StepsValue):
            return False
        return bool(self.python_value() == other.python_value())
    
    def __hash__(self) -> int:
        val = self.python_value()
        if isinstance(val, (list, dict)):
            return id(self)  # Mutable types use identity
        return hash(val)


@dataclass
class StepsNumber(StepsValue):
    """Numeric value (integer or decimal)."""
    value: float
    
    def python_value(self) -> float:
        return self.value
    
    def type_name(self) -> str:
        return "number"
    
    def is_truthy(self) -> bool:
        return self.value != 0
    
    def display_string(self) -> str:
        # Display integers without decimal point
        if self.value == int(self.value):
            return str(int(self.value))
        return str(self.value)
    
    def as_number(self) -> "StepsNumber":
        return self
    
    # Arithmetic operations
    def __add__(self, other: "StepsNumber") -> "StepsNumber":
        if isinstance(other, StepsNumber):
            return StepsNumber(self.value + other.value)
        return NotImplemented
    
    def __sub__(self, other: "StepsNumber") -> "StepsNumber":
        if isinstance(other, StepsNumber):
            return StepsNumber(self.value - other.value)
        return NotImplemented
    
    def __mul__(self, other: "StepsNumber") -> "StepsNumber":
        if isinstance(other, StepsNumber):
            return StepsNumber(self.value * other.value)
        return NotImplemented
    
    def __truediv__(self, other: "StepsNumber") -> "StepsNumber":
        if isinstance(other, StepsNumber):
            if other.value == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return StepsNumber(self.value / other.value)
        return NotImplemented
    
    def __neg__(self) -> "StepsNumber":
        return StepsNumber(-self.value)
    
    # Comparison operations
    def __lt__(self, other: "StepsNumber") -> bool:
        if isinstance(other, StepsNumber):
            return self.value < other.value
        return NotImplemented
    
    def __le__(self, other: "StepsNumber") -> bool:
        if isinstance(other, StepsNumber):
            return self.value <= other.value
        return NotImplemented
    
    def __gt__(self, other: "StepsNumber") -> bool:
        if isinstance(other, StepsNumber):
            return self.value > other.value
        return NotImplemented
    
    def __ge__(self, other: "StepsNumber") -> bool:
        if isinstance(other, StepsNumber):
            return self.value >= other.value
        return NotImplemented


@dataclass
class StepsText(StepsValue):
    """String value."""
    value: str
    
    def python_value(self) -> str:
        return self.value
    
    def type_name(self) -> str:
        return "text"
    
    def is_truthy(self) -> bool:
        return len(self.value) > 0
    
    def display_string(self) -> str:
        return self.value
    
    def as_number(self) -> StepsNumber:
        try:
            return StepsNumber(float(self.value))
        except ValueError:
            raise ValueError(f'Cannot convert "{self.value}" to number')
    
    def as_text(self) -> "StepsText":
        return self
    
    # Text operations
    def added_to(self, other: "StepsText") -> "StepsText":
        """Concatenate with another text value."""
        return StepsText(self.value + other.value)
    
    def split_by(self, delimiter: str) -> "StepsList":
        """Split text by delimiter."""
        parts = self.value.split(delimiter)
        return StepsList([StepsText(part) for part in parts])
    
    def character_at(self, index: int) -> "StepsText":
        """Get character at index."""
        if index < 0 or index >= len(self.value):
            raise IndexError(f"Index {index} out of bounds for text of length {len(self.value)}")
        return StepsText(self.value[index])
    
    def length(self) -> int:
        """Get text length."""
        return len(self.value)
    
    def contains(self, substring: str) -> "StepsBoolean":
        """Check if text contains substring."""
        return StepsBoolean(substring in self.value)
    
    def starts_with(self, prefix: str) -> "StepsBoolean":
        """Check if text starts with prefix."""
        return StepsBoolean(self.value.startswith(prefix))
    
    def ends_with(self, suffix: str) -> "StepsBoolean":
        """Check if text ends with suffix."""
        return StepsBoolean(self.value.endswith(suffix))


@dataclass
class StepsBoolean(StepsValue):
    """Boolean value (true or false)."""
    value: bool
    
    def python_value(self) -> bool:
        return self.value
    
    def type_name(self) -> str:
        return "boolean"
    
    def is_truthy(self) -> bool:
        return self.value
    
    def display_string(self) -> str:
        return "true" if self.value else "false"
    
    def as_number(self) -> StepsNumber:
        return StepsNumber(1.0 if self.value else 0.0)
    
    def as_boolean(self) -> "StepsBoolean":
        return self
    
    # Boolean operations
    def __and__(self, other: "StepsBoolean") -> "StepsBoolean":
        if isinstance(other, StepsBoolean):
            return StepsBoolean(self.value and other.value)
        return NotImplemented
    
    def __or__(self, other: "StepsBoolean") -> "StepsBoolean":
        if isinstance(other, StepsBoolean):
            return StepsBoolean(self.value or other.value)
        return NotImplemented
    
    def __invert__(self) -> "StepsBoolean":
        return StepsBoolean(not self.value)


@dataclass
class StepsList(StepsValue):
    """Ordered collection of values."""
    elements: List[StepsValue] = field(default_factory=list)
    
    def python_value(self) -> List[Any]:
        return [elem.python_value() for elem in self.elements]
    
    def type_name(self) -> str:
        return "list"
    
    def is_truthy(self) -> bool:
        return len(self.elements) > 0
    
    def display_string(self) -> str:
        items = ", ".join(elem.display_string() for elem in self.elements)
        return f"[{items}]"
    
    def length(self) -> int:
        """Get list length."""
        return len(self.elements)
    
    def get(self, index: int) -> StepsValue:
        """Get element at index."""
        if index < 0 or index >= len(self.elements):
            raise IndexError(
                f"Index {index} out of bounds for list of length {len(self.elements)}"
            )
        return self.elements[index]
    
    def add(self, item: StepsValue) -> None:
        """Add item to end of list."""
        self.elements.append(item)
    
    def remove(self, item: StepsValue) -> bool:
        """Remove first occurrence of item. Returns True if found."""
        for i, elem in enumerate(self.elements):
            if elem == item:
                del self.elements[i]
                return True
        return False
    
    def contains(self, item: StepsValue) -> StepsBoolean:
        """Check if item is in list."""
        return StepsBoolean(item in self.elements)
    
    def __iter__(self) -> Iterator[StepsValue]:
        return iter(self.elements)


@dataclass
class StepsTable(StepsValue):
    """Key-value mapping."""
    pairs: Dict[str, StepsValue] = field(default_factory=dict)
    
    def python_value(self) -> Dict[str, Any]:
        return {k: v.python_value() for k, v in self.pairs.items()}
    
    def type_name(self) -> str:
        return "table"
    
    def is_truthy(self) -> bool:
        return len(self.pairs) > 0
    
    def display_string(self) -> str:
        items = ", ".join(
            f'"{k}": {v.display_string()}' for k, v in self.pairs.items()
        )
        return f"[{items}]"
    
    def length(self) -> int:
        """Get number of key-value pairs."""
        return len(self.pairs)
    
    def get(self, key: str) -> StepsValue:
        """Get value for key."""
        if key not in self.pairs:
            available = ", ".join(f'"{k}"' for k in self.pairs.keys())
            raise KeyError(f'Key "{key}" not found. Available keys: {available}')
        return self.pairs[key]
    
    def set(self, key: str, value: StepsValue) -> None:
        """Set value for key."""
        self.pairs[key] = value
    
    def has_key(self, key: str) -> StepsBoolean:
        """Check if key exists."""
        return StepsBoolean(key in self.pairs)
    
    def keys(self) -> "StepsList":
        """Get list of keys."""
        return StepsList([StepsText(k) for k in self.pairs.keys()])


@dataclass
class StepsNothing(StepsValue):
    """Represents 'nothing' - the absence of a value."""
    
    def python_value(self) -> None:
        return None
    
    def type_name(self) -> str:
        return "nothing"
    
    def is_truthy(self) -> bool:
        return False
    
    def display_string(self) -> str:
        return "nothing"
    
    def as_number(self) -> StepsNumber:
        raise ValueError("Cannot convert nothing to number")
    
    def as_boolean(self) -> StepsBoolean:
        return StepsBoolean(False)


# Type aliases for convenience
Value = Union[StepsNumber, StepsText, StepsBoolean, StepsList, StepsTable, StepsNothing]


def make_value(python_value: Any) -> StepsValue:
    """Convert a Python value to a Steps value.
    
    Args:
        python_value: A Python value (int, float, str, bool, list, dict, None)
    
    Returns:
        The corresponding StepsValue
    
    Raises:
        TypeError: If the Python value type is not supported
    """
    if python_value is None:
        return StepsNothing()
    elif isinstance(python_value, bool):  # Check before int (bool is subclass of int)
        return StepsBoolean(python_value)
    elif isinstance(python_value, (int, float)):
        return StepsNumber(float(python_value))
    elif isinstance(python_value, str):
        return StepsText(python_value)
    elif isinstance(python_value, list):
        return StepsList([make_value(item) for item in python_value])
    elif isinstance(python_value, dict):
        return StepsTable({str(k): make_value(v) for k, v in python_value.items()})
    elif isinstance(python_value, StepsValue):
        return python_value
    else:
        raise TypeError(f"Cannot convert {type(python_value).__name__} to Steps value")


def get_type_name(value: StepsValue) -> str:
    """Get the Steps type name for a value."""
    return value.type_name()


def is_same_type(a: StepsValue, b: StepsValue) -> bool:
    """Check if two values have the same Steps type."""
    return a.type_name() == b.type_name()
