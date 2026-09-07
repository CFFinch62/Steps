# STEPS Programming Language

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-437%20passing-green.svg)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

![STEPS IDE Screenshot](images/STEPSIDE.png)

> **An educational programming language that makes program structure visible and mandatory.**

STEPS teaches programming through an architectural metaphor, enforcing decomposition and clear structure from day one. STEPS is the first of 3 teaching labugaes crreated by Fragillidae Software. The others are PLAIN (general purpose scripting lanauge like a mix if Python and Go) and FORGE(statically types system programming language with easier beginer entry than C).



---

## 🏗️ The Building Metaphor

STEPS uses architecture to make program structure explicit and visible:

| Construct    | Purpose                                 | File Extension   |
| ------------ | --------------------------------------- | ---------------- |
| **Building** | Complete program (entry point)          | `.building`      |
| **Floor**    | Functional grouping of related STEPS    | (in `.building`) |
| **Step**     | Single unit of work (one file per step) | `.step`          |
| **Riser**    | Private helper function within a step   | (inside `.step`) |

This hierarchy enforces decomposition - you can't write monolithic code in STEPS!

---

## 📦 Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/CFFinch62/STEPS.git
cd STEPS

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# The full local setup — CLI, the PyQt6 IDE, and serial support
./setup.sh
```

`./setup.sh` is the one-command path and installs everything below. If you
prefer to do it by hand, pick what you need:

```bash
pip install -e .                   # CLI only — steps run / check / repl
pip install -e ".[ide]"            # + the PyQt6 desktop IDE (steps-ide)
pip install -e ".[ide,serial]"     # + pyserial, for the instruments projects
pip install -e ".[dev]"            # + pytest, mypy, black, isort
```

The base install pulls in **no third-party packages at all** — the language
core is standard library only, so `steps run` works on a bare checkout without
downloading Qt. The extras are additive; `steps-ide` tells you which one to
install if you run it without PyQt6.

---

## 🚀 Quick Start

### 1. Create a Simple Program

Create a project folder with a `.building` file:

```
hello_world/
└── hello_world.building
```

In `hello_world.building`:
```STEPS
building: hello_world
    display "Hello, World!"
    exit
```

### 2. Run Your Program

```bash
python -m STEPS.main run hello_world/
```

### 3. Or Use the Interactive REPL

```bash
python -m STEPS_repl.main
```

```
STEPS REPL v0.1 - Educational Programming Environment
Type 'help' for available commands, 'exit' to quit.

>>> set greeting to "Hello, STEPS!"
>>> display greeting
Hello, STEPS!
>>> vars
Variables:
  greeting = "Hello, STEPS!"
```

### 4. Launch the STEPS IDE

```bash
python -m STEPS_ide.main
```

The IDE provides a full development environment with:
- Project browser (Ctrl+Shift+P)
- Syntax-aware editor with code completion (Ctrl+Space or automatic)
- Scaffold from Building — auto-create floor folders and step files (Ctrl+Shift+G)
- Run (F5) and Check (F6) commands
- Terminal output panel (Ctrl+J)
- Project diagram viewer (Ctrl+D)
- Integrated debugger with breakpoints

---

## 📚 A Complete Example

Here's a more complete program with floors and STEPS:

```
price_calculator/
├── price_calculator.building
└── calculations/
    ├── calculate_subtotal.step
    └── apply_discount.step
```

**price_calculator.building:**
```STEPS
building: price_calculator
    note: Calculate the final price with discount

    floors:
        floor: calculations
            step: calculate_subtotal
            step: apply_discount

    display "Enter price: "
    set price to input as number

    display "Enter quantity: "
    set quantity to input as number

    call calculate_subtotal with price, quantity storing result in subtotal
    call apply_discount with subtotal, 10 storing result in final_price

    display "Final price: $" added to (final_price as text)
    exit
```

**calculations/calculate_subtotal.step:**
```STEPS
step: calculate_subtotal
    belongs to: calculations
    expects: price, quantity
    returns: total

    do:
        set total to price * quantity
        return total
```

**calculations/apply_discount.step:**
```STEPS
step: apply_discount
    belongs to: calculations
    expects: amount, percent
    returns: discounted

    declare:
        discount as number

    do:
        set discount to amount * (percent / 100)
        set discounted to amount - discount
        return discounted
```

---

## 🛠️ CLI Commands

| Command                               | Description                                                     |
| ------------------------------------- | --------------------------------------------------------------- |
| `python -m steps.main run <path>`     | Run a STEPS project                                             |
| `python -m steps.main check <path>`   | Validate syntax without running                                 |
| `python -m steps.main repl`           | Start the interactive REPL                                      |
| `python -m steps.main diagram <path>` | Generate ASCII flow diagram (also available in IDE with Ctrl+D) |
| `python -m steps_repl.main`           | Start REPL directly                                             |
| `python -m steps_ide.main`            | Launch the STEPS IDE                                            |

---

## ⚡ NucleusVM Execution Engine (Experimental)

STEPS can also run projects by compiling them to bytecode for
[NucleusVM](../NucleusVM), a shared VM built to give this and other
Python-hosted teaching languages a faster execution path than
tree-walking, instead of interpreting the AST directly. It's opt-in and
additive — the tree-walking interpreter remains the default and is
untouched by this.

> **Not installed by default, and no longer under active development.**
> NucleusVM did not deliver the speed-up it was built for when measured, so
> the experiment is parked. The code still works and is kept for reference,
> but it is an optional extra rather than a dependency: STEPS installs and
> runs without it, and nothing else in the language needs it.
>
> NucleusVM is not on PyPI. To try this path, install it from a local
> checkout of the sibling repo:
>
> ```bash
> pip install -e ../NucleusVM
> ```
>
> Without it, `--engine vm` reports what is missing and exits 1 rather than
> failing with an import error.

```bash
python -m steps.main run --engine vm my_project/
```

```python
from steps.main import run_project

run_project("my_project/", engine="vm")  # engine="tree" is the default
```

**Status**: a first vertical slice, not the full language yet. It covers
`repeat while` (the dominant loop — 99 of the sibling `PROJECT_EULER`
project's 100 STEPS Project Euler solutions use it), `if`/`otherwise`/
`otherwise if`, `exit`, `return`, `call` for steps/risers/the built-ins
real usage showed matter (`create_list`, `characters`, `slice`, `sqrt`,
`index_of`, `read_file`, `replace`, `list_sum`, `sqr`, `pow`, `log10`,
`log`), lists, `set`/indexed `set`, arithmetic/comparison/boolean
operators, `as number`/`as text`/`as boolean`, `length of`, `added to`,
`split by`/`character at`/`contains`/`is in`, `display`, and dynamic
scoping end to end. `attempt`/`unsuccessful`, tables, `repeat for each`,
`repeat <N> times`, and `fixed` type-locking aren't implemented yet (all
confirmed 0 or negligible real usage across the same 100 solutions) — an
unsupported construct raises a clear `NotImplementedError` at compile
time rather than running incorrectly. The iteration-limit safety guard
`repeat while` has under the tree-walker (`set iteration limit to`)
isn't enforced by this engine yet either.

**Verified**: every one of the 100 Project Euler solutions that completes
within a practical time budget under the tree-walker produces
byte-identical output under the VM engine too (0 divergences found).
**Measured faster**, not just architecturally different: ~3.1x on
call-heavy recursive code, ~46% on loop-heavy arithmetic/comparison code
(the shape most Project Euler solutions actually take) — achieved on the
first implementation pass, no separate optimization work needed, since
this slice's operators already compile to raw VM instructions rather than
native-function calls. See NucleusVM's `PROGRESS.md` for the full
investigation, including a real dynamic-scoping gap in NucleusVM's shared
core (STEPS is the first language to actually exercise it) that was
caught and fixed before this engine's compiler was even written.

---

## 🧩 Editor Support

[editors/vscode](editors/vscode) is a VS Code extension for `.building` and
`.step` files.

Highlighting is generated from the lexer's own tables — 27 multi-word keywords,
11 colon keywords, 50 plain keywords and the 56 native functions. The
multi-word operators are matched first, so `is greater than or equal to`,
`storing result in`, `added to` and `for each` highlight as single operators
instead of dissolving into their component words. `building:`, `floor:`,
`step:` and `riser:` names are scoped as definitions.

**Run works on projects, not files** — as the language intends. `steps run`
takes the directory holding the `.building` file, so the extension walks up
from whatever you have open until it finds one, and runs the whole project. It
works the same from the `.building` itself or from a `.step` three directories
down. Running a single step in isolation stays a terminal job
(`steps run-step`).

The indentation rules distinguish cases the syntax overloads: a `step:` at
column 0 defines a step and opens its body, while an indented `step:` inside a
`floors:` block is one entry in a list and opens nothing. `expects:`,
`belongs to:` and `returns:` are header lines, not blocks.

**Show Flow Diagram** (`Ctrl+D`, matching the IDE) renders `steps diagram` in a
panel beside the editor rather than a terminal that scrolls away. Diagnostics
land on the exact character with the error code attached, and a runtime error's
`Hint:` line is folded into the same message.

---

## 📖 Documentation

| Document                                       | Description                     |
| ---------------------------------------------- | ------------------------------- |
| [USER-GUIDE.md](USER-GUIDE.md)                 | Getting started guide for users |
| [LANGUAGE-REFERENCE.md](LANGUAGE-REFERENCE.md) | Complete language reference     |
| [dev-docs/](dev-docs/)                         | Developer documentation         |

### Developer Documentation (dev-docs/)

- `PROJECT_OVERVIEW.md` - High-level project orientation
- `LANGUAGE_SPEC.md` - Complete syntax and semantics
- `ARCHITECTURE.md` - Interpreter design
- `DEVELOPMENT_GUIDE.md` - Development workflow

---

## 🧪 Development

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/unit/test_lexer.py
```

### With Coverage

```bash
pytest --cov=STEPS --cov-report=html
```

### Type Checking

```bash
mypy src/STEPS src/STEPS_repl --ignore-missing-imports
```

### Project Structure

```
STEPS/
├── src/
│   ├── STEPS/           # Core interpreter
│   │   ├── lexer.py     # Tokenization
│   │   ├── parser.py    # AST construction
│   │   ├── interpreter.py  # Execution engine
│   │   ├── environment.py  # Scopes and registry
│   │   └── ...
│   ├── STEPS_repl/      # Interactive REPL
│   └── STEPS_ide/       # TUI-based IDE
├── tests/
│   ├── unit/            # Unit tests
│   └── integration/     # Integration tests
├── dev-docs/            # Developer documentation
└── README.md
```

---

## 🚢 Real-World Example Applications

STEPS includes example applications that demonstrate real-world capability beyond teaching exercises. The NMEA 0183 Marine Instruments app parses live serial data from marine electronics and displays navigation instruments including compass heading, GPS position, speed, and wind data.

![NMEA 0183 Marine Instruments — Built with STEPS](images/Step_Instruments_Screenshot.png)

---

## 🎯 Design Philosophy

1. **Visible Structure** - Program architecture is explicit, not hidden
2. **Mandatory Decomposition** - One step per file prevents monolithic code
3. **Conscious Engagement** - English-readable syntax requires understanding
4. **Clear Data Flow** - Explicit `expects`/`returns` declarations
5. **Educational Error Messages** - Errors teach, not frustrate
6. **Attractive Console Output** - Built-in TUI functions for boxes, banners, menus, and dynamic progress bars

---

## 📄 License

MIT License

---

## 🤝 Contributing

Contributions are welcome! Please see `dev-docs/DEVELOPMENT_GUIDE.md` for guidelines.
