// Expresions start here
// This kinda works but newlines are valid in expressions if they are in parantheses
start : (assignExpr NEWLINE)* (assignExpr NEWLINE| assignExpr) EOF; // allow multiple expressions per file

assignExpr
    : ID ASSIGN_OP assignExpr
    | expr
    ;



expr : expr ('*'|'/'|'%') expr
    | expr ('+'|'-') expr
    | '(' expr ')' 
    | INT
    | ID
    ;


ASSIGN_OP : '=' | '+=' | '-=' | '*=' | '/=';

ID : [a-zA-Z_][a-zA-Z_0-9]*;
INT : [0-9]+;
// Need to account for python not caring about whitespace (kinda); the space is important
// Please note this will not work if we are determining tabs between blocks
NEWLINE : ('\r\n' | '\n'); // Work for windows and unix style line endings
WS : [ \t]+ -> skip; // This is fine for now
