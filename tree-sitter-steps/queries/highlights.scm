; Tree-sitter highlight queries for Steps language
; Simplified version that works with the current grammar

; Comments
(comment) @comment
(block_comment) @comment

; Structure keywords
"building:" @keyword.function
"floor:" @keyword.function
"step:" @keyword.function
"riser:" @keyword.function
"belongs to:" @keyword
"expects:" @keyword
"returns:" @keyword
"do:" @keyword
"declare:" @keyword

; Control flow keywords
"if" @keyword.control
"otherwise if" @keyword.control
"otherwise" @keyword.control
"repeat" @keyword.control
"times" @keyword.control
"for each" @keyword.control
"in" @keyword.control
"while" @keyword.control
"attempt:" @keyword.control
"if unsuccessful:" @keyword.control
"then continue:" @keyword.control
(exit_statement) @keyword.control

; Variable keywords
"set" @keyword
"to" @keyword
"as" @keyword
"fixed" @keyword

; Function keywords
"call" @keyword.function
"with" @keyword
"storing result in" @keyword
"return" @keyword.function
"display" @function.builtin
"input" @function.builtin

; List keywords
"add" @keyword
"remove" @keyword
"from" @keyword

; Types
(type) @type.builtin

; Literals
(number) @number
(string) @string
(boolean) @boolean
(nothing) @constant.builtin

; Operators
(binary_operator) @operator
(unary_operator) @operator

; Identifiers
(identifier) @variable

