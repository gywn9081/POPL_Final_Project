grammar Arithmetic;


///////////////////////////
// Expresions start here //
///////////////////////////

// This kinda works but newlines are valid in expressions if they are in parantheses
start
    : (statementOrEmptyLine)* EOF
    ;

statementOrEmptyLine
    : assignExpr NEWLINE?
    | NEWLINE  // empty line
    ;

assignExpr
    : ID ASSIGN_OP assignExpr
    | expr
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

// 3rd Deliverable will need for and while loops
// Comments
// Nesting

// Lexer rules
ASSIGN_OP : '=' | '+=' | '-=' | '*=' | '/=';
COMPARISON_OP : '>' | '>=' | '<' | '<=' | '==' | '!=';


ID : [a-zA-Z_][a-zA-Z_0-9]*;
INT : [0-9.]+;
STRING 
    : '"""' .*? '"""' // Double quotes triple strings
    | '\'\'\'' .*? '\'\'\'' // Single qoutes triple strings
    | '"' (~["\r\n])* '"'
    |'\'' (~['"\r\n])* '\''
    ; // Note you don't need alternate chars here

ELEMENT : (ID|INT|STRING);



// Need to account for python not caring about whitespace (kinda); the space is important
// Please note this will not work if we are determining tabs between blocks
NEWLINE : ('\r\n' | '\n'); // Work for windows and unix style line endings
WS : [ \t]+ -> skip; // This is fine for now

// We will just ignore one line comments
COMMENT
    : '#' ~[\r\n]* -> skip  // Single line comment
    ;



// Source - https://stackoverflow.com/a/18797779
// Posted by Sam Harwell
// Retrieved 2025-11-18, License - CC BY-SA 3.0
// We are using the below lexer rule to move all lexer errors to parser to allow our tests to catch lexer errors.
ErrorChar : . ;
