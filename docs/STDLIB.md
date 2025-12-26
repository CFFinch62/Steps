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
| `reverse` | `s as text` | `text` | Reverse text |
| `repeat_text` | `s as text, count as number` | `text` | Repeat text N times |

### Examples

```steps
call reverse with "hello" storing result in r      # "olleh"
call repeat_text with "*", 5 storing result in s   # "*****"
```

---

## Native String Functions

These string functions are *native* - implemented in Python for better performance.

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `lowercase` | `text` | `text` | Convert to lowercase |
| `uppercase` | `text` | `text` | Convert to uppercase |
| `trim` | `text` | `text` | Remove leading/trailing spaces |
| `slice` | `text, start, end` | `text` | Extract substring (start inclusive, end exclusive) |
| `index_of` | `text, search` | `number` | Find position of substring (-1 if not found) |
| `replace` | `text, old, new` | `text` | Replace all occurrences |
| `characters` | `text` | `list` | Convert text to list of characters |

### Examples

```steps
call lowercase with "HELLO" storing result in l    # "hello"
call uppercase with "hello" storing result in u    # "HELLO"
call trim with "  hi  " storing result in t        # "hi"
call slice with "hello", 0, 2 storing result in s  # "he"
call index_of with "hello", "ll" storing result in i  # 2
call replace with "hello", "l", "L" storing result in r  # "heLLo"

note: Iterate over a string character by character
call characters with "hello" storing result in chars
repeat for each char in chars
    display char
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



## TUI Floor (Text User Interface)

Create attractive console interfaces with boxes, banners, menus, and more.

### Native TUI Functions

Core drawing primitives implemented in Python:

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `box` | `content, width` | `text` | Draw single-line box around text |
| `line` | `width, style` | `text` | Horizontal line (styles: "single", "double", "dashed", "thick") |
| `banner` | `title, width` | `text` | Decorative title banner (double-line box) |
| `center_text` | `text, width` | `text` | Center-pad text to width |
| `pad_text` | `text, width, align` | `text` | Pad text ("left", "right", "center") |
| `progress_bar` | `current, total, width` | `text` | Text progress bar |

### Examples

```steps
note: Draw a banner
call banner with "My App", 40 storing result in b
display b

note: Draw a box
call box with "Welcome!", 30 storing result in bx
display bx

note: Draw a line
call line with 40, "double" storing result in ln
display ln

note: Show progress
call progress_bar with 7, 10, 20 storing result in pb
display pb
```

Output:
```
╔══════════════════════════════════════╗
║                My App                ║
╚══════════════════════════════════════╝

┌────────────────────────────┐
│         Welcome!           │
└────────────────────────────┘

════════════════════════════════════════

[██████████████░░░░░░] 70%
```

---

### Stdlib TUI Functions

Higher-level helpers written in Steps (extendable):

| Step | Parameters | Description |
|------|------------|-------------|
| `menu` | `options as list` | Display numbered menu |
| `table_display` | `rows as list, columns as list` | Display aligned columns |
| `divider` | `label as text, width as number` | Labeled divider line |

### Examples

```steps
note: Display a menu
call menu with ["Add Contact", "Search", "Exit"]

note: Display a table
set cols to ["name", "age"]
set data to []
add ["name": "Alice", "age": "30"] to data
add ["name": "Bob", "age": "25"] to data
call table_display with data, cols

note: Display a divider
call divider with "Options", 40
```

---



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
├── strings/
│   ├── strings.floor
│   ├── reverse.step
│   └── repeat_text.step
└── tui/
    ├── tui.floor
    ├── menu.step
    ├── table_display.step
    └── divider.step
```

> [!NOTE]
> Native functions (string operations like `lowercase`, `trim`, `slice` and TUI primitives like `box`, `banner`, `line`) are implemented in Python in `builtins/`, not as stdlib .step files.

