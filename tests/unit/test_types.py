"""Unit Tests for Steps Type System.

Tests for StepsNumber, StepsText, StepsBoolean, StepsList, 
StepsTable, StepsNothing, and type conversions.
"""

import pytest
from steps.types import (
    StepsNumber, StepsText, StepsBoolean, StepsList, 
    StepsTable, StepsNothing, make_value, get_type_name, is_same_type
)


class TestStepsNumber:
    """Tests for numeric type."""
    
    def test_integer_display(self):
        num = StepsNumber(42.0)
        assert num.display_string() == "42"
    
    def test_decimal_display(self):
        num = StepsNumber(3.14)
        assert num.display_string() == "3.14"
    
    def test_negative_number(self):
        num = StepsNumber(-7.0)
        assert num.display_string() == "-7"
    
    def test_truthiness_nonzero(self):
        assert StepsNumber(42.0).is_truthy() is True
    
    def test_truthiness_zero(self):
        assert StepsNumber(0.0).is_truthy() is False
    
    def test_addition(self):
        result = StepsNumber(10) + StepsNumber(5)
        assert result.value == 15
    
    def test_subtraction(self):
        result = StepsNumber(10) - StepsNumber(3)
        assert result.value == 7
    
    def test_multiplication(self):
        result = StepsNumber(6) * StepsNumber(7)
        assert result.value == 42
    
    def test_division(self):
        result = StepsNumber(20) / StepsNumber(4)
        assert result.value == 5
    
    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            StepsNumber(10) / StepsNumber(0)
    
    def test_negation(self):
        result = -StepsNumber(5)
        assert result.value == -5
    
    def test_comparison_less_than(self):
        assert StepsNumber(5) < StepsNumber(10)
        assert not StepsNumber(10) < StepsNumber(5)
    
    def test_comparison_greater_than(self):
        assert StepsNumber(10) > StepsNumber(5)
        assert not StepsNumber(5) > StepsNumber(10)
    
    def test_equality(self):
        assert StepsNumber(42) == StepsNumber(42)
        assert not StepsNumber(42) == StepsNumber(43)
    
    def test_as_text(self):
        num = StepsNumber(42)
        text = num.as_text()
        assert isinstance(text, StepsText)
        assert text.value == "42"
    
    def test_as_boolean(self):
        assert StepsNumber(1).as_boolean().value is True
        assert StepsNumber(0).as_boolean().value is False


class TestStepsText:
    """Tests for text type."""
    
    def test_display_string(self):
        text = StepsText("Hello, World!")
        assert text.display_string() == "Hello, World!"
    
    def test_truthiness_nonempty(self):
        assert StepsText("hello").is_truthy() is True
    
    def test_truthiness_empty(self):
        assert StepsText("").is_truthy() is False
    
    def test_added_to(self):
        result = StepsText("Hello, ").added_to(StepsText("World!"))
        assert result.value == "Hello, World!"
    
    def test_split_by(self):
        result = StepsText("a,b,c").split_by(",")
        assert len(result.elements) == 3
        assert result.elements[0].value == "a"
        assert result.elements[1].value == "b"
        assert result.elements[2].value == "c"
    
    def test_character_at(self):
        result = StepsText("hello").character_at(0)
        assert result.value == "h"
    
    def test_character_at_out_of_bounds(self):
        with pytest.raises(IndexError):
            StepsText("hello").character_at(10)
    
    def test_length(self):
        assert StepsText("hello").length() == 5
        assert StepsText("").length() == 0
    
    def test_contains(self):
        text = StepsText("hello world")
        assert text.contains("world").value is True
        assert text.contains("foo").value is False
    
    def test_starts_with(self):
        text = StepsText("hello world")
        assert text.starts_with("hello").value is True
        assert text.starts_with("world").value is False
    
    def test_ends_with(self):
        text = StepsText("hello world")
        assert text.ends_with("world").value is True
        assert text.ends_with("hello").value is False
    
    def test_as_number_valid(self):
        text = StepsText("42")
        result = text.as_number()
        assert result.value == 42.0
    
    def test_as_number_decimal(self):
        text = StepsText("3.14")
        result = text.as_number()
        assert result.value == 3.14
    
    def test_as_number_invalid(self):
        with pytest.raises(ValueError) as exc:
            StepsText("hello").as_number()
        assert "hello" in str(exc.value)


class TestStepsBoolean:
    """Tests for boolean type."""
    
    def test_true_display(self):
        assert StepsBoolean(True).display_string() == "true"
    
    def test_false_display(self):
        assert StepsBoolean(False).display_string() == "false"
    
    def test_truthiness(self):
        assert StepsBoolean(True).is_truthy() is True
        assert StepsBoolean(False).is_truthy() is False
    
    def test_and_operation(self):
        assert (StepsBoolean(True) & StepsBoolean(True)).value is True
        assert (StepsBoolean(True) & StepsBoolean(False)).value is False
        assert (StepsBoolean(False) & StepsBoolean(False)).value is False
    
    def test_or_operation(self):
        assert (StepsBoolean(True) | StepsBoolean(False)).value is True
        assert (StepsBoolean(False) | StepsBoolean(False)).value is False
    
    def test_not_operation(self):
        assert (~StepsBoolean(True)).value is False
        assert (~StepsBoolean(False)).value is True
    
    def test_as_number(self):
        assert StepsBoolean(True).as_number().value == 1.0
        assert StepsBoolean(False).as_number().value == 0.0


class TestStepsList:
    """Tests for list type."""
    
    def test_empty_list(self):
        lst = StepsList()
        assert lst.length() == 0
        assert lst.display_string() == "[]"
    
    def test_list_with_numbers(self):
        lst = StepsList([StepsNumber(1), StepsNumber(2), StepsNumber(3)])
        assert lst.length() == 3
        assert lst.display_string() == "[1, 2, 3]"
    
    def test_truthiness(self):
        assert StepsList([StepsNumber(1)]).is_truthy() is True
        assert StepsList().is_truthy() is False
    
    def test_get_element(self):
        lst = StepsList([StepsText("a"), StepsText("b")])
        assert lst.get(0).value == "a"
        assert lst.get(1).value == "b"
    
    def test_get_out_of_bounds(self):
        lst = StepsList([StepsNumber(1)])
        with pytest.raises(IndexError):
            lst.get(5)
    
    def test_add_element(self):
        lst = StepsList()
        lst.add(StepsNumber(42))
        assert lst.length() == 1
        assert lst.get(0).value == 42
    
    def test_remove_element(self):
        lst = StepsList([StepsNumber(1), StepsNumber(2), StepsNumber(3)])
        result = lst.remove(StepsNumber(2))
        assert result is True
        assert lst.length() == 2
    
    def test_remove_nonexistent(self):
        lst = StepsList([StepsNumber(1)])
        result = lst.remove(StepsNumber(99))
        assert result is False
        assert lst.length() == 1
    
    def test_contains(self):
        lst = StepsList([StepsNumber(1), StepsNumber(2)])
        assert lst.contains(StepsNumber(1)).value is True
        assert lst.contains(StepsNumber(99)).value is False
    
    def test_iteration(self):
        lst = StepsList([StepsNumber(1), StepsNumber(2)])
        values = [item.value for item in lst]
        assert values == [1.0, 2.0]


class TestStepsTable:
    """Tests for table type."""
    
    def test_empty_table(self):
        table = StepsTable()
        assert table.length() == 0
    
    def test_table_with_pairs(self):
        table = StepsTable({"name": StepsText("Alice"), "age": StepsNumber(30)})
        assert table.length() == 2
    
    def test_truthiness(self):
        assert StepsTable({"key": StepsNumber(1)}).is_truthy() is True
        assert StepsTable().is_truthy() is False
    
    def test_get_value(self):
        table = StepsTable({"name": StepsText("Bob")})
        result = table.get("name")
        assert result.value == "Bob"
    
    def test_get_missing_key(self):
        table = StepsTable({"name": StepsText("Bob")})
        with pytest.raises(KeyError) as exc:
            table.get("missing")
        assert "missing" in str(exc.value)
    
    def test_set_value(self):
        table = StepsTable()
        table.set("key", StepsNumber(42))
        assert table.get("key").value == 42
    
    def test_has_key(self):
        table = StepsTable({"name": StepsText("Alice")})
        assert table.has_key("name").value is True
        assert table.has_key("missing").value is False
    
    def test_keys(self):
        table = StepsTable({"a": StepsNumber(1), "b": StepsNumber(2)})
        keys = table.keys()
        key_values = [k.value for k in keys]
        assert "a" in key_values
        assert "b" in key_values


class TestStepsNothing:
    """Tests for nothing type."""
    
    def test_display_string(self):
        assert StepsNothing().display_string() == "nothing"
    
    def test_truthiness(self):
        assert StepsNothing().is_truthy() is False
    
    def test_python_value(self):
        assert StepsNothing().python_value() is None
    
    def test_as_number_fails(self):
        with pytest.raises(ValueError):
            StepsNothing().as_number()
    
    def test_as_boolean(self):
        assert StepsNothing().as_boolean().value is False


class TestMakeValue:
    """Tests for Python to Steps value conversion."""
    
    def test_from_int(self):
        result = make_value(42)
        assert isinstance(result, StepsNumber)
        assert result.value == 42.0
    
    def test_from_float(self):
        result = make_value(3.14)
        assert isinstance(result, StepsNumber)
        assert result.value == 3.14
    
    def test_from_string(self):
        result = make_value("hello")
        assert isinstance(result, StepsText)
        assert result.value == "hello"
    
    def test_from_bool_true(self):
        result = make_value(True)
        assert isinstance(result, StepsBoolean)
        assert result.value is True
    
    def test_from_bool_false(self):
        result = make_value(False)
        assert isinstance(result, StepsBoolean)
        assert result.value is False
    
    def test_from_none(self):
        result = make_value(None)
        assert isinstance(result, StepsNothing)
    
    def test_from_list(self):
        result = make_value([1, 2, 3])
        assert isinstance(result, StepsList)
        assert result.length() == 3
    
    def test_from_dict(self):
        result = make_value({"key": "value"})
        assert isinstance(result, StepsTable)
        assert result.get("key").value == "value"
    
    def test_nested_structures(self):
        result = make_value({"numbers": [1, 2, 3]})
        assert isinstance(result, StepsTable)
        numbers = result.get("numbers")
        assert isinstance(numbers, StepsList)
        assert numbers.length() == 3
    
    def test_from_steps_value_passthrough(self):
        original = StepsNumber(42)
        result = make_value(original)
        assert result is original


class TestTypeHelpers:
    """Tests for type helper functions."""
    
    def test_get_type_name(self):
        assert get_type_name(StepsNumber(1)) == "number"
        assert get_type_name(StepsText("a")) == "text"
        assert get_type_name(StepsBoolean(True)) == "boolean"
        assert get_type_name(StepsList()) == "list"
        assert get_type_name(StepsTable()) == "table"
        assert get_type_name(StepsNothing()) == "nothing"
    
    def test_is_same_type_true(self):
        assert is_same_type(StepsNumber(1), StepsNumber(2)) is True
        assert is_same_type(StepsText("a"), StepsText("b")) is True
    
    def test_is_same_type_false(self):
        assert is_same_type(StepsNumber(1), StepsText("1")) is False
        assert is_same_type(StepsList(), StepsTable()) is False
