from classGrammar import Grammar 
import re
class LR0_parser:
    def __init__(self, grammar): 
        self.__grammar = grammar
        self.__workingStack = []
        self.__inputStack = []
        self.__result = []

    def closure(self, productions): 
        
        if productions == []:
            return None
        C = productions
        finished = False 
        
        while not finished:
            finished = True 
            for dottedProd in C:
                dotIndex = dottedProd[1].index('.')
                alpha = dottedProd[1][:dotIndex]
                Bbeta = dottedProd[1][dotIndex + 1:]

                if len(Bbeta) == 0: 
                    continue
                    
                B = Bbeta[0]
                if self.__grammar.isTerminal(B): 
                    continue
                    
                for prod in self.__grammar.getProductionsFor(B):
                    dottedProd = (prod[0], ['.'] + prod[1])
                    if dottedProd not in C: 
                        C += [ dottedProd ]
                        finished = False 
        return C

    def goTo(self, state, symbol):
        C = []
        
        for dottedProd in state:
            dotIndex = dottedProd[1].index('.')
            alpha = dottedProd[1][:dotIndex]
            Xbeta = dottedProd[1][dotIndex + 1:]

            if len(Xbeta) == 0:
                continue

            X, beta = Xbeta[0], Xbeta[1:]

            if X == symbol:
                resultProd = (dottedProd[0], alpha + [X] + ['.'] + beta)
                C = C + [ resultProd ]

        return self.closure(C)

        
    def getCannonicalCollection(self):
        C = [ self.closure([('S1', ['.', self.__grammar.S])]) ]
        finished = False

        while not finished:
            finished = True

            for state in C:
                for symbol in self.__grammar.N + self.__grammar.E:
                    nextState = self.goTo(state, symbol)
                    if nextState is not None and nextState not in C:
                        C = C + [ nextState ]
                        finished = False

        return C


    def getTable(self): 
        states = self.getCannonicalCollection()
        table = [{} for _ in range(len(states))]
        
        for index, state in enumerate(states):
            meetsFirstRule = 0
            meetsSecondRule = 0 
            meetsThirdRule = 0 
            
            for prod in state: 
                dotIndex = prod[1].index('.')
                alpha = prod[1][:dotIndex]
                beta = prod[1][dotIndex + 1:]
                if len(beta) != 0:
                    meetsFirstRule += 1
                else:
                    if prod[0] != 'S1':
                        meetsSecondRule += 1
                        productionIndex = self.__grammar.P.index((prod[0], alpha))
                    elif alpha == [self.__grammar.S]: 
                        meetsThirdRule += 1
                
            if meetsFirstRule == len(state): 
                table[index]['action'] = 'shift'
                
            elif meetsSecondRule == len(state):
                table[index]['action'] = 'reduce ' + str(productionIndex)
                
            elif meetsThirdRule == len(state):
                table[index]['action'] = 'acc'
                
            else: 
                raise(Exception('No action detected for state ' + str(index) + ' ' + str(state)))
                
            
            for symbol in self.__grammar.N + self.__grammar.E: 
                nextState = self.goTo(state, symbol)
                if nextState in states: 
                    table[index][symbol] = states.index(nextState)
            
        return table


    def parse(self, inputSequence): 
        table = self.getTable()
        
        self.__workingStack = ['0']
        self.__inputStack = [symbol for symbol in inputSequence]
        self.__output = []

        while len(self.__workingStack) != 0: 
            state = int(self.__workingStack[-1])
            if len(self.__inputStack) > 0:
                symbol = self.__inputStack.pop(0)
            else: 
                symbol = None
            if table[state]['action'] == 'shift': 
                if symbol not in table[state]: 
                    print('workstack', self.__workingStack)
                    print('inputstack', self.__inputStack)
                    print('state', state)
                    print('symbol', symbol)
                    
                    raise(Exception('Cannot parse shift'))
                self.__workingStack.append(symbol)
                self.__workingStack.append(table[state][symbol])
                
            elif table[state]['action'] == 'acc': 
                if len(self.__inputStack) != 0:
                    raise(Exception('Cannot Parse acc'))
                
                self.__workingStack.clear()
                
            else: 
                reducedState = int(table[state]['action'].split(' ')[1])
                reducedProduction = self.__grammar.P[reducedState]
                
                toRemoveFromWorkingStack = [symbol for symbol in reducedProduction[1]]


                while len(toRemoveFromWorkingStack) > 0 and len(self.__workingStack) > 0:
                    if self.__workingStack[-1] == toRemoveFromWorkingStack[-1]: 
                        toRemoveFromWorkingStack.pop()
                    self.__workingStack.pop()
                    
                if len(toRemoveFromWorkingStack) != 0: 
                    raise(Exception('Cannot Parse reduce'))
                
                self.__inputStack.insert(0, reducedProduction[0])
                self.__output.insert(0, str(reducedState))
            
        return self.__output


g = Grammar.fromFile("grammar.txt")
lr0 = LR0_parser(g)
# Cannonical  
print("Aici e Cannonical")
for index, state in enumerate(lr0.getCannonicalCollection()):
    print(index, state)

# GoTo
s0 = lr0.closure([ ('S1', ['.', g.S]) ])

for s in g.N + g.E: 
    print('goto( s0, ' + s + ') = ', lr0.goTo(s0, s))


# Table
for index, line in enumerate(lr0.getTable()): 
    print(index, line)


print(lr0.parse("abbc"))


    
# def isPartOfOperator(char): 
#     for op in operators: 
#         if char in op: 
#             return True 
#     return False

# def isEscapedQuote(line, index):
#     return False if index == 0 else line[index -1] == '\\'


# def getStringToken(line, index):
#     token = ''
#     quoteCount = 0
    
#     while index < len(line) and quoteCount < 2:
#         if line[index] == '"' and not isEscapedQuote(line, index):
#             quoteCount += 1 
#         token += line[index]
#         index += 1
        
#     return token, index

# def getOperatorToken(line, index):
#     token = ''
    
#     while index < len(line) and isPartOfOperator(line[index]):
#         token += line[index]
#         index += 1 
        
#     return token, index


# def tokenGenerator(line, separators): 
#     token = ''
#     index = 0
    
#     while index < len(line):
#         if line[index] == '"': 
#             if token: 
#                 yield token
#             token, index = getStringToken(line, index)
#             yield token
#             token = ''
            
#         elif isPartOfOperator(line[index]):
#             if token: 
#                 yield token
#             token, index = getOperatorToken(line, index)
#             yield token
#             token = ''
        
#         elif line[index] in separators:
#             if token: 
#                 yield token
#             token, index = line[index], index + 1
#             yield token
#             token = ''
            
#         else:
#             token += line[index]
#             index += 1 
#     if token: 
#         yield token

# class SymbolTable():
#     def __init__(self):
#         self.__content = dict() 
#         self.__count = -1
        
#     def add(self, value):
#         self.__count += 1
#         self.__content[self.__count] = value
#         return self.__count
    
#     def __str__(self):
#         return str(self.__content)

# class ProgramInternalForm: 
#     def __init__(self):
#         self.__content = []
        
#     def add(self, code, id):
#         self.__content.append((code, id))
        
#     def getCodes(self): 
#         return [ code[0] for code in self.__content]
    
#     def __str__(self):
#         return str(self.__content)

# def isIdentifier(token): 
#     return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,8}$', token) is not None

# def isConstant(token):
#     return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None

# separators = ['[', ']', '{', '}', '(', ')', ',', ' '] 
# operators = ['+', '-', '*', '/', '<', '<=', '=', '>=', '>', '>>', '<<', '==', '&&', '||', '!', '&']
# reservedWords = ['int', 'char', 'bool', 'float', 'array', 'struct', 'if', 'else', 'for', 'while', 'cout', 'true', 'false']

# everything = separators + operators + reservedWords
# codification = dict( [ [everything[i], i + 2] for i in range(len(everything))])
# codification['identifier'] = 0
# codification['constant'] = 1

# identifierTable = SymbolTable()
# constantsTable = SymbolTable()
# pif = ProgramInternalForm()

# fileName = 'program.txt'

# with open(fileName, 'r') as file: 
#     lineNo = 0
#     for line in file:
#         lineNo += 1 
#         for token in tokenGenerator(line.strip('\n'), separators): 
#             if token == ' ': 
#                 continue
#             if token in separators + operators + reservedWords: 
#                 pif.add(codification[token], -1)
#             elif isIdentifier(token): 
#                 id = identifierTable.add(token)
#                 pif.add(codification['identifier'], id)
#             elif isConstant(token): 
#                 id = constantsTable.add(token)
#                 pif.add(codification['constant'], id)
#             else:
#                 raise Exception('Unknown token ' + token + ' at line ' + str(lineNo)) 
                
# print('Program Internal Form: \n', pif)
# print('Identifier Table: \n', identifierTable) 
# print('Constants Table: \n', constantsTable)


# inverseCodification = dict( [ [codification[key], key] for key in codification])

# for code in pif.getCodes(): 
#     print(code, ' : ', inverseCodification[code])
    
# inputStack = [str(code) for code in pif.getCodes()]
# #print(input)
        
# g = Grammar.fromFile("grammar.txt")
# g.P = [('S1', ['.', g.S])] + g.P
# g.N += ['S1']
# lr0 = LR0_parser(g)

# #print(g)

# print(lr0.parse(inputStack))