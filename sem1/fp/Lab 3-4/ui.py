import time
import cmd
import tests
   
def UIBased(category, cmdList, undo):

   category = cmd.buildCategList()
   cmd.printMenu()

   undo = []
   
   '''
   try:
      tests.testEverything()
      print("All tests passed")
   except Exception as ex:
      print(ex)
      exit(0)
    '''
   while True:

        userInput = input("Enter a command:")

        stepCount = len(undo)
       
        command = cmd.getCommand(userInput)
        remainderAfterCommand = cmd.getRemainder(userInput)


        if command == 'add':
            sum, categorie = add1(category)
            userInput = str(command) + " " + str(sum) + " " + str(categorie)
            print (cmd.addExpense(userInput, category, undo, stepCount))
        elif command == 'insert':
            day, sum, categorie = insert1(category)
            userInput = str(command) + " " + str(day) + " " + str(sum) + " " + str(categorie)
            print(cmd.insertExpense(userInput, category, undo, 1, stepCount)) 
        elif command == 'remove':
            userInput = str(command) + " " + remove1(category)
            print(cmd.removeExpense(userInput, category, undo, stepCount))
        elif command == 'list':
            userInput = str(command) + " " + list1(category)
            printList = cmd.list(userInput, category)
            printFunc(printList)
        elif command == 'sum':
           userInput = str(command) + " " + sum1(category)
           print(cmd.sum1(userInput, category)) 
        elif command == 'max':
           userInput = str(command) + " " + max1()
           print(cmd.max(userInput, category))
        elif command == 'sort':
           userInput = str(command) + " " + sort1(category)
           printList = cmd.sort(userInput, category)
           printFunc(printList)
        elif command == 'filter':
           userInput = str(command) + " " + filter1(category)
           print(cmd.filter(userInput, category, undo, stepCount)) 
        elif command == 'undo':
           print(cmd.undo(userInput, category, undo, stepCount))
        elif command == 'exit':
            return
        else:
            print("Invalid syntax")

def add1(category):
    '''
    descr: read the sum and the category 
    in: category list
    out: sum and category 
    '''
    s = getValue("Enter the sum: ")
    categorie = getCategory("Enter the category: ", category)

    return s, categorie

def getValue(value):
    '''
    descr: read and check if the value is int
    in: value
    '''
    while True:
        x = input(value)
        try:
            x = int(x)
            return x
        except ValueError:
            print("Invalid number.")
            
def getCategory(s, category):
    '''
    in: the user command and the list of categories, read the category from the user
    descr: check if the category is valid 
    out: category or error message
    '''
    while True:
        categorie = input(s)
        if categorie not in category:
            print("Invalid category")
        else:
            return categorie
            
def printFunc(List):
    '''
    descr: print the list List
    in: the list to print 
    out: -
    '''
    for i in List:
        print(i)

def getDayValue(day):
    '''
    descr: check if the day s is valid
    in: the user command
    out: the day or error message
    '''
    while True:
        try:
            day1 = int(input(day))
            if day1 < 1 or day1 > 30:
                print(" Invalid day")
                continue
            return day1
        except ValueError:
            print("Invalid day")

def getSymbol(s):
    '''
    descr: check if the symbol is < , > or =
    in: read the symbol s
    out: the symbol if is valid or error message
    '''
    while True:
        symbol = input(s)
        if symbol not in ['>', '<', '=']:
            print("   Invalid symbol.")
        else:
            return symbol

def getDay(s):
    '''
    descr: check the day
    '''
    while True:
        t = input(s)
        if t == "day":
            return t


def insert1(category):
    '''
    descr: read the day, sum and the category 
    in: list of categories
    out: day, sum and category read
    '''

    day = getDayValue("Please enter a day: ")
    s = getValue("Please enter a sum: ")
    categorie = getCategory("Enter the category: ", category)

    return day, s, categorie

def remove1(category):
    '''
    descr: print the options for the remove and do the specific things for each of them
    in: the list of categories
    '''
    UIType = '0'

    while UIType not in ['1', '2', '3']:
        print(" 1. Remove only a specific day.")
        print(" 2. Remove multiple days - begin with start day to end day.")
        print(" 3. Remove a category.")
        UIType = input("Give the command:")

    if UIType == '1':
        day = getDayValue("Enter a day to be removed: ")

        return str(day)

    elif UIType == '2':
        start_day = getDayValue("Enter the start day: ")
        end_day = getDayValue("Enter the end day: ")

        return str(start_day) + " to " + str(end_day)

    else:
        categorie = getCategory("Enter a category: ", category)

        return str(categorie)

def list1(category):
    '''
    descr: print the options for the list and do the specific things for each of them  
    in: the list of categories
    '''
    UIType = '0'
    while UIType not in ['1', '2', '3']:
        print("1. List all the expenses")
        print("2. List expenses from a specific category.")
        print("3. List expeneses by category less, greater or equal to a value")
        UIType = input("Give the command: ")

    if UIType == '1':
        return " "

    elif UIType == '2':
        category = getCategory("Enter a category: ", category)

        return str(category)

    else:
        category = getCategory("Enter a category: ", category)
        symbol = getSymbol("Enter a symbol ('<', '>', '='): ")
        value = getValue("Enter a value: ")

        return str(category) + " " + str(symbol) + " " + str(value)

def sum1(category):
    '''
    descr: read the category for the sum function
    in: the list of categories
    out: the category 
    '''
    categorie = getCategory("Enter a category: ", category)

    return str(categorie)

def max1():
    '''
    descr: read the day for the max function
    in: - 
    out: the day for which is calculated the max
    '''
    day = getDay("Enter 'day': ")
    return day

def filter1(category):
    '''
    descr:print the options for the filter and do the specific things
    in: the list of categories
    out: the category or the category and the symbol for filter function
    '''
    UIType = '0'
    while UIType not in ['1', '2']:
        print(" 1. Filter by category.")
        print("2. Filter by category less, greater or equal to a value.")
        UIType = input("Gibe the command: ")

    if UIType == '1':
        category = getCategory("Enter a category: ", category)

        return str(category)

    else:
        category = getCategory("Enter a category: ", category)
        symbol = getSymbol("Enter a symbol ('<', '>', '='): ")
        value = getValue("Enter a value: ")

        return str(category) + " " + str(symbol) + " " + str(value)

def sort1(category):
    '''
    descr: print the options available and do the specific things for each of them 
    in: the list of categories
    out: the day or the category - for the sort function
    '''
    UIType = '0'

    while UIType not in ['1', '2']:
        os.system('clear')
        print("1. Sort by day.")
        print("2. Sort by category.")
        UIType = input("Give the command: ")

    if UIType == '1':
        day = getDayValue("Enter day: ")
        return str(day)

    else:
        categorie = getCategory("Enter a category: ", category)
        return str(categorie)
