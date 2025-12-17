#include <tree_sitter/parser.h>

#if defined(__GNUC__) || defined(__clang__)
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmissing-field-initializers"
#endif

#ifdef _MSC_VER
#pragma optimize("", off)
#elif defined(__clang__)
#pragma clang optimize off
#elif defined(__GNUC__)
#pragma GCC optimize ("O0")
#endif

#define LANGUAGE_VERSION 14
#define STATE_COUNT 151
#define LARGE_STATE_COUNT 2
#define SYMBOL_COUNT 144
#define ALIAS_COUNT 0
#define TOKEN_COUNT 87
#define EXTERNAL_TOKEN_COUNT 0
#define FIELD_COUNT 0
#define MAX_ALIAS_SEQUENCE_LENGTH 7
#define PRODUCTION_ID_COUNT 1

enum {
  sym_identifier = 1,
  anon_sym_do_COLON = 2,
  anon_sym_declare_COLON = 3,
  anon_sym_note_COLON = 4,
  sym_comment_content = 5,
  anon_sym_noteblock_COLON = 6,
  anon_sym_endnote = 7,
  aux_sym_block_comment_content_token1 = 8,
  aux_sym_block_comment_content_token2 = 9,
  aux_sym_block_comment_content_token3 = 10,
  aux_sym_block_comment_content_token4 = 11,
  aux_sym_block_comment_content_token5 = 12,
  aux_sym_block_comment_content_token6 = 13,
  aux_sym_block_comment_content_token7 = 14,
  aux_sym_block_comment_content_token8 = 15,
  anon_sym_building_COLON = 16,
  anon_sym_floor_COLON = 17,
  anon_sym_step_COLON = 18,
  anon_sym_riser_COLON = 19,
  anon_sym_belongsto_COLON = 20,
  anon_sym_expects_COLON = 21,
  anon_sym_returns_COLON = 22,
  anon_sym_COMMA = 23,
  anon_sym_as = 24,
  anon_sym_number = 25,
  anon_sym_text = 26,
  anon_sym_boolean = 27,
  anon_sym_list = 28,
  anon_sym_table = 29,
  anon_sym_fixed = 30,
  anon_sym_EQ = 31,
  anon_sym_set = 32,
  anon_sym_to = 33,
  anon_sym_call = 34,
  anon_sym_with = 35,
  anon_sym_storingresultin = 36,
  anon_sym_display = 37,
  anon_sym_input = 38,
  anon_sym_return = 39,
  sym_exit_statement = 40,
  anon_sym_if = 41,
  anon_sym_otherwiseif = 42,
  anon_sym_otherwise = 43,
  anon_sym_repeat = 44,
  anon_sym_times = 45,
  anon_sym_foreach = 46,
  anon_sym_in = 47,
  anon_sym_while = 48,
  anon_sym_attempt_COLON = 49,
  anon_sym_ifunsuccessful_COLON = 50,
  anon_sym_thencontinue_COLON = 51,
  anon_sym_add = 52,
  anon_sym_remove = 53,
  anon_sym_from = 54,
  sym_number = 55,
  anon_sym_DQUOTE = 56,
  aux_sym_string_content_token1 = 57,
  sym_escape_sequence = 58,
  anon_sym_true = 59,
  anon_sym_false = 60,
  sym_nothing = 61,
  anon_sym_LBRACK = 62,
  anon_sym_RBRACK = 63,
  anon_sym_PLUS = 64,
  anon_sym_DASH = 65,
  anon_sym_STAR = 66,
  anon_sym_SLASH = 67,
  anon_sym_isequalto = 68,
  anon_sym_equals = 69,
  anon_sym_isnotequalto = 70,
  anon_sym_islessthan = 71,
  anon_sym_isgreaterthan = 72,
  anon_sym_islessthanorequalto = 73,
  anon_sym_isgreaterthanorequalto = 74,
  anon_sym_and = 75,
  anon_sym_or = 76,
  anon_sym_addedto = 77,
  anon_sym_contains = 78,
  anon_sym_startswith = 79,
  anon_sym_endswith = 80,
  anon_sym_isin = 81,
  anon_sym_not = 82,
  anon_sym_lengthof = 83,
  anon_sym_LPAREN = 84,
  anon_sym_RPAREN = 85,
  sym__newline = 86,
  sym_source_file = 87,
  sym__statement = 88,
  sym_section_marker = 89,
  sym_comment = 90,
  sym_block_comment = 91,
  sym_block_comment_content = 92,
  sym_structure_definition = 93,
  sym_building_def = 94,
  sym_floor_def = 95,
  sym_step_def = 96,
  sym_riser_def = 97,
  sym_step_clauses = 98,
  sym_belongs_clause = 99,
  sym_expects_clause = 100,
  sym_returns_clause = 101,
  sym_parameter_list = 102,
  sym_parameter = 103,
  sym_type = 104,
  sym_declaration = 105,
  sym_assignment = 106,
  sym_call_statement = 107,
  sym_with_clause = 108,
  sym_storing_clause = 109,
  sym_argument_list = 110,
  sym_display_statement = 111,
  sym_input_statement = 112,
  sym_return_statement = 113,
  sym_if_statement = 114,
  sym_otherwise_if_clause = 115,
  sym_otherwise_clause = 116,
  sym_repeat_statement = 117,
  sym_for_each_statement = 118,
  sym_while_statement = 119,
  sym_attempt_statement = 120,
  sym_if_unsuccessful_clause = 121,
  sym_then_continue_clause = 122,
  sym_add_statement = 123,
  sym_remove_statement = 124,
  sym__expression = 125,
  sym_string = 126,
  sym_string_content = 127,
  sym_boolean = 128,
  sym_list_literal = 129,
  sym_binary_expression = 130,
  sym_binary_operator = 131,
  sym_unary_expression = 132,
  sym_unary_operator = 133,
  sym_call_expression = 134,
  sym_index_expression = 135,
  sym_parenthesized_expression = 136,
  aux_sym_source_file_repeat1 = 137,
  aux_sym_block_comment_content_repeat1 = 138,
  aux_sym_step_clauses_repeat1 = 139,
  aux_sym_parameter_list_repeat1 = 140,
  aux_sym_argument_list_repeat1 = 141,
  aux_sym_if_statement_repeat1 = 142,
  aux_sym_string_content_repeat1 = 143,
};

static const char * const ts_symbol_names[] = {
  [ts_builtin_sym_end] = "end",
  [sym_identifier] = "identifier",
  [anon_sym_do_COLON] = "do:",
  [anon_sym_declare_COLON] = "declare:",
  [anon_sym_note_COLON] = "note:",
  [sym_comment_content] = "comment_content",
  [anon_sym_noteblock_COLON] = "note block:",
  [anon_sym_endnote] = "end note",
  [aux_sym_block_comment_content_token1] = "block_comment_content_token1",
  [aux_sym_block_comment_content_token2] = "block_comment_content_token2",
  [aux_sym_block_comment_content_token3] = "block_comment_content_token3",
  [aux_sym_block_comment_content_token4] = "block_comment_content_token4",
  [aux_sym_block_comment_content_token5] = "block_comment_content_token5",
  [aux_sym_block_comment_content_token6] = "block_comment_content_token6",
  [aux_sym_block_comment_content_token7] = "block_comment_content_token7",
  [aux_sym_block_comment_content_token8] = "block_comment_content_token8",
  [anon_sym_building_COLON] = "building:",
  [anon_sym_floor_COLON] = "floor:",
  [anon_sym_step_COLON] = "step:",
  [anon_sym_riser_COLON] = "riser:",
  [anon_sym_belongsto_COLON] = "belongs to:",
  [anon_sym_expects_COLON] = "expects:",
  [anon_sym_returns_COLON] = "returns:",
  [anon_sym_COMMA] = ",",
  [anon_sym_as] = "as",
  [anon_sym_number] = "number",
  [anon_sym_text] = "text",
  [anon_sym_boolean] = "boolean",
  [anon_sym_list] = "list",
  [anon_sym_table] = "table",
  [anon_sym_fixed] = "fixed",
  [anon_sym_EQ] = "=",
  [anon_sym_set] = "set",
  [anon_sym_to] = "to",
  [anon_sym_call] = "call",
  [anon_sym_with] = "with",
  [anon_sym_storingresultin] = "storing result in",
  [anon_sym_display] = "display",
  [anon_sym_input] = "input",
  [anon_sym_return] = "return",
  [sym_exit_statement] = "exit_statement",
  [anon_sym_if] = "if",
  [anon_sym_otherwiseif] = "otherwise if",
  [anon_sym_otherwise] = "otherwise",
  [anon_sym_repeat] = "repeat",
  [anon_sym_times] = "times",
  [anon_sym_foreach] = "for each",
  [anon_sym_in] = "in",
  [anon_sym_while] = "while",
  [anon_sym_attempt_COLON] = "attempt:",
  [anon_sym_ifunsuccessful_COLON] = "if unsuccessful:",
  [anon_sym_thencontinue_COLON] = "then continue:",
  [anon_sym_add] = "add",
  [anon_sym_remove] = "remove",
  [anon_sym_from] = "from",
  [sym_number] = "number",
  [anon_sym_DQUOTE] = "\"",
  [aux_sym_string_content_token1] = "string_content_token1",
  [sym_escape_sequence] = "escape_sequence",
  [anon_sym_true] = "true",
  [anon_sym_false] = "false",
  [sym_nothing] = "nothing",
  [anon_sym_LBRACK] = "[",
  [anon_sym_RBRACK] = "]",
  [anon_sym_PLUS] = "+",
  [anon_sym_DASH] = "-",
  [anon_sym_STAR] = "*",
  [anon_sym_SLASH] = "/",
  [anon_sym_isequalto] = "is equal to",
  [anon_sym_equals] = "equals",
  [anon_sym_isnotequalto] = "is not equal to",
  [anon_sym_islessthan] = "is less than",
  [anon_sym_isgreaterthan] = "is greater than",
  [anon_sym_islessthanorequalto] = "is less than or equal to",
  [anon_sym_isgreaterthanorequalto] = "is greater than or equal to",
  [anon_sym_and] = "and",
  [anon_sym_or] = "or",
  [anon_sym_addedto] = "added to",
  [anon_sym_contains] = "contains",
  [anon_sym_startswith] = "starts with",
  [anon_sym_endswith] = "ends with",
  [anon_sym_isin] = "is in",
  [anon_sym_not] = "not",
  [anon_sym_lengthof] = "length of",
  [anon_sym_LPAREN] = "(",
  [anon_sym_RPAREN] = ")",
  [sym__newline] = "_newline",
  [sym_source_file] = "source_file",
  [sym__statement] = "_statement",
  [sym_section_marker] = "section_marker",
  [sym_comment] = "comment",
  [sym_block_comment] = "block_comment",
  [sym_block_comment_content] = "block_comment_content",
  [sym_structure_definition] = "structure_definition",
  [sym_building_def] = "building_def",
  [sym_floor_def] = "floor_def",
  [sym_step_def] = "step_def",
  [sym_riser_def] = "riser_def",
  [sym_step_clauses] = "step_clauses",
  [sym_belongs_clause] = "belongs_clause",
  [sym_expects_clause] = "expects_clause",
  [sym_returns_clause] = "returns_clause",
  [sym_parameter_list] = "parameter_list",
  [sym_parameter] = "parameter",
  [sym_type] = "type",
  [sym_declaration] = "declaration",
  [sym_assignment] = "assignment",
  [sym_call_statement] = "call_statement",
  [sym_with_clause] = "with_clause",
  [sym_storing_clause] = "storing_clause",
  [sym_argument_list] = "argument_list",
  [sym_display_statement] = "display_statement",
  [sym_input_statement] = "input_statement",
  [sym_return_statement] = "return_statement",
  [sym_if_statement] = "if_statement",
  [sym_otherwise_if_clause] = "otherwise_if_clause",
  [sym_otherwise_clause] = "otherwise_clause",
  [sym_repeat_statement] = "repeat_statement",
  [sym_for_each_statement] = "for_each_statement",
  [sym_while_statement] = "while_statement",
  [sym_attempt_statement] = "attempt_statement",
  [sym_if_unsuccessful_clause] = "if_unsuccessful_clause",
  [sym_then_continue_clause] = "then_continue_clause",
  [sym_add_statement] = "add_statement",
  [sym_remove_statement] = "remove_statement",
  [sym__expression] = "_expression",
  [sym_string] = "string",
  [sym_string_content] = "string_content",
  [sym_boolean] = "boolean",
  [sym_list_literal] = "list_literal",
  [sym_binary_expression] = "binary_expression",
  [sym_binary_operator] = "binary_operator",
  [sym_unary_expression] = "unary_expression",
  [sym_unary_operator] = "unary_operator",
  [sym_call_expression] = "call_expression",
  [sym_index_expression] = "index_expression",
  [sym_parenthesized_expression] = "parenthesized_expression",
  [aux_sym_source_file_repeat1] = "source_file_repeat1",
  [aux_sym_block_comment_content_repeat1] = "block_comment_content_repeat1",
  [aux_sym_step_clauses_repeat1] = "step_clauses_repeat1",
  [aux_sym_parameter_list_repeat1] = "parameter_list_repeat1",
  [aux_sym_argument_list_repeat1] = "argument_list_repeat1",
  [aux_sym_if_statement_repeat1] = "if_statement_repeat1",
  [aux_sym_string_content_repeat1] = "string_content_repeat1",
};

static const TSSymbol ts_symbol_map[] = {
  [ts_builtin_sym_end] = ts_builtin_sym_end,
  [sym_identifier] = sym_identifier,
  [anon_sym_do_COLON] = anon_sym_do_COLON,
  [anon_sym_declare_COLON] = anon_sym_declare_COLON,
  [anon_sym_note_COLON] = anon_sym_note_COLON,
  [sym_comment_content] = sym_comment_content,
  [anon_sym_noteblock_COLON] = anon_sym_noteblock_COLON,
  [anon_sym_endnote] = anon_sym_endnote,
  [aux_sym_block_comment_content_token1] = aux_sym_block_comment_content_token1,
  [aux_sym_block_comment_content_token2] = aux_sym_block_comment_content_token2,
  [aux_sym_block_comment_content_token3] = aux_sym_block_comment_content_token3,
  [aux_sym_block_comment_content_token4] = aux_sym_block_comment_content_token4,
  [aux_sym_block_comment_content_token5] = aux_sym_block_comment_content_token5,
  [aux_sym_block_comment_content_token6] = aux_sym_block_comment_content_token6,
  [aux_sym_block_comment_content_token7] = aux_sym_block_comment_content_token7,
  [aux_sym_block_comment_content_token8] = aux_sym_block_comment_content_token8,
  [anon_sym_building_COLON] = anon_sym_building_COLON,
  [anon_sym_floor_COLON] = anon_sym_floor_COLON,
  [anon_sym_step_COLON] = anon_sym_step_COLON,
  [anon_sym_riser_COLON] = anon_sym_riser_COLON,
  [anon_sym_belongsto_COLON] = anon_sym_belongsto_COLON,
  [anon_sym_expects_COLON] = anon_sym_expects_COLON,
  [anon_sym_returns_COLON] = anon_sym_returns_COLON,
  [anon_sym_COMMA] = anon_sym_COMMA,
  [anon_sym_as] = anon_sym_as,
  [anon_sym_number] = anon_sym_number,
  [anon_sym_text] = anon_sym_text,
  [anon_sym_boolean] = anon_sym_boolean,
  [anon_sym_list] = anon_sym_list,
  [anon_sym_table] = anon_sym_table,
  [anon_sym_fixed] = anon_sym_fixed,
  [anon_sym_EQ] = anon_sym_EQ,
  [anon_sym_set] = anon_sym_set,
  [anon_sym_to] = anon_sym_to,
  [anon_sym_call] = anon_sym_call,
  [anon_sym_with] = anon_sym_with,
  [anon_sym_storingresultin] = anon_sym_storingresultin,
  [anon_sym_display] = anon_sym_display,
  [anon_sym_input] = anon_sym_input,
  [anon_sym_return] = anon_sym_return,
  [sym_exit_statement] = sym_exit_statement,
  [anon_sym_if] = anon_sym_if,
  [anon_sym_otherwiseif] = anon_sym_otherwiseif,
  [anon_sym_otherwise] = anon_sym_otherwise,
  [anon_sym_repeat] = anon_sym_repeat,
  [anon_sym_times] = anon_sym_times,
  [anon_sym_foreach] = anon_sym_foreach,
  [anon_sym_in] = anon_sym_in,
  [anon_sym_while] = anon_sym_while,
  [anon_sym_attempt_COLON] = anon_sym_attempt_COLON,
  [anon_sym_ifunsuccessful_COLON] = anon_sym_ifunsuccessful_COLON,
  [anon_sym_thencontinue_COLON] = anon_sym_thencontinue_COLON,
  [anon_sym_add] = anon_sym_add,
  [anon_sym_remove] = anon_sym_remove,
  [anon_sym_from] = anon_sym_from,
  [sym_number] = sym_number,
  [anon_sym_DQUOTE] = anon_sym_DQUOTE,
  [aux_sym_string_content_token1] = aux_sym_string_content_token1,
  [sym_escape_sequence] = sym_escape_sequence,
  [anon_sym_true] = anon_sym_true,
  [anon_sym_false] = anon_sym_false,
  [sym_nothing] = sym_nothing,
  [anon_sym_LBRACK] = anon_sym_LBRACK,
  [anon_sym_RBRACK] = anon_sym_RBRACK,
  [anon_sym_PLUS] = anon_sym_PLUS,
  [anon_sym_DASH] = anon_sym_DASH,
  [anon_sym_STAR] = anon_sym_STAR,
  [anon_sym_SLASH] = anon_sym_SLASH,
  [anon_sym_isequalto] = anon_sym_isequalto,
  [anon_sym_equals] = anon_sym_equals,
  [anon_sym_isnotequalto] = anon_sym_isnotequalto,
  [anon_sym_islessthan] = anon_sym_islessthan,
  [anon_sym_isgreaterthan] = anon_sym_isgreaterthan,
  [anon_sym_islessthanorequalto] = anon_sym_islessthanorequalto,
  [anon_sym_isgreaterthanorequalto] = anon_sym_isgreaterthanorequalto,
  [anon_sym_and] = anon_sym_and,
  [anon_sym_or] = anon_sym_or,
  [anon_sym_addedto] = anon_sym_addedto,
  [anon_sym_contains] = anon_sym_contains,
  [anon_sym_startswith] = anon_sym_startswith,
  [anon_sym_endswith] = anon_sym_endswith,
  [anon_sym_isin] = anon_sym_isin,
  [anon_sym_not] = anon_sym_not,
  [anon_sym_lengthof] = anon_sym_lengthof,
  [anon_sym_LPAREN] = anon_sym_LPAREN,
  [anon_sym_RPAREN] = anon_sym_RPAREN,
  [sym__newline] = sym__newline,
  [sym_source_file] = sym_source_file,
  [sym__statement] = sym__statement,
  [sym_section_marker] = sym_section_marker,
  [sym_comment] = sym_comment,
  [sym_block_comment] = sym_block_comment,
  [sym_block_comment_content] = sym_block_comment_content,
  [sym_structure_definition] = sym_structure_definition,
  [sym_building_def] = sym_building_def,
  [sym_floor_def] = sym_floor_def,
  [sym_step_def] = sym_step_def,
  [sym_riser_def] = sym_riser_def,
  [sym_step_clauses] = sym_step_clauses,
  [sym_belongs_clause] = sym_belongs_clause,
  [sym_expects_clause] = sym_expects_clause,
  [sym_returns_clause] = sym_returns_clause,
  [sym_parameter_list] = sym_parameter_list,
  [sym_parameter] = sym_parameter,
  [sym_type] = sym_type,
  [sym_declaration] = sym_declaration,
  [sym_assignment] = sym_assignment,
  [sym_call_statement] = sym_call_statement,
  [sym_with_clause] = sym_with_clause,
  [sym_storing_clause] = sym_storing_clause,
  [sym_argument_list] = sym_argument_list,
  [sym_display_statement] = sym_display_statement,
  [sym_input_statement] = sym_input_statement,
  [sym_return_statement] = sym_return_statement,
  [sym_if_statement] = sym_if_statement,
  [sym_otherwise_if_clause] = sym_otherwise_if_clause,
  [sym_otherwise_clause] = sym_otherwise_clause,
  [sym_repeat_statement] = sym_repeat_statement,
  [sym_for_each_statement] = sym_for_each_statement,
  [sym_while_statement] = sym_while_statement,
  [sym_attempt_statement] = sym_attempt_statement,
  [sym_if_unsuccessful_clause] = sym_if_unsuccessful_clause,
  [sym_then_continue_clause] = sym_then_continue_clause,
  [sym_add_statement] = sym_add_statement,
  [sym_remove_statement] = sym_remove_statement,
  [sym__expression] = sym__expression,
  [sym_string] = sym_string,
  [sym_string_content] = sym_string_content,
  [sym_boolean] = sym_boolean,
  [sym_list_literal] = sym_list_literal,
  [sym_binary_expression] = sym_binary_expression,
  [sym_binary_operator] = sym_binary_operator,
  [sym_unary_expression] = sym_unary_expression,
  [sym_unary_operator] = sym_unary_operator,
  [sym_call_expression] = sym_call_expression,
  [sym_index_expression] = sym_index_expression,
  [sym_parenthesized_expression] = sym_parenthesized_expression,
  [aux_sym_source_file_repeat1] = aux_sym_source_file_repeat1,
  [aux_sym_block_comment_content_repeat1] = aux_sym_block_comment_content_repeat1,
  [aux_sym_step_clauses_repeat1] = aux_sym_step_clauses_repeat1,
  [aux_sym_parameter_list_repeat1] = aux_sym_parameter_list_repeat1,
  [aux_sym_argument_list_repeat1] = aux_sym_argument_list_repeat1,
  [aux_sym_if_statement_repeat1] = aux_sym_if_statement_repeat1,
  [aux_sym_string_content_repeat1] = aux_sym_string_content_repeat1,
};

static const TSSymbolMetadata ts_symbol_metadata[] = {
  [ts_builtin_sym_end] = {
    .visible = false,
    .named = true,
  },
  [sym_identifier] = {
    .visible = true,
    .named = true,
  },
  [anon_sym_do_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_declare_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_note_COLON] = {
    .visible = true,
    .named = false,
  },
  [sym_comment_content] = {
    .visible = true,
    .named = true,
  },
  [anon_sym_noteblock_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_endnote] = {
    .visible = true,
    .named = false,
  },
  [aux_sym_block_comment_content_token1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_block_comment_content_token2] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_block_comment_content_token3] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_block_comment_content_token4] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_block_comment_content_token5] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_block_comment_content_token6] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_block_comment_content_token7] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_block_comment_content_token8] = {
    .visible = false,
    .named = false,
  },
  [anon_sym_building_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_floor_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_step_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_riser_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_belongsto_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_expects_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_returns_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_COMMA] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_as] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_number] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_text] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_boolean] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_list] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_table] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_fixed] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_EQ] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_set] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_to] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_call] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_with] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_storingresultin] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_display] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_input] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_return] = {
    .visible = true,
    .named = false,
  },
  [sym_exit_statement] = {
    .visible = true,
    .named = true,
  },
  [anon_sym_if] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_otherwiseif] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_otherwise] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_repeat] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_times] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_foreach] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_in] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_while] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_attempt_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_ifunsuccessful_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_thencontinue_COLON] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_add] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_remove] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_from] = {
    .visible = true,
    .named = false,
  },
  [sym_number] = {
    .visible = true,
    .named = true,
  },
  [anon_sym_DQUOTE] = {
    .visible = true,
    .named = false,
  },
  [aux_sym_string_content_token1] = {
    .visible = false,
    .named = false,
  },
  [sym_escape_sequence] = {
    .visible = true,
    .named = true,
  },
  [anon_sym_true] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_false] = {
    .visible = true,
    .named = false,
  },
  [sym_nothing] = {
    .visible = true,
    .named = true,
  },
  [anon_sym_LBRACK] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_RBRACK] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_PLUS] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_DASH] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_STAR] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_SLASH] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_isequalto] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_equals] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_isnotequalto] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_islessthan] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_isgreaterthan] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_islessthanorequalto] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_isgreaterthanorequalto] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_and] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_or] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_addedto] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_contains] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_startswith] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_endswith] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_isin] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_not] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_lengthof] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_LPAREN] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_RPAREN] = {
    .visible = true,
    .named = false,
  },
  [sym__newline] = {
    .visible = false,
    .named = true,
  },
  [sym_source_file] = {
    .visible = true,
    .named = true,
  },
  [sym__statement] = {
    .visible = false,
    .named = true,
  },
  [sym_section_marker] = {
    .visible = true,
    .named = true,
  },
  [sym_comment] = {
    .visible = true,
    .named = true,
  },
  [sym_block_comment] = {
    .visible = true,
    .named = true,
  },
  [sym_block_comment_content] = {
    .visible = true,
    .named = true,
  },
  [sym_structure_definition] = {
    .visible = true,
    .named = true,
  },
  [sym_building_def] = {
    .visible = true,
    .named = true,
  },
  [sym_floor_def] = {
    .visible = true,
    .named = true,
  },
  [sym_step_def] = {
    .visible = true,
    .named = true,
  },
  [sym_riser_def] = {
    .visible = true,
    .named = true,
  },
  [sym_step_clauses] = {
    .visible = true,
    .named = true,
  },
  [sym_belongs_clause] = {
    .visible = true,
    .named = true,
  },
  [sym_expects_clause] = {
    .visible = true,
    .named = true,
  },
  [sym_returns_clause] = {
    .visible = true,
    .named = true,
  },
  [sym_parameter_list] = {
    .visible = true,
    .named = true,
  },
  [sym_parameter] = {
    .visible = true,
    .named = true,
  },
  [sym_type] = {
    .visible = true,
    .named = true,
  },
  [sym_declaration] = {
    .visible = true,
    .named = true,
  },
  [sym_assignment] = {
    .visible = true,
    .named = true,
  },
  [sym_call_statement] = {
    .visible = true,
    .named = true,
  },
  [sym_with_clause] = {
    .visible = true,
    .named = true,
  },
  [sym_storing_clause] = {
    .visible = true,
    .named = true,
  },
  [sym_argument_list] = {
    .visible = true,
    .named = true,
  },
  [sym_display_statement] = {
    .visible = true,
    .named = true,
  },
  [sym_input_statement] = {
    .visible = true,
    .named = true,
  },
  [sym_return_statement] = {
    .visible = true,
    .named = true,
  },
  [sym_if_statement] = {
    .visible = true,
    .named = true,
  },
  [sym_otherwise_if_clause] = {
    .visible = true,
    .named = true,
  },
  [sym_otherwise_clause] = {
    .visible = true,
    .named = true,
  },
  [sym_repeat_statement] = {
    .visible = true,
    .named = true,
  },
  [sym_for_each_statement] = {
    .visible = true,
    .named = true,
  },
  [sym_while_statement] = {
    .visible = true,
    .named = true,
  },
  [sym_attempt_statement] = {
    .visible = true,
    .named = true,
  },
  [sym_if_unsuccessful_clause] = {
    .visible = true,
    .named = true,
  },
  [sym_then_continue_clause] = {
    .visible = true,
    .named = true,
  },
  [sym_add_statement] = {
    .visible = true,
    .named = true,
  },
  [sym_remove_statement] = {
    .visible = true,
    .named = true,
  },
  [sym__expression] = {
    .visible = false,
    .named = true,
  },
  [sym_string] = {
    .visible = true,
    .named = true,
  },
  [sym_string_content] = {
    .visible = true,
    .named = true,
  },
  [sym_boolean] = {
    .visible = true,
    .named = true,
  },
  [sym_list_literal] = {
    .visible = true,
    .named = true,
  },
  [sym_binary_expression] = {
    .visible = true,
    .named = true,
  },
  [sym_binary_operator] = {
    .visible = true,
    .named = true,
  },
  [sym_unary_expression] = {
    .visible = true,
    .named = true,
  },
  [sym_unary_operator] = {
    .visible = true,
    .named = true,
  },
  [sym_call_expression] = {
    .visible = true,
    .named = true,
  },
  [sym_index_expression] = {
    .visible = true,
    .named = true,
  },
  [sym_parenthesized_expression] = {
    .visible = true,
    .named = true,
  },
  [aux_sym_source_file_repeat1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_block_comment_content_repeat1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_step_clauses_repeat1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_parameter_list_repeat1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_argument_list_repeat1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_if_statement_repeat1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_string_content_repeat1] = {
    .visible = false,
    .named = false,
  },
};

static const TSSymbol ts_alias_sequences[PRODUCTION_ID_COUNT][MAX_ALIAS_SEQUENCE_LENGTH] = {
  [0] = {0},
};

static const uint16_t ts_non_terminal_alias_map[] = {
  0,
};

static const TSStateId ts_primary_state_ids[STATE_COUNT] = {
  [0] = 0,
  [1] = 1,
  [2] = 2,
  [3] = 3,
  [4] = 4,
  [5] = 5,
  [6] = 2,
  [7] = 7,
  [8] = 8,
  [9] = 9,
  [10] = 10,
  [11] = 11,
  [12] = 3,
  [13] = 13,
  [14] = 8,
  [15] = 15,
  [16] = 16,
  [17] = 17,
  [18] = 18,
  [19] = 19,
  [20] = 20,
  [21] = 4,
  [22] = 5,
  [23] = 23,
  [24] = 2,
  [25] = 25,
  [26] = 26,
  [27] = 27,
  [28] = 28,
  [29] = 29,
  [30] = 30,
  [31] = 31,
  [32] = 32,
  [33] = 33,
  [34] = 34,
  [35] = 35,
  [36] = 36,
  [37] = 37,
  [38] = 38,
  [39] = 39,
  [40] = 40,
  [41] = 41,
  [42] = 42,
  [43] = 43,
  [44] = 8,
  [45] = 45,
  [46] = 46,
  [47] = 47,
  [48] = 48,
  [49] = 7,
  [50] = 50,
  [51] = 51,
  [52] = 52,
  [53] = 53,
  [54] = 54,
  [55] = 55,
  [56] = 56,
  [57] = 57,
  [58] = 58,
  [59] = 59,
  [60] = 46,
  [61] = 61,
  [62] = 17,
  [63] = 63,
  [64] = 64,
  [65] = 65,
  [66] = 66,
  [67] = 67,
  [68] = 68,
  [69] = 69,
  [70] = 70,
  [71] = 71,
  [72] = 72,
  [73] = 73,
  [74] = 74,
  [75] = 75,
  [76] = 76,
  [77] = 77,
  [78] = 78,
  [79] = 79,
  [80] = 80,
  [81] = 81,
  [82] = 82,
  [83] = 83,
  [84] = 84,
  [85] = 85,
  [86] = 86,
  [87] = 87,
  [88] = 87,
  [89] = 87,
  [90] = 90,
  [91] = 91,
  [92] = 92,
  [93] = 93,
  [94] = 94,
  [95] = 95,
  [96] = 92,
  [97] = 97,
  [98] = 98,
  [99] = 99,
  [100] = 100,
  [101] = 101,
  [102] = 97,
  [103] = 103,
  [104] = 104,
  [105] = 105,
  [106] = 106,
  [107] = 107,
  [108] = 108,
  [109] = 109,
  [110] = 110,
  [111] = 111,
  [112] = 112,
  [113] = 113,
  [114] = 114,
  [115] = 115,
  [116] = 116,
  [117] = 117,
  [118] = 118,
  [119] = 119,
  [120] = 120,
  [121] = 121,
  [122] = 122,
  [123] = 123,
  [124] = 124,
  [125] = 125,
  [126] = 126,
  [127] = 127,
  [128] = 128,
  [129] = 129,
  [130] = 130,
  [131] = 131,
  [132] = 132,
  [133] = 133,
  [134] = 134,
  [135] = 135,
  [136] = 136,
  [137] = 137,
  [138] = 138,
  [139] = 139,
  [140] = 140,
  [141] = 141,
  [142] = 142,
  [143] = 143,
  [144] = 144,
  [145] = 145,
  [146] = 145,
  [147] = 147,
  [148] = 148,
  [149] = 149,
  [150] = 150,
};

static bool ts_lex(TSLexer *lexer, TSStateId state) {
  START_LEXER();
  eof = lexer->eof(lexer);
  switch (state) {
    case 0:
      if (eof) ADVANCE(267);
      if (lookahead == '\n') ADVANCE(611);
      if (lookahead == '"') ADVANCE(441);
      if (lookahead == '(') ADVANCE(462);
      if (lookahead == ')') ADVANCE(463);
      if (lookahead == '*') ADVANCE(449);
      if (lookahead == '+') ADVANCE(447);
      if (lookahead == ',') ADVANCE(389);
      if (lookahead == '-') ADVANCE(448);
      if (lookahead == '/') ADVANCE(450);
      if (lookahead == '=') ADVANCE(390);
      if (lookahead == '[') ADVANCE(445);
      if (lookahead == '\\') ADVANCE(253);
      if (lookahead == ']') ADVANCE(446);
      if (lookahead == 'a') ADVANCE(493);
      if (lookahead == 'b') ADVANCE(503);
      if (lookahead == 'c') ADVANCE(485);
      if (lookahead == 'd') ADVANCE(504);
      if (lookahead == 'e') ADVANCE(554);
      if (lookahead == 'f') ADVANCE(545);
      if (lookahead == 'i') ADVANCE(526);
      if (lookahead == 'l') ADVANCE(505);
      if (lookahead == 'n') ADVANCE(565);
      if (lookahead == 'o') ADVANCE(595);
      if (lookahead == 'r') ADVANCE(506);
      if (lookahead == 's') ADVANCE(518);
      if (lookahead == 't') ADVANCE(535);
      if (lookahead == 'w') ADVANCE(536);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(0)
      if (('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('g' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 1:
      if (lookahead == ' ') ADVANCE(3);
      if (lookahead != 0) ADVANCE(371);
      END_STATE();
    case 2:
      if (lookahead == ' ') ADVANCE(61);
      END_STATE();
    case 3:
      if (lookahead == ' ') ADVANCE(141);
      if (lookahead == 'n') ADVANCE(167);
      END_STATE();
    case 4:
      if (lookahead == ' ') ADVANCE(47);
      if (lookahead == ':') ADVANCE(272);
      END_STATE();
    case 5:
      if (lookahead == ' ') ADVANCE(50);
      END_STATE();
    case 6:
      if (lookahead == ' ') ADVANCE(183);
      END_STATE();
    case 7:
      if (lookahead == ' ') ADVANCE(89);
      END_STATE();
    case 8:
      if (lookahead == ' ') ADVANCE(217);
      END_STATE();
    case 9:
      if (lookahead == ' ') ADVANCE(155);
      END_STATE();
    case 10:
      if (lookahead == ' ') ADVANCE(221);
      END_STATE();
    case 11:
      if (lookahead == ' ') ADVANCE(112);
      END_STATE();
    case 12:
      if (lookahead == ' ') ADVANCE(222);
      END_STATE();
    case 13:
      if (lookahead == ' ') ADVANCE(225);
      END_STATE();
    case 14:
      if (lookahead == ' ') ADVANCE(228);
      END_STATE();
    case 15:
      if (lookahead == ' ') ADVANCE(229);
      END_STATE();
    case 16:
      if (lookahead == ' ') ADVANCE(231);
      END_STATE();
    case 17:
      if (lookahead == ' ') ADVANCE(90);
      END_STATE();
    case 18:
      if (lookahead == ' ') ADVANCE(91);
      END_STATE();
    case 19:
      if (lookahead == '"') ADVANCE(441);
      if (lookahead == '(') ADVANCE(462);
      if (lookahead == '-') ADVANCE(254);
      if (lookahead == '[') ADVANCE(445);
      if (lookahead == ']') ADVANCE(446);
      if (lookahead == 'c') ADVANCE(485);
      if (lookahead == 'l') ADVANCE(505);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(19)
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(439);
      if (('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 20:
      if (lookahead == '"') ADVANCE(441);
      if (lookahead == '\\') ADVANCE(253);
      if (lookahead == '\t' ||
          lookahead == ' ') ADVANCE(442);
      if (lookahead != 0) ADVANCE(443);
      END_STATE();
    case 21:
      if (lookahead == ')') ADVANCE(463);
      if (lookahead == '*') ADVANCE(449);
      if (lookahead == '+') ADVANCE(447);
      if (lookahead == '-') ADVANCE(448);
      if (lookahead == '/') ADVANCE(450);
      if (lookahead == '[') ADVANCE(445);
      if (lookahead == ']') ADVANCE(446);
      if (lookahead == 'a') ADVANCE(499);
      if (lookahead == 'e') ADVANCE(562);
      if (lookahead == 'i') ADVANCE(582);
      if (lookahead == 's') ADVANCE(601);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(21)
      if (('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('b' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 22:
      if (lookahead == ':') ADVANCE(268);
      END_STATE();
    case 23:
      if (lookahead == ':') ADVANCE(382);
      END_STATE();
    case 24:
      if (lookahead == ':') ADVANCE(380);
      END_STATE();
    case 25:
      if (lookahead == ':') ADVANCE(384);
      END_STATE();
    case 26:
      if (lookahead == ':') ADVANCE(428);
      END_STATE();
    case 27:
      if (lookahead == ':') ADVANCE(270);
      END_STATE();
    case 28:
      if (lookahead == ':') ADVANCE(387);
      END_STATE();
    case 29:
      if (lookahead == ':') ADVANCE(388);
      END_STATE();
    case 30:
      if (lookahead == ':') ADVANCE(378);
      END_STATE();
    case 31:
      if (lookahead == ':') ADVANCE(386);
      END_STATE();
    case 32:
      if (lookahead == ':') ADVANCE(361);
      END_STATE();
    case 33:
      if (lookahead == ':') ADVANCE(431);
      END_STATE();
    case 34:
      if (lookahead == ':') ADVANCE(430);
      END_STATE();
    case 35:
      if (lookahead == 'a') ADVANCE(251);
      END_STATE();
    case 36:
      if (lookahead == 'a') ADVANCE(48);
      END_STATE();
    case 37:
      if (lookahead == 'a') ADVANCE(122);
      END_STATE();
    case 38:
      if (lookahead == 'a') ADVANCE(142);
      END_STATE();
    case 39:
      if (lookahead == 'a') ADVANCE(220);
      END_STATE();
    case 40:
      if (lookahead == 'a') ADVANCE(128);
      END_STATE();
    case 41:
      if (lookahead == 'a') ADVANCE(143);
      END_STATE();
    case 42:
      if (lookahead == 'a') ADVANCE(212);
      END_STATE();
    case 43:
      if (lookahead == 'a') ADVANCE(189);
      END_STATE();
    case 44:
      if (lookahead == 'a') ADVANCE(133);
      END_STATE();
    case 45:
      if (lookahead == 'a') ADVANCE(134);
      END_STATE();
    case 46:
      if (lookahead == 'a') ADVANCE(135);
      END_STATE();
    case 47:
      if (lookahead == 'b') ADVANCE(125);
      END_STATE();
    case 48:
      if (lookahead == 'c') ADVANCE(100);
      END_STATE();
    case 49:
      if (lookahead == 'c') ADVANCE(120);
      END_STATE();
    case 50:
      if (lookahead == 'c') ADVANCE(166);
      END_STATE();
    case 51:
      if (lookahead == 'c') ADVANCE(54);
      END_STATE();
    case 52:
      if (lookahead == 'c') ADVANCE(126);
      END_STATE();
    case 53:
      if (lookahead == 'c') ADVANCE(223);
      END_STATE();
    case 54:
      if (lookahead == 'c') ADVANCE(85);
      END_STATE();
    case 55:
      if (lookahead == 'd') ADVANCE(56);
      if (lookahead == 't') ADVANCE(224);
      END_STATE();
    case 56:
      if (lookahead == 'd') ADVANCE(432);
      END_STATE();
    case 57:
      if (lookahead == 'd') ADVANCE(1);
      if (lookahead != 0) ADVANCE(369);
      END_STATE();
    case 58:
      if (lookahead == 'd') ADVANCE(9);
      END_STATE();
    case 59:
      if (lookahead == 'd') ADVANCE(116);
      END_STATE();
    case 60:
      if (lookahead == 'e') ADVANCE(179);
      if (lookahead == 'g') ADVANCE(190);
      if (lookahead == 'i') ADVANCE(140);
      if (lookahead == 'l') ADVANCE(70);
      if (lookahead == 'n') ADVANCE(156);
      END_STATE();
    case 61:
      if (lookahead == 'e') ADVANCE(36);
      END_STATE();
    case 62:
      if (lookahead == 'e') ADVANCE(363);
      END_STATE();
    case 63:
      if (lookahead == 'e') ADVANCE(137);
      if (lookahead == 'i') ADVANCE(203);
      END_STATE();
    case 64:
      if (lookahead == 'e') ADVANCE(136);
      END_STATE();
    case 65:
      if (lookahead == 'e') ADVANCE(4);
      END_STATE();
    case 66:
      if (lookahead == 'e') ADVANCE(425);
      END_STATE();
    case 67:
      if (lookahead == 'e') ADVANCE(436);
      END_STATE();
    case 68:
      if (lookahead == 'e') ADVANCE(418);
      END_STATE();
    case 69:
      if (lookahead == 'e') ADVANCE(148);
      if (lookahead == '\t' ||
          lookahead == ' ') ADVANCE(364);
      if (lookahead != 0) ADVANCE(365);
      END_STATE();
    case 70:
      if (lookahead == 'e') ADVANCE(199);
      END_STATE();
    case 71:
      if (lookahead == 'e') ADVANCE(193);
      END_STATE();
    case 72:
      if (lookahead == 'e') ADVANCE(39);
      END_STATE();
    case 73:
      if (lookahead == 'e') ADVANCE(33);
      END_STATE();
    case 74:
      if (lookahead == 'e') ADVANCE(175);
      END_STATE();
    case 75:
      if (lookahead == 'e') ADVANCE(175);
      if (lookahead == 'o') ADVANCE(192);
      END_STATE();
    case 76:
      if (lookahead == 'e') ADVANCE(52);
      if (lookahead == 'i') ADVANCE(197);
      if (lookahead == 'o') ADVANCE(22);
      END_STATE();
    case 77:
      if (lookahead == 'e') ADVANCE(53);
      END_STATE();
    case 78:
      if (lookahead == 'e') ADVANCE(154);
      END_STATE();
    case 79:
      if (lookahead == 'e') ADVANCE(191);
      END_STATE();
    case 80:
      if (lookahead == 'e') ADVANCE(27);
      END_STATE();
    case 81:
      if (lookahead == 'e') ADVANCE(209);
      if (lookahead == 't') ADVANCE(75);
      END_STATE();
    case 82:
      if (lookahead == 'e') ADVANCE(209);
      if (lookahead == 't') ADVANCE(74);
      END_STATE();
    case 83:
      if (lookahead == 'e') ADVANCE(201);
      END_STATE();
    case 84:
      if (lookahead == 'e') ADVANCE(132);
      if (lookahead == 'u') ADVANCE(111);
      END_STATE();
    case 85:
      if (lookahead == 'e') ADVANCE(202);
      END_STATE();
    case 86:
      if (lookahead == 'e') ADVANCE(42);
      END_STATE();
    case 87:
      if (lookahead == 'e') ADVANCE(186);
      END_STATE();
    case 88:
      if (lookahead == 'e') ADVANCE(138);
      if (lookahead == 'i') ADVANCE(203);
      END_STATE();
    case 89:
      if (lookahead == 'e') ADVANCE(180);
      END_STATE();
    case 90:
      if (lookahead == 'e') ADVANCE(181);
      END_STATE();
    case 91:
      if (lookahead == 'e') ADVANCE(182);
      END_STATE();
    case 92:
      if (lookahead == 'f') ADVANCE(461);
      END_STATE();
    case 93:
      if (lookahead == 'f') ADVANCE(417);
      END_STATE();
    case 94:
      if (lookahead == 'f') ADVANCE(412);
      if (lookahead == 'n') ADVANCE(176);
      END_STATE();
    case 95:
      if (lookahead == 'f') ADVANCE(413);
      if (lookahead == 'n') ADVANCE(176);
      END_STATE();
    case 96:
      if (lookahead == 'f') ADVANCE(237);
      END_STATE();
    case 97:
      if (lookahead == 'g') ADVANCE(206);
      END_STATE();
    case 98:
      if (lookahead == 'g') ADVANCE(6);
      END_STATE();
    case 99:
      if (lookahead == 'g') ADVANCE(30);
      END_STATE();
    case 100:
      if (lookahead == 'h') ADVANCE(423);
      END_STATE();
    case 101:
      if (lookahead == 'h') ADVANCE(459);
      END_STATE();
    case 102:
      if (lookahead == 'h') ADVANCE(458);
      END_STATE();
    case 103:
      if (lookahead == 'h') ADVANCE(38);
      END_STATE();
    case 104:
      if (lookahead == 'h') ADVANCE(78);
      END_STATE();
    case 105:
      if (lookahead == 'h') ADVANCE(79);
      END_STATE();
    case 106:
      if (lookahead == 'h') ADVANCE(41);
      END_STATE();
    case 107:
      if (lookahead == 'h') ADVANCE(114);
      END_STATE();
    case 108:
      if (lookahead == 'i') ADVANCE(93);
      END_STATE();
    case 109:
      if (lookahead == 'i') ADVANCE(152);
      END_STATE();
    case 110:
      if (lookahead == 'i') ADVANCE(214);
      END_STATE();
    case 111:
      if (lookahead == 'i') ADVANCE(123);
      END_STATE();
    case 112:
      if (lookahead == 'i') ADVANCE(144);
      END_STATE();
    case 113:
      if (lookahead == 'i') ADVANCE(219);
      END_STATE();
    case 114:
      if (lookahead == 'i') ADVANCE(130);
      END_STATE();
    case 115:
      if (lookahead == 'i') ADVANCE(146);
      END_STATE();
    case 116:
      if (lookahead == 'i') ADVANCE(150);
      END_STATE();
    case 117:
      if (lookahead == 'i') ADVANCE(210);
      END_STATE();
    case 118:
      if (lookahead == 'i') ADVANCE(210);
      if (lookahead == 'p') ADVANCE(77);
      END_STATE();
    case 119:
      if (lookahead == 'i') ADVANCE(205);
      END_STATE();
    case 120:
      if (lookahead == 'k') ADVANCE(32);
      END_STATE();
    case 121:
      if (lookahead == 'l') ADVANCE(394);
      END_STATE();
    case 122:
      if (lookahead == 'l') ADVANCE(12);
      END_STATE();
    case 123:
      if (lookahead == 'l') ADVANCE(59);
      END_STATE();
    case 124:
      if (lookahead == 'l') ADVANCE(34);
      END_STATE();
    case 125:
      if (lookahead == 'l') ADVANCE(169);
      END_STATE();
    case 126:
      if (lookahead == 'l') ADVANCE(43);
      END_STATE();
    case 127:
      if (lookahead == 'l') ADVANCE(35);
      END_STATE();
    case 128:
      if (lookahead == 'l') ADVANCE(121);
      END_STATE();
    case 129:
      if (lookahead == 'l') ADVANCE(173);
      if (lookahead == 'o') ADVANCE(184);
      END_STATE();
    case 130:
      if (lookahead == 'l') ADVANCE(66);
      END_STATE();
    case 131:
      if (lookahead == 'l') ADVANCE(218);
      END_STATE();
    case 132:
      if (lookahead == 'l') ADVANCE(172);
      END_STATE();
    case 133:
      if (lookahead == 'l') ADVANCE(13);
      END_STATE();
    case 134:
      if (lookahead == 'l') ADVANCE(14);
      END_STATE();
    case 135:
      if (lookahead == 'l') ADVANCE(15);
      END_STATE();
    case 136:
      if (lookahead == 'm') ADVANCE(178);
      END_STATE();
    case 137:
      if (lookahead == 'm') ADVANCE(165);
      if (lookahead == 'p') ADVANCE(86);
      if (lookahead == 't') ADVANCE(239);
      END_STATE();
    case 138:
      if (lookahead == 'm') ADVANCE(165);
      if (lookahead == 'p') ADVANCE(86);
      if (lookahead == 't') ADVANCE(241);
      END_STATE();
    case 139:
      if (lookahead == 'n') ADVANCE(198);
      END_STATE();
    case 140:
      if (lookahead == 'n') ADVANCE(460);
      END_STATE();
    case 141:
      if (lookahead == 'n') ADVANCE(157);
      if (lookahead != 0) ADVANCE(374);
      END_STATE();
    case 142:
      if (lookahead == 'n') ADVANCE(453);
      END_STATE();
    case 143:
      if (lookahead == 'n') ADVANCE(454);
      END_STATE();
    case 144:
      if (lookahead == 'n') ADVANCE(397);
      END_STATE();
    case 145:
      if (lookahead == 'n') ADVANCE(404);
      END_STATE();
    case 146:
      if (lookahead == 'n') ADVANCE(98);
      END_STATE();
    case 147:
      if (lookahead == 'n') ADVANCE(406);
      END_STATE();
    case 148:
      if (lookahead == 'n') ADVANCE(57);
      if (lookahead != 0) ADVANCE(366);
      END_STATE();
    case 149:
      if (lookahead == 'n') ADVANCE(58);
      if (lookahead == 'x') ADVANCE(117);
      END_STATE();
    case 150:
      if (lookahead == 'n') ADVANCE(99);
      END_STATE();
    case 151:
      if (lookahead == 'n') ADVANCE(97);
      END_STATE();
    case 152:
      if (lookahead == 'n') ADVANCE(238);
      END_STATE();
    case 153:
      if (lookahead == 'n') ADVANCE(213);
      END_STATE();
    case 154:
      if (lookahead == 'n') ADVANCE(5);
      END_STATE();
    case 155:
      if (lookahead == 'n') ADVANCE(167);
      END_STATE();
    case 156:
      if (lookahead == 'o') ADVANCE(207);
      END_STATE();
    case 157:
      if (lookahead == 'o') ADVANCE(208);
      if (lookahead != 0) ADVANCE(375);
      END_STATE();
    case 158:
      if (lookahead == 'o') ADVANCE(457);
      END_STATE();
    case 159:
      if (lookahead == 'o') ADVANCE(92);
      END_STATE();
    case 160:
      if (lookahead == 'o') ADVANCE(31);
      END_STATE();
    case 161:
      if (lookahead == 'o') ADVANCE(451);
      END_STATE();
    case 162:
      if (lookahead == 'o') ADVANCE(452);
      END_STATE();
    case 163:
      if (lookahead == 'o') ADVANCE(455);
      END_STATE();
    case 164:
      if (lookahead == 'o') ADVANCE(456);
      END_STATE();
    case 165:
      if (lookahead == 'o') ADVANCE(245);
      END_STATE();
    case 166:
      if (lookahead == 'o') ADVANCE(153);
      END_STATE();
    case 167:
      if (lookahead == 'o') ADVANCE(215);
      END_STATE();
    case 168:
      if (lookahead == 'o') ADVANCE(194);
      END_STATE();
    case 169:
      if (lookahead == 'o') ADVANCE(49);
      END_STATE();
    case 170:
      if (lookahead == 'o') ADVANCE(185);
      END_STATE();
    case 171:
      if (lookahead == 'o') ADVANCE(227);
      END_STATE();
    case 172:
      if (lookahead == 'o') ADVANCE(151);
      END_STATE();
    case 173:
      if (lookahead == 'o') ADVANCE(170);
      END_STATE();
    case 174:
      if (lookahead == 'o') ADVANCE(195);
      END_STATE();
    case 175:
      if (lookahead == 'p') ADVANCE(23);
      END_STATE();
    case 176:
      if (lookahead == 'p') ADVANCE(240);
      END_STATE();
    case 177:
      if (lookahead == 'p') ADVANCE(127);
      END_STATE();
    case 178:
      if (lookahead == 'p') ADVANCE(226);
      END_STATE();
    case 179:
      if (lookahead == 'q') ADVANCE(233);
      END_STATE();
    case 180:
      if (lookahead == 'q') ADVANCE(242);
      END_STATE();
    case 181:
      if (lookahead == 'q') ADVANCE(243);
      END_STATE();
    case 182:
      if (lookahead == 'q') ADVANCE(244);
      END_STATE();
    case 183:
      if (lookahead == 'r') ADVANCE(83);
      END_STATE();
    case 184:
      if (lookahead == 'r') ADVANCE(2);
      END_STATE();
    case 185:
      if (lookahead == 'r') ADVANCE(24);
      END_STATE();
    case 186:
      if (lookahead == 'r') ADVANCE(25);
      END_STATE();
    case 187:
      if (lookahead == 'r') ADVANCE(145);
      END_STATE();
    case 188:
      if (lookahead == 'r') ADVANCE(147);
      END_STATE();
    case 189:
      if (lookahead == 'r') ADVANCE(80);
      END_STATE();
    case 190:
      if (lookahead == 'r') ADVANCE(72);
      END_STATE();
    case 191:
      if (lookahead == 'r') ADVANCE(247);
      END_STATE();
    case 192:
      if (lookahead == 'r') ADVANCE(115);
      END_STATE();
    case 193:
      if (lookahead == 'r') ADVANCE(16);
      END_STATE();
    case 194:
      if (lookahead == 'r') ADVANCE(17);
      END_STATE();
    case 195:
      if (lookahead == 'r') ADVANCE(18);
      END_STATE();
    case 196:
      if (lookahead == 's') ADVANCE(8);
      END_STATE();
    case 197:
      if (lookahead == 's') ADVANCE(177);
      END_STATE();
    case 198:
      if (lookahead == 's') ADVANCE(234);
      END_STATE();
    case 199:
      if (lookahead == 's') ADVANCE(196);
      END_STATE();
    case 200:
      if (lookahead == 's') ADVANCE(96);
      END_STATE();
    case 201:
      if (lookahead == 's') ADVANCE(235);
      END_STATE();
    case 202:
      if (lookahead == 's') ADVANCE(200);
      END_STATE();
    case 203:
      if (lookahead == 's') ADVANCE(87);
      END_STATE();
    case 204:
      if (lookahead == 's') ADVANCE(28);
      END_STATE();
    case 205:
      if (lookahead == 's') ADVANCE(68);
      END_STATE();
    case 206:
      if (lookahead == 's') ADVANCE(10);
      END_STATE();
    case 207:
      if (lookahead == 't') ADVANCE(7);
      END_STATE();
    case 208:
      if (lookahead == 't') ADVANCE(256);
      if (lookahead != 0) ADVANCE(376);
      END_STATE();
    case 209:
      if (lookahead == 't') ADVANCE(391);
      END_STATE();
    case 210:
      if (lookahead == 't') ADVANCE(409);
      END_STATE();
    case 211:
      if (lookahead == 't') ADVANCE(401);
      END_STATE();
    case 212:
      if (lookahead == 't') ADVANCE(420);
      END_STATE();
    case 213:
      if (lookahead == 't') ADVANCE(109);
      END_STATE();
    case 214:
      if (lookahead == 't') ADVANCE(101);
      END_STATE();
    case 215:
      if (lookahead == 't') ADVANCE(62);
      END_STATE();
    case 216:
      if (lookahead == 't') ADVANCE(158);
      END_STATE();
    case 217:
      if (lookahead == 't') ADVANCE(103);
      END_STATE();
    case 218:
      if (lookahead == 't') ADVANCE(11);
      END_STATE();
    case 219:
      if (lookahead == 't') ADVANCE(102);
      END_STATE();
    case 220:
      if (lookahead == 't') ADVANCE(71);
      END_STATE();
    case 221:
      if (lookahead == 't') ADVANCE(160);
      END_STATE();
    case 222:
      if (lookahead == 't') ADVANCE(161);
      END_STATE();
    case 223:
      if (lookahead == 't') ADVANCE(204);
      END_STATE();
    case 224:
      if (lookahead == 't') ADVANCE(64);
      END_STATE();
    case 225:
      if (lookahead == 't') ADVANCE(162);
      END_STATE();
    case 226:
      if (lookahead == 't') ADVANCE(26);
      END_STATE();
    case 227:
      if (lookahead == 't') ADVANCE(65);
      END_STATE();
    case 228:
      if (lookahead == 't') ADVANCE(163);
      END_STATE();
    case 229:
      if (lookahead == 't') ADVANCE(164);
      END_STATE();
    case 230:
      if (lookahead == 't') ADVANCE(105);
      END_STATE();
    case 231:
      if (lookahead == 't') ADVANCE(106);
      END_STATE();
    case 232:
      if (lookahead == 'u') ADVANCE(139);
      END_STATE();
    case 233:
      if (lookahead == 'u') ADVANCE(37);
      END_STATE();
    case 234:
      if (lookahead == 'u') ADVANCE(51);
      END_STATE();
    case 235:
      if (lookahead == 'u') ADVANCE(131);
      END_STATE();
    case 236:
      if (lookahead == 'u') ADVANCE(111);
      END_STATE();
    case 237:
      if (lookahead == 'u') ADVANCE(124);
      END_STATE();
    case 238:
      if (lookahead == 'u') ADVANCE(73);
      END_STATE();
    case 239:
      if (lookahead == 'u') ADVANCE(187);
      END_STATE();
    case 240:
      if (lookahead == 'u') ADVANCE(211);
      END_STATE();
    case 241:
      if (lookahead == 'u') ADVANCE(188);
      END_STATE();
    case 242:
      if (lookahead == 'u') ADVANCE(44);
      END_STATE();
    case 243:
      if (lookahead == 'u') ADVANCE(45);
      END_STATE();
    case 244:
      if (lookahead == 'u') ADVANCE(46);
      END_STATE();
    case 245:
      if (lookahead == 'v') ADVANCE(67);
      END_STATE();
    case 246:
      if (lookahead == 'w') ADVANCE(110);
      END_STATE();
    case 247:
      if (lookahead == 'w') ADVANCE(119);
      END_STATE();
    case 248:
      if (lookahead == 'w') ADVANCE(113);
      END_STATE();
    case 249:
      if (lookahead == 'x') ADVANCE(118);
      END_STATE();
    case 250:
      if (lookahead == 'x') ADVANCE(117);
      END_STATE();
    case 251:
      if (lookahead == 'y') ADVANCE(398);
      END_STATE();
    case 252:
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(252)
      if (('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 253:
      if (lookahead == '"' ||
          lookahead == '\\' ||
          lookahead == 'n' ||
          lookahead == 'r' ||
          lookahead == 't') ADVANCE(444);
      END_STATE();
    case 254:
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(439);
      END_STATE();
    case 255:
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(440);
      END_STATE();
    case 256:
      if (lookahead != 0 &&
          lookahead != 'e') ADVANCE(377);
      END_STATE();
    case 257:
      if (eof) ADVANCE(267);
      if (lookahead == '\n') ADVANCE(611);
      if (lookahead == '"') ADVANCE(441);
      if (lookahead == '(') ADVANCE(462);
      if (lookahead == '-') ADVANCE(254);
      if (lookahead == '[') ADVANCE(445);
      if (lookahead == 'a') ADVANCE(498);
      if (lookahead == 'b') ADVANCE(602);
      if (lookahead == 'c') ADVANCE(485);
      if (lookahead == 'd') ADVANCE(504);
      if (lookahead == 'e') ADVANCE(608);
      if (lookahead == 'f') ADVANCE(545);
      if (lookahead == 'i') ADVANCE(528);
      if (lookahead == 'l') ADVANCE(505);
      if (lookahead == 'n') ADVANCE(565);
      if (lookahead == 'r') ADVANCE(525);
      if (lookahead == 's') ADVANCE(521);
      if (lookahead == 'w') ADVANCE(536);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(257)
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(439);
      if (('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('g' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 258:
      if (eof) ADVANCE(267);
      if (lookahead == '\n') ADVANCE(611);
      if (lookahead == ')') ADVANCE(463);
      if (lookahead == '*') ADVANCE(449);
      if (lookahead == '+') ADVANCE(447);
      if (lookahead == ',') ADVANCE(389);
      if (lookahead == '-') ADVANCE(448);
      if (lookahead == '/') ADVANCE(450);
      if (lookahead == '[') ADVANCE(445);
      if (lookahead == ']') ADVANCE(446);
      if (lookahead == 'a') ADVANCE(493);
      if (lookahead == 'b') ADVANCE(602);
      if (lookahead == 'c') ADVANCE(485);
      if (lookahead == 'd') ADVANCE(504);
      if (lookahead == 'e') ADVANCE(561);
      if (lookahead == 'f') ADVANCE(545);
      if (lookahead == 'i') ADVANCE(527);
      if (lookahead == 'n') ADVANCE(565);
      if (lookahead == 'o') ADVANCE(595);
      if (lookahead == 'r') ADVANCE(525);
      if (lookahead == 's') ADVANCE(518);
      if (lookahead == 'w') ADVANCE(536);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(258)
      if (('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('g' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 259:
      if (eof) ADVANCE(267);
      if (lookahead == '\n') ADVANCE(611);
      if (lookahead == ')') ADVANCE(463);
      if (lookahead == '*') ADVANCE(449);
      if (lookahead == '+') ADVANCE(447);
      if (lookahead == ',') ADVANCE(389);
      if (lookahead == '-') ADVANCE(448);
      if (lookahead == '/') ADVANCE(450);
      if (lookahead == '[') ADVANCE(445);
      if (lookahead == ']') ADVANCE(446);
      if (lookahead == 'a') ADVANCE(493);
      if (lookahead == 'b') ADVANCE(602);
      if (lookahead == 'c') ADVANCE(485);
      if (lookahead == 'd') ADVANCE(504);
      if (lookahead == 'e') ADVANCE(561);
      if (lookahead == 'f') ADVANCE(545);
      if (lookahead == 'i') ADVANCE(527);
      if (lookahead == 'n') ADVANCE(565);
      if (lookahead == 'o') ADVANCE(595);
      if (lookahead == 'r') ADVANCE(525);
      if (lookahead == 's') ADVANCE(519);
      if (lookahead == 'w') ADVANCE(536);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(259)
      if (('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('g' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 260:
      if (eof) ADVANCE(267);
      if (lookahead == '\n') ADVANCE(611);
      if (lookahead == '*') ADVANCE(449);
      if (lookahead == '+') ADVANCE(447);
      if (lookahead == ',') ADVANCE(389);
      if (lookahead == '-') ADVANCE(448);
      if (lookahead == '/') ADVANCE(450);
      if (lookahead == '[') ADVANCE(445);
      if (lookahead == ']') ADVANCE(446);
      if (lookahead == 'a') ADVANCE(493);
      if (lookahead == 'b') ADVANCE(602);
      if (lookahead == 'c') ADVANCE(485);
      if (lookahead == 'd') ADVANCE(504);
      if (lookahead == 'e') ADVANCE(561);
      if (lookahead == 'f') ADVANCE(545);
      if (lookahead == 'i') ADVANCE(527);
      if (lookahead == 'n') ADVANCE(565);
      if (lookahead == 'r') ADVANCE(525);
      if (lookahead == 's') ADVANCE(518);
      if (lookahead == 'w') ADVANCE(536);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(260)
      if (('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('g' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 261:
      if (eof) ADVANCE(267);
      if (lookahead == '\n') ADVANCE(611);
      if (lookahead == '*') ADVANCE(449);
      if (lookahead == '+') ADVANCE(447);
      if (lookahead == '-') ADVANCE(448);
      if (lookahead == '/') ADVANCE(450);
      if (lookahead == '[') ADVANCE(445);
      if (lookahead == 'a') ADVANCE(493);
      if (lookahead == 'b') ADVANCE(602);
      if (lookahead == 'c') ADVANCE(485);
      if (lookahead == 'd') ADVANCE(504);
      if (lookahead == 'e') ADVANCE(561);
      if (lookahead == 'f') ADVANCE(545);
      if (lookahead == 'i') ADVANCE(527);
      if (lookahead == 'n') ADVANCE(565);
      if (lookahead == 'r') ADVANCE(525);
      if (lookahead == 's') ADVANCE(519);
      if (lookahead == 'w') ADVANCE(536);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(261)
      if (('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('g' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 262:
      if (eof) ADVANCE(267);
      if (lookahead == '\n') ADVANCE(611);
      if (lookahead == ',') ADVANCE(389);
      if (lookahead == '=') ADVANCE(390);
      if (lookahead == ']') ADVANCE(446);
      if (lookahead == 'a') ADVANCE(55);
      if (lookahead == 'b') ADVANCE(236);
      if (lookahead == 'c') ADVANCE(40);
      if (lookahead == 'd') ADVANCE(76);
      if (lookahead == 'e') ADVANCE(149);
      if (lookahead == 'f') ADVANCE(129);
      if (lookahead == 'i') ADVANCE(94);
      if (lookahead == 'n') ADVANCE(171);
      if (lookahead == 'o') ADVANCE(230);
      if (lookahead == 'r') ADVANCE(63);
      if (lookahead == 's') ADVANCE(81);
      if (lookahead == 't') ADVANCE(104);
      if (lookahead == 'w') ADVANCE(107);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(262)
      END_STATE();
    case 263:
      if (eof) ADVANCE(267);
      if (lookahead == '\n') ADVANCE(611);
      if (lookahead == ',') ADVANCE(389);
      if (lookahead == 'a') ADVANCE(55);
      if (lookahead == 'b') ADVANCE(84);
      if (lookahead == 'c') ADVANCE(40);
      if (lookahead == 'd') ADVANCE(76);
      if (lookahead == 'e') ADVANCE(249);
      if (lookahead == 'f') ADVANCE(129);
      if (lookahead == 'i') ADVANCE(94);
      if (lookahead == 'n') ADVANCE(171);
      if (lookahead == 'r') ADVANCE(88);
      if (lookahead == 's') ADVANCE(82);
      if (lookahead == 'w') ADVANCE(107);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(263)
      END_STATE();
    case 264:
      if (eof) ADVANCE(267);
      if (lookahead == '\n') ADVANCE(611);
      if (lookahead == 'a') ADVANCE(55);
      if (lookahead == 'b') ADVANCE(236);
      if (lookahead == 'c') ADVANCE(40);
      if (lookahead == 'd') ADVANCE(76);
      if (lookahead == 'e') ADVANCE(250);
      if (lookahead == 'f') ADVANCE(129);
      if (lookahead == 'i') ADVANCE(95);
      if (lookahead == 'n') ADVANCE(171);
      if (lookahead == 'r') ADVANCE(63);
      if (lookahead == 's') ADVANCE(82);
      if (lookahead == 't') ADVANCE(104);
      if (lookahead == 'w') ADVANCE(107);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(264)
      END_STATE();
    case 265:
      if (eof) ADVANCE(267);
      if (lookahead == '\n') ADVANCE(611);
      if (lookahead == 'a') ADVANCE(498);
      if (lookahead == 'b') ADVANCE(602);
      if (lookahead == 'c') ADVANCE(485);
      if (lookahead == 'd') ADVANCE(504);
      if (lookahead == 'e') ADVANCE(608);
      if (lookahead == 'f') ADVANCE(545);
      if (lookahead == 'i') ADVANCE(528);
      if (lookahead == 'n') ADVANCE(565);
      if (lookahead == 'r') ADVANCE(525);
      if (lookahead == 's') ADVANCE(521);
      if (lookahead == 'w') ADVANCE(536);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(265)
      if (('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('g' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 266:
      if (eof) ADVANCE(267);
      if (lookahead == '\n') ADVANCE(611);
      if (lookahead == 'a') ADVANCE(498);
      if (lookahead == 'b') ADVANCE(602);
      if (lookahead == 'c') ADVANCE(485);
      if (lookahead == 'd') ADVANCE(504);
      if (lookahead == 'e') ADVANCE(608);
      if (lookahead == 'f') ADVANCE(545);
      if (lookahead == 'i') ADVANCE(528);
      if (lookahead == 'n') ADVANCE(565);
      if (lookahead == 'r') ADVANCE(525);
      if (lookahead == 's') ADVANCE(520);
      if (lookahead == 'w') ADVANCE(536);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(266)
      if (('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('g' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 267:
      ACCEPT_TOKEN(ts_builtin_sym_end);
      END_STATE();
    case 268:
      ACCEPT_TOKEN(anon_sym_do_COLON);
      END_STATE();
    case 269:
      ACCEPT_TOKEN(anon_sym_do_COLON);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 270:
      ACCEPT_TOKEN(anon_sym_declare_COLON);
      END_STATE();
    case 271:
      ACCEPT_TOKEN(anon_sym_declare_COLON);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 272:
      ACCEPT_TOKEN(anon_sym_note_COLON);
      END_STATE();
    case 273:
      ACCEPT_TOKEN(anon_sym_note_COLON);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 274:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == ' ') ADVANCE(290);
      if (lookahead == ':') ADVANCE(273);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 275:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == ' ') ADVANCE(306);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 276:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == ':') ADVANCE(269);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 277:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == ':') ADVANCE(383);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 278:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == ':') ADVANCE(381);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 279:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == ':') ADVANCE(385);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 280:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == ':') ADVANCE(429);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 281:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == ':') ADVANCE(271);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 282:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == ':') ADVANCE(379);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 283:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == ':') ADVANCE(362);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 284:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'a') ADVANCE(294);
      if (lookahead == 'b') ADVANCE(353);
      if (lookahead == 'c') ADVANCE(285);
      if (lookahead == 'd') ADVANCE(297);
      if (lookahead == 'e') ADVANCE(357);
      if (lookahead == 'f') ADVANCE(320);
      if (lookahead == 'i') ADVANCE(309);
      if (lookahead == 'n') ADVANCE(334);
      if (lookahead == 'r') ADVANCE(298);
      if (lookahead == 's') ADVANCE(303);
      if (lookahead == 'w') ADVANCE(312);
      if (lookahead == '\t' ||
          lookahead == ' ') ADVANCE(284);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 285:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'a') ADVANCE(322);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 286:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'a') ADVANCE(358);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 287:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'a') ADVANCE(292);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 288:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'a') ADVANCE(343);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 289:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'a') ADVANCE(349);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 290:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'b') ADVANCE(324);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 291:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'c') ADVANCE(317);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 292:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'c') ADVANCE(311);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 293:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'c') ADVANCE(319);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 294:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'd') ADVANCE(295);
      if (lookahead == 't') ADVANCE(350);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 295:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'd') ADVANCE(435);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 296:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'd') ADVANCE(314);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 297:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(293);
      if (lookahead == 'i') ADVANCE(344);
      if (lookahead == 'o') ADVANCE(276);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 298:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(326);
      if (lookahead == 'i') ADVANCE(345);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 299:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(327);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 300:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(274);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 301:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(427);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 302:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(438);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 303:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(346);
      if (lookahead == 't') ADVANCE(305);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 304:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(289);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 305:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(336);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 306:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(287);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 307:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(281);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 308:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'e') ADVANCE(342);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 309:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'f') ADVANCE(416);
      if (lookahead == 'n') ADVANCE(335);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 310:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'g') ADVANCE(282);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 311:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'h') ADVANCE(424);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 312:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'h') ADVANCE(316);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 313:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'i') ADVANCE(321);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 314:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'i') ADVANCE(329);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 315:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'i') ADVANCE(347);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 316:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'i') ADVANCE(325);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 317:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'k') ADVANCE(283);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 318:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'l') ADVANCE(396);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 319:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'l') ADVANCE(288);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 320:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'l') ADVANCE(332);
      if (lookahead == 'o') ADVANCE(339);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 321:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'l') ADVANCE(296);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 322:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'l') ADVANCE(318);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 323:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'l') ADVANCE(286);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 324:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'l') ADVANCE(333);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 325:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'l') ADVANCE(301);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 326:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'm') ADVANCE(330);
      if (lookahead == 'p') ADVANCE(304);
      if (lookahead == 't') ADVANCE(354);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 327:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'm') ADVANCE(337);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 328:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'n') ADVANCE(408);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 329:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'n') ADVANCE(310);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 330:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'o') ADVANCE(356);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 331:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'o') ADVANCE(341);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 332:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'o') ADVANCE(331);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 333:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'o') ADVANCE(291);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 334:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'o') ADVANCE(351);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 335:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'p') ADVANCE(355);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 336:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'p') ADVANCE(277);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 337:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'p') ADVANCE(352);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 338:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'p') ADVANCE(323);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 339:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'r') ADVANCE(275);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 340:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'r') ADVANCE(328);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 341:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'r') ADVANCE(278);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 342:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'r') ADVANCE(279);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 343:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'r') ADVANCE(307);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 344:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 's') ADVANCE(338);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 345:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 's') ADVANCE(308);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 346:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 't') ADVANCE(393);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 347:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 't') ADVANCE(411);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 348:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 't') ADVANCE(403);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 349:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 't') ADVANCE(422);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 350:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 't') ADVANCE(299);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 351:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 't') ADVANCE(300);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 352:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 't') ADVANCE(280);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 353:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'u') ADVANCE(313);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 354:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'u') ADVANCE(340);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 355:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'u') ADVANCE(348);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 356:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'v') ADVANCE(302);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 357:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'x') ADVANCE(315);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 358:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead == 'y') ADVANCE(400);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 359:
      ACCEPT_TOKEN(sym_comment_content);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 360:
      ACCEPT_TOKEN(sym_comment_content);
      if (eof) ADVANCE(267);
      if (lookahead == 'a') ADVANCE(294);
      if (lookahead == 'b') ADVANCE(353);
      if (lookahead == 'c') ADVANCE(285);
      if (lookahead == 'd') ADVANCE(297);
      if (lookahead == 'e') ADVANCE(357);
      if (lookahead == 'f') ADVANCE(320);
      if (lookahead == 'i') ADVANCE(309);
      if (lookahead == 'n') ADVANCE(334);
      if (lookahead == 'r') ADVANCE(298);
      if (lookahead == 's') ADVANCE(303);
      if (lookahead == 'w') ADVANCE(312);
      if (lookahead == '\t' ||
          lookahead == ' ') ADVANCE(284);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 361:
      ACCEPT_TOKEN(anon_sym_noteblock_COLON);
      END_STATE();
    case 362:
      ACCEPT_TOKEN(anon_sym_noteblock_COLON);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 363:
      ACCEPT_TOKEN(anon_sym_endnote);
      END_STATE();
    case 364:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token1);
      if (lookahead == '\t' ||
          lookahead == ' ') ADVANCE(364);
      if (lookahead != 0 &&
          lookahead != 'e') ADVANCE(365);
      END_STATE();
    case 365:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token1);
      if (lookahead != 0 &&
          lookahead != 'e') ADVANCE(365);
      END_STATE();
    case 366:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token2);
      END_STATE();
    case 367:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token2);
      if (lookahead == 'i') ADVANCE(591);
      if (lookahead == 'p') ADVANCE(513);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 368:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token2);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 369:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token3);
      END_STATE();
    case 370:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token3);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 371:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token4);
      END_STATE();
    case 372:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token4);
      if (lookahead == ' ') ADVANCE(246);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 373:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token4);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 374:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token5);
      END_STATE();
    case 375:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token6);
      END_STATE();
    case 376:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token7);
      END_STATE();
    case 377:
      ACCEPT_TOKEN(aux_sym_block_comment_content_token8);
      END_STATE();
    case 378:
      ACCEPT_TOKEN(anon_sym_building_COLON);
      END_STATE();
    case 379:
      ACCEPT_TOKEN(anon_sym_building_COLON);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 380:
      ACCEPT_TOKEN(anon_sym_floor_COLON);
      END_STATE();
    case 381:
      ACCEPT_TOKEN(anon_sym_floor_COLON);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 382:
      ACCEPT_TOKEN(anon_sym_step_COLON);
      END_STATE();
    case 383:
      ACCEPT_TOKEN(anon_sym_step_COLON);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 384:
      ACCEPT_TOKEN(anon_sym_riser_COLON);
      END_STATE();
    case 385:
      ACCEPT_TOKEN(anon_sym_riser_COLON);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 386:
      ACCEPT_TOKEN(anon_sym_belongsto_COLON);
      END_STATE();
    case 387:
      ACCEPT_TOKEN(anon_sym_expects_COLON);
      END_STATE();
    case 388:
      ACCEPT_TOKEN(anon_sym_returns_COLON);
      END_STATE();
    case 389:
      ACCEPT_TOKEN(anon_sym_COMMA);
      END_STATE();
    case 390:
      ACCEPT_TOKEN(anon_sym_EQ);
      END_STATE();
    case 391:
      ACCEPT_TOKEN(anon_sym_set);
      END_STATE();
    case 392:
      ACCEPT_TOKEN(anon_sym_set);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 393:
      ACCEPT_TOKEN(anon_sym_set);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 394:
      ACCEPT_TOKEN(anon_sym_call);
      END_STATE();
    case 395:
      ACCEPT_TOKEN(anon_sym_call);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 396:
      ACCEPT_TOKEN(anon_sym_call);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 397:
      ACCEPT_TOKEN(anon_sym_storingresultin);
      END_STATE();
    case 398:
      ACCEPT_TOKEN(anon_sym_display);
      END_STATE();
    case 399:
      ACCEPT_TOKEN(anon_sym_display);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 400:
      ACCEPT_TOKEN(anon_sym_display);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 401:
      ACCEPT_TOKEN(anon_sym_input);
      END_STATE();
    case 402:
      ACCEPT_TOKEN(anon_sym_input);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 403:
      ACCEPT_TOKEN(anon_sym_input);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 404:
      ACCEPT_TOKEN(anon_sym_return);
      END_STATE();
    case 405:
      ACCEPT_TOKEN(anon_sym_return);
      if (lookahead == 's') ADVANCE(482);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 406:
      ACCEPT_TOKEN(anon_sym_return);
      if (lookahead == 's') ADVANCE(29);
      END_STATE();
    case 407:
      ACCEPT_TOKEN(anon_sym_return);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 408:
      ACCEPT_TOKEN(anon_sym_return);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 409:
      ACCEPT_TOKEN(sym_exit_statement);
      END_STATE();
    case 410:
      ACCEPT_TOKEN(sym_exit_statement);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 411:
      ACCEPT_TOKEN(sym_exit_statement);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 412:
      ACCEPT_TOKEN(anon_sym_if);
      END_STATE();
    case 413:
      ACCEPT_TOKEN(anon_sym_if);
      if (lookahead == ' ') ADVANCE(232);
      END_STATE();
    case 414:
      ACCEPT_TOKEN(anon_sym_if);
      if (lookahead == ' ') ADVANCE(232);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 415:
      ACCEPT_TOKEN(anon_sym_if);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 416:
      ACCEPT_TOKEN(anon_sym_if);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 417:
      ACCEPT_TOKEN(anon_sym_otherwiseif);
      END_STATE();
    case 418:
      ACCEPT_TOKEN(anon_sym_otherwise);
      if (lookahead == ' ') ADVANCE(108);
      END_STATE();
    case 419:
      ACCEPT_TOKEN(anon_sym_otherwise);
      if (lookahead == ' ') ADVANCE(108);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 420:
      ACCEPT_TOKEN(anon_sym_repeat);
      END_STATE();
    case 421:
      ACCEPT_TOKEN(anon_sym_repeat);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 422:
      ACCEPT_TOKEN(anon_sym_repeat);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 423:
      ACCEPT_TOKEN(anon_sym_foreach);
      END_STATE();
    case 424:
      ACCEPT_TOKEN(anon_sym_foreach);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 425:
      ACCEPT_TOKEN(anon_sym_while);
      END_STATE();
    case 426:
      ACCEPT_TOKEN(anon_sym_while);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 427:
      ACCEPT_TOKEN(anon_sym_while);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 428:
      ACCEPT_TOKEN(anon_sym_attempt_COLON);
      END_STATE();
    case 429:
      ACCEPT_TOKEN(anon_sym_attempt_COLON);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 430:
      ACCEPT_TOKEN(anon_sym_ifunsuccessful_COLON);
      END_STATE();
    case 431:
      ACCEPT_TOKEN(anon_sym_thencontinue_COLON);
      END_STATE();
    case 432:
      ACCEPT_TOKEN(anon_sym_add);
      END_STATE();
    case 433:
      ACCEPT_TOKEN(anon_sym_add);
      if (lookahead == 'e') ADVANCE(497);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 434:
      ACCEPT_TOKEN(anon_sym_add);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 435:
      ACCEPT_TOKEN(anon_sym_add);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 436:
      ACCEPT_TOKEN(anon_sym_remove);
      END_STATE();
    case 437:
      ACCEPT_TOKEN(anon_sym_remove);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 438:
      ACCEPT_TOKEN(anon_sym_remove);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(359);
      END_STATE();
    case 439:
      ACCEPT_TOKEN(sym_number);
      if (lookahead == '.') ADVANCE(255);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(439);
      END_STATE();
    case 440:
      ACCEPT_TOKEN(sym_number);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(440);
      END_STATE();
    case 441:
      ACCEPT_TOKEN(anon_sym_DQUOTE);
      END_STATE();
    case 442:
      ACCEPT_TOKEN(aux_sym_string_content_token1);
      if (lookahead == '\t' ||
          lookahead == ' ') ADVANCE(442);
      if (lookahead != 0 &&
          lookahead != '"' &&
          lookahead != '\\') ADVANCE(443);
      END_STATE();
    case 443:
      ACCEPT_TOKEN(aux_sym_string_content_token1);
      if (lookahead != 0 &&
          lookahead != '"' &&
          lookahead != '\\') ADVANCE(443);
      END_STATE();
    case 444:
      ACCEPT_TOKEN(sym_escape_sequence);
      END_STATE();
    case 445:
      ACCEPT_TOKEN(anon_sym_LBRACK);
      END_STATE();
    case 446:
      ACCEPT_TOKEN(anon_sym_RBRACK);
      END_STATE();
    case 447:
      ACCEPT_TOKEN(anon_sym_PLUS);
      END_STATE();
    case 448:
      ACCEPT_TOKEN(anon_sym_DASH);
      END_STATE();
    case 449:
      ACCEPT_TOKEN(anon_sym_STAR);
      END_STATE();
    case 450:
      ACCEPT_TOKEN(anon_sym_SLASH);
      END_STATE();
    case 451:
      ACCEPT_TOKEN(anon_sym_isequalto);
      END_STATE();
    case 452:
      ACCEPT_TOKEN(anon_sym_isnotequalto);
      END_STATE();
    case 453:
      ACCEPT_TOKEN(anon_sym_islessthan);
      if (lookahead == ' ') ADVANCE(168);
      END_STATE();
    case 454:
      ACCEPT_TOKEN(anon_sym_isgreaterthan);
      if (lookahead == ' ') ADVANCE(174);
      END_STATE();
    case 455:
      ACCEPT_TOKEN(anon_sym_islessthanorequalto);
      END_STATE();
    case 456:
      ACCEPT_TOKEN(anon_sym_isgreaterthanorequalto);
      END_STATE();
    case 457:
      ACCEPT_TOKEN(anon_sym_addedto);
      END_STATE();
    case 458:
      ACCEPT_TOKEN(anon_sym_startswith);
      END_STATE();
    case 459:
      ACCEPT_TOKEN(anon_sym_endswith);
      END_STATE();
    case 460:
      ACCEPT_TOKEN(anon_sym_isin);
      END_STATE();
    case 461:
      ACCEPT_TOKEN(anon_sym_lengthof);
      END_STATE();
    case 462:
      ACCEPT_TOKEN(anon_sym_LPAREN);
      END_STATE();
    case 463:
      ACCEPT_TOKEN(anon_sym_RPAREN);
      END_STATE();
    case 464:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ' ') ADVANCE(60);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 465:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ' ') ADVANCE(3);
      if (lookahead == 's') ADVANCE(372);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(373);
      if (lookahead != 0) ADVANCE(371);
      END_STATE();
    case 466:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ' ') ADVANCE(61);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 467:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ' ') ADVANCE(246);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 468:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ' ') ADVANCE(47);
      if (lookahead == ':') ADVANCE(272);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 469:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ' ') ADVANCE(50);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 470:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ' ') ADVANCE(183);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 471:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ' ') ADVANCE(216);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 472:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ' ') ADVANCE(159);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 473:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ' ') ADVANCE(221);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 474:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ' ') ADVANCE(248);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 475:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ':') ADVANCE(268);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 476:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ':') ADVANCE(382);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 477:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ':') ADVANCE(380);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 478:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ':') ADVANCE(384);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 479:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ':') ADVANCE(428);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 480:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ':') ADVANCE(270);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 481:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ':') ADVANCE(387);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 482:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ':') ADVANCE(388);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 483:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == ':') ADVANCE(378);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 484:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'a') ADVANCE(609);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('b' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 485:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'a') ADVANCE(549);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('b' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 486:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'a') ADVANCE(580);
      if (lookahead == 'e') ADVANCE(569);
      if (lookahead == 'o') ADVANCE(574);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('b' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 487:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'a') ADVANCE(580);
      if (lookahead == 'e') ADVANCE(569);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('b' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 488:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'a') ADVANCE(580);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('b' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 489:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'a') ADVANCE(592);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('b' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 490:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'a') ADVANCE(581);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('b' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 491:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'c') ADVANCE(544);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 492:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'c') ADVANCE(599);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 493:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'd') ADVANCE(494);
      if (lookahead == 't') ADVANCE(594);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 494:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'd') ADVANCE(433);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 495:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'd') ADVANCE(465);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(370);
      if (lookahead != 0) ADVANCE(369);
      END_STATE();
    case 496:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'd') ADVANCE(434);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 497:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'd') ADVANCE(471);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 498:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'd') ADVANCE(496);
      if (lookahead == 't') ADVANCE(594);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 499:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'd') ADVANCE(500);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 500:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'd') ADVANCE(512);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 501:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'd') ADVANCE(542);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 502:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'd') ADVANCE(589);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 503:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(546);
      if (lookahead == 'u') ADVANCE(537);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 504:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(491);
      if (lookahead == 'i') ADVANCE(583);
      if (lookahead == 'o') ADVANCE(475);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 505:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(555);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 506:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(552);
      if (lookahead == 'i') ADVANCE(588);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 507:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(551);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 508:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(468);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 509:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(426);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 510:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(437);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 511:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(419);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 512:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(497);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 513:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(492);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 514:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(559);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 515:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(569);
      if (lookahead == 'o') ADVANCE(574);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 516:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(569);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 517:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(489);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 518:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(590);
      if (lookahead == 't') ADVANCE(486);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 519:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(590);
      if (lookahead == 't') ADVANCE(487);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 520:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(590);
      if (lookahead == 't') ADVANCE(515);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 521:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(590);
      if (lookahead == 't') ADVANCE(516);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 522:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(573);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 523:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(480);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 524:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(578);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 525:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'e') ADVANCE(553);
      if (lookahead == 'i') ADVANCE(588);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 526:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'f') ADVANCE(414);
      if (lookahead == 's') ADVANCE(464);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 527:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'f') ADVANCE(415);
      if (lookahead == 'n') ADVANCE(570);
      if (lookahead == 's') ADVANCE(464);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 528:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'f') ADVANCE(415);
      if (lookahead == 'n') ADVANCE(570);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 529:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'g') ADVANCE(470);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 530:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'g') ADVANCE(483);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 531:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'g') ADVANCE(598);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 532:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'g') ADVANCE(587);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 533:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'h') ADVANCE(522);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 534:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'h') ADVANCE(472);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 535:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'h') ADVANCE(514);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 536:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'h') ADVANCE(539);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 537:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'i') ADVANCE(547);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 538:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'i') ADVANCE(591);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 539:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'i') ADVANCE(550);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 540:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'i') ADVANCE(586);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 541:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'i') ADVANCE(560);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 542:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'i') ADVANCE(563);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 543:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'l') ADVANCE(395);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 544:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'l') ADVANCE(490);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 545:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'l') ADVANCE(566);
      if (lookahead == 'o') ADVANCE(575);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 546:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'l') ADVANCE(568);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 547:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'l') ADVANCE(501);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 548:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'l') ADVANCE(484);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 549:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'l') ADVANCE(543);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 550:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'l') ADVANCE(509);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 551:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'm') ADVANCE(572);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 552:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'm') ADVANCE(564);
      if (lookahead == 'p') ADVANCE(517);
      if (lookahead == 't') ADVANCE(603);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 553:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'm') ADVANCE(564);
      if (lookahead == 'p') ADVANCE(517);
      if (lookahead == 't') ADVANCE(604);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 554:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'n') ADVANCE(495);
      if (lookahead == 'x') ADVANCE(367);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(368);
      if (lookahead != 0) ADVANCE(366);
      END_STATE();
    case 555:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'n') ADVANCE(531);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 556:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'n') ADVANCE(405);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 557:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'n') ADVANCE(407);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 558:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'n') ADVANCE(532);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 559:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'n') ADVANCE(469);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 560:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'n') ADVANCE(529);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 561:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'n') ADVANCE(502);
      if (lookahead == 'x') ADVANCE(538);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 562:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'n') ADVANCE(502);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 563:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'n') ADVANCE(530);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 564:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'o') ADVANCE(606);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 565:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'o') ADVANCE(597);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 566:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'o') ADVANCE(567);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 567:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'o') ADVANCE(576);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 568:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'o') ADVANCE(558);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 569:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'p') ADVANCE(476);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 570:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'p') ADVANCE(605);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 571:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'p') ADVANCE(548);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 572:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'p') ADVANCE(600);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 573:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'r') ADVANCE(607);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 574:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'r') ADVANCE(541);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 575:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'r') ADVANCE(466);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 576:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'r') ADVANCE(477);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 577:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'r') ADVANCE(556);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 578:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'r') ADVANCE(478);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 579:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'r') ADVANCE(557);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 580:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'r') ADVANCE(596);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 581:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'r') ADVANCE(523);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 582:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 's') ADVANCE(464);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 583:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 's') ADVANCE(571);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 584:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 's') ADVANCE(474);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 585:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 's') ADVANCE(481);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 586:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 's') ADVANCE(511);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 587:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 's') ADVANCE(473);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 588:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 's') ADVANCE(524);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 589:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 's') ADVANCE(467);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 590:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(392);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 591:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(410);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 592:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(421);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 593:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(402);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 594:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(507);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 595:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(533);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 596:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(584);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 597:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(508);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 598:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(534);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 599:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(585);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 600:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(479);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 601:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 't') ADVANCE(488);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 602:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'u') ADVANCE(537);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 603:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'u') ADVANCE(577);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 604:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'u') ADVANCE(579);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 605:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'u') ADVANCE(593);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 606:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'v') ADVANCE(510);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 607:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'w') ADVANCE(540);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 608:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'x') ADVANCE(538);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 609:
      ACCEPT_TOKEN(sym_identifier);
      if (lookahead == 'y') ADVANCE(399);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 610:
      ACCEPT_TOKEN(sym_identifier);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          lookahead == '_' ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(610);
      END_STATE();
    case 611:
      ACCEPT_TOKEN(sym__newline);
      END_STATE();
    default:
      return false;
  }
}

static bool ts_lex_keywords(TSLexer *lexer, TSStateId state) {
  START_LEXER();
  eof = lexer->eof(lexer);
  switch (state) {
    case 0:
      if (lookahead == 'a') ADVANCE(1);
      if (lookahead == 'b') ADVANCE(2);
      if (lookahead == 'c') ADVANCE(3);
      if (lookahead == 'e') ADVANCE(4);
      if (lookahead == 'f') ADVANCE(5);
      if (lookahead == 'i') ADVANCE(6);
      if (lookahead == 'l') ADVANCE(7);
      if (lookahead == 'n') ADVANCE(8);
      if (lookahead == 'o') ADVANCE(9);
      if (lookahead == 't') ADVANCE(10);
      if (lookahead == 'w') ADVANCE(11);
      if (lookahead == '\t' ||
          lookahead == ' ') SKIP(0)
      END_STATE();
    case 1:
      if (lookahead == 'n') ADVANCE(12);
      if (lookahead == 's') ADVANCE(13);
      END_STATE();
    case 2:
      if (lookahead == 'o') ADVANCE(14);
      END_STATE();
    case 3:
      if (lookahead == 'o') ADVANCE(15);
      END_STATE();
    case 4:
      if (lookahead == 'q') ADVANCE(16);
      END_STATE();
    case 5:
      if (lookahead == 'a') ADVANCE(17);
      if (lookahead == 'i') ADVANCE(18);
      if (lookahead == 'r') ADVANCE(19);
      END_STATE();
    case 6:
      if (lookahead == 'n') ADVANCE(20);
      END_STATE();
    case 7:
      if (lookahead == 'i') ADVANCE(21);
      END_STATE();
    case 8:
      if (lookahead == 'o') ADVANCE(22);
      if (lookahead == 'u') ADVANCE(23);
      END_STATE();
    case 9:
      if (lookahead == 'r') ADVANCE(24);
      END_STATE();
    case 10:
      if (lookahead == 'a') ADVANCE(25);
      if (lookahead == 'e') ADVANCE(26);
      if (lookahead == 'i') ADVANCE(27);
      if (lookahead == 'o') ADVANCE(28);
      if (lookahead == 'r') ADVANCE(29);
      END_STATE();
    case 11:
      if (lookahead == 'i') ADVANCE(30);
      END_STATE();
    case 12:
      if (lookahead == 'd') ADVANCE(31);
      END_STATE();
    case 13:
      ACCEPT_TOKEN(anon_sym_as);
      END_STATE();
    case 14:
      if (lookahead == 'o') ADVANCE(32);
      END_STATE();
    case 15:
      if (lookahead == 'n') ADVANCE(33);
      END_STATE();
    case 16:
      if (lookahead == 'u') ADVANCE(34);
      END_STATE();
    case 17:
      if (lookahead == 'l') ADVANCE(35);
      END_STATE();
    case 18:
      if (lookahead == 'x') ADVANCE(36);
      END_STATE();
    case 19:
      if (lookahead == 'o') ADVANCE(37);
      END_STATE();
    case 20:
      ACCEPT_TOKEN(anon_sym_in);
      END_STATE();
    case 21:
      if (lookahead == 's') ADVANCE(38);
      END_STATE();
    case 22:
      if (lookahead == 't') ADVANCE(39);
      END_STATE();
    case 23:
      if (lookahead == 'm') ADVANCE(40);
      END_STATE();
    case 24:
      ACCEPT_TOKEN(anon_sym_or);
      END_STATE();
    case 25:
      if (lookahead == 'b') ADVANCE(41);
      END_STATE();
    case 26:
      if (lookahead == 'x') ADVANCE(42);
      END_STATE();
    case 27:
      if (lookahead == 'm') ADVANCE(43);
      END_STATE();
    case 28:
      ACCEPT_TOKEN(anon_sym_to);
      END_STATE();
    case 29:
      if (lookahead == 'u') ADVANCE(44);
      END_STATE();
    case 30:
      if (lookahead == 't') ADVANCE(45);
      END_STATE();
    case 31:
      ACCEPT_TOKEN(anon_sym_and);
      END_STATE();
    case 32:
      if (lookahead == 'l') ADVANCE(46);
      END_STATE();
    case 33:
      if (lookahead == 't') ADVANCE(47);
      END_STATE();
    case 34:
      if (lookahead == 'a') ADVANCE(48);
      END_STATE();
    case 35:
      if (lookahead == 's') ADVANCE(49);
      END_STATE();
    case 36:
      if (lookahead == 'e') ADVANCE(50);
      END_STATE();
    case 37:
      if (lookahead == 'm') ADVANCE(51);
      END_STATE();
    case 38:
      if (lookahead == 't') ADVANCE(52);
      END_STATE();
    case 39:
      ACCEPT_TOKEN(anon_sym_not);
      if (lookahead == 'h') ADVANCE(53);
      END_STATE();
    case 40:
      if (lookahead == 'b') ADVANCE(54);
      END_STATE();
    case 41:
      if (lookahead == 'l') ADVANCE(55);
      END_STATE();
    case 42:
      if (lookahead == 't') ADVANCE(56);
      END_STATE();
    case 43:
      if (lookahead == 'e') ADVANCE(57);
      END_STATE();
    case 44:
      if (lookahead == 'e') ADVANCE(58);
      END_STATE();
    case 45:
      if (lookahead == 'h') ADVANCE(59);
      END_STATE();
    case 46:
      if (lookahead == 'e') ADVANCE(60);
      END_STATE();
    case 47:
      if (lookahead == 'a') ADVANCE(61);
      END_STATE();
    case 48:
      if (lookahead == 'l') ADVANCE(62);
      END_STATE();
    case 49:
      if (lookahead == 'e') ADVANCE(63);
      END_STATE();
    case 50:
      if (lookahead == 'd') ADVANCE(64);
      END_STATE();
    case 51:
      ACCEPT_TOKEN(anon_sym_from);
      END_STATE();
    case 52:
      ACCEPT_TOKEN(anon_sym_list);
      END_STATE();
    case 53:
      if (lookahead == 'i') ADVANCE(65);
      END_STATE();
    case 54:
      if (lookahead == 'e') ADVANCE(66);
      END_STATE();
    case 55:
      if (lookahead == 'e') ADVANCE(67);
      END_STATE();
    case 56:
      ACCEPT_TOKEN(anon_sym_text);
      END_STATE();
    case 57:
      if (lookahead == 's') ADVANCE(68);
      END_STATE();
    case 58:
      ACCEPT_TOKEN(anon_sym_true);
      END_STATE();
    case 59:
      ACCEPT_TOKEN(anon_sym_with);
      END_STATE();
    case 60:
      if (lookahead == 'a') ADVANCE(69);
      END_STATE();
    case 61:
      if (lookahead == 'i') ADVANCE(70);
      END_STATE();
    case 62:
      if (lookahead == 's') ADVANCE(71);
      END_STATE();
    case 63:
      ACCEPT_TOKEN(anon_sym_false);
      END_STATE();
    case 64:
      ACCEPT_TOKEN(anon_sym_fixed);
      END_STATE();
    case 65:
      if (lookahead == 'n') ADVANCE(72);
      END_STATE();
    case 66:
      if (lookahead == 'r') ADVANCE(73);
      END_STATE();
    case 67:
      ACCEPT_TOKEN(anon_sym_table);
      END_STATE();
    case 68:
      ACCEPT_TOKEN(anon_sym_times);
      END_STATE();
    case 69:
      if (lookahead == 'n') ADVANCE(74);
      END_STATE();
    case 70:
      if (lookahead == 'n') ADVANCE(75);
      END_STATE();
    case 71:
      ACCEPT_TOKEN(anon_sym_equals);
      END_STATE();
    case 72:
      if (lookahead == 'g') ADVANCE(76);
      END_STATE();
    case 73:
      ACCEPT_TOKEN(anon_sym_number);
      END_STATE();
    case 74:
      ACCEPT_TOKEN(anon_sym_boolean);
      END_STATE();
    case 75:
      if (lookahead == 's') ADVANCE(77);
      END_STATE();
    case 76:
      ACCEPT_TOKEN(sym_nothing);
      END_STATE();
    case 77:
      ACCEPT_TOKEN(anon_sym_contains);
      END_STATE();
    default:
      return false;
  }
}

static const TSLexMode ts_lex_modes[STATE_COUNT] = {
  [0] = {.lex_state = 0},
  [1] = {.lex_state = 262},
  [2] = {.lex_state = 258},
  [3] = {.lex_state = 258},
  [4] = {.lex_state = 258},
  [5] = {.lex_state = 258},
  [6] = {.lex_state = 259},
  [7] = {.lex_state = 258},
  [8] = {.lex_state = 258},
  [9] = {.lex_state = 258},
  [10] = {.lex_state = 258},
  [11] = {.lex_state = 258},
  [12] = {.lex_state = 259},
  [13] = {.lex_state = 258},
  [14] = {.lex_state = 259},
  [15] = {.lex_state = 258},
  [16] = {.lex_state = 258},
  [17] = {.lex_state = 258},
  [18] = {.lex_state = 258},
  [19] = {.lex_state = 258},
  [20] = {.lex_state = 258},
  [21] = {.lex_state = 259},
  [22] = {.lex_state = 259},
  [23] = {.lex_state = 259},
  [24] = {.lex_state = 260},
  [25] = {.lex_state = 262},
  [26] = {.lex_state = 262},
  [27] = {.lex_state = 259},
  [28] = {.lex_state = 261},
  [29] = {.lex_state = 261},
  [30] = {.lex_state = 261},
  [31] = {.lex_state = 261},
  [32] = {.lex_state = 257},
  [33] = {.lex_state = 261},
  [34] = {.lex_state = 261},
  [35] = {.lex_state = 261},
  [36] = {.lex_state = 263},
  [37] = {.lex_state = 263},
  [38] = {.lex_state = 263},
  [39] = {.lex_state = 263},
  [40] = {.lex_state = 263},
  [41] = {.lex_state = 262},
  [42] = {.lex_state = 263},
  [43] = {.lex_state = 263},
  [44] = {.lex_state = 262},
  [45] = {.lex_state = 264},
  [46] = {.lex_state = 263},
  [47] = {.lex_state = 263},
  [48] = {.lex_state = 263},
  [49] = {.lex_state = 262},
  [50] = {.lex_state = 266},
  [51] = {.lex_state = 262},
  [52] = {.lex_state = 263},
  [53] = {.lex_state = 263},
  [54] = {.lex_state = 263},
  [55] = {.lex_state = 265},
  [56] = {.lex_state = 262},
  [57] = {.lex_state = 262},
  [58] = {.lex_state = 360},
  [59] = {.lex_state = 262},
  [60] = {.lex_state = 262},
  [61] = {.lex_state = 262},
  [62] = {.lex_state = 262},
  [63] = {.lex_state = 262},
  [64] = {.lex_state = 262},
  [65] = {.lex_state = 262},
  [66] = {.lex_state = 262},
  [67] = {.lex_state = 262},
  [68] = {.lex_state = 262},
  [69] = {.lex_state = 262},
  [70] = {.lex_state = 19},
  [71] = {.lex_state = 262},
  [72] = {.lex_state = 262},
  [73] = {.lex_state = 262},
  [74] = {.lex_state = 262},
  [75] = {.lex_state = 262},
  [76] = {.lex_state = 262},
  [77] = {.lex_state = 262},
  [78] = {.lex_state = 262},
  [79] = {.lex_state = 262},
  [80] = {.lex_state = 262},
  [81] = {.lex_state = 262},
  [82] = {.lex_state = 262},
  [83] = {.lex_state = 262},
  [84] = {.lex_state = 262},
  [85] = {.lex_state = 262},
  [86] = {.lex_state = 262},
  [87] = {.lex_state = 19},
  [88] = {.lex_state = 19},
  [89] = {.lex_state = 19},
  [90] = {.lex_state = 19},
  [91] = {.lex_state = 21},
  [92] = {.lex_state = 19},
  [93] = {.lex_state = 19},
  [94] = {.lex_state = 19},
  [95] = {.lex_state = 19},
  [96] = {.lex_state = 19},
  [97] = {.lex_state = 19},
  [98] = {.lex_state = 19},
  [99] = {.lex_state = 19},
  [100] = {.lex_state = 21},
  [101] = {.lex_state = 19},
  [102] = {.lex_state = 19},
  [103] = {.lex_state = 19},
  [104] = {.lex_state = 21},
  [105] = {.lex_state = 19},
  [106] = {.lex_state = 21},
  [107] = {.lex_state = 19},
  [108] = {.lex_state = 19},
  [109] = {.lex_state = 19},
  [110] = {.lex_state = 21},
  [111] = {.lex_state = 19},
  [112] = {.lex_state = 19},
  [113] = {.lex_state = 69},
  [114] = {.lex_state = 19},
  [115] = {.lex_state = 19},
  [116] = {.lex_state = 69},
  [117] = {.lex_state = 69},
  [118] = {.lex_state = 252},
  [119] = {.lex_state = 252},
  [120] = {.lex_state = 252},
  [121] = {.lex_state = 252},
  [122] = {.lex_state = 20},
  [123] = {.lex_state = 20},
  [124] = {.lex_state = 20},
  [125] = {.lex_state = 252},
  [126] = {.lex_state = 252},
  [127] = {.lex_state = 252},
  [128] = {.lex_state = 252},
  [129] = {.lex_state = 0},
  [130] = {.lex_state = 252},
  [131] = {.lex_state = 252},
  [132] = {.lex_state = 252},
  [133] = {.lex_state = 0},
  [134] = {.lex_state = 252},
  [135] = {.lex_state = 252},
  [136] = {.lex_state = 252},
  [137] = {.lex_state = 0},
  [138] = {.lex_state = 252},
  [139] = {.lex_state = 252},
  [140] = {.lex_state = 252},
  [141] = {.lex_state = 252},
  [142] = {.lex_state = 252},
  [143] = {.lex_state = 252},
  [144] = {.lex_state = 262},
  [145] = {.lex_state = 252},
  [146] = {.lex_state = 252},
  [147] = {.lex_state = 252},
  [148] = {.lex_state = 252},
  [149] = {.lex_state = 252},
  [150] = {.lex_state = 252},
};

static const uint16_t ts_parse_table[LARGE_STATE_COUNT][SYMBOL_COUNT] = {
  [0] = {
    [ts_builtin_sym_end] = ACTIONS(1),
    [sym_identifier] = ACTIONS(1),
    [anon_sym_do_COLON] = ACTIONS(1),
    [anon_sym_declare_COLON] = ACTIONS(1),
    [anon_sym_note_COLON] = ACTIONS(1),
    [anon_sym_noteblock_COLON] = ACTIONS(1),
    [anon_sym_endnote] = ACTIONS(1),
    [aux_sym_block_comment_content_token2] = ACTIONS(1),
    [aux_sym_block_comment_content_token3] = ACTIONS(1),
    [aux_sym_block_comment_content_token4] = ACTIONS(1),
    [aux_sym_block_comment_content_token5] = ACTIONS(1),
    [aux_sym_block_comment_content_token6] = ACTIONS(1),
    [aux_sym_block_comment_content_token7] = ACTIONS(1),
    [aux_sym_block_comment_content_token8] = ACTIONS(1),
    [anon_sym_building_COLON] = ACTIONS(1),
    [anon_sym_floor_COLON] = ACTIONS(1),
    [anon_sym_step_COLON] = ACTIONS(1),
    [anon_sym_riser_COLON] = ACTIONS(1),
    [anon_sym_belongsto_COLON] = ACTIONS(1),
    [anon_sym_expects_COLON] = ACTIONS(1),
    [anon_sym_returns_COLON] = ACTIONS(1),
    [anon_sym_COMMA] = ACTIONS(1),
    [anon_sym_as] = ACTIONS(1),
    [anon_sym_number] = ACTIONS(1),
    [anon_sym_text] = ACTIONS(1),
    [anon_sym_boolean] = ACTIONS(1),
    [anon_sym_list] = ACTIONS(1),
    [anon_sym_table] = ACTIONS(1),
    [anon_sym_fixed] = ACTIONS(1),
    [anon_sym_EQ] = ACTIONS(1),
    [anon_sym_set] = ACTIONS(1),
    [anon_sym_to] = ACTIONS(1),
    [anon_sym_call] = ACTIONS(1),
    [anon_sym_with] = ACTIONS(1),
    [anon_sym_storingresultin] = ACTIONS(1),
    [anon_sym_display] = ACTIONS(1),
    [anon_sym_return] = ACTIONS(1),
    [sym_exit_statement] = ACTIONS(1),
    [anon_sym_if] = ACTIONS(1),
    [anon_sym_otherwiseif] = ACTIONS(1),
    [anon_sym_otherwise] = ACTIONS(1),
    [anon_sym_repeat] = ACTIONS(1),
    [anon_sym_times] = ACTIONS(1),
    [anon_sym_foreach] = ACTIONS(1),
    [anon_sym_in] = ACTIONS(1),
    [anon_sym_while] = ACTIONS(1),
    [anon_sym_attempt_COLON] = ACTIONS(1),
    [anon_sym_ifunsuccessful_COLON] = ACTIONS(1),
    [anon_sym_thencontinue_COLON] = ACTIONS(1),
    [anon_sym_add] = ACTIONS(1),
    [anon_sym_remove] = ACTIONS(1),
    [anon_sym_from] = ACTIONS(1),
    [anon_sym_DQUOTE] = ACTIONS(1),
    [sym_escape_sequence] = ACTIONS(1),
    [anon_sym_true] = ACTIONS(1),
    [anon_sym_false] = ACTIONS(1),
    [sym_nothing] = ACTIONS(1),
    [anon_sym_LBRACK] = ACTIONS(1),
    [anon_sym_RBRACK] = ACTIONS(1),
    [anon_sym_PLUS] = ACTIONS(1),
    [anon_sym_DASH] = ACTIONS(1),
    [anon_sym_STAR] = ACTIONS(1),
    [anon_sym_SLASH] = ACTIONS(1),
    [anon_sym_isequalto] = ACTIONS(1),
    [anon_sym_equals] = ACTIONS(1),
    [anon_sym_isnotequalto] = ACTIONS(1),
    [anon_sym_islessthan] = ACTIONS(1),
    [anon_sym_isgreaterthan] = ACTIONS(1),
    [anon_sym_islessthanorequalto] = ACTIONS(1),
    [anon_sym_isgreaterthanorequalto] = ACTIONS(1),
    [anon_sym_and] = ACTIONS(1),
    [anon_sym_or] = ACTIONS(1),
    [anon_sym_addedto] = ACTIONS(1),
    [anon_sym_contains] = ACTIONS(1),
    [anon_sym_startswith] = ACTIONS(1),
    [anon_sym_endswith] = ACTIONS(1),
    [anon_sym_isin] = ACTIONS(1),
    [anon_sym_not] = ACTIONS(1),
    [anon_sym_lengthof] = ACTIONS(1),
    [anon_sym_LPAREN] = ACTIONS(1),
    [anon_sym_RPAREN] = ACTIONS(1),
    [sym__newline] = ACTIONS(1),
  },
  [1] = {
    [sym_source_file] = STATE(129),
    [sym__statement] = STATE(26),
    [sym_section_marker] = STATE(26),
    [sym_comment] = STATE(26),
    [sym_block_comment] = STATE(26),
    [sym_structure_definition] = STATE(26),
    [sym_building_def] = STATE(67),
    [sym_floor_def] = STATE(67),
    [sym_step_def] = STATE(67),
    [sym_riser_def] = STATE(67),
    [sym_declaration] = STATE(26),
    [sym_assignment] = STATE(26),
    [sym_call_statement] = STATE(26),
    [sym_display_statement] = STATE(26),
    [sym_input_statement] = STATE(26),
    [sym_return_statement] = STATE(26),
    [sym_if_statement] = STATE(26),
    [sym_repeat_statement] = STATE(26),
    [sym_for_each_statement] = STATE(26),
    [sym_while_statement] = STATE(26),
    [sym_attempt_statement] = STATE(26),
    [sym_add_statement] = STATE(26),
    [sym_remove_statement] = STATE(26),
    [aux_sym_source_file_repeat1] = STATE(26),
    [ts_builtin_sym_end] = ACTIONS(3),
    [anon_sym_do_COLON] = ACTIONS(5),
    [anon_sym_declare_COLON] = ACTIONS(7),
    [anon_sym_note_COLON] = ACTIONS(9),
    [anon_sym_noteblock_COLON] = ACTIONS(11),
    [anon_sym_building_COLON] = ACTIONS(13),
    [anon_sym_floor_COLON] = ACTIONS(15),
    [anon_sym_step_COLON] = ACTIONS(17),
    [anon_sym_riser_COLON] = ACTIONS(19),
    [anon_sym_set] = ACTIONS(21),
    [anon_sym_call] = ACTIONS(23),
    [anon_sym_display] = ACTIONS(25),
    [anon_sym_input] = ACTIONS(27),
    [anon_sym_return] = ACTIONS(29),
    [sym_exit_statement] = ACTIONS(31),
    [anon_sym_if] = ACTIONS(33),
    [anon_sym_repeat] = ACTIONS(35),
    [anon_sym_foreach] = ACTIONS(37),
    [anon_sym_while] = ACTIONS(39),
    [anon_sym_attempt_COLON] = ACTIONS(41),
    [anon_sym_add] = ACTIONS(43),
    [anon_sym_remove] = ACTIONS(45),
    [sym__newline] = ACTIONS(31),
  },
};

static const uint16_t ts_small_parse_table[] = {
  [0] = 7,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    STATE(8), 1,
      aux_sym_argument_list_repeat1,
    STATE(96), 1,
      sym_binary_operator,
    ACTIONS(49), 2,
      anon_sym_otherwise,
      anon_sym_add,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(47), 30,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_RBRACK,
      anon_sym_RPAREN,
      sym__newline,
  [68] = 4,
    ACTIONS(59), 1,
      anon_sym_with,
    STATE(20), 1,
      sym_with_clause,
    ACTIONS(61), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(57), 47,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [130] = 4,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    STATE(96), 1,
      sym_binary_operator,
    ACTIONS(65), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(63), 46,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [191] = 4,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    STATE(96), 1,
      sym_binary_operator,
    ACTIONS(69), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(67), 46,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [252] = 8,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(71), 1,
      anon_sym_COMMA,
    STATE(14), 1,
      aux_sym_argument_list_repeat1,
    STATE(96), 1,
      sym_binary_operator,
    ACTIONS(49), 2,
      anon_sym_otherwise,
      anon_sym_add,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(47), 28,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_RBRACK,
      anon_sym_RPAREN,
      sym__newline,
  [321] = 4,
    ACTIONS(75), 1,
      anon_sym_COMMA,
    STATE(7), 1,
      aux_sym_argument_list_repeat1,
    ACTIONS(78), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(73), 46,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [382] = 3,
    STATE(7), 1,
      aux_sym_argument_list_repeat1,
    ACTIONS(82), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(80), 47,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [441] = 6,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    STATE(96), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(78), 2,
      anon_sym_otherwise,
      anon_sym_add,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(73), 30,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_RBRACK,
      anon_sym_RPAREN,
      sym__newline,
  [506] = 2,
    ACTIONS(86), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(84), 47,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [562] = 2,
    ACTIONS(90), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(88), 47,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [618] = 4,
    ACTIONS(92), 1,
      anon_sym_with,
    STATE(20), 1,
      sym_with_clause,
    ACTIONS(61), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(57), 45,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [678] = 2,
    ACTIONS(96), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(94), 47,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [734] = 4,
    ACTIONS(71), 1,
      anon_sym_COMMA,
    STATE(7), 1,
      aux_sym_argument_list_repeat1,
    ACTIONS(82), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(80), 45,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [794] = 2,
    ACTIONS(100), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(98), 47,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [850] = 2,
    ACTIONS(104), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(102), 47,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [906] = 2,
    ACTIONS(108), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(106), 47,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [962] = 2,
    ACTIONS(112), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(110), 47,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [1018] = 2,
    ACTIONS(116), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(114), 47,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [1074] = 2,
    ACTIONS(120), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(118), 47,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [1130] = 4,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(65), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(63), 44,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [1189] = 4,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(69), 4,
      anon_sym_otherwise,
      anon_sym_add,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(67), 44,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_to,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_times,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_from,
      anon_sym_RBRACK,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
      anon_sym_RPAREN,
      sym__newline,
  [1248] = 10,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(124), 1,
      anon_sym_otherwiseif,
    ACTIONS(126), 1,
      anon_sym_otherwise,
    ACTIONS(128), 1,
      anon_sym_add,
    STATE(75), 1,
      sym_otherwise_clause,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    STATE(41), 2,
      sym_otherwise_if_clause,
      aux_sym_if_statement_repeat1,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(122), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      sym__newline,
  [1317] = 8,
    ACTIONS(49), 1,
      anon_sym_add,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(71), 1,
      anon_sym_COMMA,
    STATE(44), 1,
      aux_sym_argument_list_repeat1,
    STATE(96), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(47), 24,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      anon_sym_RBRACK,
      sym__newline,
  [1381] = 24,
    ACTIONS(130), 1,
      ts_builtin_sym_end,
    ACTIONS(132), 1,
      anon_sym_do_COLON,
    ACTIONS(135), 1,
      anon_sym_declare_COLON,
    ACTIONS(138), 1,
      anon_sym_note_COLON,
    ACTIONS(141), 1,
      anon_sym_noteblock_COLON,
    ACTIONS(144), 1,
      anon_sym_building_COLON,
    ACTIONS(147), 1,
      anon_sym_floor_COLON,
    ACTIONS(150), 1,
      anon_sym_step_COLON,
    ACTIONS(153), 1,
      anon_sym_riser_COLON,
    ACTIONS(156), 1,
      anon_sym_set,
    ACTIONS(159), 1,
      anon_sym_call,
    ACTIONS(162), 1,
      anon_sym_display,
    ACTIONS(165), 1,
      anon_sym_input,
    ACTIONS(168), 1,
      anon_sym_return,
    ACTIONS(174), 1,
      anon_sym_if,
    ACTIONS(177), 1,
      anon_sym_repeat,
    ACTIONS(180), 1,
      anon_sym_foreach,
    ACTIONS(183), 1,
      anon_sym_while,
    ACTIONS(186), 1,
      anon_sym_attempt_COLON,
    ACTIONS(189), 1,
      anon_sym_add,
    ACTIONS(192), 1,
      anon_sym_remove,
    ACTIONS(171), 2,
      sym_exit_statement,
      sym__newline,
    STATE(67), 4,
      sym_building_def,
      sym_floor_def,
      sym_step_def,
      sym_riser_def,
    STATE(25), 19,
      sym__statement,
      sym_section_marker,
      sym_comment,
      sym_block_comment,
      sym_structure_definition,
      sym_declaration,
      sym_assignment,
      sym_call_statement,
      sym_display_statement,
      sym_input_statement,
      sym_return_statement,
      sym_if_statement,
      sym_repeat_statement,
      sym_for_each_statement,
      sym_while_statement,
      sym_attempt_statement,
      sym_add_statement,
      sym_remove_statement,
      aux_sym_source_file_repeat1,
  [1476] = 24,
    ACTIONS(5), 1,
      anon_sym_do_COLON,
    ACTIONS(7), 1,
      anon_sym_declare_COLON,
    ACTIONS(9), 1,
      anon_sym_note_COLON,
    ACTIONS(11), 1,
      anon_sym_noteblock_COLON,
    ACTIONS(13), 1,
      anon_sym_building_COLON,
    ACTIONS(15), 1,
      anon_sym_floor_COLON,
    ACTIONS(17), 1,
      anon_sym_step_COLON,
    ACTIONS(19), 1,
      anon_sym_riser_COLON,
    ACTIONS(21), 1,
      anon_sym_set,
    ACTIONS(23), 1,
      anon_sym_call,
    ACTIONS(25), 1,
      anon_sym_display,
    ACTIONS(27), 1,
      anon_sym_input,
    ACTIONS(29), 1,
      anon_sym_return,
    ACTIONS(33), 1,
      anon_sym_if,
    ACTIONS(35), 1,
      anon_sym_repeat,
    ACTIONS(37), 1,
      anon_sym_foreach,
    ACTIONS(39), 1,
      anon_sym_while,
    ACTIONS(41), 1,
      anon_sym_attempt_COLON,
    ACTIONS(43), 1,
      anon_sym_add,
    ACTIONS(45), 1,
      anon_sym_remove,
    ACTIONS(195), 1,
      ts_builtin_sym_end,
    ACTIONS(197), 2,
      sym_exit_statement,
      sym__newline,
    STATE(67), 4,
      sym_building_def,
      sym_floor_def,
      sym_step_def,
      sym_riser_def,
    STATE(25), 19,
      sym__statement,
      sym_section_marker,
      sym_comment,
      sym_block_comment,
      sym_structure_definition,
      sym_declaration,
      sym_assignment,
      sym_call_statement,
      sym_display_statement,
      sym_input_statement,
      sym_return_statement,
      sym_if_statement,
      sym_repeat_statement,
      sym_for_each_statement,
      sym_while_statement,
      sym_attempt_statement,
      sym_add_statement,
      sym_remove_statement,
      aux_sym_source_file_repeat1,
  [1571] = 6,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(201), 2,
      anon_sym_otherwise,
      anon_sym_add,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(199), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_otherwiseif,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      sym__newline,
  [1629] = 6,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(205), 1,
      anon_sym_add,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(203), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      sym__newline,
  [1685] = 6,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(209), 1,
      anon_sym_add,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(207), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      sym__newline,
  [1741] = 6,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(213), 1,
      anon_sym_add,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(211), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      sym__newline,
  [1797] = 6,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(217), 1,
      anon_sym_add,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(215), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      sym__newline,
  [1853] = 13,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(227), 1,
      sym_number,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(221), 2,
      sym_nothing,
      sym_identifier,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    STATE(30), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
    ACTIONS(223), 10,
      anon_sym_set,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_while,
      anon_sym_add,
      anon_sym_remove,
    ACTIONS(219), 12,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_foreach,
      anon_sym_attempt_COLON,
      sym__newline,
  [1923] = 6,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(243), 1,
      anon_sym_add,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(241), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      sym__newline,
  [1979] = 6,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(247), 1,
      anon_sym_add,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(245), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      sym__newline,
  [2035] = 6,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(251), 1,
      anon_sym_add,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
    ACTIONS(249), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_remove,
      sym__newline,
  [2091] = 7,
    ACTIONS(255), 1,
      anon_sym_belongsto_COLON,
    ACTIONS(257), 1,
      anon_sym_expects_COLON,
    ACTIONS(259), 1,
      anon_sym_returns_COLON,
    ACTIONS(261), 1,
      anon_sym_return,
    STATE(68), 1,
      sym_step_clauses,
    STATE(39), 4,
      sym_belongs_clause,
      sym_expects_clause,
      sym_returns_clause,
      aux_sym_step_clauses_repeat1,
    ACTIONS(253), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2137] = 7,
    ACTIONS(255), 1,
      anon_sym_belongsto_COLON,
    ACTIONS(257), 1,
      anon_sym_expects_COLON,
    ACTIONS(259), 1,
      anon_sym_returns_COLON,
    ACTIONS(265), 1,
      anon_sym_return,
    STATE(69), 1,
      sym_step_clauses,
    STATE(39), 4,
      sym_belongs_clause,
      sym_expects_clause,
      sym_returns_clause,
      aux_sym_step_clauses_repeat1,
    ACTIONS(263), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2183] = 6,
    ACTIONS(269), 1,
      anon_sym_belongsto_COLON,
    ACTIONS(272), 1,
      anon_sym_expects_COLON,
    ACTIONS(275), 1,
      anon_sym_returns_COLON,
    ACTIONS(278), 1,
      anon_sym_return,
    STATE(38), 4,
      sym_belongs_clause,
      sym_expects_clause,
      sym_returns_clause,
      aux_sym_step_clauses_repeat1,
    ACTIONS(267), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2226] = 6,
    ACTIONS(255), 1,
      anon_sym_belongsto_COLON,
    ACTIONS(257), 1,
      anon_sym_expects_COLON,
    ACTIONS(259), 1,
      anon_sym_returns_COLON,
    ACTIONS(282), 1,
      anon_sym_return,
    STATE(38), 4,
      sym_belongs_clause,
      sym_expects_clause,
      sym_returns_clause,
      aux_sym_step_clauses_repeat1,
    ACTIONS(280), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2269] = 4,
    ACTIONS(286), 1,
      anon_sym_COMMA,
    ACTIONS(288), 1,
      anon_sym_return,
    STATE(43), 1,
      aux_sym_parameter_list_repeat1,
    ACTIONS(284), 25,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_belongsto_COLON,
      anon_sym_expects_COLON,
      anon_sym_returns_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2306] = 5,
    ACTIONS(124), 1,
      anon_sym_otherwiseif,
    ACTIONS(126), 1,
      anon_sym_otherwise,
    STATE(66), 1,
      sym_otherwise_clause,
    STATE(51), 2,
      sym_otherwise_if_clause,
      aux_sym_if_statement_repeat1,
    ACTIONS(290), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2345] = 4,
    ACTIONS(294), 1,
      anon_sym_COMMA,
    ACTIONS(297), 1,
      anon_sym_return,
    STATE(42), 1,
      aux_sym_parameter_list_repeat1,
    ACTIONS(292), 25,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_belongsto_COLON,
      anon_sym_expects_COLON,
      anon_sym_returns_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2382] = 4,
    ACTIONS(286), 1,
      anon_sym_COMMA,
    ACTIONS(301), 1,
      anon_sym_return,
    STATE(42), 1,
      aux_sym_parameter_list_repeat1,
    ACTIONS(299), 25,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_belongsto_COLON,
      anon_sym_expects_COLON,
      anon_sym_returns_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2419] = 3,
    ACTIONS(71), 1,
      anon_sym_COMMA,
    STATE(49), 1,
      aux_sym_argument_list_repeat1,
    ACTIONS(80), 25,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      anon_sym_RBRACK,
      sym__newline,
  [2453] = 6,
    ACTIONS(305), 1,
      anon_sym_if,
    ACTIONS(307), 1,
      anon_sym_ifunsuccessful_COLON,
    ACTIONS(309), 1,
      anon_sym_thencontinue_COLON,
    STATE(56), 1,
      sym_if_unsuccessful_clause,
    STATE(80), 1,
      sym_then_continue_clause,
    ACTIONS(303), 22,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2493] = 2,
    ACTIONS(313), 1,
      anon_sym_return,
    ACTIONS(311), 26,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_belongsto_COLON,
      anon_sym_expects_COLON,
      anon_sym_returns_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2525] = 2,
    ACTIONS(297), 1,
      anon_sym_return,
    ACTIONS(292), 26,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_belongsto_COLON,
      anon_sym_expects_COLON,
      anon_sym_returns_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2557] = 2,
    ACTIONS(317), 1,
      anon_sym_return,
    ACTIONS(315), 26,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_belongsto_COLON,
      anon_sym_expects_COLON,
      anon_sym_returns_COLON,
      anon_sym_COMMA,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2589] = 3,
    ACTIONS(75), 1,
      anon_sym_COMMA,
    STATE(49), 1,
      aux_sym_argument_list_repeat1,
    ACTIONS(73), 25,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      anon_sym_RBRACK,
      sym__newline,
  [2623] = 5,
    ACTIONS(321), 1,
      anon_sym_with,
    ACTIONS(323), 1,
      anon_sym_storingresultin,
    STATE(57), 1,
      sym_with_clause,
    STATE(74), 1,
      sym_storing_clause,
    ACTIONS(319), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2661] = 4,
    ACTIONS(327), 1,
      anon_sym_otherwiseif,
    ACTIONS(330), 1,
      anon_sym_otherwise,
    STATE(51), 2,
      sym_otherwise_if_clause,
      aux_sym_if_statement_repeat1,
    ACTIONS(325), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2697] = 2,
    ACTIONS(334), 1,
      anon_sym_return,
    ACTIONS(332), 25,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_belongsto_COLON,
      anon_sym_expects_COLON,
      anon_sym_returns_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2728] = 2,
    ACTIONS(338), 1,
      anon_sym_return,
    ACTIONS(336), 25,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_belongsto_COLON,
      anon_sym_expects_COLON,
      anon_sym_returns_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2759] = 2,
    ACTIONS(342), 1,
      anon_sym_return,
    ACTIONS(340), 25,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_belongsto_COLON,
      anon_sym_expects_COLON,
      anon_sym_returns_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2790] = 4,
    ACTIONS(346), 1,
      sym_identifier,
    ACTIONS(348), 1,
      anon_sym_fixed,
    ACTIONS(350), 11,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_while,
      anon_sym_add,
      anon_sym_remove,
    ACTIONS(344), 12,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_foreach,
      anon_sym_attempt_COLON,
      sym__newline,
  [2824] = 3,
    ACTIONS(309), 1,
      anon_sym_thencontinue_COLON,
    STATE(82), 1,
      sym_then_continue_clause,
    ACTIONS(352), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2856] = 3,
    ACTIONS(323), 1,
      anon_sym_storingresultin,
    STATE(65), 1,
      sym_storing_clause,
    ACTIONS(354), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2888] = 3,
    ACTIONS(356), 1,
      ts_builtin_sym_end,
    ACTIONS(360), 1,
      sym_comment_content,
    ACTIONS(358), 22,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2919] = 2,
    ACTIONS(364), 1,
      anon_sym_EQ,
    ACTIONS(362), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2948] = 1,
    ACTIONS(311), 24,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_EQ,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [2975] = 1,
    ACTIONS(366), 24,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_thencontinue_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3002] = 1,
    ACTIONS(106), 24,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_storingresultin,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3029] = 2,
    ACTIONS(370), 1,
      anon_sym_EQ,
    ACTIONS(368), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3058] = 1,
    ACTIONS(372), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3084] = 1,
    ACTIONS(374), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3110] = 1,
    ACTIONS(376), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3136] = 1,
    ACTIONS(378), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3162] = 1,
    ACTIONS(380), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3188] = 1,
    ACTIONS(382), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3214] = 13,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(386), 1,
      anon_sym_call,
    ACTIONS(388), 1,
      sym_number,
    ACTIONS(390), 1,
      anon_sym_RBRACK,
    STATE(97), 1,
      sym_unary_operator,
    STATE(137), 1,
      sym_argument_list,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(384), 2,
      sym_nothing,
      sym_identifier,
    STATE(24), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [3264] = 1,
    ACTIONS(392), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3290] = 1,
    ACTIONS(394), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3316] = 1,
    ACTIONS(396), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3342] = 1,
    ACTIONS(354), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3368] = 1,
    ACTIONS(290), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3394] = 1,
    ACTIONS(398), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3420] = 1,
    ACTIONS(344), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3446] = 1,
    ACTIONS(400), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3472] = 1,
    ACTIONS(402), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3498] = 1,
    ACTIONS(352), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3524] = 1,
    ACTIONS(404), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3550] = 1,
    ACTIONS(406), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3576] = 1,
    ACTIONS(408), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3602] = 1,
    ACTIONS(410), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3628] = 1,
    ACTIONS(412), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3654] = 1,
    ACTIONS(414), 23,
      ts_builtin_sym_end,
      anon_sym_do_COLON,
      anon_sym_declare_COLON,
      anon_sym_note_COLON,
      anon_sym_noteblock_COLON,
      anon_sym_building_COLON,
      anon_sym_floor_COLON,
      anon_sym_step_COLON,
      anon_sym_riser_COLON,
      anon_sym_set,
      anon_sym_call,
      anon_sym_display,
      anon_sym_input,
      anon_sym_return,
      sym_exit_statement,
      anon_sym_if,
      anon_sym_repeat,
      anon_sym_foreach,
      anon_sym_while,
      anon_sym_attempt_COLON,
      anon_sym_add,
      anon_sym_remove,
      sym__newline,
  [3680] = 12,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(386), 1,
      anon_sym_call,
    ACTIONS(388), 1,
      sym_number,
    STATE(62), 1,
      sym_argument_list,
    STATE(97), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(384), 2,
      sym_nothing,
      sym_identifier,
    STATE(24), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [3727] = 12,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(386), 1,
      anon_sym_call,
    ACTIONS(418), 1,
      sym_number,
    STATE(17), 1,
      sym_argument_list,
    STATE(97), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(416), 2,
      sym_nothing,
      sym_identifier,
    STATE(6), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [3774] = 12,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(386), 1,
      anon_sym_call,
    ACTIONS(422), 1,
      sym_number,
    STATE(17), 1,
      sym_argument_list,
    STATE(97), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(420), 2,
      sym_nothing,
      sym_identifier,
    STATE(2), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [3821] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(426), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(424), 2,
      sym_nothing,
      sym_identifier,
    STATE(29), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [3865] = 5,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(428), 1,
      anon_sym_RPAREN,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
  [3897] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(432), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(430), 2,
      sym_nothing,
      sym_identifier,
    STATE(21), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [3941] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(436), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(434), 2,
      sym_nothing,
      sym_identifier,
    STATE(27), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [3985] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(440), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(438), 2,
      sym_nothing,
      sym_identifier,
    STATE(31), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4029] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(444), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(442), 2,
      sym_nothing,
      sym_identifier,
    STATE(106), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4073] = 11,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(386), 1,
      anon_sym_call,
    ACTIONS(448), 1,
      sym_number,
    STATE(97), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(446), 2,
      sym_nothing,
      sym_identifier,
    STATE(4), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4117] = 11,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(386), 1,
      anon_sym_call,
    ACTIONS(452), 1,
      sym_number,
    STATE(97), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(450), 2,
      sym_nothing,
      sym_identifier,
    STATE(5), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4161] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(456), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(454), 2,
      sym_nothing,
      sym_identifier,
    STATE(110), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4205] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(460), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(458), 2,
      sym_nothing,
      sym_identifier,
    STATE(91), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4249] = 5,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(462), 1,
      anon_sym_RBRACK,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
  [4281] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(466), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(464), 2,
      sym_nothing,
      sym_identifier,
    STATE(100), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4325] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(470), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(468), 2,
      sym_nothing,
      sym_identifier,
    STATE(22), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4369] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(474), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(472), 2,
      sym_nothing,
      sym_identifier,
    STATE(33), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4413] = 5,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(476), 1,
      anon_sym_times,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
  [4445] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(480), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(478), 2,
      sym_nothing,
      sym_identifier,
    STATE(35), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4489] = 5,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(482), 1,
      anon_sym_to,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
  [4521] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(486), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(484), 2,
      sym_nothing,
      sym_identifier,
    STATE(23), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4565] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(490), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(488), 2,
      sym_nothing,
      sym_identifier,
    STATE(28), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4609] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(494), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(492), 2,
      sym_nothing,
      sym_identifier,
    STATE(104), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4653] = 5,
    ACTIONS(51), 1,
      anon_sym_LBRACK,
    ACTIONS(496), 1,
      anon_sym_from,
    STATE(92), 1,
      sym_binary_operator,
    ACTIONS(55), 2,
      anon_sym_islessthan,
      anon_sym_isgreaterthan,
    ACTIONS(53), 16,
      anon_sym_PLUS,
      anon_sym_DASH,
      anon_sym_STAR,
      anon_sym_SLASH,
      anon_sym_isequalto,
      anon_sym_equals,
      anon_sym_isnotequalto,
      anon_sym_islessthanorequalto,
      anon_sym_isgreaterthanorequalto,
      anon_sym_and,
      anon_sym_or,
      anon_sym_addedto,
      anon_sym_contains,
      anon_sym_startswith,
      anon_sym_endswith,
      anon_sym_isin,
  [4685] = 11,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(386), 1,
      anon_sym_call,
    ACTIONS(500), 1,
      sym_number,
    STATE(97), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(498), 2,
      sym_nothing,
      sym_identifier,
    STATE(9), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4729] = 11,
    ACTIONS(225), 1,
      anon_sym_call,
    ACTIONS(229), 1,
      anon_sym_DQUOTE,
    ACTIONS(233), 1,
      anon_sym_LBRACK,
    ACTIONS(235), 1,
      anon_sym_not,
    ACTIONS(237), 1,
      anon_sym_lengthof,
    ACTIONS(239), 1,
      anon_sym_LPAREN,
    ACTIONS(504), 1,
      sym_number,
    STATE(102), 1,
      sym_unary_operator,
    ACTIONS(231), 2,
      anon_sym_true,
      anon_sym_false,
    ACTIONS(502), 2,
      sym_nothing,
      sym_identifier,
    STATE(34), 9,
      sym__expression,
      sym_string,
      sym_boolean,
      sym_list_literal,
      sym_binary_expression,
      sym_unary_expression,
      sym_call_expression,
      sym_index_expression,
      sym_parenthesized_expression,
  [4773] = 5,
    ACTIONS(506), 1,
      anon_sym_endnote,
    ACTIONS(508), 1,
      aux_sym_block_comment_content_token1,
    STATE(117), 1,
      aux_sym_block_comment_content_repeat1,
    STATE(144), 1,
      sym_block_comment_content,
    ACTIONS(510), 7,
      aux_sym_block_comment_content_token2,
      aux_sym_block_comment_content_token3,
      aux_sym_block_comment_content_token4,
      aux_sym_block_comment_content_token5,
      aux_sym_block_comment_content_token6,
      aux_sym_block_comment_content_token7,
      aux_sym_block_comment_content_token8,
  [4795] = 2,
    ACTIONS(514), 5,
      sym_number,
      anon_sym_DQUOTE,
      anon_sym_LBRACK,
      anon_sym_lengthof,
      anon_sym_LPAREN,
    ACTIONS(512), 6,
      anon_sym_call,
      anon_sym_true,
      anon_sym_false,
      sym_nothing,
      anon_sym_not,
      sym_identifier,
  [4811] = 2,
    ACTIONS(518), 5,
      sym_number,
      anon_sym_DQUOTE,
      anon_sym_LBRACK,
      anon_sym_lengthof,
      anon_sym_LPAREN,
    ACTIONS(516), 6,
      anon_sym_call,
      anon_sym_true,
      anon_sym_false,
      sym_nothing,
      anon_sym_not,
      sym_identifier,
  [4827] = 4,
    ACTIONS(520), 1,
      anon_sym_endnote,
    ACTIONS(522), 1,
      aux_sym_block_comment_content_token1,
    STATE(116), 1,
      aux_sym_block_comment_content_repeat1,
    ACTIONS(525), 7,
      aux_sym_block_comment_content_token2,
      aux_sym_block_comment_content_token3,
      aux_sym_block_comment_content_token4,
      aux_sym_block_comment_content_token5,
      aux_sym_block_comment_content_token6,
      aux_sym_block_comment_content_token7,
      aux_sym_block_comment_content_token8,
  [4846] = 4,
    ACTIONS(528), 1,
      anon_sym_endnote,
    ACTIONS(530), 1,
      aux_sym_block_comment_content_token1,
    STATE(116), 1,
      aux_sym_block_comment_content_repeat1,
    ACTIONS(532), 7,
      aux_sym_block_comment_content_token2,
      aux_sym_block_comment_content_token3,
      aux_sym_block_comment_content_token4,
      aux_sym_block_comment_content_token5,
      aux_sym_block_comment_content_token6,
      aux_sym_block_comment_content_token7,
      aux_sym_block_comment_content_token8,
  [4865] = 2,
    STATE(59), 1,
      sym_type,
    ACTIONS(534), 5,
      anon_sym_number,
      anon_sym_text,
      anon_sym_boolean,
      anon_sym_list,
      anon_sym_table,
  [4876] = 2,
    STATE(53), 1,
      sym_type,
    ACTIONS(536), 5,
      anon_sym_number,
      anon_sym_text,
      anon_sym_boolean,
      anon_sym_list,
      anon_sym_table,
  [4887] = 2,
    STATE(63), 1,
      sym_type,
    ACTIONS(534), 5,
      anon_sym_number,
      anon_sym_text,
      anon_sym_boolean,
      anon_sym_list,
      anon_sym_table,
  [4898] = 2,
    STATE(48), 1,
      sym_type,
    ACTIONS(536), 5,
      anon_sym_number,
      anon_sym_text,
      anon_sym_boolean,
      anon_sym_list,
      anon_sym_table,
  [4909] = 5,
    ACTIONS(538), 1,
      anon_sym_DQUOTE,
    ACTIONS(540), 1,
      aux_sym_string_content_token1,
    ACTIONS(542), 1,
      sym_escape_sequence,
    STATE(124), 1,
      aux_sym_string_content_repeat1,
    STATE(133), 1,
      sym_string_content,
  [4925] = 4,
    ACTIONS(544), 1,
      anon_sym_DQUOTE,
    ACTIONS(546), 1,
      aux_sym_string_content_token1,
    ACTIONS(549), 1,
      sym_escape_sequence,
    STATE(123), 1,
      aux_sym_string_content_repeat1,
  [4938] = 4,
    ACTIONS(552), 1,
      anon_sym_DQUOTE,
    ACTIONS(554), 1,
      aux_sym_string_content_token1,
    ACTIONS(556), 1,
      sym_escape_sequence,
    STATE(123), 1,
      aux_sym_string_content_repeat1,
  [4951] = 3,
    ACTIONS(558), 1,
      sym_identifier,
    STATE(40), 1,
      sym_parameter,
    STATE(52), 1,
      sym_parameter_list,
  [4961] = 2,
    ACTIONS(558), 1,
      sym_identifier,
    STATE(47), 1,
      sym_parameter,
  [4968] = 1,
    ACTIONS(560), 1,
      sym_identifier,
  [4972] = 1,
    ACTIONS(562), 1,
      sym_identifier,
  [4976] = 1,
    ACTIONS(564), 1,
      ts_builtin_sym_end,
  [4980] = 1,
    ACTIONS(566), 1,
      sym_identifier,
  [4984] = 1,
    ACTIONS(568), 1,
      sym_identifier,
  [4988] = 1,
    ACTIONS(570), 1,
      anon_sym_as,
  [4992] = 1,
    ACTIONS(572), 1,
      anon_sym_DQUOTE,
  [4996] = 1,
    ACTIONS(574), 1,
      anon_sym_in,
  [5000] = 1,
    ACTIONS(576), 1,
      sym_identifier,
  [5004] = 1,
    ACTIONS(578), 1,
      sym_identifier,
  [5008] = 1,
    ACTIONS(580), 1,
      anon_sym_RBRACK,
  [5012] = 1,
    ACTIONS(582), 1,
      sym_identifier,
  [5016] = 1,
    ACTIONS(584), 1,
      sym_identifier,
  [5020] = 1,
    ACTIONS(586), 1,
      sym_identifier,
  [5024] = 1,
    ACTIONS(588), 1,
      sym_identifier,
  [5028] = 1,
    ACTIONS(590), 1,
      anon_sym_to,
  [5032] = 1,
    ACTIONS(592), 1,
      sym_identifier,
  [5036] = 1,
    ACTIONS(594), 1,
      anon_sym_endnote,
  [5040] = 1,
    ACTIONS(596), 1,
      sym_identifier,
  [5044] = 1,
    ACTIONS(598), 1,
      sym_identifier,
  [5048] = 1,
    ACTIONS(600), 1,
      anon_sym_as,
  [5052] = 1,
    ACTIONS(602), 1,
      sym_identifier,
  [5056] = 1,
    ACTIONS(604), 1,
      sym_identifier,
  [5060] = 1,
    ACTIONS(606), 1,
      anon_sym_as,
};

static const uint32_t ts_small_parse_table_map[] = {
  [SMALL_STATE(2)] = 0,
  [SMALL_STATE(3)] = 68,
  [SMALL_STATE(4)] = 130,
  [SMALL_STATE(5)] = 191,
  [SMALL_STATE(6)] = 252,
  [SMALL_STATE(7)] = 321,
  [SMALL_STATE(8)] = 382,
  [SMALL_STATE(9)] = 441,
  [SMALL_STATE(10)] = 506,
  [SMALL_STATE(11)] = 562,
  [SMALL_STATE(12)] = 618,
  [SMALL_STATE(13)] = 678,
  [SMALL_STATE(14)] = 734,
  [SMALL_STATE(15)] = 794,
  [SMALL_STATE(16)] = 850,
  [SMALL_STATE(17)] = 906,
  [SMALL_STATE(18)] = 962,
  [SMALL_STATE(19)] = 1018,
  [SMALL_STATE(20)] = 1074,
  [SMALL_STATE(21)] = 1130,
  [SMALL_STATE(22)] = 1189,
  [SMALL_STATE(23)] = 1248,
  [SMALL_STATE(24)] = 1317,
  [SMALL_STATE(25)] = 1381,
  [SMALL_STATE(26)] = 1476,
  [SMALL_STATE(27)] = 1571,
  [SMALL_STATE(28)] = 1629,
  [SMALL_STATE(29)] = 1685,
  [SMALL_STATE(30)] = 1741,
  [SMALL_STATE(31)] = 1797,
  [SMALL_STATE(32)] = 1853,
  [SMALL_STATE(33)] = 1923,
  [SMALL_STATE(34)] = 1979,
  [SMALL_STATE(35)] = 2035,
  [SMALL_STATE(36)] = 2091,
  [SMALL_STATE(37)] = 2137,
  [SMALL_STATE(38)] = 2183,
  [SMALL_STATE(39)] = 2226,
  [SMALL_STATE(40)] = 2269,
  [SMALL_STATE(41)] = 2306,
  [SMALL_STATE(42)] = 2345,
  [SMALL_STATE(43)] = 2382,
  [SMALL_STATE(44)] = 2419,
  [SMALL_STATE(45)] = 2453,
  [SMALL_STATE(46)] = 2493,
  [SMALL_STATE(47)] = 2525,
  [SMALL_STATE(48)] = 2557,
  [SMALL_STATE(49)] = 2589,
  [SMALL_STATE(50)] = 2623,
  [SMALL_STATE(51)] = 2661,
  [SMALL_STATE(52)] = 2697,
  [SMALL_STATE(53)] = 2728,
  [SMALL_STATE(54)] = 2759,
  [SMALL_STATE(55)] = 2790,
  [SMALL_STATE(56)] = 2824,
  [SMALL_STATE(57)] = 2856,
  [SMALL_STATE(58)] = 2888,
  [SMALL_STATE(59)] = 2919,
  [SMALL_STATE(60)] = 2948,
  [SMALL_STATE(61)] = 2975,
  [SMALL_STATE(62)] = 3002,
  [SMALL_STATE(63)] = 3029,
  [SMALL_STATE(64)] = 3058,
  [SMALL_STATE(65)] = 3084,
  [SMALL_STATE(66)] = 3110,
  [SMALL_STATE(67)] = 3136,
  [SMALL_STATE(68)] = 3162,
  [SMALL_STATE(69)] = 3188,
  [SMALL_STATE(70)] = 3214,
  [SMALL_STATE(71)] = 3264,
  [SMALL_STATE(72)] = 3290,
  [SMALL_STATE(73)] = 3316,
  [SMALL_STATE(74)] = 3342,
  [SMALL_STATE(75)] = 3368,
  [SMALL_STATE(76)] = 3394,
  [SMALL_STATE(77)] = 3420,
  [SMALL_STATE(78)] = 3446,
  [SMALL_STATE(79)] = 3472,
  [SMALL_STATE(80)] = 3498,
  [SMALL_STATE(81)] = 3524,
  [SMALL_STATE(82)] = 3550,
  [SMALL_STATE(83)] = 3576,
  [SMALL_STATE(84)] = 3602,
  [SMALL_STATE(85)] = 3628,
  [SMALL_STATE(86)] = 3654,
  [SMALL_STATE(87)] = 3680,
  [SMALL_STATE(88)] = 3727,
  [SMALL_STATE(89)] = 3774,
  [SMALL_STATE(90)] = 3821,
  [SMALL_STATE(91)] = 3865,
  [SMALL_STATE(92)] = 3897,
  [SMALL_STATE(93)] = 3941,
  [SMALL_STATE(94)] = 3985,
  [SMALL_STATE(95)] = 4029,
  [SMALL_STATE(96)] = 4073,
  [SMALL_STATE(97)] = 4117,
  [SMALL_STATE(98)] = 4161,
  [SMALL_STATE(99)] = 4205,
  [SMALL_STATE(100)] = 4249,
  [SMALL_STATE(101)] = 4281,
  [SMALL_STATE(102)] = 4325,
  [SMALL_STATE(103)] = 4369,
  [SMALL_STATE(104)] = 4413,
  [SMALL_STATE(105)] = 4445,
  [SMALL_STATE(106)] = 4489,
  [SMALL_STATE(107)] = 4521,
  [SMALL_STATE(108)] = 4565,
  [SMALL_STATE(109)] = 4609,
  [SMALL_STATE(110)] = 4653,
  [SMALL_STATE(111)] = 4685,
  [SMALL_STATE(112)] = 4729,
  [SMALL_STATE(113)] = 4773,
  [SMALL_STATE(114)] = 4795,
  [SMALL_STATE(115)] = 4811,
  [SMALL_STATE(116)] = 4827,
  [SMALL_STATE(117)] = 4846,
  [SMALL_STATE(118)] = 4865,
  [SMALL_STATE(119)] = 4876,
  [SMALL_STATE(120)] = 4887,
  [SMALL_STATE(121)] = 4898,
  [SMALL_STATE(122)] = 4909,
  [SMALL_STATE(123)] = 4925,
  [SMALL_STATE(124)] = 4938,
  [SMALL_STATE(125)] = 4951,
  [SMALL_STATE(126)] = 4961,
  [SMALL_STATE(127)] = 4968,
  [SMALL_STATE(128)] = 4972,
  [SMALL_STATE(129)] = 4976,
  [SMALL_STATE(130)] = 4980,
  [SMALL_STATE(131)] = 4984,
  [SMALL_STATE(132)] = 4988,
  [SMALL_STATE(133)] = 4992,
  [SMALL_STATE(134)] = 4996,
  [SMALL_STATE(135)] = 5000,
  [SMALL_STATE(136)] = 5004,
  [SMALL_STATE(137)] = 5008,
  [SMALL_STATE(138)] = 5012,
  [SMALL_STATE(139)] = 5016,
  [SMALL_STATE(140)] = 5020,
  [SMALL_STATE(141)] = 5024,
  [SMALL_STATE(142)] = 5028,
  [SMALL_STATE(143)] = 5032,
  [SMALL_STATE(144)] = 5036,
  [SMALL_STATE(145)] = 5040,
  [SMALL_STATE(146)] = 5044,
  [SMALL_STATE(147)] = 5048,
  [SMALL_STATE(148)] = 5052,
  [SMALL_STATE(149)] = 5056,
  [SMALL_STATE(150)] = 5060,
};

static const TSParseActionEntry ts_parse_actions[] = {
  [0] = {.entry = {.count = 0, .reusable = false}},
  [1] = {.entry = {.count = 1, .reusable = false}}, RECOVER(),
  [3] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_source_file, 0),
  [5] = {.entry = {.count = 1, .reusable = true}}, SHIFT(77),
  [7] = {.entry = {.count = 1, .reusable = true}}, SHIFT(55),
  [9] = {.entry = {.count = 1, .reusable = true}}, SHIFT(58),
  [11] = {.entry = {.count = 1, .reusable = true}}, SHIFT(113),
  [13] = {.entry = {.count = 1, .reusable = true}}, SHIFT(143),
  [15] = {.entry = {.count = 1, .reusable = true}}, SHIFT(141),
  [17] = {.entry = {.count = 1, .reusable = true}}, SHIFT(140),
  [19] = {.entry = {.count = 1, .reusable = true}}, SHIFT(139),
  [21] = {.entry = {.count = 1, .reusable = true}}, SHIFT(128),
  [23] = {.entry = {.count = 1, .reusable = true}}, SHIFT(136),
  [25] = {.entry = {.count = 1, .reusable = true}}, SHIFT(105),
  [27] = {.entry = {.count = 1, .reusable = true}}, SHIFT(135),
  [29] = {.entry = {.count = 1, .reusable = true}}, SHIFT(32),
  [31] = {.entry = {.count = 1, .reusable = true}}, SHIFT(26),
  [33] = {.entry = {.count = 1, .reusable = true}}, SHIFT(107),
  [35] = {.entry = {.count = 1, .reusable = true}}, SHIFT(109),
  [37] = {.entry = {.count = 1, .reusable = true}}, SHIFT(127),
  [39] = {.entry = {.count = 1, .reusable = true}}, SHIFT(112),
  [41] = {.entry = {.count = 1, .reusable = true}}, SHIFT(45),
  [43] = {.entry = {.count = 1, .reusable = true}}, SHIFT(95),
  [45] = {.entry = {.count = 1, .reusable = true}}, SHIFT(98),
  [47] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_argument_list, 1),
  [49] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_argument_list, 1),
  [51] = {.entry = {.count = 1, .reusable = true}}, SHIFT(101),
  [53] = {.entry = {.count = 1, .reusable = true}}, SHIFT(115),
  [55] = {.entry = {.count = 1, .reusable = false}}, SHIFT(115),
  [57] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_call_expression, 2),
  [59] = {.entry = {.count = 1, .reusable = true}}, SHIFT(89),
  [61] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_call_expression, 2),
  [63] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_binary_expression, 3),
  [65] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_binary_expression, 3),
  [67] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_unary_expression, 2),
  [69] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_unary_expression, 2),
  [71] = {.entry = {.count = 1, .reusable = true}}, SHIFT(111),
  [73] = {.entry = {.count = 1, .reusable = true}}, REDUCE(aux_sym_argument_list_repeat1, 2),
  [75] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_argument_list_repeat1, 2), SHIFT_REPEAT(111),
  [78] = {.entry = {.count = 1, .reusable = false}}, REDUCE(aux_sym_argument_list_repeat1, 2),
  [80] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_argument_list, 2),
  [82] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_argument_list, 2),
  [84] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_boolean, 1),
  [86] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_boolean, 1),
  [88] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_string, 2),
  [90] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_string, 2),
  [92] = {.entry = {.count = 1, .reusable = true}}, SHIFT(88),
  [94] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_index_expression, 4),
  [96] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_index_expression, 4),
  [98] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_list_literal, 2),
  [100] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_list_literal, 2),
  [102] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_parenthesized_expression, 3),
  [104] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_parenthesized_expression, 3),
  [106] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_with_clause, 2),
  [108] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_with_clause, 2),
  [110] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_list_literal, 3),
  [112] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_list_literal, 3),
  [114] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_string, 3),
  [116] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_string, 3),
  [118] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_call_expression, 3),
  [120] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_call_expression, 3),
  [122] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_if_statement, 2),
  [124] = {.entry = {.count = 1, .reusable = true}}, SHIFT(93),
  [126] = {.entry = {.count = 1, .reusable = false}}, SHIFT(86),
  [128] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_if_statement, 2),
  [130] = {.entry = {.count = 1, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2),
  [132] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(77),
  [135] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(55),
  [138] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(58),
  [141] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(113),
  [144] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(143),
  [147] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(141),
  [150] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(140),
  [153] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(139),
  [156] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(128),
  [159] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(136),
  [162] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(105),
  [165] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(135),
  [168] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(32),
  [171] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(25),
  [174] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(107),
  [177] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(109),
  [180] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(127),
  [183] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(112),
  [186] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(45),
  [189] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(95),
  [192] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2), SHIFT_REPEAT(98),
  [195] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_source_file, 1),
  [197] = {.entry = {.count = 1, .reusable = true}}, SHIFT(25),
  [199] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_otherwise_if_clause, 2),
  [201] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_otherwise_if_clause, 2),
  [203] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_declaration, 7),
  [205] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_declaration, 7),
  [207] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_assignment, 4),
  [209] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_assignment, 4),
  [211] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_return_statement, 2),
  [213] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_return_statement, 2),
  [215] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_for_each_statement, 4),
  [217] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_for_each_statement, 4),
  [219] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_return_statement, 1),
  [221] = {.entry = {.count = 1, .reusable = false}}, SHIFT(30),
  [223] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_return_statement, 1),
  [225] = {.entry = {.count = 1, .reusable = false}}, SHIFT(145),
  [227] = {.entry = {.count = 1, .reusable = true}}, SHIFT(30),
  [229] = {.entry = {.count = 1, .reusable = true}}, SHIFT(122),
  [231] = {.entry = {.count = 1, .reusable = false}}, SHIFT(10),
  [233] = {.entry = {.count = 1, .reusable = true}}, SHIFT(70),
  [235] = {.entry = {.count = 1, .reusable = false}}, SHIFT(114),
  [237] = {.entry = {.count = 1, .reusable = true}}, SHIFT(114),
  [239] = {.entry = {.count = 1, .reusable = true}}, SHIFT(99),
  [241] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_declaration, 6),
  [243] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_declaration, 6),
  [245] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_while_statement, 2),
  [247] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_while_statement, 2),
  [249] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_display_statement, 2),
  [251] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_display_statement, 2),
  [253] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_step_def, 2),
  [255] = {.entry = {.count = 1, .reusable = true}}, SHIFT(148),
  [257] = {.entry = {.count = 1, .reusable = true}}, SHIFT(125),
  [259] = {.entry = {.count = 1, .reusable = true}}, SHIFT(119),
  [261] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_step_def, 2),
  [263] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_riser_def, 2),
  [265] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_riser_def, 2),
  [267] = {.entry = {.count = 1, .reusable = true}}, REDUCE(aux_sym_step_clauses_repeat1, 2),
  [269] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_step_clauses_repeat1, 2), SHIFT_REPEAT(148),
  [272] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_step_clauses_repeat1, 2), SHIFT_REPEAT(125),
  [275] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_step_clauses_repeat1, 2), SHIFT_REPEAT(119),
  [278] = {.entry = {.count = 1, .reusable = false}}, REDUCE(aux_sym_step_clauses_repeat1, 2),
  [280] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_step_clauses, 1),
  [282] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_step_clauses, 1),
  [284] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_parameter_list, 1),
  [286] = {.entry = {.count = 1, .reusable = true}}, SHIFT(126),
  [288] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_parameter_list, 1),
  [290] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_if_statement, 3),
  [292] = {.entry = {.count = 1, .reusable = true}}, REDUCE(aux_sym_parameter_list_repeat1, 2),
  [294] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_parameter_list_repeat1, 2), SHIFT_REPEAT(126),
  [297] = {.entry = {.count = 1, .reusable = false}}, REDUCE(aux_sym_parameter_list_repeat1, 2),
  [299] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_parameter_list, 2),
  [301] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_parameter_list, 2),
  [303] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_attempt_statement, 1),
  [305] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_attempt_statement, 1),
  [307] = {.entry = {.count = 1, .reusable = true}}, SHIFT(61),
  [309] = {.entry = {.count = 1, .reusable = true}}, SHIFT(64),
  [311] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_type, 1),
  [313] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_type, 1),
  [315] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_parameter, 3),
  [317] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_parameter, 3),
  [319] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_call_statement, 2),
  [321] = {.entry = {.count = 1, .reusable = true}}, SHIFT(87),
  [323] = {.entry = {.count = 1, .reusable = true}}, SHIFT(130),
  [325] = {.entry = {.count = 1, .reusable = true}}, REDUCE(aux_sym_if_statement_repeat1, 2),
  [327] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_if_statement_repeat1, 2), SHIFT_REPEAT(93),
  [330] = {.entry = {.count = 1, .reusable = false}}, REDUCE(aux_sym_if_statement_repeat1, 2),
  [332] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_expects_clause, 2),
  [334] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_expects_clause, 2),
  [336] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_returns_clause, 2),
  [338] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_returns_clause, 2),
  [340] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_belongs_clause, 2),
  [342] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_belongs_clause, 2),
  [344] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_section_marker, 1),
  [346] = {.entry = {.count = 1, .reusable = false}}, SHIFT(132),
  [348] = {.entry = {.count = 1, .reusable = false}}, SHIFT(131),
  [350] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_section_marker, 1),
  [352] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_attempt_statement, 2),
  [354] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_call_statement, 3),
  [356] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_comment, 1),
  [358] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_comment, 1),
  [360] = {.entry = {.count = 1, .reusable = false}}, SHIFT(72),
  [362] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_declaration, 4),
  [364] = {.entry = {.count = 1, .reusable = true}}, SHIFT(103),
  [366] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_if_unsuccessful_clause, 1),
  [368] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_declaration, 5),
  [370] = {.entry = {.count = 1, .reusable = true}}, SHIFT(108),
  [372] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_then_continue_clause, 1),
  [374] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_call_statement, 4),
  [376] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_if_statement, 4),
  [378] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_structure_definition, 1),
  [380] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_step_def, 3),
  [382] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_riser_def, 3),
  [384] = {.entry = {.count = 1, .reusable = false}}, SHIFT(24),
  [386] = {.entry = {.count = 1, .reusable = false}}, SHIFT(146),
  [388] = {.entry = {.count = 1, .reusable = true}}, SHIFT(24),
  [390] = {.entry = {.count = 1, .reusable = true}}, SHIFT(15),
  [392] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_block_comment, 3),
  [394] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_comment, 2),
  [396] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_add_statement, 4),
  [398] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_storing_clause, 2),
  [400] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_remove_statement, 4),
  [402] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_block_comment, 2),
  [404] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_input_statement, 2),
  [406] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_attempt_statement, 3),
  [408] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_repeat_statement, 3),
  [410] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_floor_def, 2),
  [412] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_building_def, 2),
  [414] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_otherwise_clause, 1),
  [416] = {.entry = {.count = 1, .reusable = false}}, SHIFT(6),
  [418] = {.entry = {.count = 1, .reusable = true}}, SHIFT(6),
  [420] = {.entry = {.count = 1, .reusable = false}}, SHIFT(2),
  [422] = {.entry = {.count = 1, .reusable = true}}, SHIFT(2),
  [424] = {.entry = {.count = 1, .reusable = false}}, SHIFT(29),
  [426] = {.entry = {.count = 1, .reusable = true}}, SHIFT(29),
  [428] = {.entry = {.count = 1, .reusable = true}}, SHIFT(16),
  [430] = {.entry = {.count = 1, .reusable = false}}, SHIFT(21),
  [432] = {.entry = {.count = 1, .reusable = true}}, SHIFT(21),
  [434] = {.entry = {.count = 1, .reusable = false}}, SHIFT(27),
  [436] = {.entry = {.count = 1, .reusable = true}}, SHIFT(27),
  [438] = {.entry = {.count = 1, .reusable = false}}, SHIFT(31),
  [440] = {.entry = {.count = 1, .reusable = true}}, SHIFT(31),
  [442] = {.entry = {.count = 1, .reusable = false}}, SHIFT(106),
  [444] = {.entry = {.count = 1, .reusable = true}}, SHIFT(106),
  [446] = {.entry = {.count = 1, .reusable = false}}, SHIFT(4),
  [448] = {.entry = {.count = 1, .reusable = true}}, SHIFT(4),
  [450] = {.entry = {.count = 1, .reusable = false}}, SHIFT(5),
  [452] = {.entry = {.count = 1, .reusable = true}}, SHIFT(5),
  [454] = {.entry = {.count = 1, .reusable = false}}, SHIFT(110),
  [456] = {.entry = {.count = 1, .reusable = true}}, SHIFT(110),
  [458] = {.entry = {.count = 1, .reusable = false}}, SHIFT(91),
  [460] = {.entry = {.count = 1, .reusable = true}}, SHIFT(91),
  [462] = {.entry = {.count = 1, .reusable = true}}, SHIFT(13),
  [464] = {.entry = {.count = 1, .reusable = false}}, SHIFT(100),
  [466] = {.entry = {.count = 1, .reusable = true}}, SHIFT(100),
  [468] = {.entry = {.count = 1, .reusable = false}}, SHIFT(22),
  [470] = {.entry = {.count = 1, .reusable = true}}, SHIFT(22),
  [472] = {.entry = {.count = 1, .reusable = false}}, SHIFT(33),
  [474] = {.entry = {.count = 1, .reusable = true}}, SHIFT(33),
  [476] = {.entry = {.count = 1, .reusable = true}}, SHIFT(83),
  [478] = {.entry = {.count = 1, .reusable = false}}, SHIFT(35),
  [480] = {.entry = {.count = 1, .reusable = true}}, SHIFT(35),
  [482] = {.entry = {.count = 1, .reusable = true}}, SHIFT(138),
  [484] = {.entry = {.count = 1, .reusable = false}}, SHIFT(23),
  [486] = {.entry = {.count = 1, .reusable = true}}, SHIFT(23),
  [488] = {.entry = {.count = 1, .reusable = false}}, SHIFT(28),
  [490] = {.entry = {.count = 1, .reusable = true}}, SHIFT(28),
  [492] = {.entry = {.count = 1, .reusable = false}}, SHIFT(104),
  [494] = {.entry = {.count = 1, .reusable = true}}, SHIFT(104),
  [496] = {.entry = {.count = 1, .reusable = true}}, SHIFT(149),
  [498] = {.entry = {.count = 1, .reusable = false}}, SHIFT(9),
  [500] = {.entry = {.count = 1, .reusable = true}}, SHIFT(9),
  [502] = {.entry = {.count = 1, .reusable = false}}, SHIFT(34),
  [504] = {.entry = {.count = 1, .reusable = true}}, SHIFT(34),
  [506] = {.entry = {.count = 1, .reusable = false}}, SHIFT(79),
  [508] = {.entry = {.count = 1, .reusable = true}}, SHIFT(117),
  [510] = {.entry = {.count = 1, .reusable = false}}, SHIFT(117),
  [512] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_unary_operator, 1),
  [514] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_unary_operator, 1),
  [516] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_binary_operator, 1),
  [518] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_binary_operator, 1),
  [520] = {.entry = {.count = 1, .reusable = false}}, REDUCE(aux_sym_block_comment_content_repeat1, 2),
  [522] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_block_comment_content_repeat1, 2), SHIFT_REPEAT(116),
  [525] = {.entry = {.count = 2, .reusable = false}}, REDUCE(aux_sym_block_comment_content_repeat1, 2), SHIFT_REPEAT(116),
  [528] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_block_comment_content, 1),
  [530] = {.entry = {.count = 1, .reusable = true}}, SHIFT(116),
  [532] = {.entry = {.count = 1, .reusable = false}}, SHIFT(116),
  [534] = {.entry = {.count = 1, .reusable = true}}, SHIFT(60),
  [536] = {.entry = {.count = 1, .reusable = true}}, SHIFT(46),
  [538] = {.entry = {.count = 1, .reusable = false}}, SHIFT(11),
  [540] = {.entry = {.count = 1, .reusable = true}}, SHIFT(124),
  [542] = {.entry = {.count = 1, .reusable = false}}, SHIFT(124),
  [544] = {.entry = {.count = 1, .reusable = false}}, REDUCE(aux_sym_string_content_repeat1, 2),
  [546] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_string_content_repeat1, 2), SHIFT_REPEAT(123),
  [549] = {.entry = {.count = 2, .reusable = false}}, REDUCE(aux_sym_string_content_repeat1, 2), SHIFT_REPEAT(123),
  [552] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_string_content, 1),
  [554] = {.entry = {.count = 1, .reusable = true}}, SHIFT(123),
  [556] = {.entry = {.count = 1, .reusable = false}}, SHIFT(123),
  [558] = {.entry = {.count = 1, .reusable = true}}, SHIFT(147),
  [560] = {.entry = {.count = 1, .reusable = true}}, SHIFT(134),
  [562] = {.entry = {.count = 1, .reusable = true}}, SHIFT(142),
  [564] = {.entry = {.count = 1, .reusable = true}},  ACCEPT_INPUT(),
  [566] = {.entry = {.count = 1, .reusable = true}}, SHIFT(76),
  [568] = {.entry = {.count = 1, .reusable = true}}, SHIFT(150),
  [570] = {.entry = {.count = 1, .reusable = true}}, SHIFT(118),
  [572] = {.entry = {.count = 1, .reusable = true}}, SHIFT(19),
  [574] = {.entry = {.count = 1, .reusable = true}}, SHIFT(94),
  [576] = {.entry = {.count = 1, .reusable = true}}, SHIFT(81),
  [578] = {.entry = {.count = 1, .reusable = true}}, SHIFT(50),
  [580] = {.entry = {.count = 1, .reusable = true}}, SHIFT(18),
  [582] = {.entry = {.count = 1, .reusable = true}}, SHIFT(73),
  [584] = {.entry = {.count = 1, .reusable = true}}, SHIFT(37),
  [586] = {.entry = {.count = 1, .reusable = true}}, SHIFT(36),
  [588] = {.entry = {.count = 1, .reusable = true}}, SHIFT(84),
  [590] = {.entry = {.count = 1, .reusable = true}}, SHIFT(90),
  [592] = {.entry = {.count = 1, .reusable = true}}, SHIFT(85),
  [594] = {.entry = {.count = 1, .reusable = true}}, SHIFT(71),
  [596] = {.entry = {.count = 1, .reusable = true}}, SHIFT(12),
  [598] = {.entry = {.count = 1, .reusable = true}}, SHIFT(3),
  [600] = {.entry = {.count = 1, .reusable = true}}, SHIFT(121),
  [602] = {.entry = {.count = 1, .reusable = true}}, SHIFT(54),
  [604] = {.entry = {.count = 1, .reusable = true}}, SHIFT(78),
  [606] = {.entry = {.count = 1, .reusable = true}}, SHIFT(120),
};

#ifdef __cplusplus
extern "C" {
#endif
#ifdef _WIN32
#define extern __declspec(dllexport)
#endif

extern const TSLanguage *tree_sitter_steps(void) {
  static const TSLanguage language = {
    .version = LANGUAGE_VERSION,
    .symbol_count = SYMBOL_COUNT,
    .alias_count = ALIAS_COUNT,
    .token_count = TOKEN_COUNT,
    .external_token_count = EXTERNAL_TOKEN_COUNT,
    .state_count = STATE_COUNT,
    .large_state_count = LARGE_STATE_COUNT,
    .production_id_count = PRODUCTION_ID_COUNT,
    .field_count = FIELD_COUNT,
    .max_alias_sequence_length = MAX_ALIAS_SEQUENCE_LENGTH,
    .parse_table = &ts_parse_table[0][0],
    .small_parse_table = ts_small_parse_table,
    .small_parse_table_map = ts_small_parse_table_map,
    .parse_actions = ts_parse_actions,
    .symbol_names = ts_symbol_names,
    .symbol_metadata = ts_symbol_metadata,
    .public_symbol_map = ts_symbol_map,
    .alias_map = ts_non_terminal_alias_map,
    .alias_sequences = &ts_alias_sequences[0][0],
    .lex_modes = ts_lex_modes,
    .lex_fn = ts_lex,
    .keyword_lex_fn = ts_lex_keywords,
    .keyword_capture_token = sym_identifier,
    .primary_state_ids = ts_primary_state_ids,
  };
  return &language;
}
#ifdef __cplusplus
}
#endif
