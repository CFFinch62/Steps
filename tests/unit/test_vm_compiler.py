"""Tests for the NucleusVM-backed compiler (`steps.vm_compiler`) — the
first vertical slice described in NucleusVM's dev-docs/PLAN.md (Phase 2).

Mirrors FragBASIC's own test_vm_compiler.py in spirit: the real
correctness contract is "matches the tree-walker's output byte for byte,"
so most tests run the *same* program through both engines and compare,
rather than asserting a hardcoded expected value independently.
"""
from typing import Dict

from steps.environment import Environment, StepDefinition, RiserDefinition
from steps.parser import parse_building, parse_step
from steps.interpreter import run_building
from steps.vm_compiler import run_building_vm


def _step_def_from_source(source: str) -> StepDefinition:
    """Mirrors loader.py's StepNode -> StepDefinition conversion exactly,
    so tests don't need real files on disk."""
    result = parse_step(source)
    assert result.success, result.errors
    step_node = result.ast

    risers: Dict[str, RiserDefinition] = {}
    for riser in step_node.risers:
        risers[riser.name] = RiserDefinition(
            name=riser.name,
            parameters=[p.name for p in riser.expects],
            returns=riser.returns.name if riser.returns else None,
            declarations=riser.declarations,
            body=riser.body,
        )

    return StepDefinition(
        name=step_node.name,
        belongs_to=step_node.belongs_to,
        parameters=[p.name for p in step_node.expects],
        returns=step_node.returns.name if step_node.returns else None,
        body=step_node.body,
        declarations=step_node.declarations,
        risers=risers,
    )


def _make_env(step_sources=()):
    env = Environment()
    for src in step_sources:
        env.register_step(_step_def_from_source(src))
    return env


def run_tree(building_source, step_sources=()):
    env = _make_env(step_sources)
    out = []
    env.output_handler = lambda s: out.append(s)
    building = parse_building(building_source).ast
    run_building(building, env)
    return "".join(out)


def run_vm(building_source, step_sources=()):
    env = _make_env(step_sources)
    out = []
    building = parse_building(building_source).ast
    run_building_vm(building, env, output_func=out.append)
    return "".join(out)


def run_both(building_source, step_sources=()):
    return run_tree(building_source, step_sources), run_vm(building_source, step_sources)


def test_arithmetic_and_display():
    src = """building: test
    set x to 7
    set y to 2
    display x + y
    display x - y
    display x * y
    display x / y
    display x modulo y
"""
    tree_out, vm_out = run_both(src)
    assert vm_out == tree_out
    assert vm_out.splitlines() == ["9", "5", "14", "3.5", "1"]


def test_comparisons_and_booleans_display_lowercase():
    src = """building: test
    display 5 is greater than 3
    display 5 is less than 3
    display (5 is greater than 3) and (2 is greater than 1)
    display (5 is greater than 3) and (2 is less than 1)
    display not (5 is greater than 3)
"""
    tree_out, vm_out = run_both(src)
    assert vm_out == tree_out
    assert vm_out.splitlines() == ["true", "false", "true", "false", "false"]


def test_if_otherwise_if_otherwise():
    src = """building: test
    set i to 0
    repeat while i is less than 3
        if i equals 0
            display "zero"
        otherwise if i equals 1
            display "one"
        otherwise
            display "other"
        set i to i + 1
"""
    tree_out, vm_out = run_both(src)
    assert vm_out == tree_out
    assert vm_out.splitlines() == ["zero", "one", "other"]


def test_repeat_while():
    src = """building: test
    set i to 0
    repeat while i is less than 5
        display i
        set i to i + 1
"""
    tree_out, vm_out = run_both(src)
    assert vm_out == tree_out
    assert vm_out.splitlines() == ["0", "1", "2", "3", "4"]


def test_list_literal_indexing_and_mutation():
    src = """building: test
    set numbers to [10, 20, 30]
    display numbers[1]
    set numbers[1] to 99
    display numbers[1]
    add 40 to numbers
    display length of numbers
    display numbers
"""
    tree_out, vm_out = run_both(src)
    assert vm_out == tree_out
    assert vm_out.splitlines() == ["20", "99", "4", "[10, 99, 30, 40]"]


def test_type_conversion_number_text_boolean():
    src = """building: test
    display "42" as number
    display 42 as text
    display 0 as boolean
    display 1 as boolean
"""
    tree_out, vm_out = run_both(src)
    assert vm_out == tree_out
    assert vm_out.splitlines() == ["42", "42", "false", "true"]


def test_added_to_text_concat():
    src = """building: test
    display "Hello, " added to "World"
"""
    tree_out, vm_out = run_both(src)
    assert vm_out == tree_out
    assert vm_out.strip() == "Hello, World"


def test_text_operations():
    src = """building: test
    display "a,b,c" split by ","
    display character at 1 of "hello"
    display "hello world" contains "wor"
    display 3 is in [1, 2, 3]
    display 9 is in [1, 2, 3]
"""
    tree_out, vm_out = run_both(src)
    assert vm_out == tree_out
    assert vm_out.splitlines() == ["[a, b, c]", "e", "true", "true", "false"]


def test_step_call_with_return_value():
    step_src = """step: square
    belongs to: main
    expects: n
    returns: result

    declare:
        result as number

    do:
        set result to n * n
        return result
"""
    building_src = """building: test
    floors:
        floor: main
            step: square

    call square with 6 storing result in answer
    display answer
"""
    tree_out, vm_out = run_both(building_src, [step_src])
    assert vm_out == tree_out
    assert vm_out.strip() == "36"


def test_recursive_step_call():
    step_src = """step: fact
    belongs to: main
    expects: n
    returns: result

    do:
        if n is less than 2
            return 1
        otherwise
            call fact with n - 1 storing result in sub_result
            return n * sub_result
"""
    building_src = """building: test
    floors:
        floor: main
            step: fact

    call fact with 10 storing result in answer
    display answer
"""
    tree_out, vm_out = run_both(building_src, [step_src])
    assert vm_out == tree_out
    assert vm_out.strip() == "3628800"


def test_riser_private_helper():
    step_src = """step: double_it
    belongs to: main
    expects: n
    returns: result

    riser: helper
        expects: x
        returns: doubled

        do:
            set doubled to x * 2
            return doubled

    do:
        call helper with n storing result in result
        return result
"""
    building_src = """building: test
    floors:
        floor: main
            step: double_it

    call double_it with 21 storing result in answer
    display answer
"""
    tree_out, vm_out = run_both(building_src, [step_src])
    assert vm_out == tree_out
    assert vm_out.strip() == "42"


def test_bare_set_mutates_outer_dynamic_scope_across_call():
    """The single most distinctive behavior this whole phase exists to
    prove out: a step's bare `set` on a name that already exists in its
    *caller's* scope mutates it there, in place — dynamic (call-chain)
    scoping, not lexical. Confirmed at the raw VM opcode level in
    NucleusVM's own tests/test_vm_core.py; this proves the real compiler
    reproduces it end to end against the actual tree-walker."""
    step_src = """step: bump
    belongs to: main

    do:
        set shared to shared + 1
"""
    building_src = """building: test
    floors:
        floor: main
            step: bump

    set shared to 10
    call bump
    call bump
    display shared
"""
    tree_out, vm_out = run_both(building_src, [step_src])
    assert vm_out == tree_out
    assert vm_out.strip() == "12"


def test_unsupported_construct_raises_not_implemented():
    import pytest

    src = """building: test
    attempt:
        display "x"
    if unsuccessful:
        display "y"
"""
    env = _make_env()
    building = parse_building(src).ast
    with pytest.raises(NotImplementedError):
        run_building_vm(building, env, output_func=lambda s: None)
