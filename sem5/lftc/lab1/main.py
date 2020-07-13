from b.py import make_minilang_lexer

lexer = make_minilang_lexer()

print(lexer.lex('1 + 2; signed int a;'))
print(lexer.lex('1+2 $$ -3'))