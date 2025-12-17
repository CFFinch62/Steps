# Steps Lexer Specification

## Overview

The lexer (tokenizer) converts Steps source code into a stream of tokens. It handles:
- Significant whitespace (indentation tracking)
- Multi-word keywords
- String literals
- Numbers
- Identifiers
- Comments

## Token Types

```python
from enum import Enum, auto

class TokenType(Enum):
    # Structure
    BUILDING = auto()          # "building:"
    FLOOR = auto()             # "floor:"
    STEP = auto()              # "step:"
    RISER = auto()             # "riser:"
    BELONGS_TO = auto()        # "belongs to:"
    EXPECTS = auto()           # "expects:"
    RETURNS = auto()           # "returns:"
    DECLARE = auto()           # "declare:"
    DO = auto()                # "do:"
    EXIT = auto()              # "exit"
    
    # Variables
    AS = auto()                # "as"
    FIXED = auto()             # "fixed"
    SET = auto()               # "set"
    TO = auto()                # "to"
    
    # Invocation
    CALL = auto()              # "call"
    WITH = auto()              # "with"
    STORING_RESULT_IN = auto() # "storing result in"
    RETURN = auto()            # "return"
    DISPLAY = auto()           # "display"
    INPUT = auto()             # "input"
    
    # Control Flow
    IF = auto()                # "if"
    OTHERWISE_IF = auto()      # "otherwise if"
    OTHERWISE = auto()         # "otherwise"
    REPEAT = auto()            # "repeat"
    TIMES = auto()             # "times"
    FOR_EACH = auto()          # "for each"
    IN = auto()                # "in"
    WHILE = auto()             # "while"
    
    # Error Handling
    ATTEMPT = auto()           # "attempt:"
    IF_UNSUCCESSFUL = auto()   # "if unsuccessful:"
    THEN_CONTINUE = auto()     # "then continue:"
    
    # Comments
    NOTE = auto()              # "note:"
    NOTE_BLOCK = auto()        # "note block:"
    END_NOTE = auto()          # "end note"
    
    # Operators - Comparison
    IS_EQUAL_TO = auto()       # "is equal to"
    EQUALS = auto()            # "equals"
    IS_NOT_EQUAL_TO = auto()   # "is not equal to"
    IS_LESS_THAN = auto()      # "is less than"
    IS_GREATER_THAN = auto()   # "is greater than"
    IS_LESS_THAN_OR_EQUAL_TO = auto()     # "is less than or equal to"
    IS_GREATER_THAN_OR_EQUAL_TO = auto()  # "is greater than or equal to"
    
    # Operators - Boolean
    AND = auto()               # "and"
    OR = auto()                # "or"
    NOT = auto()               # "not"
    
    # Operators - Text
    ADDED_TO = auto()          # "added to"
    SPLIT_BY = auto()          # "split by"
    CHARACTER_AT = auto()      # "character at"
    LENGTH_OF = auto()         # "length of"
    CONTAINS = auto()          # "contains"
    STARTS_WITH = auto()       # "starts with"
    ENDS_WITH = auto()         # "ends with"
    
    # Operators - List
    ADD = auto()               # "add"
    REMOVE = auto()            # "remove"
    FROM = auto()              # "from"
    IS_IN = auto()             # "is in"
    
    # Operators - Math
    PLUS = auto()              # "+"
    MINUS = auto()             # "-"
    MULTIPLY = auto()          # "*"
    DIVIDE = auto()            # "/"
    
    # Punctuation
    COLON = auto()             # ":"
    COMMA = auto()             # ","
    LBRACKET = auto()          # "["
    RBRACKET = auto()          # "]"
    LPAREN = auto()            # "("
    RPAREN = auto()            # ")"
    
    # Literals
    NUMBER = auto()            # 42, 3.14
    TEXT = auto()              # "hello"
    TRUE = auto()              # "true"
    FALSE = auto()             # "false"
    NOTHING = auto()           # "nothing"
    
    # Types
    TYPE_NUMBER = auto()       # "number"
    TYPE_TEXT = auto()         # "text"
    TYPE_BOOLEAN = auto()      # "boolean"
    TYPE_LIST = auto()         # "list"
    TYPE_TABLE = auto()        # "table"
    
    # Other
    IDENTIFIER = auto()        # variable/step names
    NEWLINE = auto()           # end of line
    INDENT = auto()            # increase in indentation
    DEDENT = auto()            # decrease in indentation
    EOF = auto()               # end of file
```

## Token Structure

```python
@dataclass
class Token:
    type: TokenType
    value: str                 # Original text
    line: int                  # 1-indexed line number
    column: int                # 1-indexed column number
    file: Path                 # Source file
```

## Multi-Word Keywords

These keywords span multiple words and must be matched as units:

| Keyword | Token Type |
|---------|------------|
| `belongs to:` | BELONGS_TO |
| `storing result in` | STORING_RESULT_IN |
| `otherwise if` | OTHERWISE_IF |
| `for each` | FOR_EACH |
| `is equal to` | IS_EQUAL_TO |
| `is not equal to` | IS_NOT_EQUAL_TO |
| `is less than` | IS_LESS_THAN |
| `is greater than` | IS_GREATER_THAN |
| `is less than or equal to` | IS_LESS_THAN_OR_EQUAL_TO |
| `is greater than or equal to` | IS_GREATER_THAN_OR_EQUAL_TO |
| `added to` | ADDED_TO |
| `split by` | SPLIT_BY |
| `character at` | CHARACTER_AT |
| `length of` | LENGTH_OF |
| `starts with` | STARTS_WITH |
| `ends with` | ENDS_WITH |
| `is in` | IS_IN |
| `note block:` | NOTE_BLOCK |
| `end note` | END_NOTE |
| `if unsuccessful:` | IF_UNSUCCESSFUL |
| `then continue:` | THEN_CONTINUE |

**Implementation Note:** Match longest keyword first. "is greater than or equal to" must match before "is greater than".

## Indentation Handling

Steps uses significant whitespace like Python. The lexer tracks indentation levels and emits INDENT/DEDENT tokens.

**Rules:**
1. Use 4 spaces for indentation (tabs are errors)
2. Track a stack of indentation levels
3. At start of line, compare current indentation to stack top
4. Emit INDENT if deeper, DEDENT(s) if shallower
5. Multiple DEDENTs may be emitted for a single line

**Example:**

```
building: test     ← indent_stack = [0]
    display "hi"   ← INDENT emitted, indent_stack = [0, 4]
    if true        ← no change
        display 1  ← INDENT emitted, indent_stack = [0, 4, 8]
    display "bye"  ← DEDENT emitted, indent_stack = [0, 4]
exit               ← DEDENT emitted, indent_stack = [0]
```

**Pseudocode:**

```python
def handle_indentation(self) -> List[Token]:
    tokens = []
    spaces = 0
    while self.current_char == ' ':
        spaces += 1
        self.advance()
    
    if spaces % 4 != 0:
        raise LexerError("Indentation must be multiple of 4 spaces")
    
    current_level = self.indent_stack[-1]
    
    if spaces > current_level:
        if spaces != current_level + 4:
            raise LexerError("Indentation increased by more than one level")
        self.indent_stack.append(spaces)
        tokens.append(Token(TokenType.INDENT, "", self.line, 1, self.file))
    
    while spaces < self.indent_stack[-1]:
        self.indent_stack.pop()
        tokens.append(Token(TokenType.DEDENT, "", self.line, 1, self.file))
    
    if spaces != self.indent_stack[-1]:
        raise LexerError("Inconsistent indentation")
    
    return tokens
```

## String Literals

- Delimited by double quotes: `"hello"`
- Support escape sequences: `\"`, `\\`, `\n`, `\t`
- No single-quote strings
- Multiline strings not allowed (use note block for long text)

```python
def read_string(self) -> Token:
    start_line = self.line
    start_col = self.column
    self.advance()  # skip opening quote
    
    value = ""
    while self.current_char != '"':
        if self.current_char == '\n':
            raise LexerError("Unterminated string")
        if self.current_char == '\\':
            self.advance()
            value += self.escape_char(self.current_char)
        else:
            value += self.current_char
        self.advance()
    
    self.advance()  # skip closing quote
    return Token(TokenType.TEXT, value, start_line, start_col, self.file)
```

## Number Literals

- Integer: `42`, `0`, `-7`
- Decimal: `3.14`, `0.5`, `-2.718`
- No scientific notation in v1.0
- No hex/octal/binary literals in v1.0

```python
def read_number(self) -> Token:
    start_col = self.column
    value = ""
    
    if self.current_char == '-':
        value += '-'
        self.advance()
    
    while self.current_char.isdigit():
        value += self.current_char
        self.advance()
    
    if self.current_char == '.':
        value += '.'
        self.advance()
        while self.current_char.isdigit():
            value += self.current_char
            self.advance()
    
    return Token(TokenType.NUMBER, value, self.line, start_col, self.file)
```

## Identifiers

- Start with letter or underscore
- Contain letters, digits, underscores
- Case-sensitive
- Cannot be reserved words

```python
def read_identifier(self) -> Token:
    start_col = self.column
    value = ""
    
    while self.current_char.isalnum() or self.current_char == '_':
        value += self.current_char
        self.advance()
    
    # Check if it's a keyword
    token_type = self.keywords.get(value, TokenType.IDENTIFIER)
    return Token(token_type, value, self.line, start_col, self.file)
```

## Comments

Single-line comments consume to end of line:

```python
def read_note(self) -> Token:
    start_col = self.column
    self.advance_past("note:")
    self.skip_whitespace()
    
    value = ""
    while self.current_char != '\n' and self.current_char != EOF:
        value += self.current_char
        self.advance()
    
    return Token(TokenType.NOTE, value.strip(), self.line, start_col, self.file)
```

Block comments consume until "end note":

```python
def read_note_block(self) -> Token:
    start_line = self.line
    start_col = self.column
    self.advance_past("note block:")
    
    lines = []
    while not self.match("end note"):
        if self.current_char == EOF:
            raise LexerError("Unterminated note block")
        lines.append(self.read_line())
    
    self.advance_past("end note")
    return Token(TokenType.NOTE_BLOCK, '\n'.join(lines), start_line, start_col, self.file)
```

## Lexer Class Outline

```python
class Lexer:
    def __init__(self, source: str, file_path: Path):
        self.source = source
        self.file = file_path
        self.pos = 0
        self.line = 1
        self.column = 1
        self.indent_stack = [0]
        self.at_line_start = True
        
        # Build keyword lookup table
        self.keywords = self._build_keywords()
        self.multi_word_keywords = self._build_multi_word_keywords()
    
    @property
    def current_char(self) -> str:
        if self.pos >= len(self.source):
            return '\0'  # EOF sentinel
        return self.source[self.pos]
    
    def advance(self):
        if self.current_char == '\n':
            self.line += 1
            self.column = 1
            self.at_line_start = True
        else:
            self.column += 1
        self.pos += 1
    
    def peek(self, offset: int = 1) -> str:
        pos = self.pos + offset
        if pos >= len(self.source):
            return '\0'
        return self.source[pos]
    
    def match_ahead(self, text: str) -> bool:
        """Check if upcoming text matches (for multi-word keywords)."""
        return self.source[self.pos:].startswith(text)
    
    def tokenize(self) -> List[Token]:
        tokens = []
        
        while self.pos < len(self.source):
            if self.at_line_start:
                # Handle indentation at start of line
                indent_tokens = self.handle_indentation()
                tokens.extend(indent_tokens)
                self.at_line_start = False
            
            if self.current_char == '\0':
                break
            elif self.current_char == '\n':
                tokens.append(self.make_token(TokenType.NEWLINE))
                self.advance()
            elif self.current_char == ' ':
                self.skip_whitespace()
            elif self.current_char == '"':
                tokens.append(self.read_string())
            elif self.current_char.isdigit() or (self.current_char == '-' and self.peek().isdigit()):
                tokens.append(self.read_number())
            elif self.current_char.isalpha() or self.current_char == '_':
                tokens.append(self.read_identifier_or_keyword())
            elif self.current_char in '+-*/':
                tokens.append(self.read_operator())
            elif self.current_char in ':,[]()':
                tokens.append(self.read_punctuation())
            else:
                raise LexerError(f"Unexpected character: {self.current_char}")
        
        # Emit remaining DEDENTs
        while len(self.indent_stack) > 1:
            self.indent_stack.pop()
            tokens.append(Token(TokenType.DEDENT, "", self.line, 1, self.file))
        
        tokens.append(Token(TokenType.EOF, "", self.line, self.column, self.file))
        return tokens
    
    def read_identifier_or_keyword(self) -> Token:
        """Read identifier, checking for multi-word keywords first."""
        start_col = self.column
        
        # Check multi-word keywords (longest first)
        for keyword, token_type in self.multi_word_keywords:
            if self.match_ahead(keyword):
                self.pos += len(keyword)
                self.column += len(keyword)
                return Token(token_type, keyword, self.line, start_col, self.file)
        
        # Read single identifier
        value = ""
        while self.current_char.isalnum() or self.current_char == '_':
            value += self.current_char
            self.advance()
        
        # Check single-word keywords
        token_type = self.keywords.get(value, TokenType.IDENTIFIER)
        return Token(token_type, value, self.line, start_col, self.file)
```

## Error Messages

The lexer should produce helpful error messages:

| Error | Message |
|-------|---------|
| Invalid character | `Line 5, column 12: Unexpected character '@'. Steps doesn't use this symbol.` |
| Bad indentation | `Line 8: Indentation must use exactly 4 spaces per level. Found 3 spaces.` |
| Unterminated string | `Line 12: String starting here was never closed. Add a " at the end.` |
| Tab character | `Line 3: Found a tab character. Steps uses 4 spaces for indentation, not tabs.` |
| Inconsistent indent | `Line 15: This line's indentation doesn't match any previous level.` |
