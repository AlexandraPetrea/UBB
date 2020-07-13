import time
import operator
import ui
import cmd
    
def commandBased(category, cmdList, undo):
    cmd.printMenu()

    category= cmd.buildCategList()
    
    
    while True:

        userInput = input("Please give the command:")
        stepCount= len(undo)

        command = cmd.getCommand(userInput)

        if command == "add":
            print (cmd.addExpense(userInput, category, undo, stepCount))
        elif command == "insert":
            print (cmd.insertExpense(userInput, category, undo, 1, stepCount))
        elif command == "remove":
            print (cmd.removeExpense(userInput, category, undo, stepCount))
        elif command == "list":
            printList = (cmd.list(userInput, category))
            printFunc(printList)
        elif command == "sum":
            print (cmd.suma(userInput, category))
        elif command == "max":
            print (cmd.maxi(userInput, category))
        elif command == "sort":
            printList = (cmd.sort(userInput, category))
            cmd.printFunc(printList)
        elif command == "filter":
            print (cmd.filter(userInput, category, undo, stepCount))
        elif command == "undo":
            print (cmd.undoCommand(userInput, category, undo, stepCount))
        elif command == "help":
            cmd.printMenu()
        elif command == "exit":
            return 0

def printFunc(list):
    '''
    in: the list
    out: -
    descr: print the list
    '''
    for i in list:
        print(i)