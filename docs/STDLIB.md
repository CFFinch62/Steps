# Steps Standard Library

The Steps standard library (stdlib) is automatically available to all buildings.

---

## Usage

Stdlib functions are called like any other step:

```steps
call abs with -5 storing result in x
call reverse with "hello" storing result in r
```

---

## Math Floor

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `abs` | `n as number` | `number` | Absolute value |
| `max` | `a as number, b as number` | `number` | Larger of two numbers |
| `min` | `a as number, b as number` | `number` | Smaller of two numbers |
| `round` | `n as number` | `number` | Round to nearest integer |

### Examples

```steps
call abs with -5 storing result in x        # 5
call max with 3, 7 storing result in y      # 7
call min with 3, 7 storing result in z      # 3
call round with 3.7 storing result in r     # 4
```

---

## Strings Floor

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `uppercase` | `s as text` | `text` | Convert to uppercase |
| `lowercase` | `s as text` | `text` | Convert to lowercase |
| `trim` | `s as text` | `text` | Remove leading/trailing spaces |
| `reverse` | `s as text` | `text` | Reverse text |
| `repeat_text` | `s as text, count as number` | `text` | Repeat text N times |

### Examples

```steps
call uppercase with "hello" storing result in u    # "HELLO"
call lowercase with "HELLO" storing result in l    # "hello"
call trim with "  hi  " storing result in t        # "hi"
call reverse with "hello" storing result in r      # "olleh"
call repeat_text with "*", 5 storing result in s   # "*****"
```

---

## Overriding Stdlib

Project floors can override stdlib definitions. If your project has a floor with the same name as a stdlib floor, your project's definitions take precedence.

---

## Extending Stdlib

To add new stdlib functions:

1. Create a new `.step` file in the appropriate floor folder
2. Add the step name to the `.floor` file
3. Rebuild/reinstall the package

### Naming Conventions

> [!CAUTION]
> **Avoid reserved words** when naming floors, steps, and parameters.

These caused conflicts and had to be renamed:
- `text` → `strings` (floor name)
- `times` → `count` (parameter name)

See [Reserved Words](LANGUAGE-REFERENCE.md#14-reserved-words) for the complete list.

---

## Stdlib Location

The stdlib is bundled at: `src/steps/stdlib/`

```
stdlib/
├── math/
│   ├── math.floor
│   ├── abs.step
│   ├── max.step
│   ├── min.step
│   └── round.step
└── strings/
    ├── strings.floor
    ├── uppercase.step
    ├── lowercase.step
    ├── trim.step
    ├── reverse.step
    └── repeat_text.step
```
