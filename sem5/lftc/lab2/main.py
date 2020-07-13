from fa import FiniteAutomata 
from rg import Grammar 


class UI:
    def main(self):
        while True:
            self.displayMenu()
            char = input()
            if char == '1':
                grammar = Grammar.fromFile(self.__regularFile) 
            elif char == '2':
                finiteAutomata = FiniteAutomata.fromFile(self.__finiteFile)
            elif char == '0':
                break
            else:
                print('Is it so hard to follow instructions?')
            while char == '1':
                try:
                    self.displayCommandGrammar()
                    inp = input()
                    if inp == '1':
                        print(grammar.getNonTerminals())
                    elif inp == '2':
                        print(grammar.getTerminals())
                    elif inp == '3':
                        print(grammar.getProductions())
                           
                    elif inp =='4':
                        print(grammar.getStartSymbol())
                    elif inp == '5':
                        print('Insert a non-terminal symbol')
                        symbol = input()
                        for prod in grammar.getProductionsFor(symbol):
                            print(prod)
                    elif inp == '6':
                        print(grammar.isRegular())
                    elif inp == '7':
                        if (grammar.isRegular()):
                            print(FiniteAutomata.fromRegularGrammar(grammar))
                        else:
                            print("Unavailable option")
                    elif inp == '0':
                        break
                    else:
                        print('invalid key')
                except Exception as e:
                    print(e)
            while char == '2':
                self.displayCommandsFa()
                inp = input()
                if inp == '1':
                    print(finiteAutomata.getStates())
                elif inp == '2':
                    print(finiteAutomata.getSymbols())
                elif inp == '3':
                    print(finiteAutomata.getInitState())
                elif inp == '4':
                    print(finiteAutomata.getFinalState())
                elif inp == '5':
                    finiteAutomata.showTrans()
                elif inp == '6':
                    print(Grammar.fromFiniteAutomata(finiteAutomata))
                elif inp == '0':
                    break
                else:
                    print('invalid key')


    def displayMenu(self):
        print('press the associated keys:\n\
1. Read a Grammar from file\n\
2. Read a Finite Automaton from file\n\
0. Exit :)')

    def displayCommandGrammar(self):
        print('1. Display set of non-terminals\n\
2. Display set of terminals\n\
3. Display set of productions\n\
4. Display starting symbol\n\
5. Display productions of a non-terminal symbol\n\
6. Verify if the grammar is regular\n\
7. Compute Finite Automaton from current grammar\n\
0. Go back to the main menu')

    def displayCommandsFa(self):
        print('1. Display set of states\n\
2. Display alphabet\n\
3. Display starting state\n\
4. Display set of final states\n\
5. Display set of transitions\n\
6. Compute Regular grammar from current Automation\n\
0. Go back to the main menu')

    def __init__(self, finiteFile, regularFile):
        self.__finiteFile = finiteFile
        self.__regularFile = regularFile
        self.main()


ui = UI('fa1.txt', 'not1.txt')