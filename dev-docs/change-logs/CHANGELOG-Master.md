# Steps Language - Master Changelog

> **Educational Programming Language**
> Making Program Structure Visible and Mandatory

---

## Project Overview

Steps is an educational programming language designed for teaching programming concepts through its unique **building/floor/step/riser** architectural metaphor. The language enforces decomposition through a "one step per file" structure and uses English-readable syntax to promote conscious engagement over rote memorization.

### Target Version: 1.0

**Key Features:**
- Python-based interpreter
- CLI for running and checking programs
- Interactive REPL for learning language fundamentals
- Steps IDE (TUI-based, evolved from Only Code editor)
- Visual flow diagram generation
- Educational error messages

---

## Development Phases

| Phase | Description | Status |
|-------|-------------|--------|
| **Phase 1** | Foundation & Setup | ✅ Completed |
| **Phase 2** | Lexer Implementation | ✅ Completed |
| **Phase 3** | Parser & AST | ✅ Completed |
| **Phase 4** | Interpreter & Runtime | ✅ Completed |
| **Phase 5** | CLI & REPL | ✅ Completed |
| **Phase 6** | Steps IDE (from Only Code) | ✅ Completed |
| **Phase 7** | Packaging & Documentation | 🔲 Not Started |

**Legend:**
- 🔲 Not Started
- 🔄 In Progress
- ✅ Completed
- ⏸️ Paused/Blocked

---

## Version History

### Pre-Release Development

#### Planning Phase
- **Date:** 2025-12-07
- **Summary:** Initial project documentation review and implementation planning
- **Artifacts:**
  - Reviewed 12 specification documents in `/dev-docs`
  - Created 6-phase implementation plan
  - Established CHANGELOG structure

#### Phase 4 Completion
- **Date:** 2025-12-08
- **Summary:** Completed interpreter and runtime implementation
- **Details:** See CHANGELOG-Phase4.md

#### Architecture Update
- **Date:** 2025-12-08
- **Summary:** Added REPL and IDE specifications
- **Changes:**
  - REPL is a **standalone teaching tool** (simple, single-scope, no steps/floors)
  - IDE is evolved from **Only Code** TUI editor (full project support)
  - Added Only_Code source to project for IDE development reference
  - Updated phases to separate REPL (Phase 5), IDE (Phase 6), and Documentation (Phase 7)

#### Phase 5 Completion
- **Date:** 2025-12-09
- **Summary:** Completed CLI and REPL implementation
- **Details:** See [CHANGELOG-Phase5.md](CHANGELOG-Phase5.md)
- **Highlights:**
  - CLI with run, check, repl, and diagram commands
  - Standalone REPL for learning Steps fundamentals
  - 15 new integration tests (364 total tests)
  - All mypy type checks pass (17 source files)

#### Phase 6 Completion
- **Date:** 2025-12-09
- **Summary:** Completed Steps IDE implementation
- **Details:** See [CHANGELOG-Phase6.md](CHANGELOG-Phase6.md)
- **Highlights:**
  - Full TUI-based IDE evolved from Only Code editor
  - Project browser with building/floor/step tree structure
  - Steps-aware editor with validation
  - F5 (Run) and F6 (Check) integration
  - Project operation dialogs (New Project/Floor/Step)
  - Command palette integration for all Steps operations

---

## Phase Changelog Index

Upon completion of each development phase, a detailed changelog will be created:

| Phase | Changelog File | Status |
|-------|----------------|--------|
| Phase 1 | [CHANGELOG-Phase1.md](CHANGELOG-Phase1.md) | ✅ Completed |
| Phase 2 | [CHANGELOG-Phase2.md](CHANGELOG-Phase2.md) | ✅ Completed |
| Phase 3 | [CHANGELOG-Phase3.md](CHANGELOG-Phase3.md) | ✅ Completed |
| Phase 4 | [CHANGELOG-Phase4.md](CHANGELOG-Phase4.md) | ✅ Completed |
| Phase 5 | [CHANGELOG-Phase5.md](CHANGELOG-Phase5.md) | ✅ Completed |
| Phase 6 | [CHANGELOG-Phase6.md](CHANGELOG-Phase6.md) | ✅ Completed |
| Phase 7 | `CHANGELOG-Phase7.md` | 🔲 Pending |

---

## Architecture Summary

### Interpreter Pipeline

```
Source Files → Loader → Lexer → Tokens → Parser → AST → Interpreter → Output
                                                          ↓
                                                     Environment
```

### Project Structure (Interpreter)

```
steps/
├── src/steps/
│   ├── __init__.py        # Package init, version
│   ├── main.py            # CLI entry point
│   ├── repl.py            # Interactive REPL
│   ├── lexer.py           # Tokenization
│   ├── parser.py          # AST construction
│   ├── ast_nodes.py       # AST node definitions
│   ├── interpreter.py     # Execution engine
│   ├── environment.py     # Scopes and registry
│   ├── types.py           # Type system
│   ├── builtins.py        # Built-in operations
│   ├── loader.py          # Project discovery
│   ├── errors.py          # Error definitions
│   └── diagram.py         # Flow diagram generator
├── tests/                  # Test suite
├── examples/               # Example programs
├── docs/                   # User documentation
├── pyproject.toml          # Project configuration
└── README.md               # Project readme
```

### User Project Structure (Steps Programs)

```
my_program/                  # Building folder
├── my_program.building      # Entry point
├── floor_one/               # Floor folder
│   ├── floor_one.floor      # Floor definition
│   ├── step_a.step
│   └── step_b.step
└── floor_two/
    ├── floor_two.floor
    └── step_c.step
```

---

## Key Documentation References

| Document | Location | Purpose |
|----------|----------|---------|
| Project Overview | `dev-docs/PROJECT_OVERVIEW.md` | High-level orientation |
| Language Spec | `dev-docs/LANGUAGE_SPEC.md` | Syntax and semantics |
| Architecture | `dev-docs/ARCHITECTURE.md` | Interpreter design |
| AST Spec | `dev-docs/AST_SPECIFICATION.md` | Node definitions |
| Lexer Spec | `dev-docs/LEXER_SPEC.md` | Token types |
| Parser Spec | `dev-docs/PARSER_SPEC.md` | Grammar rules |
| Error Messages | `dev-docs/ERROR_MESSAGES.md` | Error catalog |
| Development Guide | `dev-docs/DEVELOPMENT_GUIDE.md` | Workflow guide |
| Testing Strategy | `dev-docs/TESTING_STRATEGY.md` | Test approach |
| **REPL Spec** | `dev-docs/REPL_SPEC.md` | REPL capabilities and limits |
| **REPL Implementation** | `dev-docs/REPL_IMPLEMENTATION.md` | REPL implementation guide |
| **IDE Spec** | `dev-docs/IDE_SPEC.md` | IDE features and design |
| **IDE Implementation** | `dev-docs/IDE_IMPLEMENTATION.md` | IDE transformation from Only Code |

---

## External Resources

| Resource | Location | Purpose |
|----------|----------|---------|
| Only Code Source | `Only_Code/` | Base TUI editor for Steps IDE |

---

## Success Metrics

- [x] All 11 interpreter modules implemented
- [x] Complete token type coverage (~65 types)
- [x] All statement types parseable
- [x] All expression types evaluable
- [x] Educational error messages for all error codes
- [ ] Example programs execute correctly
- [ ] 90%+ test coverage
- [ ] Cross-platform compatibility (Linux, macOS, Windows)
- [x] Python 3.10+ support

---

## Next Steps

1. **Begin Phase 6:** Steps IDE (from Only Code)
   - Transform Only Code into Steps IDE (per IDE_IMPLEMENTATION.md)
   - Replace FileBrowser with ProjectBrowser
   - Add Steps-aware editor
   - Integrate interpreter for run/check commands

2. **Phase 7:** Packaging & Documentation
   - Create pip-installable package
   - Write user documentation
   - Create tutorial examples
   - Integrate interpreter for validation and execution

3. **Phase 7:** Packaging & Documentation

---

*Last Updated: 2025-12-08*
