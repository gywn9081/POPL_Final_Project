grammar Arithmetic;

start : expr;
expr : expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | '(' expr ')'
    | INT;


INT : [0-9]+;
// Need to account for python not caring about whitespace (kinda); the space is important
// Please note this will not work if we are determining tabs between blocks
WS : [ \t\r\n]+ -> skip;