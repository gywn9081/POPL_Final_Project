grammar Arithmetic;

///////////////////////////
// Expresions start here //
///////////////////////////
// This kinda works but newlines are valid in expressions if they are in parantheses
start
    : (statementOrEmptyLine)* EOF
    ;

statementOrEmptyLine
    : STRING NEWLINE
    | COMMENT
    | assignExpr NEWLINE?
    | ifStmt
    | forStmt
    | whileStmt
    | blockStmt
    | NEWLINE  // empty line
    ;

simpleStmt
    : assignExpr NEWLINE?
    | NEWLINE  // empty line
    ;

assignExpr
    : ID ASSIGN_OP (assignExpr | expr)
    ;

// Forcing a Expression to eval to something is the problem with the parantheses tests
// Not allowing ')' in the middle bit kills this
// Expression rules with precedence and unary support
expr
    : additiveExpr
    ;

additiveExpr // This is needed because we were not allowing addition and subtraction between 
    : multiplicativeExpr (('+' | '-') multiplicativeExpr)*
    ;

multiplicativeExpr
    : unaryExpr (('*' | '/' | '%') unaryExpr)*
    ;

unaryExpr
    : ('+' | '-') unaryExpr
    | primaryExpr
    ;

primaryExpr
    : INT
    | ID
    | '('expr')'
    | STRING // Allow strings to be in the grammar
    | array
    ;

// Here is the array format
array
    : '[' (expr (',' expr)*)? (',')? ']'
    ;

// Need to allow if, elif, else statements

blockStmt
    : '<bang>' statementOrEmptyLine+ '<debang>' NEWLINE?;
    

ifStmt
    : IF conditionalExpr ':' NEWLINE blockStmt (elifBranch)* (elseBranch)? 
    ;

elifBranch
    : ELIF conditionalExpr ':' NEWLINE blockStmt
    ;

elseBranch
    : ELSE ':' NEWLINE blockStmt
    ;

whileStmt
    : WHILE conditionalExpr ':' NEWLINE blockStmt
    ;

forStmt
    : FOR ID 'in' (ID | array | 'range''(' (expr | expr ',' expr)')') ':' NEWLINE blockStmt
    ;

conditionalExpr
    : ID
    | INT
    | NOT_OP operand
    | operand COMPARISON_OP operand
    | '(' conditionalExpr ')'
    | conditionalExpr LOGICAL_OP conditionalExpr
    // | conditionalExpr
    ;

operand
    : ID
    | INT
    ;

// 3rd Deliverable will need for and while loops
// Comments
// Nesting

// Lexer rules
ASSIGN_OP : '=' | '+=' | '-=' | '*=' | '/=';
COMPARISON_OP : '>' | '>=' | '<' | '<=' | '==' | '!=';
LOGICAL_OP : 'and' | 'or';
NOT_OP : 'not';

IF      : 'if';
ELIF    : 'elif';
ELSE    : 'else';
WHILE   : 'while';
FOR     : 'for';

ID : [a-zA-Z_][a-zA-Z_0-9]*;
INT : ([0-9]+'.'?[0-9]* | '.'[0-9]+);

STRING 
    : '"""' .*? '"""' // Double quotes triple strings
    | '\'\'\'' .*? '\'\'\'' // Single qoutes triple strings
    | '"' (~["\r\n])* '"'
    | '\'' (~['"\r\n])* '\''
    ; // Note you don't need alternate chars here

ELEMENT : (ID|INT|STRING);

NEWLINE : ([\r\n]+);

INDENT : '<indent>';
DEDENT : '<dedent>';

WS : [ \t]+ -> skip; // This is fine for now

// We will just ignore one line comments
COMMENT : '#' ~[\r\n]*;  // Single line comment

COLON : ':';
LPAREN : '(';
RPAREN : ')';

// Source - https://stackoverflow.com/a/18797779
// Posted by Sam Harwell
// Retrieved 2025-11-18, License - CC BY-SA 3.0
// We are using the below lexer rule to move all lexer errors to parser to allow our tests to catch lexer errors.
ErrorChar : . ;