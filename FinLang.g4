grammar FinLang;

program
    : statement* EOF
    ;

statement
    : blockStmt
    | ifStmt
    | whileStmt
    | assignStmt
    | printStmt
    | breakStmt
    | leaveStmt
    | exitStmt
    ;

blockStmt
    : '{' statement* '}'
    ;

ifStmt
    : 'if' '(' expr ')' statement ('else' statement)?
    ;

whileStmt
    : 'while' '(' expr ')' statement
    ;

assignStmt
    : ID '=' expr ';'
    ;

printStmt
    : 'print' expr ';'
    ;

breakStmt
    : 'break' ';'
    ;

leaveStmt
    : 'leave' ';'
    ;

exitStmt
    : 'exit' ';'
    ;

expr
    : expr op=('*' | '/' | '%') expr              # MulDivModExpr
    | expr op=('+' | '-') expr                      # AddSubExpr
    | expr op=('<' | '<=' | '>' | '>=') expr        # RelationalExpr
    | expr op=('==' | '!=') expr                    # EqualityExpr
    | expr op='&' expr                              # NonShortAndExpr
    | expr op='|' expr                              # NonShortOrExpr
    | expr op='and' expr                            # AndExpr
    | expr op='or' expr                             # OrExpr
    | 'not' expr                                    # NotExpr
    | '(' expr ')'                                  # ParenExpr
    | BOOL                                          # BoolExpr
    | INT                                           # IntExpr
    | FLOAT                                         # FloatExpr
    | STRING                                        # StringExpr
    | CHAR                                          # CharExpr
    | ID                                            # IdExpr
    ;

BOOL: 'true' | 'false';
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' (~["\r\n\\] | '\\' .)* '"';
CHAR: '\'' (~['\r\n\\] | '\\' .) '\'';
ID: [a-zA-Z_][a-zA-Z0-9_]*;

COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;