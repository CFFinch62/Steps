# Steps Language Reference

> **Complete reference for the Steps programming language**

Version 1.0

---

## Table of Contents

1. [Lexical Structure](#1-lexical-structure)
2. [Data Types](#2-data-types)
3. [Program Structure](#3-program-structure)
4. [Variables and Declarations](#4-variables-and-declarations)
5. [Operators](#5-operators)
6. [Expressions](#6-expressions)
7. [Statements](#7-statements)
8. [Control Flow](#8-control-flow)
9. [Steps and Risers](#9-steps-and-risers)
10. [Floors and Buildings](#10-floors-and-buildings)
11. [Error Handling](#11-error-handling)
12. [Built-in Operations](#12-built-in-operations)
13. [Comments](#13-comments)
14. [Reserved Words](#14-reserved-words)
15. [File Extensions](#15-file-extensions)
16. [Standard Library](#16-standard-library)

---

## 1. Lexical Structure

### 1.1 Whitespace and Indentation

Steps uses **significant whitespace**. Indentation defines code blocks.

- **Indent unit**: 4 spaces (tabs are converted to spaces)
- **Block start**: Increased indentation after `:` or block keyword
- **Block end**: Return to previous indentation level

```steps
if condition
    # This is inside the if block (4 spaces)
    display "Inside"
# This is outside the if block (0 spaces)
display "Outside"
```

### 1.2 Line Continuation

Statements are single-line. Long expressions can use parentheses:

```steps
set result to (first_value +
    second_value +
    third_value)
```

### 1.3 Case Sensitivity

Steps is **case-sensitive**:
- `myVariable` and `myvariable` are different variables
- Keywords must be lowercase: `if`, `set`, `display`

### 1.4 Identifiers

Valid identifiers:
- Start with a letter or underscore
- Contain letters, digits, or underscores
- Cannot be reserved words

```steps
# Valid
my_variable
_private
count2
firstName

# Invalid
2count      # Starts with digit
my-var      # Contains hyphen
if          # Reserved word
```

---

## 2. Data Types

### 2.1 Number

Integers and floating-point numbers:

```steps
set integer to 42
set negative to -17
set decimal to 3.14159
set scientific to 1.5e10
```

### 2.2 Text

String values enclosed in double quotes:

```steps
set greeting to "Hello, World!"
set empty to ""
set with_quotes to "She said \"Hello\""
```

**Escape sequences:**

| Sequence | Meaning |
|----------|---------|
| `\"` | Double quote |
| `\\` | Backslash |
| `\n` | Newline |
| `\t` | Tab |

### 2.3 Boolean

Logical true or false:

```steps
set is_active to true
set is_complete to false
```

### 2.4 List

Ordered collection of values:

```steps
set empty_list to []
set numbers to [1, 2, 3, 4, 5]
set mixed to ["hello", 42, true]
set nested to [[1, 2], [3, 4]]
```

### 2.5 Table

Key-value pairs (dictionary/map):

```steps
set empty_table to [:]
set person to ["name": "Alice", "age": 25]
set nested_table to ["user": ["id": 1, "name": "Bob"]]
```

### 2.6 Nothing

Represents absence of value:

```steps
set result to nothing
```

### 2.7 Type Conversion

Convert between types with `as`:

```steps
set text_num to "42"
set num to text_num as number      # 42

set num to 42
set text to num as text            # "42"

set num to 1
set bool to num as boolean         # true (non-zero = true)

set text to "true"
set bool to text as boolean        # true
```

---

## 3. Program Structure

### 3.1 File Organization

```
project_name/                    # Project folder
├── project_name.building        # Entry point (required)
├── floor_name/                  # Floor folder
│   ├── floor_name.floor         # Floor definition
│   ├── step_one.step            # Step files
│   └── step_two.step
└── another_floor/
    ├── another_floor.floor
    └── another_step.step
```

### 3.2 Execution Flow

1. Interpreter loads the `.building` file
2. Floors are discovered from subdirectories
3. Steps are loaded as needed (lazy loading)
4. Execution begins at the building's `do:` section
5. Program ends at `exit` or natural completion

---

## 4. Variables and Declarations

### 4.1 Simple Assignment

```steps
set variable_name to value
```

### 4.2 Declaration Section

In steps, use `declare:` for explicit type declarations:

```steps
step: example
    declare:
        count as number
        message as text
        items as list
        config as table
        flag as boolean
    
    do:
        set count to 0
```

### 4.3 Type Locking

Use `fixed` to prevent type changes:

```steps
declare:
    score as number fixed    # Cannot be reassigned to non-number
    label as text           # Can be reassigned to any type
```

### 4.4 Scope

- **Building scope**: Variables in building are global
- **Step scope**: Variables in step are local
- **Riser scope**: Variables in riser are local to riser
- **Block scope**: Loop variables are scoped to the loop

---

## 5. Operators

### 5.1 Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` → `8` |
| `-` | Subtraction | `5 - 3` → `2` |
| `*` | Multiplication | `5 * 3` → `15` |
| `/` | Division | `15 / 3` → `5` |
| `-` (unary) | Negation | `-5` |

### 5.2 Comparison Operators

| Operator | Description |
|----------|-------------|
| `is equal to` | Equality test |
| `equals` | Equality test (shorthand) |
| `is not equal to` | Inequality test |
| `is less than` | Less than |
| `is greater than` | Greater than |
| `is less than or equal to` | Less than or equal |
| `is greater than or equal to` | Greater than or equal |

```steps
if x is equal to 10
if name equals "Alice"
if age is greater than 18
if score is less than or equal to 100
```

### 5.3 Boolean Operators

| Operator | Description |
|----------|-------------|
| `and` | Logical AND |
| `or` | Logical OR |
| `not` | Logical NOT |

```steps
if age is greater than 18 and has_license
    display "Can drive"

if is_admin or is_moderator
    display "Has permissions"

if not is_locked
    display "Accessible"
```

### 5.4 Text Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `added to` | Concatenation | `"Hello, " added to name` |

```steps
set greeting to "Hello, " added to name added to "!"
```

### 5.5 Operator Precedence

From highest to lowest:

1. Parentheses `()`
2. Unary operators: `not`, `-`
3. Multiplication/Division: `*`, `/`
4. Addition/Subtraction: `+`, `-`
5. Comparison: `is equal to`, `is less than`, etc.
6. Logical AND: `and`
7. Logical OR: `or`

---

## 6. Expressions

### 6.1 Literal Expressions

```steps
42                          # Number
3.14                        # Decimal
"Hello"                     # Text
true                        # Boolean
false                       # Boolean
nothing                     # Nothing
[1, 2, 3]                   # List
["key": "value"]            # Table
```

### 6.2 Variable References

```steps
display my_variable
set x to y + z
```

### 6.3 Input Expression

```steps
set name to input
set age to input as number
```

### 6.4 Index Access

```steps
# List access (0-based)
set first to my_list[0]
set last to my_list[length of my_list - 1]

# Table access
set value to my_table["key"]
```

### 6.5 Type Conversion

```steps
set num to "42" as number
set text to 42 as text
set bool to 1 as boolean
```

### 6.6 Grouped Expressions

```steps
set result to (a + b) * c
set complex to ((x + y) * z) / w
```

---

## 7. Statements

### 7.1 Assignment Statement

```steps
set variable to expression
```

Assign to index:
```steps
set my_list[0] to "new value"
set my_table["key"] to 42
```

### 7.2 Display Statement

```steps
display expression
display "Hello, " added to name
```

### 7.3 Return Statement

```steps
return expression
return nothing
```

### 7.4 Exit Statement

```steps
exit    # Ends program execution
```

### 7.5 Call Statement

```steps
# Call without arguments
call step_name

# Call with arguments
call step_name with arg1, arg2

# Call and capture result
call step_name storing result in variable

# Call with arguments and capture result
call step_name with arg1, arg2 storing result in variable
```

### 7.6 List Manipulation

```steps
add item to my_list
remove item from my_list
```

---

## 8. Control Flow

### 8.1 If Statement

```steps
if condition
    statements
```

### 8.2 If-Otherwise Statement

```steps
if condition
    statements
otherwise
    statements
```

### 8.3 If-Otherwise If-Otherwise Statement

```steps
if condition1
    statements
otherwise if condition2
    statements
otherwise if condition3
    statements
otherwise
    statements
```

### 8.4 Repeat Times Loop

```steps
repeat 10 times
    statements
```

With a variable count:
```steps
repeat count times
    statements
```

### 8.5 Repeat For Each Loop

```steps
repeat for each item in collection
    display item
```

### 8.6 Repeat While Loop

```steps
repeat while condition
    statements
```

### 8.7 Loop Control

Currently, Steps does not have `break` or `continue`. Use conditionals within loops instead.

---

## 9. Steps and Risers

### 9.1 Step Definition

```steps
step: step_name
    belongs to: floor_name
    expects: param1, param2
    returns: return_value

    declare:
        local_var as type

    do:
        statements
        return return_value
```

### 9.2 Step Sections

| Section | Required | Description |
|---------|----------|-------------|
| `step:` | Yes | Step name (must match filename) |
| `belongs to:` | Yes | Parent floor name |
| `expects:` | No | Parameters (comma-separated) |
| `returns:` | No | Return value name |
| `declare:` | No | Variable declarations |
| `do:` | Yes | Executable statements |

### 9.3 Calling Steps

```steps
# No arguments, no return
call validate_data

# With arguments
call process_item with item, options

# With return value
call calculate_total storing result in total

# With arguments and return value
call calculate_tax with amount, rate storing result in tax
```

### 9.4 Riser Definition

Risers are private helpers inside a step:

```steps
step: parent_step
    expects: value
    returns: result

    riser: helper_function
        expects: input
        returns: output

        do:
            set output to input * 2
            return output

    do:
        call helper_function with value storing result in doubled
        set result to doubled + 10
        return result
```

### 9.5 Riser Visibility

- Risers are only visible within their parent step
- Cannot be called from other steps or the building
- Perfect for helper functions that shouldn't be exposed

---

## 10. Floors and Buildings

### 10.1 Floor Definition

```steps
floor: floor_name
    step: step_one
    step: step_two
    step: step_three
```

### 10.2 Building Definition

```steps
building: project_name
    note: Optional description

    declare:
        variables as type

    do:
        statements
        exit
```

### 10.3 Building Sections

| Section | Required | Description |
|---------|----------|-------------|
| `building:` | Yes | Program name (must match folder) |
| `note:` | No | Description/comment |
| `declare:` | No | Global variable declarations |
| `do:` | Yes | Main program logic |

---

## 11. Error Handling

### 11.1 Attempt Block

```steps
attempt:
    risky_statements
if unsuccessful:
    error_handling_statements
then continue:
    cleanup_statements
```

### 11.2 Sections

| Section | Required | Description |
|---------|----------|-------------|
| `attempt:` | Yes | Code that might fail |
| `if unsuccessful:` | No | Error handling |
| `then continue:` | No | Always executed (cleanup) |

### 11.3 The `problem_message` Variable

Available in `if unsuccessful:` block:

```steps
attempt:
    set value to "abc" as number
if unsuccessful:
    display "Error occurred: " added to problem_message
```

### 11.4 Example

```steps
attempt:
    display "Enter a number: "
    set num to input as number
    set result to 100 / num
    display "Result: " added to (result as text)
if unsuccessful:
    display "Invalid input: " added to problem_message
    set result to 0
then continue:
    display "Operation complete"
```

---

## 12. Built-in Operations

### 12.1 Type Checking

| Operation | Description | Example |
|-----------|-------------|---------|
| `type of` | Get type name as text | `type of 42` → `"number"` |
| `is a number` | Check if number | `x is a number` |
| `is a text` | Check if text | `x is a text` |
| `is a boolean` | Check if boolean | `x is a boolean` |
| `is a list` | Check if list | `x is a list` |
| `is a table` | Check if table | `x is a table` |

### 12.2 Text Operations

| Operation | Description | Example |
|-----------|-------------|---------|
| `length of` | Get text length | `length of "hello"` → `5` |
| `character at N of` | Get character at index | `character at 0 of "hello"` → `"h"` |
| `added to` | Concatenate | `"a" added to "b"` → `"ab"` |
| `contains` | Check substring | `"hello" contains "ell"` → `true` |
| `starts with` | Check prefix | `"hello" starts with "he"` → `true` |
| `ends with` | Check suffix | `"hello" ends with "lo"` → `true` |
| `split by` | Split into list | `"a,b,c" split by ","` → `["a", "b", "c"]` |

```steps
set text to "Hello, World!"

set len to length of text                    # 13
set first to character at 0 of text          # "H"
set has_world to text contains "World"       # true
set words to text split by " "               # ["Hello,", "World!"]
```

### 12.3 List Operations

| Operation | Description | Example |
|-----------|-------------|---------|
| `length of` | Get list length | `length of [1, 2, 3]` → `3` |
| `list[N]` | Access by index | `my_list[0]` |
| `add X to list` | Append item | `add 4 to my_list` |
| `remove X from list` | Remove item | `remove 2 from my_list` |
| `X is in list` | Check membership | `3 is in [1, 2, 3]` → `true` |

```steps
set numbers to [1, 2, 3]

set len to length of numbers     # 3
set first to numbers[0]          # 1

add 4 to numbers                 # [1, 2, 3, 4]
remove 2 from numbers            # [1, 3, 4]

if 3 is in numbers
    display "Found 3"
```

### 12.4 Table Operations

| Operation | Description | Example |
|-----------|-------------|---------|
| `table["key"]` | Access value | `person["name"]` |
| `set table["key"] to` | Set value | `set person["age"] to 26` |

```steps
set person to ["name": "Alice", "age": 25]

set name to person["name"]           # "Alice"
set person["city"] to "Boston"       # Add new key
set person["age"] to 26              # Update existing key
```

### 12.5 Numeric Operations

| Operation | Description |
|-----------|-------------|
| `+`, `-`, `*`, `/` | Basic arithmetic |
| `-` (unary) | Negation |

```steps
set a to 10
set b to 3

set sum to a + b          # 13
set diff to a - b         # 7
set prod to a * b         # 30
set quot to a / b         # 3.333...
set neg to -a             # -10
```

---

## 13. Comments

### 13.1 Single-Line Comments

```steps
note: This is a comment
set x to 10    note: inline comment not supported
```

### 13.2 Multi-Line Comments

```steps
note block:
    This comment spans
    multiple lines.

    It continues until "end note"
end note
```

### 13.3 Documentation Comments

Use `note:` at the beginning of a step to document its purpose:

```steps
step: calculate_tax
    belongs to: calculations
    expects: amount, rate
    returns: tax

    note: Calculate tax based on amount and rate percentage.
    note: Rate should be between 0 and 100.

    do:
        set tax to amount * (rate / 100)
        return tax
```

---

## 14. Reserved Words

The following words are reserved and cannot be used as identifiers:

### Structure Keywords
```
building  floor  step  riser  belongs  to  expects  returns
declare  do  exit
```

### Variable Keywords
```
as  fixed  set  to
```

### Invocation Keywords
```
call  with  storing  result  in  return  display  input
```

### Control Flow Keywords
```
if  otherwise  repeat  times  for  each  while
```

### Error Handling Keywords
```
attempt  unsuccessful  then  continue
```

### Comment Keywords
```
note  block  end
```

### Operator Keywords
```
and  or  not  is  equal  less  greater  than
added  split  by  character  at  of  length
contains  starts  ends  add  remove  from
```

### Type Keywords
```
number  text  boolean  list  table
```

### Literal Keywords
```
true  false  nothing
```

### Special Variables
```
problem_message
```

> [!CAUTION]
> **Reserved words cannot be used as:** floor names, step names, parameter names, or variable names.
> For example, `text` and `times` are keywords and will cause parse errors if used as identifiers.

---

## 15. File Extensions

| Extension | Purpose | Required Contents |
|-----------|---------|-------------------|
| `.building` | Program entry point | `building:` declaration |
| `.floor` | Floor definition | `floor:` declaration |
| `.step` | Step implementation | `step:` declaration |

### Naming Conventions

- File name should match the declaration name
- Use lowercase with underscores for multi-word names
- Folder name for floors should match floor name

**Examples:**
```
my_project/
├── my_project.building      # building: my_project
├── data_processing/
│   ├── data_processing.floor    # floor: data_processing
│   ├── load_data.step           # step: load_data
│   └── validate_data.step       # step: validate_data
└── output/
    ├── output.floor             # floor: output
    └── format_report.step       # step: format_report
```

---

## Appendix A: Grammar Summary

### Program Structure
```
program     → building
building    → "building:" IDENTIFIER sections
floor       → "floor:" IDENTIFIER step_list
step        → "step:" IDENTIFIER step_sections
riser       → "riser:" IDENTIFIER riser_sections
```

### Sections
```
sections      → note? declare? do
step_sections → belongs expects? returns? riser* declare? do
riser_sections → expects? returns? declare? do
```

### Statements
```
statement → set_stmt | display_stmt | call_stmt | return_stmt
          | if_stmt | repeat_stmt | attempt_stmt | add_stmt
          | remove_stmt | exit_stmt
```

### Expressions
```
expression → or_expr
or_expr    → and_expr ("or" and_expr)*
and_expr   → equality (and equality)*
equality   → comparison (("is equal to" | "is not equal to") comparison)*
comparison → term (("is less than" | "is greater than" | ...) term)*
term       → factor (("+" | "-" | "added to") factor)*
factor     → unary (("*" | "/") unary)*
unary      → ("not" | "-") unary | primary
primary    → literal | identifier | input | "(" expression ")" | index_access
```

---

## Appendix B: Error Messages

Steps provides educational error messages that explain what went wrong and how to fix it.

### Syntax Errors

| Error | Cause | Example |
|-------|-------|---------|
| E101 | Unexpected token | Missing keyword or operator |
| E102 | Missing colon | `building program` instead of `building: program` |
| E103 | Invalid indentation | Wrong number of spaces |

### Type Errors

| Error | Cause | Example |
|-------|-------|---------|
| E201 | Type mismatch | `"hello" + 5` |
| E202 | Invalid conversion | `"abc" as number` |
| E203 | Fixed type violation | Assigning wrong type to fixed variable |

### Runtime Errors

| Error | Cause | Example |
|-------|-------|---------|
| E301 | Undefined variable | Using variable before assignment |
| E302 | Undefined step | Calling non-existent step |
| E303 | Division by zero | `10 / 0` |
| E304 | Index out of range | `list[100]` on 3-element list |

### Structure Errors

| Error | Cause | Example |
|-------|-------|---------|
| E401 | Missing building file | No `.building` in project folder |
| E402 | Missing floor file | Floor folder without `.floor` file |
| E403 | Step not in floor | Step without `belongs to:` |

---

## Appendix C: Complete Example

Here is a complete, working Steps program:

**tip_calculator/tip_calculator.building:**
```steps
building: tip_calculator
    note: Calculate tip and total for a restaurant bill

    declare:
        bill_amount as number
        tip_percent as number
        tip_amount as number
        total as number

    do:
        display "Welcome to Tip Calculator!"
        display ""

        display "Enter bill amount: $"
        set bill_amount to input as number

        display "Enter tip percentage (e.g., 15, 18, 20): "
        set tip_percent to input as number

        call calculate_tip with bill_amount, tip_percent storing result in tip_amount
        set total to bill_amount + tip_amount

        display ""
        display "Bill:  $" added to (bill_amount as text)
        display "Tip:   $" added to (tip_amount as text)
        display "Total: $" added to (total as text)

        exit
```

**tip_calculator/math/math.floor:**
```steps
floor: math
    step: calculate_tip
    step: round_to_cents
```

**tip_calculator/math/calculate_tip.step:**
```steps
step: calculate_tip
    belongs to: math
    expects: amount, percent
    returns: tip

    note: Calculate tip based on percentage

    riser: calculate_percentage
        expects: value, pct
        returns: result

        do:
            set result to value * (pct / 100)
            return result

    declare:
        raw_tip as number

    do:
        call calculate_percentage with amount, percent storing result in raw_tip
        call round_to_cents with raw_tip storing result in tip
        return tip
```

**tip_calculator/math/round_to_cents.step:**
```steps
step: round_to_cents
    belongs to: math
    expects: amount
    returns: rounded

    note: Round a number to 2 decimal places

    do:
        note: Simple rounding (multiply, truncate, divide)
        set rounded to amount
        return rounded
```

---

## 16. Standard Library

Steps includes a bundled standard library that's automatically available to all buildings.

### Math Functions

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `abs` | `n as number` | `number` | Absolute value |
| `max` | `a, b as number` | `number` | Larger of two |
| `min` | `a, b as number` | `number` | Smaller of two |
| `round` | `n as number` | `number` | Round to nearest |

### Strings Functions

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `uppercase` | `s as text` | `text` | To uppercase |
| `lowercase` | `s as text` | `text` | To lowercase |
| `trim` | `s as text` | `text` | Remove whitespace |
| `reverse` | `s as text` | `text` | Reverse text |
| `repeat_text` | `s, count` | `text` | Repeat N times |

### Example

```steps
call abs with -5 storing result in x      # 5
call reverse with "hello" storing result in r   # "olleh"
```

> **See also:** [STDLIB.md](STDLIB.md) for complete documentation.

---

*End of Language Reference*

