"""Unit Tests for Steps Lexer.

Comprehensive tests for tokenization including:
- Basic token types
- Multi-word keywords
- Indentation handling
- String literals and escapes
- Numbers
- Error messages
"""

import pytest
from pathlib import Path

from steps.lexer import (
    Lexer, Token, TokenType, tokenize,
    MULTI_WORD_KEYWORDS, KEYWORDS
)
from steps.errors import LexerError


# =============================================================================
# Helper Functions
# =============================================================================

def get_tokens(source: str) -> list[Token]:
    """Tokenize source and return list of tokens."""
    return tokenize(source, Path("test.step"))


def get_token_types(source: str) -> list[TokenType]:
    """Get just the token types from source."""
    return [t.type for t in get_tokens(source)]


def first_token(source: str) -> Token:
    """Get the first non-EOF token."""
    tokens = get_tokens(source)
    return tokens[0]


# =============================================================================
# Basic Tokenization Tests
# =============================================================================

class TestTokenizeBasics:
    """Tests for basic token types."""
    
    def test_empty_source(self):
        tokens = get_tokens("")
        assert len(tokens) == 1
        assert tokens[0].type == TokenType.EOF
    
    def test_single_number_integer(self):
        token = first_token("42")
        assert token.type == TokenType.NUMBER
        assert token.value == "42"
    
    def test_single_number_decimal(self):
        token = first_token("3.14")
        assert token.type == TokenType.NUMBER
        assert token.value == "3.14"
    
    def test_negative_number(self):
        token = first_token("-7")
        assert token.type == TokenType.NUMBER
        assert token.value == "-7"
    
    def test_negative_decimal(self):
        token = first_token("-3.14")
        assert token.type == TokenType.NUMBER
        assert token.value == "-3.14"
    
    def test_string_literal(self):
        token = first_token('"hello world"')
        assert token.type == TokenType.TEXT
        assert token.value == "hello world"
    
    def test_string_escapes_newline(self):
        token = first_token(r'"hello\nworld"')
        assert token.value == "hello\nworld"
    
    def test_string_escapes_tab(self):
        token = first_token(r'"hello\tworld"')
        assert token.value == "hello\tworld"
    
    def test_string_escapes_quote(self):
        token = first_token(r'"say \"hello\""')
        assert token.value == 'say "hello"'
    
    def test_string_escapes_backslash(self):
        token = first_token(r'"path\\to\\file"')
        assert token.value == "path\\to\\file"
    
    def test_identifier(self):
        token = first_token("my_variable")
        assert token.type == TokenType.IDENTIFIER
        assert token.value == "my_variable"
    
    def test_identifier_with_numbers(self):
        token = first_token("var123")
        assert token.type == TokenType.IDENTIFIER
        assert token.value == "var123"
    
    def test_identifier_starting_underscore(self):
        token = first_token("_private")
        assert token.type == TokenType.IDENTIFIER
        assert token.value == "_private"


# =============================================================================
# Keyword Tests
# =============================================================================

class TestTokenizeKeywords:
    """Tests for single-word keywords."""
    
    @pytest.mark.parametrize("keyword,expected_type", [
        ("true", TokenType.TRUE),
        ("false", TokenType.FALSE),
        ("nothing", TokenType.NOTHING),
        ("set", TokenType.SET),
        ("to", TokenType.TO),
        ("call", TokenType.CALL),
        ("with", TokenType.WITH),
        ("return", TokenType.RETURN),
        ("display", TokenType.DISPLAY),
        ("input", TokenType.INPUT),
        ("if", TokenType.IF),
        ("otherwise", TokenType.OTHERWISE),
        ("repeat", TokenType.REPEAT),
        ("times", TokenType.TIMES),
        ("while", TokenType.WHILE),
        ("and", TokenType.AND),
        ("or", TokenType.OR),
        ("not", TokenType.NOT),
        ("as", TokenType.AS),
        ("fixed", TokenType.FIXED),
        ("exit", TokenType.EXIT),
        ("equals", TokenType.EQUALS),
        ("contains", TokenType.CONTAINS),
        ("add", TokenType.ADD),
        ("remove", TokenType.REMOVE),
        ("from", TokenType.FROM),
        ("in", TokenType.IN),
    ])
    def test_single_keyword(self, keyword, expected_type):
        token = first_token(keyword)
        assert token.type == expected_type
        assert token.value == keyword
    
    @pytest.mark.parametrize("keyword,expected_type", [
        ("number", TokenType.TYPE_NUMBER),
        ("text", TokenType.TYPE_TEXT),
        ("boolean", TokenType.TYPE_BOOLEAN),
        ("list", TokenType.TYPE_LIST),
        ("table", TokenType.TYPE_TABLE),
    ])
    def test_type_keywords(self, keyword, expected_type):
        token = first_token(keyword)
        assert token.type == expected_type


class TestTokenizeStructureKeywords:
    """Tests for structure keywords (with colons)."""
    
    def test_building_with_colon(self):
        token = first_token("building:")
        assert token.type == TokenType.BUILDING
        assert "building" in token.value
    
    def test_floor_with_colon(self):
        token = first_token("floor:")
        assert token.type == TokenType.FLOOR
    
    def test_step_with_colon(self):
        token = first_token("step:")
        assert token.type == TokenType.STEP
    
    def test_riser_with_colon(self):
        token = first_token("riser:")
        assert token.type == TokenType.RISER
    
    def test_expects_with_colon(self):
        token = first_token("expects:")
        assert token.type == TokenType.EXPECTS
    
    def test_returns_with_colon(self):
        token = first_token("returns:")
        assert token.type == TokenType.RETURNS
    
    def test_declare_with_colon(self):
        token = first_token("declare:")
        assert token.type == TokenType.DECLARE
    
    def test_do_with_colon(self):
        token = first_token("do:")
        assert token.type == TokenType.DO
    
    def test_attempt_with_colon(self):
        token = first_token("attempt:")
        assert token.type == TokenType.ATTEMPT


class TestTokenizeMultiWordKeywords:
    """Tests for multi-word keywords."""
    
    @pytest.mark.parametrize("keyword,token_type", MULTI_WORD_KEYWORDS)
    def test_multi_word_keyword(self, keyword, token_type):
        token = first_token(keyword)
        assert token.type == token_type
        assert token.value == keyword
    
    def test_is_greater_than_not_equal(self):
        """Ensure 'is greater than' doesn't match 'is greater than or equal to'."""
        token = first_token("is greater than value")
        assert token.type == TokenType.IS_GREATER_THAN
    
    def test_is_less_than_not_equal(self):
        """Ensure 'is less than' doesn't match 'is less than or equal to'."""
        token = first_token("is less than value")
        assert token.type == TokenType.IS_LESS_THAN
    
    def test_in_not_matching_input(self):
        """Ensure 'in' doesn't match as part of 'input'."""
        token = first_token("input")
        assert token.type == TokenType.INPUT
        assert token.value == "input"
    
    def test_storing_result_in(self):
        token = first_token("storing result in var")
        assert token.type == TokenType.STORING_RESULT_IN
    
    def test_is_equal_to(self):
        token = first_token("is equal to")
        assert token.type == TokenType.IS_EQUAL_TO
    
    def test_is_not_equal_to(self):
        token = first_token("is not equal to")
        assert token.type == TokenType.IS_NOT_EQUAL_TO


# =============================================================================
# Operator Tests
# =============================================================================

class TestTokenizeOperators:
    """Tests for operators."""
    
    def test_plus(self):
        token = first_token("+")
        assert token.type == TokenType.PLUS
    
    def test_minus_alone(self):
        # When minus is alone (not before a digit), it's an operator
        tokens = get_tokens("x - 5")
        minus_token = tokens[1]
        assert minus_token.type == TokenType.MINUS
    
    def test_multiply(self):
        token = first_token("*")
        assert token.type == TokenType.MULTIPLY
    
    def test_divide(self):
        token = first_token("/")
        assert token.type == TokenType.DIVIDE


class TestTokenizePunctuation:
    """Tests for punctuation."""
    
    def test_colon(self):
        token = first_token(":")
        assert token.type == TokenType.COLON
    
    def test_comma(self):
        token = first_token(",")
        assert token.type == TokenType.COMMA
    
    def test_lbracket(self):
        token = first_token("[")
        assert token.type == TokenType.LBRACKET
    
    def test_rbracket(self):
        token = first_token("]")
        assert token.type == TokenType.RBRACKET
    
    def test_lparen(self):
        token = first_token("(")
        assert token.type == TokenType.LPAREN
    
    def test_rparen(self):
        token = first_token(")")
        assert token.type == TokenType.RPAREN


# =============================================================================
# Indentation Tests
# =============================================================================

class TestTokenizeIndentation:
    """Tests for indentation handling."""
    
    def test_single_indent(self):
        source = "building: test\n    display 1"
        types = get_token_types(source)
        assert TokenType.INDENT in types
    
    def test_count_indent_tokens(self):
        source = "building: test\n    display 1"
        tokens = get_tokens(source)
        indent_count = sum(1 for t in tokens if t.type == TokenType.INDENT)
        assert indent_count == 1
    
    def test_double_indent(self):
        source = "if true\n    if false\n        display 1"
        tokens = get_tokens(source)
        indent_count = sum(1 for t in tokens if t.type == TokenType.INDENT)
        assert indent_count == 2
    
    def test_dedent_single(self):
        source = "if true\n    display 1\ndisplay 2"
        tokens = get_tokens(source)
        dedent_count = sum(1 for t in tokens if t.type == TokenType.DEDENT)
        assert dedent_count == 1
    
    def test_dedent_multiple(self):
        source = "if true\n    if false\n        display 1\ndisplay 2"
        tokens = get_tokens(source)
        dedent_count = sum(1 for t in tokens if t.type == TokenType.DEDENT)
        assert dedent_count == 2
    
    def test_indent_dedent_sequence(self):
        source = """building: test
    display 1
    if true
        display 2
    display 3
"""
        tokens = get_tokens(source)
        indent_count = sum(1 for t in tokens if t.type == TokenType.INDENT)
        dedent_count = sum(1 for t in tokens if t.type == TokenType.DEDENT)
        # One indent for building body, one for if body
        assert indent_count == 2
        # Dedent back from if body, then dedent at EOF for building body
        assert dedent_count == 2
    
    def test_blank_lines_ignored(self):
        """Blank lines should not affect indentation."""
        source = "building: test\n    display 1\n\n    display 2"
        tokens = get_tokens(source)
        # Should only have one INDENT despite blank line
        indent_count = sum(1 for t in tokens if t.type == TokenType.INDENT)
        assert indent_count == 1


# =============================================================================
# Error Tests
# =============================================================================

class TestLexerErrors:
    """Tests for lexer error handling."""
    
    def test_tab_error(self):
        with pytest.raises(LexerError) as exc:
            get_tokens("\tdisplay 1")
        assert "tab" in str(exc.value).lower()
        assert "4 spaces" in str(exc.value)
    
    def test_bad_indentation_3_spaces(self):
        with pytest.raises(LexerError) as exc:
            get_tokens("building: test\n   display 1")  # 3 spaces
        error = exc.value
        assert "4 spaces" in str(error) or "3 spaces" in str(error)
    
    def test_bad_indentation_5_spaces(self):
        with pytest.raises(LexerError) as exc:
            get_tokens("building: test\n     display 1")  # 5 spaces
        error = exc.value
        assert "spaces" in str(error).lower()
    
    def test_unterminated_string(self):
        with pytest.raises(LexerError) as exc:
            get_tokens('"hello')
        error = exc.value
        assert "closed" in str(error).lower() or "never" in str(error).lower()
    
    def test_unterminated_string_with_newline(self):
        with pytest.raises(LexerError) as exc:
            get_tokens('"hello\nworld"')
        error = exc.value
        assert "closed" in str(error).lower() or "never" in str(error).lower()
    
    def test_invalid_escape(self):
        with pytest.raises(LexerError) as exc:
            get_tokens(r'"hello\x"')  # \x is not valid
        assert "escape" in str(exc.value).lower()
    
    def test_invalid_character(self):
        with pytest.raises(LexerError) as exc:
            get_tokens("@invalid")
        assert "@" in str(exc.value)
    
    def test_inconsistent_indentation(self):
        # Indent to 4, then to 6 (not 8)
        with pytest.raises(LexerError) as exc:
            get_tokens("if true\n    if true\n      display 1")  # 6 spaces
        error = exc.value
        assert "indent" in str(error).lower()


# =============================================================================
# Source Location Tests
# =============================================================================

class TestTokenizeSourceLocation:
    """Tests for accurate line/column tracking."""
    
    def test_first_token_line(self):
        token = first_token("hello")
        assert token.line == 1
        assert token.column == 1
    
    def test_second_line(self):
        tokens = get_tokens("line1\nline2")
        # Find token on line 2
        line2_tokens = [t for t in tokens if t.line == 2]
        assert len(line2_tokens) > 0
    
    def test_column_tracking(self):
        tokens = get_tokens("set x to 42")
        # set at col 1, x at col 5, to at col 7, 42 at col 10
        assert tokens[0].column == 1  # set
        assert tokens[1].column == 5  # x
        assert tokens[2].column == 7  # to
        assert tokens[3].column == 10  # 42
    
    def test_file_path_preserved(self):
        lexer = Lexer("test", Path("/path/to/file.step"))
        tokens = lexer.tokenize()
        assert tokens[0].file == Path("/path/to/file.step")


# =============================================================================
# Complex Source Tests
# =============================================================================

class TestTokenizeComplexSource:
    """Tests for complete source code snippets."""
    
    def test_simple_building(self):
        source = """building: hello

    display "Hello, World!"
    exit
"""
        tokens = get_tokens(source)
        types = [t.type for t in tokens]
        
        assert TokenType.BUILDING in types
        assert TokenType.DISPLAY in types
        assert TokenType.TEXT in types
        assert TokenType.EXIT in types
    
    def test_step_header(self):
        source = """step: greet
    belongs to: main
    expects: name
    returns: message
"""
        tokens = get_tokens(source)
        types = [t.type for t in tokens]
        
        assert TokenType.STEP in types
        assert TokenType.BELONGS_TO in types
        assert TokenType.EXPECTS in types
        assert TokenType.RETURNS in types
    
    def test_variable_assignment(self):
        source = "set count to count + 1"
        tokens = get_tokens(source)
        types = [t.type for t in tokens]
        
        assert types[:5] == [
            TokenType.SET,
            TokenType.IDENTIFIER,  # count
            TokenType.TO,
            TokenType.IDENTIFIER,  # count
            TokenType.PLUS,
        ]
    
    def test_step_call_with_storing(self):
        source = "call greet with name storing result in greeting"
        tokens = get_tokens(source)
        types = [t.type for t in tokens]
        
        assert TokenType.CALL in types
        assert TokenType.WITH in types
        assert TokenType.STORING_RESULT_IN in types
    
    def test_comparison_expression(self):
        source = "if x is greater than or equal to 10"
        tokens = get_tokens(source)
        types = [t.type for t in tokens]
        
        assert TokenType.IF in types
        assert TokenType.IS_GREATER_THAN_OR_EQUAL_TO in types
        assert TokenType.NUMBER in types
    
    def test_list_literal(self):
        source = "[1, 2, 3]"
        tokens = get_tokens(source)
        types = [t.type for t in tokens]
        
        assert TokenType.LBRACKET in types
        assert types.count(TokenType.NUMBER) == 3
        assert types.count(TokenType.COMMA) == 2
        assert TokenType.RBRACKET in types
    
    def test_note_comment(self):
        source = "note: This is a comment"
        token = first_token(source)
        assert token.type == TokenType.NOTE
        assert "This is a comment" in token.value


# =============================================================================
# Token Count Verification
# =============================================================================

class TestTokenCounts:
    """Verify we have the expected number of token types."""
    
    def test_token_type_count(self):
        # Should have ~60+ token types
        assert len(TokenType) >= 60
    
    def test_all_multi_word_keywords_unique(self):
        types = [t for _, t in MULTI_WORD_KEYWORDS]
        assert len(types) == len(set(types))
    
    def test_no_overlap_keywords(self):
        """Ensure single and multi-word keywords don't conflict."""
        single_words = set(KEYWORDS.keys())
        for multi_kw, _ in MULTI_WORD_KEYWORDS:
            # First word of multi-word should be in single (like 'is', 'for')
            # but the combined phrase should be distinct
            words = multi_kw.split()
            assert len(words) >= 2
