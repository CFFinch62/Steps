"""Unit Tests for Steps Interpreter.

Comprehensive tests for the interpreter including:
- Statement execution
- Expression evaluation
- Control flow
- Error handling
"""

import pytest
from pathlib import Path
from io import StringIO

from steps.interpreter import Interpreter, run_source, run_building, ExecutionResult
from steps.environment import Environment, StepDefinition
from steps.parser import parse_building, parse_step
from steps.types import StepsNumber, StepsText, StepsBoolean, StepsList, StepsTable, StepsNothing


# =============================================================================
# Helper Functions
# =============================================================================

def run(source: str, capture_output: bool = True) -> ExecutionResult:
    """Run source and capture output."""
    result = run_source(source)
    return result


def make_env_with_output_capture() -> tuple:
    """Create environment with captured I/O."""
    env = Environment()
    outputs = []
    inputs = []
    
    env.output_handler = lambda s: outputs.append(s)
    env.input_handler = lambda: inputs.pop(0) if inputs else ""
    
    return env, outputs, inputs


# =============================================================================
# Basic Statement Tests
# =============================================================================

class TestDisplayStatement:
    """Tests for display statement."""
    
    def test_display_number(self):
        result = run("""building: test
    display 42
""")
        assert result.success
        assert "42" in result.output_lines[0]
    
    def test_display_text(self):
        result = run("""building: test
    display "Hello, World!"
""")
        assert result.success
        assert result.output_lines[0] == "Hello, World!\n"
    
    def test_display_boolean(self):
        result = run("""building: test
    display true
""")
        assert result.success
        assert result.output_lines[0] == "true\n"
    
    def test_display_expression(self):
        result = run("""building: test
    display 10 + 20
""")
        assert result.success
        assert "30" in result.output_lines[0]


class TestSetStatement:
    """Tests for set statement."""
    
    def test_set_number(self):
        result = run("""building: test
    set x to 42
    display x
""")
        assert result.success
        assert "42" in result.output_lines[0]
    
    def test_set_text(self):
        result = run("""building: test
    set name to "Alice"
    display name
""")
        assert result.success
        assert result.output_lines[0] == "Alice\n"
    
    def test_set_expression(self):
        result = run("""building: test
    set x to 10
    set y to 20
    set sum to x + y
    display sum
""")
        assert result.success
        assert "30" in result.output_lines[0]
    
    def test_reassign_variable(self):
        result = run("""building: test
    set x to 10
    set x to 20
    display x
""")
        assert result.success
        assert "20" in result.output_lines[0]


class TestExitStatement:
    """Tests for exit statement."""
    
    def test_exit_stops_execution(self):
        result = run("""building: test
    display "before"
    exit
    display "after"
""")
        assert result.success
        assert len(result.output_lines) == 1
        assert result.output_lines[0] == "before\n"


# =============================================================================
# Control Flow Tests
# =============================================================================

class TestIfStatement:
    """Tests for if/otherwise if/otherwise."""
    
    def test_if_true(self):
        result = run("""building: test
    if true
        display "yes"
""")
        assert result.success
        assert result.output_lines[0] == "yes\n"
    
    def test_if_false(self):
        result = run("""building: test
    if false
        display "yes"
""")
        assert result.success
        assert len(result.output_lines) == 0
    
    def test_if_otherwise(self):
        result = run("""building: test
    if false
        display "yes"
    otherwise
        display "no"
""")
        assert result.success
        assert result.output_lines[0] == "no\n"
    
    def test_if_otherwise_if(self):
        result = run("""building: test
    set x to 2
    if x is equal to 1
        display "one"
    otherwise if x is equal to 2
        display "two"
    otherwise
        display "other"
""")
        assert result.success
        assert result.output_lines[0] == "two\n"
    
    def test_if_comparison(self):
        result = run("""building: test
    set x to 5
    if x is greater than 3
        display "big"
""")
        assert result.success
        assert result.output_lines[0] == "big\n"


class TestRepeatStatement:
    """Tests for repeat statements."""
    
    def test_repeat_times(self):
        result = run("""building: test
    repeat 3 times
        display "hello"
""")
        assert result.success
        assert len(result.output_lines) == 3
    
    def test_repeat_for_each_list(self):
        result = run("""building: test
    set items to [1, 2, 3]
    repeat for each item in items
        display item
""")
        assert result.success
        assert len(result.output_lines) == 3
    
    def test_repeat_for_each_text(self):
        result = run("""building: test
    repeat for each char in "abc"
        display char
""")
        assert result.success
        assert result.output_lines == ["a\n", "b\n", "c\n"]
    
    def test_repeat_while(self):
        result = run("""building: test
    set x to 0
    repeat while x is less than 3
        display x
        set x to x + 1
""")
        assert result.success
        assert len(result.output_lines) == 3


class TestAttemptStatement:
    """Tests for attempt/if unsuccessful."""
    
    def test_attempt_success(self):
        result = run("""building: test
    attempt:
        display "try"
    if unsuccessful:
        display "catch"
""")
        assert result.success
        assert result.output_lines[0] == "try\n"
        assert len(result.output_lines) == 1
    
    def test_attempt_with_continue(self):
        result = run("""building: test
    attempt:
        display "try"
    then continue:
        display "finally"
""")
        assert result.success
        assert result.output_lines == ["try\n", "finally\n"]


# =============================================================================
# Expression Tests
# =============================================================================

class TestArithmeticExpressions:
    """Tests for arithmetic expressions."""
    
    def test_addition(self):
        result = run("""building: test
    display 10 + 5
""")
        assert result.success
        assert "15" in result.output_lines[0]
    
    def test_subtraction(self):
        result = run("""building: test
    display 10 - 3
""")
        assert result.success
        assert "7" in result.output_lines[0]
    
    def test_multiplication(self):
        result = run("""building: test
    display 4 * 5
""")
        assert result.success
        assert "20" in result.output_lines[0]
    
    def test_division(self):
        result = run("""building: test
    display 20 / 4
""")
        assert result.success
        assert "5" in result.output_lines[0]
    
    def test_precedence(self):
        result = run("""building: test
    display 2 + 3 * 4
""")
        assert result.success
        assert "14" in result.output_lines[0]
    
    def test_parentheses(self):
        result = run("""building: test
    display (2 + 3) * 4
""")
        assert result.success
        assert "20" in result.output_lines[0]


class TestComparisonExpressions:
    """Tests for comparison expressions."""
    
    def test_equal(self):
        result = run("""building: test
    if 5 is equal to 5
        display "yes"
""")
        assert result.success
        assert result.output_lines[0] == "yes\n"
    
    def test_not_equal(self):
        result = run("""building: test
    if 5 is not equal to 3
        display "yes"
""")
        assert result.success
        assert result.output_lines[0] == "yes\n"
    
    def test_less_than(self):
        result = run("""building: test
    if 3 is less than 5
        display "yes"
""")
        assert result.success
        assert result.output_lines[0] == "yes\n"
    
    def test_greater_than(self):
        result = run("""building: test
    if 5 is greater than 3
        display "yes"
""")
        assert result.success
        assert result.output_lines[0] == "yes\n"
    
    def test_less_than_or_equal(self):
        result = run("""building: test
    if 5 is less than or equal to 5
        display "yes"
""")
        assert result.success
        assert result.output_lines[0] == "yes\n"
    
    def test_greater_than_or_equal(self):
        result = run("""building: test
    if 5 is greater than or equal to 3
        display "yes"
""")
        assert result.success
        assert result.output_lines[0] == "yes\n"


class TestBooleanExpressions:
    """Tests for boolean expressions."""
    
    def test_and_true(self):
        result = run("""building: test
    if true and true
        display "yes"
""")
        assert result.success
        assert result.output_lines[0] == "yes\n"
    
    def test_and_false(self):
        result = run("""building: test
    if true and false
        display "yes"
    otherwise
        display "no"
""")
        assert result.success
        assert result.output_lines[0] == "no\n"
    
    def test_or_true(self):
        result = run("""building: test
    if true or false
        display "yes"
""")
        assert result.success
        assert result.output_lines[0] == "yes\n"
    
    def test_not(self):
        result = run("""building: test
    if not false
        display "yes"
""")
        assert result.success
        assert result.output_lines[0] == "yes\n"


class TestTextOperations:
    """Tests for text operations."""
    
    def test_added_to(self):
        result = run("""building: test
    display "Hello, " added to "World!"
""")
        assert result.success
        assert result.output_lines[0] == "Hello, World!\n"
    
    def test_length_of(self):
        result = run("""building: test
    display length of "Hello"
""")
        assert result.success
        assert "5" in result.output_lines[0]
    
    def test_contains(self):
        result = run("""building: test
    set message to "Hello, World!"
    if message contains "World"
        display "found"
""")
        assert result.success
        assert result.output_lines[0] == "found\n"
    
    def test_starts_with(self):
        result = run("""building: test
    set url to "https://example.com"
    if url starts with "https"
        display "secure"
""")
        assert result.success
        assert result.output_lines[0] == "secure\n"
    
    def test_ends_with(self):
        result = run("""building: test
    set filename to "document.pdf"
    if filename ends with ".pdf"
        display "pdf file"
""")
        assert result.success
        assert result.output_lines[0] == "pdf file\n"


class TestListOperations:
    """Tests for list operations."""
    
    def test_list_literal(self):
        result = run("""building: test
    set items to [1, 2, 3]
    display length of items
""")
        assert result.success
        assert "3" in result.output_lines[0]
    
    def test_list_access(self):
        result = run("""building: test
    set items to ["a", "b", "c"]
    display items[1]
""")
        assert result.success
        assert result.output_lines[0] == "b\n"
    
    def test_add_to_list(self):
        result = run("""building: test
    set items to [1, 2]
    add 3 to items
    display length of items
""")
        assert result.success
        assert "3" in result.output_lines[0]
    
    def test_remove_from_list(self):
        result = run("""building: test
    set items to [1, 2, 3]
    remove 2 from items
    display length of items
""")
        assert result.success
        assert "2" in result.output_lines[0]
    
    def test_is_in_list(self):
        result = run("""building: test
    set items to [1, 2, 3]
    if 2 is in items
        display "found"
""")
        assert result.success
        assert result.output_lines[0] == "found\n"


class TestTableOperations:
    """Tests for table operations."""
    
    def test_table_literal(self):
        result = run("""building: test
    set person to ["name": "Alice", "age": 30]
    display person["name"]
""")
        assert result.success
        assert result.output_lines[0] == "Alice\n"
    
    def test_table_length(self):
        result = run("""building: test
    set data to ["a": 1, "b": 2]
    display length of data
""")
        assert result.success
        assert "2" in result.output_lines[0]


class TestTypeConversion:
    """Tests for type conversion."""
    
    def test_text_to_number(self):
        result = run("""building: test
    set x to "42" as number
    display x + 1
""")
        assert result.success
        assert "43" in result.output_lines[0]
    
    def test_number_to_text(self):
        result = run("""building: test
    set x to 42 as text
    display x added to "!"
""")
        assert result.success
        assert result.output_lines[0] == "42!\n"


# =============================================================================
# Error Handling Tests
# =============================================================================

class TestErrorHandling:
    """Tests for error handling."""
    
    def test_undefined_variable(self):
        result = run("""building: test
    display unknown_var
""")
        assert not result.success
        assert result.error is not None
        assert "not been defined" in result.error.message
    
    def test_division_by_zero(self):
        result = run("""building: test
    display 10 / 0
""")
        assert not result.success
        assert result.error is not None
        assert "divide by zero" in result.error.message.lower()
    
    def test_type_error_addition(self):
        result = run("""building: test
    display "hello" + 5
""")
        assert not result.success
        assert result.error is not None
    
    def test_index_out_of_bounds(self):
        result = run("""building: test
    set items to [1, 2, 3]
    display items[10]
""")
        assert not result.success
        assert result.error is not None
        assert "out of bounds" in result.error.message.lower()


# =============================================================================
# Environment Tests
# =============================================================================

class TestEnvironment:
    """Tests for environment functionality."""
    
    def test_scope_push_pop(self):
        env = Environment()
        env.set_variable("x", StepsNumber(10))
        
        env.push_scope()
        env.set_variable("y", StepsNumber(20))
        
        assert env.get_variable("x").value == 10
        assert env.get_variable("y").value == 20
        
        env.pop_scope()
        
        assert env.get_variable("x").value == 10
        with pytest.raises(Exception):
            env.get_variable("y")
    
    def test_step_registry(self):
        env = Environment()
        step = StepDefinition(
            name="greet",
            belongs_to="main",
            parameters=["name"],
            returns=None,
            body=[]
        )
        env.register_step(step)
        
        assert env.step_exists("greet")
        assert not env.step_exists("unknown")
    
    def test_output_handler(self):
        outputs = []
        env = Environment()
        env.output_handler = lambda s: outputs.append(s)
        
        env.write_output("Hello")
        env.write_output("World")
        
        assert outputs == ["Hello", "World"]


# =============================================================================
# Step Call Tests
# =============================================================================

class TestStepCalls:
    """Tests for step calls (with manually registered steps)."""
    
    def test_call_registered_step(self):
        env = Environment()
        outputs = []
        env.output_handler = lambda s: outputs.append(s)
        
        # Parse and register a step
        step_source = """step: greet
    belongs to: main
    expects: name

    do:
        display name
"""
        from steps.parser import parse_step
        result = parse_step(step_source)
        assert result.success
        
        step_node = result.ast
        step_def = StepDefinition(
            name=step_node.name,
            belongs_to=step_node.belongs_to,
            parameters=[p.name for p in step_node.expects],
            returns=None,
            body=step_node.body
        )
        env.register_step(step_def)
        
        # Now call it from a building
        building_source = """building: test
    call greet with "Alice"
"""
        from steps.parser import parse_building
        build_result = parse_building(building_source)
        assert build_result.success
        
        from steps.interpreter import run_building
        exec_result = run_building(build_result.ast, env)
        assert exec_result.success
        assert outputs[0] == "Alice\n"
