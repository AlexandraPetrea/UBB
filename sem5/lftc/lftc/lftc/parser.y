%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
%}

%token IDENTIFIER
%token CONSTANT
%token END
%token START
%token IF
%token ELSE
%token WHILE
%token FOR
%token IN
%token OUT
%token STRING
%token CHAR
%token INT
%token BOOLEAN
%token ARRAY
%token FALSE
%token TRUE
%token COLON
%token SEMI_COLON
%token COMA
%token DOT
%token PLUS
%token MINUS
%token MULTIPLY
%token DIVISION
%token LEFT_ROUND_PARENTHESIS
%token RIGHT_ROUND_PARENTHESIS
%token LEFT_SQUARE_PARENTHESIS
%token RIGHT_SQUARE_PARENTHESIS
%token LESS_THAN
%token GREATER_THAN
%token LESS_OR_EQUAL_THAN
%token GREATER_OR_EQUAL_THAN
%token DIFFERENT
%token EQUAL
%token ASSIGNMENT
%token BAR

%start program

%%

program : stmtList ;
stmtList : stmt SEMI_COLON stmtList | stmt ;
stmt : decl | simpleStmt | structStmt ;
decl : type IDENTIFIER ;
type : primaryType ;
primaryType : INT | BOOLEAN ;
cmpStmt : START stmtList END ;
simpleStmt : assignment | istmt | ostmt ;
assignment : IDENTIFIER ASSIGNMENT expression ;
expression : term | term PLUS expression | term MINUS expression | term MULTIPLY expression | term DIVISION expression; 
term : IDENTIFIER | CONSTANT ;
istmt : IN term ; 
ostmt : OUT expression ; 
structStmt : ifStmt | whileStmt ;
ifStmt : IF condition stmt elseStmt;
elseStmt : ELSE stmt END| END  ;
whileStmt : WHILE condition cmpStmt ;
condition : expression relation expression ;
relation : LESS_THAN | GREATER_THAN | LESS_OR_EQUAL_THAN | GREATER_OR_EQUAL_THAN | DIFFERENT | EQUAL ;

%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if (argc > 1) 
    yyin = fopen(argv[1], "r");
  if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) ) 
    yydebug = 1;
  if ( !yyparse() ) 
    fprintf(stderr,"\t Perfect !!!\n");
}