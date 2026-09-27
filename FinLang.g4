grammar FinLang;

/* --- REGOLE SINTATTICHE --- */
program: statement* EOF ;

statement
    : '{' statement* '}'                               # BlockStmt
    | 'if' '(' expr ')' statement ('else' statement)?  # IfStmt
    | 'while' '(' expr ')' statement                   # WhileStmt
    | ID '=' expr ';'                                  # AssignStmt
    | 'print' expr ';'                                 # PrintStmt
    | 'break' ';'                                      # BreakStmt
    | 'exit' ';'                                       # ExitStmt
    ;

expr
    : 'not' expr                                       # NotExpr
    | expr op=('*'|'/'|'%') expr                       # MulDivModExpr
    | expr op=('+'|'-') expr                           # AddSubExpr
    | expr op=('<'|'<='|'>'|'>=') expr                 # RelationalExpr
    | expr op=('=='|'!=') expr                         # EqualityExpr
    | expr 'and' expr                                  # AndExpr
    | expr 'or' expr                                   # OrExpr
    | '(' expr ')'                                     # ParenExpr
    | ID                                               # IdExpr
    | INT                                              # IntExpr
    | FLOAT                                            # FloatExpr
    | STRING                                           # StringExpr
    | CHAR                                             # CharExpr
    | BOOL                                             # BoolExpr
    ;

/* --- REGOLE LESSICALI --- */
BOOL    : 'true' | 'false' ;
INT     : '-'? [0-9]+ ;
FLOAT   : '-'? [0-9]+ '.' [0-9]+ ;
CHAR    : '\'' . '\'' ;
STRING  : '"' ~["]* '"' ;

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;