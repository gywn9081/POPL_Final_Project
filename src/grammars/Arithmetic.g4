grammar Arithmetic;


///////////////////////////
// Expresions start here //
///////////////////////////

// This kinda works but newlines are valid in expressions if they are in parantheses
start
    : (statementOrEmptyLine)* EOF
    ;

statementOrEmptyLine
    : (assignExpr NEWLINE| assignExpr)
    | NEWLINE  // empty line
    ;


assignExpr
    : ID ASSIGN_OP assignExpr
    | expr
    ;


// Expression rules with precedence and unary support
expr
    : unaryExpr (('*' | '/' | '%') unaryExpr)*
    ;

// Add in unary operators
unaryExpr
    : ('+' | '-') unaryExpr                       
    | primaryExpr
    ;

primaryExpr
    : INT
    | ID
    | '(' expr ')'
    | STRING // Allow strings to be in the grammar
    ;

ASSIGN_OP : '=' | '+=' | '-=' | '*=' | '/=';

ID : [a-zA-Z_][a-zA-Z_0-9]*;
INT : [.0-9]+;
STRING : '"' ~["]* '"';
// Need to account for python not caring about whitespace (kinda); the space is important
// Please note this will not work if we are determining tabs between blocks
NEWLINE : ('\r\n' | '\n'); // Work for windows and unix style line endings
WS : [ \t]+ -> skip; // This is fine for now