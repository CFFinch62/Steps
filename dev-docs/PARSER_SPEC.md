# Steps Parser Specification

## Overview

The parser transforms a token stream into an Abstract Syntax Tree. It uses recursive descent parsing with the grammar defined below.

## Grammar Notation

- `CAPS` = Token types
- `lowercase` = Grammar rules
- `|` = Alternative
- `?` = Optional (0 or 1)
- `*` = Zero or more
- `+` = One or more
- `( )` = Grouping

## Complete Grammar

### Top-Level

```
building_file   → BUILDING IDENTIFIER NEWLINE INDENT building_body DEDENT EOF
building_body   → statement*

floor_file      → FLOOR IDENTIFIER NEWLINE INDENT floor_body DEDENT EOF
floor_body      → floor_step_decl*
floor_step_decl → STEP IDENTIFIER NEWLINE

step_file       → step_def EOF
step_def        → STEP IDENTIFIER NEWLINE INDENT step_header riser* declare_section? do_section DEDENT
```

### Step Structure

```
step_header     → belongs_clause expects_clause? returns_clause?
belongs_clause  → BELONGS_TO IDENTIFIER NEWLINE
expects_clause  → EXPECTS param_list NEWLINE
returns_clause  → RETURNS return_decl NEWLINE

param_list      → NOTHING | param (COMMA param)*
param           → IDENTIFIER (AS type_name)?
return_decl     → NOTHING | IDENTIFIER (AS type_name)?

riser           → RISER IDENTIFIER NEWLINE INDENT riser_header do_section DEDENT
riser_header    → expects_clause? returns_clause?
```

### Declarations

```
declare_section → DECLARE NEWLINE INDENT declaration+ DEDENT
declaration     → IDENTIFIER AS type_name FIXED? NEWLINE
type_name       → TYPE_NUMBER | TYPE_TEXT | TYPE_BOOLEAN | TYPE_LIST | TYPE_TABLE
```

### Statements

```
do_section      → DO NEWLINE INDENT statement+ DEDENT

statement       → display_stmt
                | set_stmt
                | call_stmt
                | return_stmt
                | exit_stmt
                | if_stmt
                | repeat_stmt
                | attempt_stmt
                | add_stmt
                | remove_stmt
                | note_stmt
                | NEWLINE

display_stmt    → DISPLAY expression NEWLINE
set_stmt        → SET IDENTIFIER TO expression NEWLINE
call_stmt       → CALL IDENTIFIER (WITH arg_list)? (STORING_RESULT_IN IDENTIFIER)? NEWLINE
return_stmt     → RETURN expression? NEWLINE
exit_stmt       → EXIT NEWLINE

if_stmt         → IF expression NEWLINE INDENT statement+ DEDENT
                  otherwise_if_clause*
                  otherwise_clause?
otherwise_if_clause → OTHERWISE_IF expression NEWLINE INDENT statement+ DEDENT
otherwise_clause    → OTHERWISE NEWLINE INDENT statement+ DEDENT

repeat_stmt     → repeat_times | repeat_for_each | repeat_while
repeat_times    → REPEAT expression TIMES NEWLINE INDENT statement+ DEDENT
repeat_for_each → REPEAT FOR_EACH IDENTIFIER IN expression NEWLINE INDENT statement+ DEDENT
repeat_while    → REPEAT WHILE expression NEWLINE INDENT statement+ DEDENT

attempt_stmt    → ATTEMPT NEWLINE INDENT statement+ DEDENT
                  unsuccessful_clause?
                  continue_clause?
unsuccessful_clause → IF_UNSUCCESSFUL NEWLINE INDENT statement+ DEDENT
continue_clause     → THEN_CONTINUE NEWLINE INDENT statement+ DEDENT

add_stmt        → ADD expression TO IDENTIFIER NEWLINE
remove_stmt     → REMOVE expression FROM IDENTIFIER NEWLINE

note_stmt       → NOTE | NOTE_BLOCK
```

### Expressions

```
expression      → or_expr

or_expr         → and_expr (OR and_expr)*
and_expr        → not_expr (AND not_expr)*
not_expr        → NOT not_expr | comparison

comparison      → addition comparison_op addition
                | addition
comparison_op   → IS_EQUAL_TO | EQUALS | IS_NOT_EQUAL_TO
                | IS_LESS_THAN | IS_GREATER_THAN
                | IS_LESS_THAN_OR_EQUAL_TO | IS_GREATER_THAN_OR_EQUAL_TO
                | CONTAINS | STARTS_WITH | ENDS_WITH | IS_IN

addition        → multiplication ((PLUS | MINUS | ADDED_TO) multiplication)*
multiplication  → unary ((MULTIPLY | DIVIDE) unary)*

unary           → MINUS unary | postfix
postfix         → primary (LBRACKET expression RBRACKET)*
                | primary AS type_name                    # Type conversion
                | LENGTH_OF primary
                | CHARACTER_AT expression OF primary
                | primary SPLIT_BY expression

primary         → NUMBER
                | TEXT
                | TRUE | FALSE
                | NOTHING
                | IDENTIFIER
                | INPUT
                | list_literal
                | table_literal
                | LPAREN expression RPAREN

list_literal    → LBRACKET (expression (COMMA expression)*)? RBRACKET
table_literal   → LBRACKET (table_pair (COMMA table_pair)*)? RBRACKET
table_pair      → expression COLON expression

arg_list        → expression (COMMA expression)*
```

## Parser Implementation

### Class Structure

```python
class Parser:
    def __init__(self, tokens: List[Token], file_type: str):
        self.tokens = tokens
        self.file_type = file_type  # "building", "floor", or "step"
        self.pos = 0
        self.errors = []
    
    @property
    def current(self) -> Token:
        if self.pos >= len(self.tokens):
            return self.tokens[-1]  # EOF
        return self.tokens[self.pos]
    
    def peek(self, offset: int = 1) -> Token:
        pos = self.pos + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[pos]
    
    def advance(self) -> Token:
        token = self.current
        self.pos += 1
        return token
    
    def match(self, *types: TokenType) -> bool:
        return self.current.type in types
    
    def expect(self, token_type: TokenType, message: str) -> Token:
        if self.current.type != token_type:
            self.error(message)
        return self.advance()
    
    def error(self, message: str):
        self.errors.append(ParseError(
            message=message,
            file=self.current.file,
            line=self.current.line,
            column=self.current.column
        ))
        # Attempt recovery by advancing
        self.advance()
```

### Parsing Entry Points

```python
def parse(self) -> ASTNode:
    if self.file_type == "building":
        return self.parse_building()
    elif self.file_type == "floor":
        return self.parse_floor()
    elif self.file_type == "step":
        return self.parse_step()

def parse_building(self) -> BuildingNode:
    location = self.current_location()
    
    self.expect(TokenType.BUILDING, "Expected 'building:'")
    name = self.expect(TokenType.IDENTIFIER, "Expected building name").value
    self.expect(TokenType.NEWLINE, "Expected newline after building name")
    self.expect(TokenType.INDENT, "Expected indented body")
    
    body = []
    while not self.match(TokenType.DEDENT, TokenType.EOF):
        body.append(self.parse_statement())
    
    self.expect(TokenType.DEDENT, "Expected end of building body")
    self.expect(TokenType.EOF, "Expected end of file")
    
    return BuildingNode(location=location, name=name, body=body)

def parse_floor(self) -> FloorNode:
    location = self.current_location()
    
    self.expect(TokenType.FLOOR, "Expected 'floor:'")
    name = self.expect(TokenType.IDENTIFIER, "Expected floor name").value
    self.expect(TokenType.NEWLINE, "Expected newline after floor name")
    self.expect(TokenType.INDENT, "Expected indented body")
    
    steps = []
    while not self.match(TokenType.DEDENT, TokenType.EOF):
        self.expect(TokenType.STEP, "Expected 'step:'")
        step_name = self.expect(TokenType.IDENTIFIER, "Expected step name").value
        steps.append(step_name)
        self.expect(TokenType.NEWLINE, "Expected newline")
    
    self.expect(TokenType.DEDENT, "Expected end of floor body")
    
    return FloorNode(location=location, name=name, steps=steps)

def parse_step(self) -> StepNode:
    location = self.current_location()
    
    self.expect(TokenType.STEP, "Expected 'step:'")
    name = self.expect(TokenType.IDENTIFIER, "Expected step name").value
    self.expect(TokenType.NEWLINE, "Expected newline")
    self.expect(TokenType.INDENT, "Expected indented body")
    
    # Parse header
    belongs_to = self.parse_belongs_to()
    expects = self.parse_expects() if self.match(TokenType.EXPECTS) else []
    returns = self.parse_returns() if self.match(TokenType.RETURNS) else None
    
    # Parse risers
    risers = []
    while self.match(TokenType.RISER):
        risers.append(self.parse_riser())
    
    # Parse declarations
    declarations = []
    if self.match(TokenType.DECLARE):
        declarations = self.parse_declare_section()
    
    # Parse body
    body = self.parse_do_section()
    
    self.expect(TokenType.DEDENT, "Expected end of step body")
    
    return StepNode(
        location=location,
        name=name,
        belongs_to=belongs_to,
        expects=expects,
        returns=returns,
        risers=risers,
        declarations=declarations,
        body=body
    )
```

### Statement Parsing

```python
def parse_statement(self) -> StatementNode:
    if self.match(TokenType.DISPLAY):
        return self.parse_display()
    elif self.match(TokenType.SET):
        return self.parse_set()
    elif self.match(TokenType.CALL):
        return self.parse_call()
    elif self.match(TokenType.RETURN):
        return self.parse_return()
    elif self.match(TokenType.EXIT):
        return self.parse_exit()
    elif self.match(TokenType.IF):
        return self.parse_if()
    elif self.match(TokenType.REPEAT):
        return self.parse_repeat()
    elif self.match(TokenType.ATTEMPT):
        return self.parse_attempt()
    elif self.match(TokenType.ADD):
        return self.parse_add()
    elif self.match(TokenType.REMOVE):
        return self.parse_remove()
    elif self.match(TokenType.NOTE, TokenType.NOTE_BLOCK):
        return self.parse_note()
    elif self.match(TokenType.NEWLINE):
        self.advance()  # Skip blank lines
        return None
    else:
        self.error(f"Unexpected token: {self.current.value}")
        return None

def parse_display(self) -> DisplayStatement:
    location = self.current_location()
    self.advance()  # consume DISPLAY
    expr = self.parse_expression()
    self.expect(TokenType.NEWLINE, "Expected newline after display")
    return DisplayStatement(location=location, expression=expr)

def parse_set(self) -> SetStatement:
    location = self.current_location()
    self.advance()  # consume SET
    target = self.expect(TokenType.IDENTIFIER, "Expected variable name").value
    self.expect(TokenType.TO, "Expected 'to' after variable name")
    value = self.parse_expression()
    self.expect(TokenType.NEWLINE, "Expected newline after set statement")
    return SetStatement(location=location, target=target, value=value)

def parse_call(self) -> CallStatement:
    location = self.current_location()
    self.advance()  # consume CALL
    step_name = self.expect(TokenType.IDENTIFIER, "Expected step name").value
    
    arguments = []
    if self.match(TokenType.WITH):
        self.advance()
        arguments = self.parse_arg_list()
    
    result_target = None
    if self.match(TokenType.STORING_RESULT_IN):
        self.advance()
        result_target = self.expect(TokenType.IDENTIFIER, "Expected variable name").value
    
    self.expect(TokenType.NEWLINE, "Expected newline after call")
    
    return CallStatement(
        location=location,
        step_name=step_name,
        arguments=arguments,
        result_target=result_target
    )

def parse_if(self) -> IfStatement:
    location = self.current_location()
    self.advance()  # consume IF
    
    condition = self.parse_expression()
    self.expect(TokenType.NEWLINE, "Expected newline after condition")
    self.expect(TokenType.INDENT, "Expected indented body")
    
    body = []
    while not self.match(TokenType.DEDENT):
        stmt = self.parse_statement()
        if stmt:
            body.append(stmt)
    self.advance()  # consume DEDENT
    
    if_branch = IfBranch(location=location, condition=condition, body=body)
    
    otherwise_if_branches = []
    while self.match(TokenType.OTHERWISE_IF):
        otherwise_if_branches.append(self.parse_otherwise_if())
    
    otherwise_branch = None
    if self.match(TokenType.OTHERWISE):
        otherwise_branch = self.parse_otherwise()
    
    return IfStatement(
        location=location,
        if_branch=if_branch,
        otherwise_if_branches=otherwise_if_branches,
        otherwise_branch=otherwise_branch
    )
```

### Expression Parsing

Using precedence climbing / Pratt parsing approach:

```python
def parse_expression(self) -> ExpressionNode:
    return self.parse_or_expr()

def parse_or_expr(self) -> ExpressionNode:
    left = self.parse_and_expr()
    
    while self.match(TokenType.OR):
        location = self.current_location()
        self.advance()
        right = self.parse_and_expr()
        left = BinaryOpNode(location=location, left=left, operator="or", right=right)
    
    return left

def parse_and_expr(self) -> ExpressionNode:
    left = self.parse_not_expr()
    
    while self.match(TokenType.AND):
        location = self.current_location()
        self.advance()
        right = self.parse_not_expr()
        left = BinaryOpNode(location=location, left=left, operator="and", right=right)
    
    return left

def parse_not_expr(self) -> ExpressionNode:
    if self.match(TokenType.NOT):
        location = self.current_location()
        self.advance()
        operand = self.parse_not_expr()
        return UnaryOpNode(location=location, operator="not", operand=operand)
    return self.parse_comparison()

def parse_comparison(self) -> ExpressionNode:
    left = self.parse_addition()
    
    comparison_ops = [
        TokenType.IS_EQUAL_TO, TokenType.EQUALS, TokenType.IS_NOT_EQUAL_TO,
        TokenType.IS_LESS_THAN, TokenType.IS_GREATER_THAN,
        TokenType.IS_LESS_THAN_OR_EQUAL_TO, TokenType.IS_GREATER_THAN_OR_EQUAL_TO,
        TokenType.CONTAINS, TokenType.STARTS_WITH, TokenType.ENDS_WITH, TokenType.IS_IN
    ]
    
    if self.match(*comparison_ops):
        location = self.current_location()
        op = self.advance().value
        right = self.parse_addition()
        return BinaryOpNode(location=location, left=left, operator=op, right=right)
    
    return left

def parse_addition(self) -> ExpressionNode:
    left = self.parse_multiplication()
    
    while self.match(TokenType.PLUS, TokenType.MINUS, TokenType.ADDED_TO):
        location = self.current_location()
        op = self.advance()
        right = self.parse_multiplication()
        
        if op.type == TokenType.ADDED_TO:
            left = AddedToNode(location=location, left=left, right=right)
        else:
            left = BinaryOpNode(location=location, left=left, operator=op.value, right=right)
    
    return left

def parse_multiplication(self) -> ExpressionNode:
    left = self.parse_unary()
    
    while self.match(TokenType.MULTIPLY, TokenType.DIVIDE):
        location = self.current_location()
        op = self.advance().value
        right = self.parse_unary()
        left = BinaryOpNode(location=location, left=left, operator=op, right=right)
    
    return left

def parse_unary(self) -> ExpressionNode:
    if self.match(TokenType.MINUS):
        location = self.current_location()
        self.advance()
        operand = self.parse_unary()
        return UnaryOpNode(location=location, operator="-", operand=operand)
    
    return self.parse_postfix()

def parse_postfix(self) -> ExpressionNode:
    expr = self.parse_primary()
    
    while True:
        if self.match(TokenType.LBRACKET):
            # Table/list access
            location = self.current_location()
            self.advance()
            key = self.parse_expression()
            self.expect(TokenType.RBRACKET, "Expected ']'")
            expr = TableAccessNode(location=location, table=expr, key=key)
        elif self.match(TokenType.AS):
            # Type conversion
            location = self.current_location()
            self.advance()
            target_type = self.expect_type_name()
            expr = TypeConversionNode(location=location, expression=expr, target_type=target_type)
        else:
            break
    
    return expr

def parse_primary(self) -> ExpressionNode:
    location = self.current_location()
    
    if self.match(TokenType.NUMBER):
        return NumberLiteral(location=location, value=float(self.advance().value))
    
    elif self.match(TokenType.TEXT):
        return TextLiteral(location=location, value=self.advance().value)
    
    elif self.match(TokenType.TRUE):
        self.advance()
        return BooleanLiteral(location=location, value=True)
    
    elif self.match(TokenType.FALSE):
        self.advance()
        return BooleanLiteral(location=location, value=False)
    
    elif self.match(TokenType.NOTHING):
        self.advance()
        return NothingLiteral(location=location)
    
    elif self.match(TokenType.INPUT):
        self.advance()
        return InputNode(location=location)
    
    elif self.match(TokenType.IDENTIFIER):
        return IdentifierNode(location=location, name=self.advance().value)
    
    elif self.match(TokenType.LENGTH_OF):
        self.advance()
        operand = self.parse_primary()
        return LengthOfNode(location=location, collection=operand)
    
    elif self.match(TokenType.LBRACKET):
        return self.parse_list_or_table_literal()
    
    elif self.match(TokenType.LPAREN):
        self.advance()
        expr = self.parse_expression()
        self.expect(TokenType.RPAREN, "Expected ')'")
        return expr
    
    else:
        self.error(f"Expected expression, got {self.current.value}")
        return NothingLiteral(location=location)
```

## Error Recovery

The parser attempts to recover from errors to report multiple issues:

```python
def synchronize(self):
    """Skip tokens until we find a statement boundary."""
    self.advance()
    
    while not self.match(TokenType.EOF):
        # After a newline at proper indentation, try to continue
        if self.tokens[self.pos - 1].type == TokenType.NEWLINE:
            return
        
        # Statement-starting keywords
        if self.match(TokenType.DISPLAY, TokenType.SET, TokenType.CALL,
                     TokenType.RETURN, TokenType.EXIT, TokenType.IF,
                     TokenType.REPEAT, TokenType.ATTEMPT):
            return
        
        self.advance()
```

## Error Messages

| Situation | Message |
|-----------|---------|
| Missing colon | `Line 5: Expected ':' after 'step'. Did you forget the colon?` |
| Missing body | `Line 8: Expected indented code after 'do:'. Every 'do:' needs code inside it.` |
| Bad expression | `Line 12: Expected a value here (number, text, or variable name).` |
| Unclosed if | `Line 15: This 'if' statement needs code inside it. Indent the code that should run when the condition is true.` |
| Wrong keyword | `Line 20: Found 'else' but Steps uses 'otherwise'. Try: otherwise` |
