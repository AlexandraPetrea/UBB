%{ 	 
#include <math.h> 
#include <stdio.h>
#include "parser.tab.h"
int lines = 0;
%} 
%option noyywrap

DIGIT 		[0-9]
WORD		["]([a-zA-Z])*["]
NUMBER		[1-9][0-9]*|0
NR_REAL		{NUMBER}+"."{DIGIT}*
CST		{WORD}|{NUMBER}|{NR_REAL}
ID 		[a-zA-Z][a-zA-Z0-9]{0,7}

%% 

"ARRAY"	{printf( "Reserved word: %s\n", yytext );  return ARRAY;}
"IF"	{printf( "Reserved word: %s\n", yytext );  return IF;}
"ELSE"	{printf( "Reserved word: %s\n", yytext );  return ELSE;}
"WHILE"	{printf( "Reserved word: %s\n", yytext );  return WHILE;}
"FOR"	{printf( "Reserved word: %s\n", yytext );  return FOR;}
"IN"	{printf( "Reserved word: %s\n", yytext );  return IN;}
"OUT"	{printf( "Reserved word: %s\n", yytext );  return OUT;}
"STRING"	{printf( "Reserved word: %s\n", yytext );  return STRING;}
"CHAR"	{printf( "Reserved word: %s\n", yytext );  return CHAR;}
"INT"	{printf( "Reserved word: %s\n", yytext );  return INT;}
"BOOL" 	{printf( "Reserved word: %s\n", yytext );  return BOOLEAN;}
"TRUE"	{printf( "Reserved word: %s\n", yytext );  return TRUE;}
"FALSE"	{printf( "Reserved word: %s\n", yytext );  return FALSE;}
"START"	{printf( "Reserved word: %s\n", yytext );  return START;}
"END"	{printf( "Reserved word: %s\n", yytext );  return END;}

{ID}	{printf( "Identifier: %s\n", yytext ); return IDENTIFIER;}

{CST}	{printf( "Constant: %s\n", yytext ); return CONSTANT;}

":"	{printf( "Separator: %s\n", yytext ); return COLON;}
";"	{printf( "Separator: %s\n", yytext ); return SEMI_COLON;}
","	{printf( "Separator: %s\n", yytext ); return COMA;}
"."	{printf( "Separator: %s\n", yytext ); return DOT;}
"+"	{printf( "Operator: %s\n", yytext ); return PLUS;}
"-"	{printf( "Operator: %s\n", yytext ); return MINUS;}
"*"	{printf( "Operator: %s\n", yytext ); return MULTIPLY;}
"/"	{printf( "Operator: %s\n", yytext ); return DIVISION;}
"("	{printf( "Separator: %s\n", yytext ); return LEFT_ROUND_PARENTHESIS;}
")"	{printf( "Separator: %s\n", yytext ); return RIGHT_ROUND_PARENTHESIS;}
"["	{printf( "Separator: %s\n", yytext ); return LEFT_SQUARE_PARENTHESIS;}
"]"	{printf( "Separator: %s\n", yytext ); return RIGHT_SQUARE_PARENTHESIS;}
"<"	{printf( "Operator: %s\n", yytext ); return LESS_THAN;}
">"	{printf( "Operator: %s\n", yytext ); return GREATER_THAN;}
"<="	{printf( "Operator: %s\n", yytext ); return LESS_OR_EQUAL_THAN;}
">="	{printf( "Operator: %s\n", yytext ); return GREATER_OR_EQUAL_THAN;}
"<>"	{printf( "Operator: %s\n", yytext ); return DIFFERENT;}
"=="	{printf( "Operator: %s\n", yytext ); return EQUAL;}
"="	{printf( "Separator: %s\n", yytext ); return ASSIGNMENT;}
"|"	{printf( "Separator: %s\n", yytext ); return BAR;}

"{"[^}\n]*"}"	/* elimina comentarii */ {}

[ \t]+	/* elimina spatii */  	{}

[\n]+	{++lines;}

[a-zA-Z][a-zA-Z0-9]{8,}	{printf("Illegal size of the identifier at line %d\n", lines); return -1;}

[0-9][a-zA-Z0-9]{0,7}	{printf("Illegal identifier at line %d\n", lines); return -1;}
		 
.	{printf("Illegal symbol at line\n"); return -1;}
%%  