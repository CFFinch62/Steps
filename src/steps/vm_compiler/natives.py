"""Native functions for the NucleusVM-backed STEPS engine.

Every function here operates on NucleusVM's native unboxed values (plain
Python float/str/bool/list — STEPS' `StepsNumber`/`StepsText`/
`StepsBoolean`/`StepsList` all wrap exactly one of these with no extra
tag, confirmed directly against `types.py`'s dataclass fields; STEPS
"number" is always Python `float` here, by convention, so every native
that produces one explicitly wraps with `float(...)` to keep that
convention meaningful everywhere it's checked).

Unlike FragBASIC, STEPS' operators mostly need *no* wrapper at all:
arithmetic (`+ - * / modulo`) is strictly numeric (no polymorphic `+` —
text concatenation is a separate `added to` operator), comparisons
already return a plain bool (STEPS' own boolean values wrap Python
`bool` directly, not a `-1`/`0` convention), and `and`/`or`/`not` are
eager (both operands always evaluated — see `boolean_and`/`boolean_or`
in `builtins/comparison.py`) with truthiness matching Python's own
`bool(x)` exactly for every value shape this slice covers. So the
compiler emits NucleusVM's raw `BINARY_*`/`COMPARE_*`/`LOGICAL_AND`/
`LOGICAL_OR`/`UNARY_NOT` opcodes directly for all of those — nothing
here duplicates them. What *is* here: display/type-conversion formatting
(STEPS-specific string rules), the handful of operations with real
Python-vs-STEPS semantic gaps (`as number`'s strict-parse-or-raise,
`modulo`'s STEPS is literally Python's own `%` so needs nothing extra,
included only where a real gap exists), list mutation helpers, and the
11 registered builtins real corpus usage showed are actually used
(`create_list`, `characters`, `slice`, `sqrt`, `index_of`, `read_file`,
`replace`, `list_sum`, `sqr`, `pow`, `log10`, `log` — see
NucleusVM's dev-docs/PLAN.md for the corpus survey behind that list).
"""
import math


def _is_str(x):
    return type(x) is str


def _is_list(x):
    return type(x) is list


def _steps_str(x):
    """Mirrors StepsValue.display_string() for the value space this
    compiler unboxes to: a whole-number float displays without a
    decimal point (StepsNumber.display_string), a bool displays as
    lowercase "true"/"false" (StepsBoolean.display_string — NOT Python's
    "True"/"False"), a list displays as "[e1, e2, ...]" recursively
    (StepsList.display_string). This is also STEPS' "as text" conversion
    rule (StepsValue.as_text()'s default implementation is literally
    `StepsText(self.display_string())`)."""
    if _is_str(x):
        return x
    if x is True or x is False:
        return "true" if x else "false"
    if _is_list(x):
        return "[" + ", ".join(_steps_str(e) for e in x) + "]"
    if x.is_integer():
        return str(int(x))
    return str(x)


def _make_display(output_func):
    def _display(x):
        output_func(_steps_str(x) + "\n")
    return _display


# ---------------------------------------------------------------------
# Type conversion ("as number"/"as text"/"as boolean" — TypeConversionNode,
# 647 combined occurrences in the corpus, the highest-frequency operation
# after plain arithmetic)
# ---------------------------------------------------------------------

def _to_number(x):
    """Mirrors convert_to_number: numbers pass through, text parses
    strictly (raises on failure — NOT a silent fallback to 0, unlike
    FragBASIC's VAL), booleans become 1.0/0.0."""
    if x is True or x is False:
        return 1.0 if x else 0.0
    if _is_str(x):
        return float(x)  # raises ValueError on bad input, matching STEPS
    return x


def _to_text(x):
    return _steps_str(x)


def _to_boolean(x):
    """Mirrors convert_to_boolean/is_truthy — Python's own bool(x) truth
    test already agrees with StepsValue.is_truthy() for every shape this
    slice covers (nonzero float, nonempty str, actual bool, nonempty
    list)."""
    return bool(x)


# ---------------------------------------------------------------------
# length of / added to (separate AST nodes, not registry builtins, but
# far higher frequency than any of them — see the corpus survey)
# ---------------------------------------------------------------------

def _length_of(x):
    return float(len(x))


def _split_by(text, delimiter):
    return text.split(delimiter)


def _character_at(index, text):
    return text[int(index)]


def _contains(text, substring):
    return substring in text


def _is_in(item, collection):
    """Mirrors list_contains' dual dispatch: list membership, or text
    substring check when collection is text (item coerced to text first,
    matching `item.as_text().value`)."""
    if _is_list(collection):
        return item in collection
    if _is_str(collection):
        return _steps_str(item) in collection
    raise TypeError(f"cannot check 'is in' membership in {type(collection).__name__}")


def _added_to(left, right):
    """`added to` is text-only concatenation (unlike FragBASIC's
    polymorphic `+`) — STEPS' own added_to is defined only on StepsText,
    so both operands are expected to already be text by the time this
    runs; a non-text operand raising here (Python's `+` on str+non-str)
    is the correct, loud failure, not a divergence to paper over."""
    return left + right


# ---------------------------------------------------------------------
# List mutation (AddToListStatement/RemoveFromListStatement — 248 + 1
# occurrences)
# ---------------------------------------------------------------------

def _add_to_list(lst, item):
    lst.append(item)


def _remove_from_list(lst, item):
    """Mirrors StepsList.remove: removes the first occurrence equal to
    item, returns whether one was found."""
    for i, elem in enumerate(lst):
        if elem == item:
            del lst[i]
            return True
    return False


# ---------------------------------------------------------------------
# The 11 registered builtins real corpus usage showed are actually used
# ---------------------------------------------------------------------

def _bi_create_list(size, value):
    """Mirrors list_create: `[value] * n` — deliberately aliases the same
    reference into every slot when value is itself a mutable list, exactly
    matching STEPS' own (Python list-multiplication) behavior."""
    return [value] * int(size)


def _bi_characters(text):
    return list(text)


def _bi_slice(text, start, end):
    return text[int(start):int(end)]


def _bi_sqrt(n):
    return math.sqrt(n)  # raises ValueError on negative, matching STEPS


def _bi_index_of(text, search):
    return float(text.find(search))


def _bi_read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _bi_replace(text, old, new):
    return text.replace(old, new)


def _bi_list_sum(lst):
    return float(sum(lst))


def _bi_sqr(n):
    return n ** 2


def _bi_pow(base, exp):
    return math.pow(base, exp)


def _bi_log10(n):
    return math.log10(n)  # raises ValueError for n<=0, matching STEPS


def _bi_log(n):
    return math.log(n)  # raises ValueError for n<=0, matching STEPS


BUILTIN_ARITY = {
    "create_list": 2, "characters": 1, "slice": 3, "sqrt": 1,
    "index_of": 2, "read_file": 1, "replace": 3, "list_sum": 1,
    "sqr": 1, "pow": 2, "log10": 1, "log": 1,
}

_BUILTIN_FUNCS = {
    "create_list": _bi_create_list, "characters": _bi_characters,
    "slice": _bi_slice, "sqrt": _bi_sqrt, "index_of": _bi_index_of,
    "read_file": _bi_read_file, "replace": _bi_replace,
    "list_sum": _bi_list_sum, "sqr": _bi_sqr, "pow": _bi_pow,
    "log10": _bi_log10, "log": _bi_log,
}


def build_natives(output_func):
    """Build the CALL_NATIVE table for one VM run. `output_func` matches
    the same signature `Environment.output_handler` expects (a single
    `text` argument)."""
    natives = {
        "_display": _make_display(output_func),
        "_to_number": _to_number,
        "_to_text": _to_text,
        "_to_boolean": _to_boolean,
        "_length_of": _length_of,
        "_added_to": _added_to,
        "_split_by": _split_by,
        "_character_at": _character_at,
        "_contains": _contains,
        "_is_in": _is_in,
        "_add_to_list": _add_to_list,
        "_remove_from_list": _remove_from_list,
    }
    natives.update(_BUILTIN_FUNCS)
    return natives
