"""AST -> NucleusVM bytecode compiler for STEPS — first vertical slice.

Covers: `repeat while` (99/100 corpus solutions — the dominant loop, needs
no scope push at all, matching the tree-walker's own `_exec_repeat_while`,
which runs the body directly in the enclosing scope); `if`/`otherwise`/
`otherwise if`; `exit`; `return`; `call ... [with ...] [storing result in
...]` for steps, risers, and the 11 actually-used builtins (resolved once
at compile time — see `_resolve_call_target`); `set`/`set X[i] to`; lists
(literals, indexing, `add`/`remove`); arithmetic/comparison/boolean
operators; `as number`/`as text`/`as boolean`; `length of`; `added to`;
`display`; and dynamic scoping end to end via NucleusVM's `LOAD_NAME`/
`STORE_NAME_DECL`/`STORE_NAME_DYNAMIC` — every variable reference goes
through this family, there is no resolved-slot tier at all, since that's
the entire point of this phase (see NucleusVM's PROGRESS.md for why
FragBASIC's slice never exercised it). Deliberately NOT covered this
slice (raises NotImplementedError): `attempt`/`unsuccessful` (0 corpus
usage), tables (0 corpus usage), `repeat for each` (1 use — needs a
lightweight non-CALL scope-push NucleusVM doesn't have a primitive for
yet), `repeat <N> times` (3 uses), `fixed` type-locking (0 real usage —
the only 8 corpus hits are the English word inside `note:` comments), the
45 unused builtins, `input`.

Value representation: unboxed native Python `float`/`str`/`bool`/`list` —
`StepsNumber`/`StepsText`/`StepsBoolean` (`types.py`) wrap exactly one of
these with no extra tag, confirmed directly from the dataclass fields,
same shape and same conclusion as FragBASIC's `Variable` audit.
`StepsNothing` (a step/riser that falls off the end without an explicit
`return`) maps to Python `None`.

Unlike FragBASIC, almost nothing here needs a `CALL_NATIVE` wrapper for
its operators: STEPS' arithmetic is strictly numeric (`+`/`-`/`*`/`/`/
`modulo` all require both operands already be numbers — text
concatenation is the separate `added to` operator, not an overload of
`+`), comparisons already return a plain Python-compatible bool (STEPS
booleans wrap `bool` directly, not FragBASIC's `-1`/`0` convention), and
`and`/`or`/`not` are eager (both operands always evaluated — see
`boolean_and`/`boolean_or` in `builtins/comparison.py`) with truthiness
matching Python's own `bool(x)` exactly. So this compiler emits
NucleusVM's raw `BINARY_*`/`COMPARE_*`/`LOGICAL_AND`/`LOGICAL_OR`/
`UNARY_NOT` opcodes directly for all of those, no wrapper at all — see
`natives.py`'s module docstring for the small set of things that
genuinely do need one (display/conversion formatting, list mutation
helpers, the 11 builtins).

STEPS statement bodies are genuinely nested (`IfBranch.body`,
`RepeatWhileStatement.body`, etc. are real child-list fields), unlike
FragBASIC's flat sibling-scanned FOR/NEXT — no structural pairing pass
needed here, each construct's children are just compiled by walking
straight into them.

Top-level `building.body` is compiled as the body of a synthetic zero-arg
call to itself (`CALL`, then `HALT`), not emitted inline at ip 0 —
`LOAD_NAME`/`STORE_NAME_DYNAMIC`/`STORE_NAME_DECL` all require an active
call frame, but `VM.run()` starts with `self.frame = None`. STEPS itself
has no "globals" tier distinct from its root `Scope` — top-level code is
just the outermost link in the same dynamic scope chain a step call
extends, so giving it a real frame this way is no more than STEPS' own
architecture already implies (see NucleusVM's `CALL` opcode fix — its new
frame now parents on the *caller's* current frame — and the hand-assembled
tests in NucleusVM's own `tests/test_vm_core.py` that prove this before
any compiler exercised it for real).
"""
from __future__ import annotations

from nucleus_vm import Chunk, Op

from ..ast_nodes import (
    DisplayStatement, SetStatement, SetIndexStatement, CallStatement,
    ReturnStatement, ExitStatement, IfStatement,
    RepeatWhileStatement, NoteStatement, AddToListStatement,
    RemoveFromListStatement,
    NumberLiteral, TextLiteral, BooleanLiteral, NothingLiteral, ListLiteral,
    IdentifierNode, BinaryOpNode, UnaryOpNode, TypeConversionNode,
    TableAccessNode, AddedToNode, LengthOfNode,
    SplitByNode, CharacterAtNode, ContainsNode, IsInNode,
)
from . import natives


_UNSUPPORTED_HINT = (
    "is not yet supported by the NucleusVM compiler slice — see "
    "dev-docs/PLAN.md's Phase 2 section in the NucleusVM repo"
)

_BINARY_OPCODE = {
    "+": Op.BINARY_ADD,
    "-": Op.BINARY_SUB,
    "*": Op.BINARY_MUL,
    "/": Op.BINARY_DIV,
    "modulo": Op.BINARY_MOD,
}

_COMPARE_OPCODE = {
    "is equal to": Op.COMPARE_EQ,
    "equals": Op.COMPARE_EQ,
    "is not equal to": Op.COMPARE_NE,
    "is less than": Op.COMPARE_LT,
    "is greater than": Op.COMPARE_GT,
    "is less than or equal to": Op.COMPARE_LE,
    "is greater than or equal to": Op.COMPARE_GE,
}


class VMCompiler:
    def __init__(self, environment):
        self.chunk = Chunk("steps_program")
        self.environment = environment
        self._step_addr: dict[str, int] = {}
        self._pending_calls: list = []  # (patch_idx, argcount, name, riser_addr_or_None)
        self._current_risers: dict = {}
        self._current_riser_addr: dict = {}
        self._synth_counter = 0
        # `environment.steps` holds the *entire* loaded stdlib alongside
        # whatever the project actually defines — most of it is never
        # called by any given program, and some of it uses constructs
        # this slice doesn't support yet. Compiling everything
        # unconditionally would both waste work and make compilation
        # fail on unreachable code. Compile reachability-driven instead:
        # only a step actually called (directly or transitively) from
        # `building.body` or another reachable step/riser ever gets
        # compiled — discovered on demand via `_queue_step`, drained by
        # `compile_program`'s worklist loop.
        self._queued: set[str] = set()
        self._worklist: list[str] = []

    # ------------------------------------------------------------------
    # Top level
    # ------------------------------------------------------------------

    def compile_program(self, building) -> Chunk:
        call_main = self.chunk.emit(Op.CALL, None)
        self.chunk.emit(Op.HALT)

        main_start = self.chunk.here()
        self._current_risers = {}
        self._current_riser_addr = {}
        self._compile_block(building.body)
        self.chunk.emit(Op.LOAD_CONST, self.chunk.add_constant(None))
        self.chunk.emit(Op.RETURN)
        self.chunk.patch_arg(call_main, (main_start, 0))

        while self._worklist:
            name = self._worklist.pop()
            if name not in self.environment.steps:
                raise NameError(f"call to undefined step {name!r}")
            self._compile_step(name, self.environment.steps[name])

        self._resolve_pending_calls()
        return self.chunk

    def _queue_step(self, name):
        if name not in self._step_addr and name not in self._queued:
            self._queued.add(name)
            self._worklist.append(name)

    def _compile_step(self, name, step_def):
        local_riser_addr: dict = {}
        for riser_name, riser_def in step_def.risers.items():
            local_riser_addr[riser_name] = self.chunk.here()
            self._current_risers = step_def.risers
            self._current_riser_addr = local_riser_addr
            self._emit_procedure_body(
                riser_def.parameters, riser_def.declarations, riser_def.body
            )

        self._step_addr[name] = self.chunk.here()
        self._current_risers = step_def.risers
        self._current_riser_addr = local_riser_addr
        self._emit_procedure_body(
            step_def.parameters, step_def.declarations, step_def.body
        )

        self._current_risers = {}
        self._current_riser_addr = {}

    def _emit_procedure_body(self, parameters, declarations, body):
        for i, pname in enumerate(parameters):
            self.chunk.emit(Op.LOAD_FAST, i)
            self.chunk.emit(Op.STORE_NAME_DECL, pname)
        for decl in declarations:
            self.chunk.emit(Op.LOAD_CONST, self.chunk.add_constant(_declare_default(decl.type_name)))
            self.chunk.emit(Op.STORE_NAME_DECL, decl.name)

        self._compile_block(body)

        # Falling off the end without an explicit `return` is StepsNothing.
        self.chunk.emit(Op.LOAD_CONST, self.chunk.add_constant(None))
        self.chunk.emit(Op.RETURN)

    # ------------------------------------------------------------------
    # Statement blocks
    # ------------------------------------------------------------------

    def _compile_block(self, statements):
        for stmt in statements:
            self._compile_stmt(stmt)

    def _compile_stmt(self, stmt):
        t = type(stmt)

        if t is NoteStatement:
            return
        if t is DisplayStatement:
            self._compile_expr(stmt.expression)
            self.chunk.emit(Op.CALL_NATIVE, ("_display", 1))
            self.chunk.emit(Op.POP_TOP)
            return
        if t is SetStatement:
            self._compile_expr(stmt.value)
            self.chunk.emit(Op.STORE_NAME_DYNAMIC, stmt.target)
            return
        if t is SetIndexStatement:
            self.chunk.emit(Op.LOAD_NAME, stmt.target)
            self._compile_expr(stmt.index)
            self.chunk.emit(Op.TO_INT)
            self._compile_expr(stmt.value)
            self.chunk.emit(Op.INDEX_SET)
            return
        if t is CallStatement:
            self._compile_call(stmt.step_name, stmt.arguments)
            if stmt.result_target:
                self.chunk.emit(Op.STORE_NAME_DYNAMIC, stmt.result_target)
            else:
                self.chunk.emit(Op.POP_TOP)
            return
        if t is ReturnStatement:
            if stmt.value is not None:
                self._compile_expr(stmt.value)
            else:
                self.chunk.emit(Op.LOAD_CONST, self.chunk.add_constant(None))
            self.chunk.emit(Op.RETURN)
            return
        if t is ExitStatement:
            self.chunk.emit(Op.HALT)
            return
        if t is IfStatement:
            self._compile_if(stmt)
            return
        if t is RepeatWhileStatement:
            self._compile_repeat_while(stmt)
            return
        if t is AddToListStatement:
            self.chunk.emit(Op.LOAD_NAME, stmt.list_name)
            self._compile_expr(stmt.item)
            self.chunk.emit(Op.CALL_NATIVE, ("_add_to_list", 2))
            self.chunk.emit(Op.POP_TOP)
            return
        if t is RemoveFromListStatement:
            self.chunk.emit(Op.LOAD_NAME, stmt.list_name)
            self._compile_expr(stmt.item)
            self.chunk.emit(Op.CALL_NATIVE, ("_remove_from_list", 2))
            self.chunk.emit(Op.POP_TOP)
            return

        raise NotImplementedError(f"STEPS statement {t.__name__} {_UNSUPPORTED_HINT}")

    def _compile_if(self, stmt):
        end_jumps = []

        self._compile_expr(stmt.if_branch.condition)
        next_jump = self.chunk.emit(Op.JUMP_IF_FALSE, None)
        self._compile_block(stmt.if_branch.body)
        end_jumps.append(self.chunk.emit(Op.JUMP, None))
        self.chunk.patch_arg(next_jump, self.chunk.here())

        for branch in stmt.otherwise_if_branches:
            self._compile_expr(branch.condition)
            nj = self.chunk.emit(Op.JUMP_IF_FALSE, None)
            self._compile_block(branch.body)
            end_jumps.append(self.chunk.emit(Op.JUMP, None))
            self.chunk.patch_arg(nj, self.chunk.here())

        if stmt.otherwise_branch:
            self._compile_block(stmt.otherwise_branch)

        end_addr = self.chunk.here()
        for j in end_jumps:
            self.chunk.patch_arg(j, end_addr)

    def _compile_repeat_while(self, stmt):
        loop_start = self.chunk.here()
        self._compile_expr(stmt.condition)
        exit_jump = self.chunk.emit(Op.JUMP_IF_FALSE, None)
        self._compile_block(stmt.body)
        self.chunk.emit(Op.JUMP, loop_start)
        self.chunk.patch_arg(exit_jump, self.chunk.here())

    # ------------------------------------------------------------------
    # Expressions
    # ------------------------------------------------------------------

    def _compile_expr(self, node):
        t = type(node)

        if t is NumberLiteral:
            self.chunk.emit(Op.LOAD_CONST, self.chunk.add_constant(float(node.value)))
            return
        if t is TextLiteral:
            self.chunk.emit(Op.LOAD_CONST, self.chunk.add_constant(node.value))
            return
        if t is BooleanLiteral:
            self.chunk.emit(Op.LOAD_CONST, self.chunk.add_constant(bool(node.value)))
            return
        if t is NothingLiteral:
            self.chunk.emit(Op.LOAD_CONST, self.chunk.add_constant(None))
            return
        if t is ListLiteral:
            for elem in node.elements:
                self._compile_expr(elem)
            self.chunk.emit(Op.BUILD_LIST, len(node.elements))
            return
        if t is IdentifierNode:
            self.chunk.emit(Op.LOAD_NAME, node.name)
            return
        if t is BinaryOpNode:
            self._compile_binary_op(node)
            return
        if t is UnaryOpNode:
            self._compile_unary_op(node)
            return
        if t is TypeConversionNode:
            self._compile_expr(node.expression)
            native = {
                "number": "_to_number", "text": "_to_text", "boolean": "_to_boolean",
            }.get(node.target_type)
            if native is None:
                raise NotImplementedError(f"conversion to {node.target_type!r} {_UNSUPPORTED_HINT}")
            self.chunk.emit(Op.CALL_NATIVE, (native, 1))
            return
        if t is TableAccessNode:
            self._compile_expr(node.table)
            self._compile_expr(node.key)
            self.chunk.emit(Op.TO_INT)
            self.chunk.emit(Op.INDEX_GET)
            return
        if t is AddedToNode:
            self._compile_expr(node.left)
            self._compile_expr(node.right)
            self.chunk.emit(Op.CALL_NATIVE, ("_added_to", 2))
            return
        if t is LengthOfNode:
            self._compile_expr(node.collection)
            self.chunk.emit(Op.CALL_NATIVE, ("_length_of", 1))
            return
        if t is SplitByNode:
            self._compile_expr(node.text)
            self._compile_expr(node.delimiter)
            self.chunk.emit(Op.CALL_NATIVE, ("_split_by", 2))
            return
        if t is CharacterAtNode:
            self._compile_expr(node.index)
            self._compile_expr(node.text)
            self.chunk.emit(Op.CALL_NATIVE, ("_character_at", 2))
            return
        if t is ContainsNode:
            self._compile_expr(node.text)
            self._compile_expr(node.substring)
            self.chunk.emit(Op.CALL_NATIVE, ("_contains", 2))
            return
        if t is IsInNode:
            self._compile_expr(node.item)
            self._compile_expr(node.collection)
            self.chunk.emit(Op.CALL_NATIVE, ("_is_in", 2))
            return

        raise NotImplementedError(f"STEPS expression {t.__name__} {_UNSUPPORTED_HINT}")

    def _compile_binary_op(self, node):
        op = node.operator
        if op in _BINARY_OPCODE:
            self._compile_expr(node.left)
            self._compile_expr(node.right)
            self.chunk.emit(_BINARY_OPCODE[op])
            return
        if op in _COMPARE_OPCODE:
            self._compile_expr(node.left)
            self._compile_expr(node.right)
            self.chunk.emit(_COMPARE_OPCODE[op])
            return
        if op == "and":
            self._compile_expr(node.left)
            self._compile_expr(node.right)
            self.chunk.emit(Op.LOGICAL_AND)
            return
        if op == "or":
            self._compile_expr(node.left)
            self._compile_expr(node.right)
            self.chunk.emit(Op.LOGICAL_OR)
            return
        raise NotImplementedError(f"binary operator {op!r} {_UNSUPPORTED_HINT}")

    def _compile_unary_op(self, node):
        if node.operator == "-":
            self._compile_expr(node.operand)
            self.chunk.emit(Op.UNARY_NEG)
            return
        if node.operator == "not":
            self._compile_expr(node.operand)
            self.chunk.emit(Op.UNARY_NOT)
            return
        raise NotImplementedError(f"unary operator {node.operator!r} {_UNSUPPORTED_HINT}")

    # ------------------------------------------------------------------
    # Calls
    # ------------------------------------------------------------------

    def _compile_call(self, name, argument_nodes):
        """Pushes exactly one value — the call's result (or None for a
        native/builtin with no meaningful return, matching CALL_NATIVE's
        own always-push-something contract). Resolution order mirrors
        `_exec_call`/`call_step` exactly: the *current* step's own risers
        first, then the 11 supported builtins, then the global step
        registry."""
        for arg in argument_nodes:
            self._compile_expr(arg)
        argcount = len(argument_nodes)

        if name in self._current_risers:
            idx = self.chunk.emit(Op.CALL, None)
            self._pending_calls.append((idx, argcount, name, self._current_riser_addr))
            return
        if name in natives.BUILTIN_ARITY:
            self.chunk.emit(Op.CALL_NATIVE, (name, argcount))
            return
        self._queue_step(name)
        idx = self.chunk.emit(Op.CALL, None)
        self._pending_calls.append((idx, argcount, name, None))

    def _resolve_pending_calls(self):
        for idx, argcount, name, riser_addr in self._pending_calls:
            if riser_addr is not None:
                if name not in riser_addr:
                    raise NameError(f"call to undefined riser {name!r}")
                addr = riser_addr[name]
            else:
                if name not in self._step_addr:
                    raise NameError(f"call to undefined step {name!r}")
                addr = self._step_addr[name]
            self.chunk.patch_arg(idx, (addr, argcount))


def _declare_default(type_name):
    if type_name == "text":
        return ""
    if type_name == "boolean":
        return False
    if type_name == "list":
        return []
    if type_name == "table":
        raise NotImplementedError(f"table declarations {_UNSUPPORTED_HINT}")
    return 0.0  # "number"


def compile_program(building, environment) -> Chunk:
    return VMCompiler(environment).compile_program(building)
