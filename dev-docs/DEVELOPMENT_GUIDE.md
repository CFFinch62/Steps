# Steps Development Guide

## Getting Started

### Prerequisites

- Python 3.10+
- pip or uv for package management
- Git

### Project Setup

```bash
# Clone repository
git clone <repository-url>
cd steps

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Run the interpreter
steps run examples/hello_world/
```

### Project Structure

```
steps/
├── src/
│   └── steps/
│       ├── __init__.py        # Package init, version
│       ├── main.py            # CLI entry point
│       ├── repl.py            # Interactive REPL
│       ├── lexer.py           # Tokenization
│       ├── parser.py          # AST construction
│       ├── ast_nodes.py       # AST node definitions
│       ├── interpreter.py     # Execution engine
│       ├── environment.py     # Scopes and registry
│       ├── types.py           # Type system
│       ├── builtins.py        # Built-in operations
│       ├── loader.py          # Project discovery
│       ├── errors.py          # Error definitions
│       └── diagram.py         # Flow diagrams
├── tests/
│   ├── conftest.py            # Pytest fixtures
│   ├── test_lexer.py
│   ├── test_parser.py
│   ├── test_interpreter.py
│   ├── test_integration.py
│   └── examples/              # Test programs
├── examples/                   # Example projects
├── docs/                       # Documentation
├── pyproject.toml
└── README.md
```

## Development Workflow

### Making Changes

1. **Create a branch** for your feature/fix
2. **Write tests first** when possible
3. **Implement the change**
4. **Run the test suite**: `pytest`
5. **Run type checking**: `mypy src/`
6. **Format code**: `black src/ tests/`
7. **Submit PR** with clear description

### Running Tests

```bash
# All tests
pytest

# Specific file
pytest tests/test_lexer.py

# Specific test
pytest tests/test_lexer.py::test_tokenize_string

# With coverage
pytest --cov=steps --cov-report=html

# Verbose output
pytest -v

# Stop on first failure
pytest -x
```

### Code Style

- **Formatter**: Black (line length 100)
- **Type hints**: Required on all public functions
- **Docstrings**: Google style
- **Imports**: isort for organization

```python
# Good
def parse_expression(self, tokens: List[Token]) -> ExpressionNode:
    """Parse an expression from the token stream.
    
    Args:
        tokens: List of tokens to parse
        
    Returns:
        The parsed expression AST node
        
    Raises:
        ParseError: If the tokens don't form a valid expression
    """
    ...

# Bad
def parse_expression(self, tokens):
    ...
```

## Component Development

### Adding a New Token Type

1. Add to `TokenType` enum in `lexer.py`:
```python
class TokenType(Enum):
    # ... existing tokens ...
    NEW_KEYWORD = auto()
```

2. Add to keyword lookup table:
```python
# For single-word keywords
self.keywords["newkeyword"] = TokenType.NEW_KEYWORD

# For multi-word keywords (add in order of length, longest first)
self.multi_word_keywords.insert(0, ("new keyword", TokenType.NEW_KEYWORD))
```

3. Add tests in `test_lexer.py`:
```python
def test_tokenize_new_keyword():
    lexer = Lexer("new keyword", Path("test.step"))
    tokens = lexer.tokenize()
    assert tokens[0].type == TokenType.NEW_KEYWORD
```

### Adding a New AST Node

1. Define the node in `ast_nodes.py`:
```python
@dataclass
class NewStatementNode(ASTNode):
    """Represents a new statement type."""
    target: str
    value: ExpressionNode
```

2. Add visitor method stub to base visitor:
```python
class ASTVisitor:
    def visit_NewStatementNode(self, node: NewStatementNode) -> Any:
        raise NotImplementedError
```

3. Implement in interpreter:
```python
class Interpreter(ASTVisitor):
    def visit_NewStatementNode(self, node: NewStatementNode) -> Any:
        value = self.visit(node.value)
        self.environment.set(node.target, value)
```

4. Add parser support in `parser.py`:
```python
def parse_new_statement(self) -> NewStatementNode:
    location = self.current_location()
    self.expect(TokenType.NEW_KEYWORD, "Expected 'new keyword'")
    # ... parse the rest ...
    return NewStatementNode(location=location, target=target, value=value)
```

### Adding a New Built-in Operation

1. Implement in `builtins.py`:
```python
def builtin_new_operation(args: List[StepsValue]) -> StepsValue:
    """Description of what this operation does."""
    if len(args) != 1:
        raise StepsRuntimeError("new_operation expects 1 argument")
    
    value = args[0]
    # ... implementation ...
    return result
```

2. Register in the builtins table:
```python
BUILTINS = {
    # ... existing builtins ...
    "new_operation": builtin_new_operation,
}
```

3. Add tests:
```python
def test_new_operation():
    result = builtin_new_operation([StepsNumber(42)])
    assert result == expected_value
```

### Adding a New Error Message

1. Define error code in `errors.py`:
```python
class ErrorCode:
    # ... existing codes ...
    E408 = "E408"  # New error type
```

2. Add error template:
```python
ERROR_TEMPLATES = {
    # ... existing templates ...
    ErrorCode.E408: ErrorTemplate(
        code=ErrorCode.E408,
        message="Description of what went wrong with {variable}",
        hint="Suggestion for how to fix it",
    ),
}
```

3. Add to ERROR_MESSAGES.md documentation

4. Create helper function if needed:
```python
def new_error(variable: str, location: SourceLocation) -> StepsError:
    return StepsError(
        code=ErrorCode.E408,
        message=ERROR_TEMPLATES[ErrorCode.E408].message.format(variable=variable),
        hint=ERROR_TEMPLATES[ErrorCode.E408].hint,
        file=location.file,
        line=location.line,
        column=location.column,
    )
```

## Testing Strategies

### Unit Tests

Test individual functions in isolation:

```python
# test_lexer.py
def test_tokenize_number():
    lexer = Lexer("42", Path("test.step"))
    tokens = lexer.tokenize()
    assert len(tokens) == 2  # NUMBER, EOF
    assert tokens[0].type == TokenType.NUMBER
    assert tokens[0].value == "42"

def test_tokenize_negative_number():
    lexer = Lexer("-3.14", Path("test.step"))
    tokens = lexer.tokenize()
    assert tokens[0].type == TokenType.NUMBER
    assert tokens[0].value == "-3.14"
```

### Integration Tests

Test components working together:

```python
# test_integration.py
def test_simple_program(tmp_path):
    # Create a minimal project
    project = tmp_path / "test_project"
    project.mkdir()
    
    (project / "test_project.building").write_text("""
building: test_project

    display "Hello"
    exit
""")
    
    # Run and capture output
    result = run_steps_project(project)
    assert result.output == "Hello\n"
    assert result.exit_code == 0
```

### Example-Based Tests

Use example projects as test cases:

```python
# test_examples.py
import pytest
from pathlib import Path

EXAMPLES_DIR = Path(__file__).parent / "examples"

@pytest.mark.parametrize("example", [
    "hello_world",
    "price_calculator",
    "guessing_game",
])
def test_example_runs(example):
    project_path = EXAMPLES_DIR / example
    result = run_steps_project(project_path)
    assert result.exit_code == 0
```

### Error Tests

Verify error messages are helpful:

```python
def test_undefined_variable_error():
    source = """
step: test
    belongs to: main
    expects: nothing
    returns: nothing
    
    do:
        display undefined_var
"""
    with pytest.raises(StepsRuntimeError) as exc_info:
        run_step(source)
    
    error = exc_info.value
    assert "undefined_var" in error.message
    assert "has not been defined" in error.message
    assert error.line == 8
```

## Debugging Tips

### Verbose Lexer Output

```python
# Add to lexer for debugging
def tokenize_debug(self) -> List[Token]:
    tokens = self.tokenize()
    for token in tokens:
        print(f"{token.type.name:20} | {repr(token.value):20} | L{token.line}:C{token.column}")
    return tokens
```

### AST Pretty Printing

```python
# Add to ast_nodes.py
def pretty_print(node: ASTNode, indent: int = 0) -> str:
    prefix = "  " * indent
    lines = [f"{prefix}{type(node).__name__}"]
    
    for field_name, field_value in node.__dict__.items():
        if field_name == "location":
            continue
        if isinstance(field_value, ASTNode):
            lines.append(f"{prefix}  {field_name}:")
            lines.append(pretty_print(field_value, indent + 2))
        elif isinstance(field_value, list):
            lines.append(f"{prefix}  {field_name}: [")
            for item in field_value:
                if isinstance(item, ASTNode):
                    lines.append(pretty_print(item, indent + 2))
                else:
                    lines.append(f"{prefix}    {repr(item)}")
            lines.append(f"{prefix}  ]")
        else:
            lines.append(f"{prefix}  {field_name}: {repr(field_value)}")
    
    return "\n".join(lines)
```

### Interpreter Tracing

```python
# Add to interpreter for debugging
class Interpreter:
    def __init__(self, ..., trace: bool = False):
        self.trace = trace
    
    def visit(self, node: ASTNode) -> Any:
        if self.trace:
            print(f"VISIT: {type(node).__name__} at L{node.location.line}")
        result = super().visit(node)
        if self.trace:
            print(f"  -> {repr(result)}")
        return result
```

## Performance Considerations

For v1.0, correctness and clarity are more important than performance. However:

1. **Don't pre-optimize** - Get it working first
2. **Profile before optimizing** - Use cProfile to find real bottlenecks
3. **Cache parsed ASTs** - Don't re-parse unchanged files
4. **Use generators** - For large token streams, consider yielding tokens

## Common Pitfalls

### Indentation Edge Cases

- Empty lines should not affect indentation tracking
- Comments should not affect indentation
- Files must end with a newline

### Multi-word Keyword Matching

- Always check longest matches first
- "is greater than or equal to" must match before "is greater than"
- Watch for partial matches: "install" should not match "in"

### Source Location Tracking

- Every AST node must have accurate source location
- Track both start and end positions for good error highlighting
- Column numbers are 1-indexed (not 0-indexed)

### Type Conversion

- "42" as number should work
- "hello" as number should raise a clear error
- Empty string "" as number should fail gracefully

## Release Checklist

Before releasing a new version:

- [ ] All tests pass
- [ ] Type checking passes (mypy)
- [ ] Code is formatted (black)
- [ ] Documentation is updated
- [ ] CHANGELOG is updated
- [ ] Version number is bumped
- [ ] Example programs work correctly
- [ ] Error messages are reviewed for clarity
