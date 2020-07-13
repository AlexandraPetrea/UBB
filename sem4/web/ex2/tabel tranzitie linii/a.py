import re 
import tokenize

fileName = 'c.txt'

def isPartOfOperator(char): 
    for op in operators: 
        if char in op: 
            return True 
    return False

def isEscapedQuote(line, index):
    return False if index == 0 else line[index -1] == '\\'

def getStringToken(line, index):
    token = ''
    quoteCount = 0
    
    while index < len(line) and quoteCount < 2:
        if line[index] == '"' and not isEscapedQuote(line, index):
            quoteCount += 1 
        token += line[index]
        index += 1
        
    return token, index

def getOperatorToken(line, index):
    token = ''
    
    while index < len(line) and isPartOfOperator(line[index]):
        token += line[index]
        index += 1 
        
    return token, index

def tokenGenerator(line, separators): 
    token = ''
    index = 0
    
    while index < len(line):
        if line[index] == '"': 
            if token: 
                yield token
            token, index = getStringToken(line, index)
            yield token
            token = ''
            
        elif isPartOfOperator(line[index]):
            if token: 
                yield token
            token, index = getOperatorToken(line, index)
            yield token
            token = ''
        
        elif line[index] in separators:
            if token: 
                yield token
            token, index = line[index], index + 1
            yield token
            token = ''
            
        else:
            token += line[index]
            index += 1 
    if token: 
        yield token

separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ','] 
operators = ['+', '-', '^', '*', '/', '<', '<=', '=', '>=', '>', '>>', '<<', '==', '&&', '||', '!']
reservedWords = ['int', 'char', 'bool', 'float', 'array', 'struct', 'if', 'else', 'for', 'while', 'cout']

everything = separators + operators + reservedWords
codification = dict( [ [everything[i], i + 2] for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1

print([ token for token in tokenGenerator('(a+b&&c/2<=8+"a<=b||2")', separators)])
print([ token for token in tokenGenerator('something', separators)])
print([ token for token in tokenGenerator('" \\"Hello\\" "', separators)])


class HashTable(): 
    def __init__(self):
        self.__content = []
       
    def __search(self, key):
        return self.__content.index(key) if key in self.__content else None 
    
    def add(self, value):
        key = self.__hash(value)
        
        index = self.__search(key)
        
        if index is not None: 
            collisionList = self.__content[index]
            if value not in collisionList: 
                collisionList.append(value)
            return (index, collisionList.index(value))
        else: 
            self.__content.append((key, [value]))
            cl_index = 0
            index = len(self.__content) - 1
            
        return (index, cl_index)
        
    def getId(self, value):
        key = self.__hash(value)
        index = self.__search(key)
        
        if index is None: 
            return None 
        
        collisionList = self.__content[index]

        if value not in collisionList:
            return None 
        
        cl_index = collisionList.index(value)
        
        return (index, cl_index)
    
    def __hash(self, value):
        sum = 0 
        nr = len(value)
        for char in value:
            sum += ord(char) 
        
        return sum / nr

    def __str__(self): 
        return str(self.__content)

class SymbolTable():
    def __init__(self):
        self.__hashTable = HashTable()
        self.__content = dict() 
        self.__count = -1
        
    def add(self, value):
        return self.__hashTable.add(value)
    
    def get(self, value):
        return self.__hashTable.getId(value)

    
    def __str__(self):
        return str(self.__hashTable)


class ProgramInternalForm: 
    def __init__(self):
        self.__content = []
        
    def add(self, code, id):
        self.__content.append((code, id))
        
    def __str__(self):
        return str(self.__content)

def isIdentifier(token): 
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,7}$', token) is not None

def isConstant(token):
    return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None

file = open(fileName, 'r')
for line in file: 
    print(line)


with open(fileName, 'r') as file: 
    for line in file: 
        print([token for token in tokenGenerator(line, separators)])

identifierTable = SymbolTable()
constantsTable = SymbolTable()
pif = ProgramInternalForm()

with open(fileName, 'r') as file: 
    lineNo = 0
    for line in file:
        lineNo += 1 
        for token in tokenGenerator(line[0:-1], separators):  
            if token in separators + operators + reservedWords: 
                pif.add(codification[token], -1)
                print("Separators, operators, reserveWords", token, codification[token])
            elif isIdentifier(token): 
                id = identifierTable.add(token)
                pif.add(codification['identifier'], id)
                print("Identifier", token, id)
             
            elif isConstant(token): 

                id = constantsTable.add(token)
                pif.add(codification['constant'], id)
                print("Constants", token, id)
              
            else:
                raise Exception('Unknown token ' + token + ' at line ' + str(lineNo)) 
               
print('Program Internal Form: \n', pif)
print('Identifier Table: \n', identifierTable) 
print('Constants Table: \n', constantsTable)
