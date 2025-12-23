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

## Random Floor (Native)

These functions are *native* - implemented in Python, not Steps code.

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `random_int` | `min_val, max_val as number` | `number` | Random integer in range (inclusive) |
| `random_choice` | `lst as list` | `any` | Pick random element from list |

### Examples

```steps
call random_int with 1, 100 storing result in r     # 42 (random)
call random_choice with my_list storing result in x # random element
```

---

## Files Floor (Native)

Text and CSV file operations.

### Text File Functions

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `read_file` | `path` | `text` | Read file contents |
| `write_file` | `path, content` | `nothing` | Write (overwrite) file |
| `append_file` | `path, content` | `nothing` | Append to file |
| `file_exists` | `path` | `boolean` | Check if file exists |

### CSV Functions

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `read_csv` | `path` | `list of tables` | Read CSV rows |
| `write_csv` | `path, data` | `nothing` | Write list of tables |

### Examples

```steps
note: Text file operations
call write_file with "output.txt", "Hello!"
call read_file with "output.txt" storing result in content

note: CSV operations
set rows to []
set row to ["name": "Alice", "age": "30"]
add row to data
call write_csv with "data.csv", rows

call read_csv with "data.csv" storing result in loaded
repeat for each person in loaded
    display person["name"]
```

### Creating Empty Tables

Use `[:]` to create an empty table:

```steps
set row to [:]              # Creates an empty table
set row["name"] to "Bob"
set row["age"] to "30"
```



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
