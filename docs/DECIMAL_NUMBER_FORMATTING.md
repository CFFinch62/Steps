# Decimal Number Formatting

I have implemented support for formatting numbers with specific decimal precision using the `as decimal(N)` syntax.

## Feature Overview

You can now format any number expression as text with a fixed number of decimal places. This is useful for displaying currency, physical measurements, or any value where precision matters for the user interface.

### Syntax
```steps
<expression> as decimal(<precision>)
```

### Examples

```steps
# Display pi with 2 decimal places (3.14)
display 3.14159 as decimal(2)

# Display price with 2 decimal places
set price to 19.99
display "The price is $" added to (price as decimal(2))

# Display integer with forced decimals (5.000)
display 5 as decimal(3)
```

## Changes

### 1. Logic Implementation
- Added [FormatNumberNode](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/src/steps/ast_nodes.py#502-514) to the AST to represent the formatting operation.
- Updated [parser.py](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/src/steps/parser.py) to recognize the `as decimal(...)` pattern in expressions.
- Added [format_number_string](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/src/steps/builtins.py#123-144) native function in [builtins.py](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/src/steps/builtins.py) to handle the actual formatting logic.
- Updated [interpreter.py](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/src/steps/interpreter.py) to evaluate the new node type.

### 2. Verification
- Validated with a manual verification script [verify_decimal.py](file:///home/chuck/Dropbox/Programming/Languages_and_Code/Programming_Projects/Programming_Tools/Steps/verify_decimal.py) covering various edge cases (0 decimals, variable precision).
- Ran full regression test suite (`tests/unit/`) to ensure no existing functionality was broken.
