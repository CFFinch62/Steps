# Steps REPL Specification

## Purpose

The Steps REPL is a **teaching tool for language fundamentals only**. It is intentionally limited in scope - it exists to demonstrate assignment, operators, expressions, and basic control flow without the complexity of projects, files, or step definitions.

For real development work, use the Steps IDE.

## Philosophy

The REPL follows the same approach used in introductory Lisp/Scheme courses:
- Show a concept
- Type it in
- See the result
- Understand it

No file loading. No step definitions. Just language primitives.

## What the REPL Supports

### Variables and Assignment

```
>>> set x to 42
>>> display x
42
>>> set name to "Chuck"
>>> display "Hello, " added to name
Hello, Chuck
```

### Math Operations

```
>>> display 10 + 5
15
>>> display 100 / 4
25
>>> set result to (10 + 5) * 2
>>> display result
30
```

### Text Operations

```
>>> set greeting to "Hello" added to ", " added to "World"
>>> display greeting
Hello, World
>>> display length of greeting
12
>>> display greeting contains "World"
true
```

### Comparisons

```
>>> display 10 is greater than 5
true
>>> display "abc" equals "abc"
true
>>> set age to 25
>>> display age is less than 18
false
```

### Boolean Logic

```
>>> display true and false
false
>>> display true or false
true
>>> display not false
true
```

### Simple Conditionals

```
>>> set age to 25
>>> if age is greater than 18
...     display "Adult"
...
Adult
```

### Simple Loops

```
>>> repeat 3 times
...     display "Hello"
...
Hello
Hello
Hello
```

### Lists

```
>>> set numbers to [1, 2, 3]
>>> display numbers
[1, 2, 3]
>>> add 4 to numbers
>>> display numbers
[1, 2, 3, 4]
>>> display length of numbers
4
```

### Tables

```
>>> set person to ["name": "Chuck", "age": 63]
>>> display person["name"]
Chuck
>>> set person["city"] to "New York"
```

### Type Conversion

```
>>> set x to "42" as number
>>> display x + 8
50
>>> set label to 100 as text
>>> display "Value: " added to label
Value: 100
```

## What the REPL Does NOT Support

- `step:` definitions (use the IDE)
- `riser:` definitions (use the IDE)
- `floor:` definitions (use the IDE)
- `building:` definitions (use the IDE)
- `call` statements (no steps to call)
- File loading/saving
- Project navigation
- `belongs to:` (no floors)
- `expects:` / `returns:` (no step signatures)
- `declare:` sections (variables are created on first assignment)
- `do:` blocks (no steps)
- `attempt:` / `if unsuccessful:` (simplified environment)
- Multi-line function definitions

## REPL Commands

| Command | Action |
|---------|--------|
| `help` | Show available commands and syntax examples |
| `exit` or `quit` | Exit the REPL |
| `clear` | Clear the screen |
| `vars` | Show all defined variables and their values |
| `reset` | Clear all variables, start fresh |

## Interface

```
Steps REPL v0.1
Type 'help' for commands, 'exit' to quit.

>>> set x to 42
>>> display x * 2
84
>>> if x is greater than 10
...     display "big number"
...
big number
>>> exit
Goodbye!
```

### Prompt Behavior

- `>>>` indicates ready for input
- `...` indicates continuation (inside if/loop block)
- Blank line ends a multi-line block
- Results display immediately after evaluation

## Implementation Notes

### Simplified Environment

The REPL uses a simplified single-scope environment:
- Variables are created on first `set`
- No `fixed` type enforcement (everything is flexible)
- No scope nesting beyond if/loop bodies

### Error Handling

Errors should still be educational:

```
>>> display undefined_var
Error: Variable 'undefined_var' has not been defined.
Try: set undefined_var to some_value

>>> set x to "hello" + 5
Error: Cannot add number to text.
To combine them: "hello" added to (5 as text)
```

### No Persistence

The REPL starts fresh each time. No session saving, no history file (though command history within a session via up/down arrows is fine).

## Use Cases

### Teaching Assignment

```
>>> set age to 25
>>> display age
25
>>> set age to age + 1
>>> display age
26
```

### Teaching Conditionals

```
>>> set score to 85
>>> if score is greater than or equal to 90
...     display "A"
... otherwise if score is greater than or equal to 80
...     display "B"
... otherwise
...     display "C"
...
B
```

### Teaching Loops

```
>>> set total to 0
>>> repeat 5 times
...     set total to total + 1
...
>>> display total
5
```

### Teaching Lists

```
>>> set fruits to ["apple", "banana"]
>>> add "cherry" to fruits
>>> repeat for each fruit in fruits
...     display fruit
...
apple
banana
cherry
```

## Relationship to IDE

The REPL teaches **what** the language constructs do.
The IDE teaches **how** to structure programs.

Students should:
1. Learn fundamentals in the REPL
2. Graduate to the IDE when ready to build actual programs
3. Return to the REPL to test small expressions quickly
