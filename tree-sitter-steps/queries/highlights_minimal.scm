; Minimal Steps highlight query for testing

; Comments
(comment) @comment
"note:" @comment

; Structure keywords
"building:" @keyword
"floor:" @keyword
"step:" @keyword
"riser:" @keyword
"do:" @keyword
"declare:" @keyword

; Control flow
"if" @keyword.control
"while" @keyword.control
(exit_statement) @keyword.control

; Identifiers
(identifier) @variable

