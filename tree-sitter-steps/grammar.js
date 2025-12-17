/**
 * Tree-sitter grammar for the Steps programming language.
 * 
 * Steps is an educational language with an architectural metaphor:
 * - Building = Program
 * - Floor = Functional grouping (module)
 * - Step = Unit of work (function)
 * - Riser = Private helper (private function)
 */

module.exports = grammar({
  name: 'steps',

  // Tokens that can appear anywhere (whitespace handling)
  extras: $ => [/[ \t]/],

  // Word characters for keyword extraction
  word: $ => $.identifier,

  rules: {
    // Entry point - a source file
    source_file: $ => repeat($._statement),

    _statement: $ => choice(
      $.comment,
      $.block_comment,
      $.structure_definition,
      $.section_marker,
      $.declaration,
      $.assignment,
      $.call_statement,
      $.display_statement,
      $.input_statement,
      $.return_statement,
      $.exit_statement,
      $.if_statement,
      $.repeat_statement,
      $.for_each_statement,
      $.while_statement,
      $.attempt_statement,
      $.add_statement,
      $.remove_statement,
      $._newline
    ),

    // Section markers (do:, declare:)
    section_marker: $ => choice('do:', 'declare:'),

    // Comments
    comment: $ => seq(
      'note:',
      optional($.comment_content)
    ),

    comment_content: $ => /[^\n]*/,

    block_comment: $ => seq(
      'note block:',
      optional($.block_comment_content),
      'end note'
    ),

    block_comment_content: $ => repeat1(choice(
      /[^e]+/,
      /e[^n]/,
      /en[^d]/,
      /end[^ ]/,
      /end [ ][^n]/,
      /end [ ]n[^o]/,
      /end [ ]no[^t]/,
      /end [ ]not[^e]/,
    )),

    // Structure definitions
    structure_definition: $ => choice(
      $.building_def,
      $.floor_def,
      $.step_def,
      $.riser_def
    ),

    building_def: $ => seq('building:', $.identifier),
    floor_def: $ => seq('floor:', $.identifier),
    step_def: $ => seq('step:', $.identifier, optional($.step_clauses)),
    riser_def: $ => seq('riser:', $.identifier, optional($.step_clauses)),

    step_clauses: $ => repeat1(choice(
      $.belongs_clause,
      $.expects_clause,
      $.returns_clause
    )),

    belongs_clause: $ => seq('belongs to:', $.identifier),
    expects_clause: $ => seq('expects:', $.parameter_list),
    returns_clause: $ => seq('returns:', $.type),

    parameter_list: $ => seq(
      $.parameter,
      repeat(seq(',', $.parameter))
    ),

    parameter: $ => seq($.identifier, 'as', $.type),

    // Types
    type: $ => choice('number', 'text', 'boolean', 'list', 'table'),

    // Declarations
    declaration: $ => seq(
      'declare:',
      optional('fixed'),
      $.identifier,
      'as',
      $.type,
      optional(seq('=', $._expression))
    ),

    // Assignment
    assignment: $ => seq('set', $.identifier, 'to', $._expression),

    // Function calls
    call_statement: $ => seq(
      'call',
      $.identifier,
      optional($.with_clause),
      optional($.storing_clause)
    ),

    with_clause: $ => seq('with', $.argument_list),
    storing_clause: $ => seq('storing result in', $.identifier),
    argument_list: $ => prec.left(seq($._expression, repeat(seq(',', $._expression)))),

    // I/O
    display_statement: $ => seq('display', $._expression),
    input_statement: $ => seq('input', $.identifier),
    return_statement: $ => prec.right(seq('return', optional($._expression))),
    exit_statement: $ => 'exit',

    // Control flow
    if_statement: $ => seq(
      'if',
      $._expression,
      optional(repeat($.otherwise_if_clause)),
      optional($.otherwise_clause)
    ),

    otherwise_if_clause: $ => seq('otherwise if', $._expression),
    otherwise_clause: $ => seq('otherwise'),

    repeat_statement: $ => seq('repeat', $._expression, 'times'),
    for_each_statement: $ => seq('for each', $.identifier, 'in', $._expression),
    while_statement: $ => seq('while', $._expression),

    attempt_statement: $ => seq(
      'attempt:',
      optional($.if_unsuccessful_clause),
      optional($.then_continue_clause)
    ),

    if_unsuccessful_clause: $ => seq('if unsuccessful:'),
    then_continue_clause: $ => seq('then continue:'),

    // List operations
    add_statement: $ => seq('add', $._expression, 'to', $.identifier),
    remove_statement: $ => seq('remove', $._expression, 'from', $.identifier),

    // Expressions
    _expression: $ => choice(
      $.identifier,
      $.number,
      $.string,
      $.boolean,
      $.nothing,
      $.list_literal,
      $.binary_expression,
      $.unary_expression,
      $.call_expression,
      $.index_expression,
      $.parenthesized_expression
    ),

    // Literals
    number: $ => /-?[0-9]+(\.[0-9]+)?/,
    string: $ => seq('"', optional($.string_content), '"'),
    string_content: $ => repeat1(choice($.escape_sequence, /[^"\\]+/)),
    escape_sequence: $ => /\\[ntr"\\]/,
    boolean: $ => choice('true', 'false'),
    nothing: $ => 'nothing',
    list_literal: $ => seq('[', optional($.argument_list), ']'),

    // Binary expressions
    binary_expression: $ => prec.left(1, seq(
      $._expression,
      $.binary_operator,
      $._expression
    )),

    binary_operator: $ => choice(
      // Math
      '+', '-', '*', '/',
      // Comparison
      'is equal to', 'equals', 'is not equal to',
      'is less than', 'is greater than',
      'is less than or equal to', 'is greater than or equal to',
      // Boolean
      'and', 'or',
      // Text
      'added to', 'contains', 'starts with', 'ends with',
      // List
      'is in'
    ),

    // Unary expressions
    unary_expression: $ => prec(2, seq(
      $.unary_operator,
      $._expression
    )),

    unary_operator: $ => choice('not', 'length of'),

    // Call expression (inline)
    call_expression: $ => seq(
      'call',
      $.identifier,
      optional($.with_clause)
    ),

    // Index expression (higher precedence than argument_list and unary)
    index_expression: $ => prec(3, seq(
      $._expression,
      '[',
      $._expression,
      ']'
    )),

    parenthesized_expression: $ => seq('(', $._expression, ')'),

    // Identifiers
    identifier: $ => /[a-zA-Z_][a-zA-Z0-9_]*/,

    // Newlines
    _newline: $ => /\n/
  }
});

