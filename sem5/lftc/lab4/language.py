# N = { PROGRAM, STMT, DECL, CONSTANT, IF} 
# E = { 16, 25, 0, 1, 32} 
# S = PROGRAM
# P = {
# 	PROGRAM -> STMT,
#     STMT -> DECL,
#     STMT -> IF,
#     DECL -> 25 0 16 CONSTANT,
#     CONSTANT -> 1,
#   	RELATION -> 17,
#     IF -> 32 CONSTANT
# }
separators = ['[', ']', '{', '}', '(', ')', ';', ' '] 
operators = ['+', '-', '*', '/', '<', '<=', '=', '>=', '>', '>>', '<<', '==', '&&', '||', '!', '&']
reservedWords = ['int', 'char', 'bool', 'float', 'array', 'struct', 'if', 'else', 'for', 'while', 'cout', 'true', 'false']

everything = separators + operators + reservedWords
codification = dict( [ [everything[i], i + 2] for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1