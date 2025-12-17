# How Steps Builtins Work

## Builtin Architecture Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                     Steps Program                                  │
│  call random_int with 1, 100 storing result in x                  │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│                    Interpreter.call_step()                        │
├──────────────────────────────────────────────────────────────────┤
│  1. Check NATIVE_FUNCTIONS registry                               │
│     → If found: call Python function directly                     │
│     → If not found: look up user-defined step                     │
└────────────────────────────┬─────────────────────────────────────┘
                             │
        ┌────────────────────┴───────────────────┐
        ▼                                        ▼
┌───────────────────────┐              ┌───────────────────────┐
│  builtins.py          │              │  User Step (.step)    │
│  NATIVE_FUNCTIONS     │              │  Pure Steps code      │
│  → Python code        │              │                       │
└───────────────────────┘              └───────────────────────┘
```

---

## Three Levels of Builtins

### Level 1: Expression Operators (Hardcoded in Interpreter)

Used by parser/interpreter for expression evaluation. **Not callable by users.**

```python
# builtins.py - used internally
add_numbers(left, right)  # for: a + b
text_concatenate(a, b)     # for: a added to b
less_than(a, b)           # for: a is less than b
```

### Level 2: Native Functions (NATIVE_FUNCTIONS Registry)

Python functions callable from Steps via [call](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/src/steps/interpreter.py#151-214). **Registered in [builtins.py](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/src/steps/builtins.py).**

```python
# builtins.py
NATIVE_FUNCTIONS = {
    "random_int": {
        "function": random_int,
        "params": ["min_val", "max_val"],
    },
}
```

Usage in Steps:
```steps
call random_int with 1, 100 storing result in x
```

### Level 3: Stdlib Steps (Pure Steps Code)

Regular [.step](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/projects/test_syntax.step) files in `src/steps/stdlib/`. **Written in Steps, not Python.**

```
stdlib/math/abs.step  → Pure Steps logic
stdlib/strings/reverse.step  → Pure Steps logic
```

---

## Adding New Native Functions

1. **Add function to `builtins.py`**:
```python
def my_native_fn(arg1: StepsValue, location=None) -> StepsValue:
    # Python code here
    return StepsNumber(42)
```

2. **Register in NATIVE_FUNCTIONS**:
```python
NATIVE_FUNCTIONS = {
    "my_native_fn": {
        "function": my_native_fn,
        "params": ["arg1"],
    },
}
```

3. **Use in Steps**:
```steps
call my_native_fn with 123 storing result in x
```

---

## Key Files

| File | Purpose |
|------|---------|
| [builtins.py](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/src/steps/builtins.py) | Native Python functions & NATIVE_FUNCTIONS registry |
| [interpreter.py](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/src/steps/interpreter.py) | `call_step()` checks natives before user steps |
| [stdlib/](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/src/steps/stdlib) | Pure Steps code stdlib |
