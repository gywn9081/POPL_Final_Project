grammar Arithmetic;

//@lexer::members {
//    from collections import deque
//    indentStack = deque([0])
//
//    def emit_indent(self, new_indent):
//        tok = self.commonToken(self.INDENT, "")
//        tok.line = self.getLine()
//        tok.column = 0
//        indentStack.append(new_indent)
//        return tok
//
//    def emit_dedent(self):
//        indentStack.pop()
//        tok = self.commonToken(self.DEDENT, "")
//        tok.line = self.getLine()
//        tok.column = 0
//        return tok
//
//    def commonToken(self, type, text):
//        from antlr4 import CommonToken
//        stop = self.getCharIndex() - 1
//        start = stop if text == "" else stop - len(text) + 1
//        return CommonToken(self._tokenFactorySourcePair, type,
//                           self.DEFAULT_TOKEN_CHANNEL, start, stop)
//}

//@lexer::header {
//    from collections import deque
//}


///////////////////////////
// Expresions start here //
///////////////////////////

// This kinda works but newlines are valid in expressions if they are in parantheses
start
    : (statementOrEmptyLine)* EOF
    ;

statementOrEmptyLine
    : assignExpr NEWLINE?
    | ifStmt
    | NEWLINE  // empty line
    ;

simpleStmt
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

blockStmt
    : (INDENT simpleStmt)+
    ;

ifStmt
    : IF conditionalExpr ':' NEWLINE blockStmt+ (elifBranch)* (elseBranch)?
    ;

elifBranch
    : ELIF conditionalExpr ':' NEWLINE blockStmt+
    ;

elseBranch
    : ELSE ':' NEWLINE blockStmt+
    ;

conditionalExpr
    : ID
    | INT
    | NOT_OP operand
    | operand COMPARISON_OP operand
    | '(' conditionalExpr ')'
    | conditionalExpr LOGICAL_OP conditionalExpr
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

ID : [a-zA-Z_][a-zA-Z_0-9]*;
INT : [0-9.]+;
STRING 
    : '"""' .*? '"""' // Double quotes triple strings
    | '\'\'\'' .*? '\'\'\'' // Single qoutes triple strings
    | '"' (~["\r\n])* '"'
    |'\'' (~['"\r\n])* '\''
    ; // Note you don't need alternate chars here

ELEMENT : (ID|INT|STRING);

//NEWLINE
//    :   ([\r\n]+)  {
//            newLine = self.text
//            spaces = 0
//            # Count leading spaces
//            la = self._input.LA(1)
//            while la == 32:  # space
//                spaces += 1
//                self._input.consume()
//                la = self._input.LA(1)
//
//            prev_indent = self.indentStack[-1]
//
//            # Emit NEWLINE token
//            self.type = PythonSubset.NEWLINE
//            self.channel = self.DEFAULT_TOKEN_CHANNEL
//
//            if la == -1:
//                # End of file, emit DEDENT tokens
//                from antlr4 import CommonToken
//                self._hitEOF = True
//                while len(self.indentStack) > 1:
//                    self.emit(self.emit_dedent())
//                return
//
//            if spaces > prev_indent:
//                self.emit(self.emit_indent(spaces))
//            else:
//                while spaces < prev_indent:
//                    self.emit(self.emit_dedent())
//                    prev_indent = self.indentStack[-1]
//        }
//    ;

NEWLINE : ([\r\n]+);

INDENT : '\t';
DEDENT : ;


WS : [ \t]+ -> skip; // This is fine for now

// We will just ignore one line comments
COMMENT
    : '#' ~[\r\n]* -> skip  // Single line comment
    ;

COLON : ':';
LPAREN : '(';
RPAREN : ')';

// Source - https://stackoverflow.com/a/18797779
// Posted by Sam Harwell
// Retrieved 2025-11-18, License - CC BY-SA 3.0
// We are using the below lexer rule to move all lexer errors to parser to allow our tests to catch lexer errors.
ErrorChar : . ;
