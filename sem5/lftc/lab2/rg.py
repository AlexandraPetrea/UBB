from fa import FiniteAutomata
class Grammar:
    @staticmethod
    def parseLine(line):
        return [ value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]
    
    @staticmethod
    def fromFile(fileName):
        with open(fileName) as file: 
            N = Grammar.parseLine(file.readline())
            E = Grammar.parseLine(file.readline())
            S = file.readline().split('=')[1].strip()
            P = Grammar.parseRules(Grammar.parseLine(''.join([line for line in file])))
            
            return Grammar(N, E, P, S)

    @staticmethod        
    def parseRules(rules):
        result = []
        
        for rule in rules:
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            rhs = [ value.strip() for value in rhs.split('|')]
            
            for value in rhs: 
                result.append((lhs, value))
        
        return result 
    
    @staticmethod
    def fromFiniteAutomata(fa):
        N = fa.Q
        E = fa.E 
        S = fa.q0
        P = []
        
        if S in fa.F:
            P.append((S, 'E'))

        for transition in fa.S: 
            lhs, state2 = transition
            state1, route = lhs
            
            P.append((state1, route + state2))
            
            if state2 in fa.F: 
                P.append((state1, route))

                
        return Grammar(N, E, P, S)
    
    def __init__(self, N, E, P, S):
        self.N = N 
        self.E = E
        self.P = P
        self.S = S
        
    def isNonTerminal(self, value):
        return value in self.N
    
    def isTerminal(self, value):
        return value in self.E 
    
    def isRegular(self):
        usedInRhs = dict() 
        notAllowedInRhs = list() 
        
        for rule in self.P: 
            lhs, rhs = rule
            hasTerminal = False 
            hasNonTerminal = False
            for char in rhs: 
                if self.isNonTerminal(char): 
                    usedInRhs[char] = True
                    hasNonTerminal = True
                elif self.isTerminal(char): 
                    if hasNonTerminal: 
                        return False
                    hasTerminal = True 
                if char == 'E': 
                    notAllowedInRhs.append(lhs)
                    
            if hasNonTerminal and not hasTerminal: 
                return False
        
        for char in notAllowedInRhs: 
            if char in usedInRhs: 
                return False 
            
        return True
    
    def getProductionsFor(self, nonTerminal): 
        if not self.isNonTerminal(nonTerminal):
            raise Exception('Can only show productions for non-terminals')
            
        return [ prod for prod in self.P if prod[0] == nonTerminal ]

    def showProductionsFor(self, nonTerminal):
        productions = self.getProductionsFor(nonTerminal)
        
        print(', '.join([' -> '.join(prod) for prod in productions]))

    def getNonTerminals(self):
        return 'N = { ' + ', '.join(self.N) + ' }'

    def getTerminals(self):
        return 'E = { ' + ', '.join(self.E) + ' }'

    def getProductions(self):
        return 'P = { ' + ', '.join([' -> '.join(prod) for prod in self.P]) + ' }\n'

    def getStartSymbol(self):
        return 'S = ' + str(self.S) + '\n'

    def getFa(self, grammar):
        if (grammar.isRegular()):
            finiteAutomata = FiniteAutomata.fromRegularGrammar(grammar)
            print(finiteAutomata)

    def getRg(self, finiteAutomata):
        grammar = Grammar.fromFiniteAutomata(finiteAutomata)
            
        
    def __str__(self):
        return 'N = { ' + ', '.join(self.N) + ' }\n' \
             + 'E = { ' + ', '.join(self.E) + ' }\n' \
             + 'P = { ' + ', '.join([' -> '.join(prod) for prod in self.P]) + ' }\n' \
             + 'S = ' + str(self.S) + '\n'

'''
grammar = Grammar.fromFile('rg1.txt') 
#print(grammar)

try:
    grammar.showProductionsFor('A')
except Exception as e:
    print(e)

grammar = Grammar.fromFile('rg1.txt')

if (grammar.isRegular()):
    finiteAutomata = FiniteAutomata.fromRegularGrammar(grammar)
    print(finiteAutomata)

finiteAutomata = FiniteAutomata.fromFile('fa1.txt')
grammar = Grammar.fromFiniteAutomata(finiteAutomata)

#print(grammar)
'''