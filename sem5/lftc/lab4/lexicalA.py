# separators = ['[', ']', '{', '}', '(', ')', ';', ' '] 
# operators = ['+', '-', '*', '/', '<', '<=', '=', '>=', '>', '>>', '<<', '==', '&&', '||', '!', '&']
# reservedWords = ['int', 'char', 'bool', 'float', 'array', 'struct', 'if', 'else', 'for', 'while', 'cout', 'true', 'false']

everything = separators + operators + reservedWords
codification = dict( [ [everything[i], i + 2] for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1

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