# Steps Syntax Highlighting System

## Overview

The Steps IDE uses **tree-sitter** for syntax highlighting. Tree-sitter is a parser generator that creates fast, incremental parsers with excellent error recovery. This document explains how the system works and how to enhance it.

## Architecture

### Components

1. **Tree-sitter Grammar** (`tree-sitter-steps/grammar.js`)
   - Defines the Steps language syntax rules
   - Written in JavaScript
   - Generates a C parser

2. **Python Bindings** (`tree-sitter-steps/bindings/python/`)
   - Exposes the C parser to Python
   - Provides `get_language()` and `get_highlight_query()` functions
   - Installed as `tree-sitter-steps` package

3. **Highlight Query** (`tree-sitter-steps/queries/highlights_minimal.scm`)
   - Maps syntax nodes to highlight styles
   - Written in tree-sitter query language
   - Currently using minimal version for stability

4. **IDE Integration** (`src/steps_ide/editor/`)
   - `register_steps_language.py` - Registers Steps with Textual
   - `steps_editor.py` - Editor with Steps language support

### Data Flow

```
.step file → StepsEditor → register_steps_language() → Textual TextArea
                                    ↓
                            tree-sitter parser
                                    ↓
                            highlight query
                                    ↓
                            styled text display
```

## Current Status

### What Works ✅

The minimal highlight query (`highlights_minimal.scm`) successfully highlights:
- Comments (`note:`)
- Structure keywords (`building:`, `floor:`, `step:`, `riser:`, `do:`, `declare:`)
- Control flow keywords (`if`, `while`, `exit`)
- Identifiers (variable names)

### What's Missing ⚠️

The full highlight query (`highlights.scm`) exists but causes errors when loaded. It includes:
- String literals and escape sequences
- Number and boolean literals
- Operators (arithmetic, comparison, logical)
- Type annotations
- Function calls
- Punctuation

## How to Expand Highlighting

### Step 1: Understand the Query Language

Tree-sitter queries use S-expressions to match syntax nodes:

```scheme
; Match a node type
(comment) @comment

; Match a literal string
"if" @keyword.control

; Match nested structures
(step_def (identifier) @function)
```

### Step 2: Check Available Node Types

Before adding a highlight rule, verify the node type exists:

```bash
cd tree-sitter-steps
grep '"type": "your_node_name"' src/node-types.json
```

Node types come in two forms:
- **Named nodes**: `(node_name)` - structural elements like `(comment)`, `(identifier)`
- **Anonymous nodes**: `"literal"` - literal strings like `"if"`, `"while"`

### Step 3: Test Individual Rules

Create a test script to verify each rule works:

```python
from tree_sitter import Language, Query
import tree_sitter_steps

lang = tree_sitter_steps.get_language()

# Test a single rule
test_query = '(string) @string'
try:
    query = Query(lang, test_query)
    print("✓ Rule works!")
except Exception as e:
    print(f"✗ Rule failed: {e}")
```

### Step 4: Add Rules Incrementally

Edit `tree-sitter-steps/queries/highlights_minimal.scm` and add rules one section at a time:

```scheme
; Strings (add this section)
(string) @string
"\"" @punctuation.delimiter

; Numbers (add this section)
(number) @number

; Test after each addition!
```

### Step 5: Test in the IDE

After adding rules:

```bash
# No need to rebuild - the query is loaded dynamically
./venv/bin/python3 test_syntax_highlighting.py
```

If tests pass, test in the actual IDE by opening a `.step` file.

## Common Issues and Solutions

### Issue: "Invalid node type" Error

**Cause**: The node type doesn't exist in the grammar.

**Solution**: 
1. Check `src/node-types.json` to see available nodes
2. Use the exact name from the JSON
3. For literals, use quotes: `"keyword"` not `(keyword)`

### Issue: Highlighting Doesn't Update

**Cause**: Python is caching the old query file.

**Solution**:
```bash
# Clear Python cache
rm -rf tree-sitter-steps/bindings/python/tree_sitter_steps/__pycache__

# Restart the IDE
```

### Issue: Grammar Changes Don't Apply

**Cause**: The parser wasn't regenerated.

**Solution**:
```bash
cd tree-sitter-steps
npm run generate  # Regenerate parser
cd ..
./venv/bin/python3 -m pip uninstall -y tree-sitter-steps
./venv/bin/python3 -m pip install -e tree-sitter-steps/
```

## Highlight Style Reference

### Available Styles

These are the standard tree-sitter highlight names that Textual recognizes:

| Style Name | Use For | Example |
|------------|---------|---------|
| `@comment` | Comments | `note: this is a comment` |
| `@keyword` | General keywords | `set`, `to`, `as` |
| `@keyword.control` | Control flow | `if`, `while`, `exit` |
| `@keyword.function` | Function-related | `call`, `return` |
| `@keyword.operator` | Word operators | `and`, `or`, `not` |
| `@function` | Function names | Step names |
| `@function.builtin` | Built-in functions | `display`, `input` |
| `@variable` | Variable names | Identifiers |
| `@variable.parameter` | Parameters | Function parameters |
| `@constant.builtin` | Built-in constants | `nothing`, `true`, `false` |
| `@string` | String literals | `"hello"` |
| `@string.escape` | Escape sequences | `\n`, `\t` |
| `@number` | Numeric literals | `42`, `3.14` |
| `@boolean` | Boolean literals | `true`, `false` |
| `@operator` | Operators | `+`, `-`, `*`, `/` |
| `@punctuation.delimiter` | Delimiters | `:`, `,` |
| `@punctuation.bracket` | Brackets | `[`, `]`, `(`, `)` |
| `@type` | Type names | `number`, `text`, `boolean` |
| `@namespace` | Namespaces | Building/floor names |

## Recommended Enhancement Order

To safely expand the highlight query, add features in this order:

### Phase 1: Literals (Low Risk)
```scheme
; Add to highlights_minimal.scm
(number) @number
(string) @string
"true" @boolean
"false" @boolean
"nothing" @constant.builtin
```

### Phase 2: Operators (Low Risk)
```scheme
"+" @operator
"-" @operator
"*" @operator
"/" @operator
"and" @keyword.operator
"or" @keyword.operator
"not" @keyword.operator
```

### Phase 3: More Keywords (Medium Risk)
```scheme
"set" @keyword
"to" @keyword
"as" @keyword
"call" @keyword.function
"return" @keyword.return
"display" @function.builtin
"input" @function.builtin
```

### Phase 4: Structured Matches (Higher Risk)
```scheme
; Function definitions
(step_def (identifier) @function)
(riser_def (identifier) @function)

; Function calls
(call_statement (identifier) @function.call)

; Parameters
(parameter (identifier) @variable.parameter)
```

## Testing Checklist

Before committing highlight query changes:

- [ ] Run `./venv/bin/python3 test_syntax_highlighting.py`
- [ ] All three tests pass
- [ ] Open a sample `.step` file in the IDE
- [ ] Verify keywords are highlighted correctly
- [ ] Verify strings and numbers are highlighted
- [ ] Verify comments are highlighted
- [ ] Check that invalid syntax doesn't crash the highlighter

## Reference Files

- **Grammar**: `tree-sitter-steps/grammar.js`
- **Node Types**: `tree-sitter-steps/src/node-types.json` (generated)
- **Highlight Query**: `tree-sitter-steps/queries/highlights_minimal.scm`
- **Full Query (broken)**: `tree-sitter-steps/queries/highlights.scm`
- **Test Script**: `test_syntax_highlighting.py`
- **Language Spec**: `docs/LANGUAGE-REFERENCE.md`

## Getting Help

If you encounter issues:

1. Check `src/node-types.json` for available node types
2. Test individual rules with the test script
3. Compare with working examples in `highlights_minimal.scm`
4. Look at other tree-sitter highlight queries (e.g., Python, JavaScript) for patterns
5. Tree-sitter query documentation: https://tree-sitter.github.io/tree-sitter/syntax-highlighting

## Future Enhancements

Potential improvements to the highlighting system:

- [ ] Semantic highlighting (context-aware colors)
- [ ] Error highlighting (show syntax errors in red)
- [ ] Scope-based highlighting (different colors for local vs global variables)
- [ ] Custom color themes
- [ ] Highlight matching brackets/parentheses
- [ ] Highlight current word occurrences

