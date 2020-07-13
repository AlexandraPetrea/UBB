import time

def printMenu():
    s = "Available commmands:\n"
    s += " add  <sum> <category>\n"
    s += " insert <day> <sum> <category>\n"
    s += " remove <day>\n"
    s += " remove <start day> to <end day>\n"
    s += " remove <category>\n"
    s += " list\n"
    s += " list <category>\n"
    s += " list <category> [ < = > ] <value >\n"
    s += " exit \n"
    print(s)
        
def addExpense(userInput, category, undo, stepCount):
    '''
    in: the user command and the list of categories, undo steps and step count
    out: modified dictionary 
    descr: extract the value and the category from userInput and adding them to the
    dictionary on the current day
    '''
    Sum, categorie, remainder = getCategoryAndValue(userInput)
    day = int(time.strftime("%d"))

    try:
        Sum = int(Sum)
        if Sum < 0:
            return "Invalid value"
    except ValueError:
        return "Invalid value"

    try:
        if len(remainder) > 0:
            return "Something in plus"
    except ValueError:
        return "Invalid syntax"


    try:
        if categorie not in category:
            return "Invalid category"
    except ValueError:
        return "Invalid category"

    dictionary = initializeDictionary(day, category)
    dictionary[categorie] += Sum
    # updating the sum of the selected category
    fileUpdate(int(time.strftime("%d")), dictionary)
    # updating the file for this day with the new information

    stepCountUpdate(undo, Sum, categorie, day, stepCount)
    #updating the undo list

    return "Added succesfully"


def insertExpense(userInput, category,undoS, undo, stepCount):
    '''
    in: the user command and the list of categories
    out: modified dictionary according to the command
    descr: insert in the dictionary for a specific day, a value on a category
    '''
    day, Sum, categorie, remainder = getDayCategoryAndValue(userInput)

    try:
        day = int(day)
        if day > 31 or day < 1:
            return "Invalid day"
    except ValueError:
        return "Invalid day"

    try:
        if categorie not in category:
            return "Invalid category"
    except ValueError:
        return "Invalid category"

    try:
        if len(remainder) > 0:
            return "Something is in plus"
    except ValueError:
        return "Invalid syntax"

    try:
        Sum = int(Sum)
        if undo == 1 and Sum < 0:
            return "Invalid sum"
    except ValueError:
        return "Invalid value"

    dictionary = initializeDictionary(day, category)
    dictionary[categorie] += Sum
    fileUpdate(day, dictionary)

    if undo:
        stepCountUpdate(undoS, Sum, category, day, stepCount)
        return "Inserted successfully"

def removeExpense(userInput, category, undo, stepCount):
    '''
    in: the user command and the list of categories
    out: modified dictionary
    descr: remove one item from the list 
    '''
    dayOrCategory = getRemainder(userInput)

    if " to " in dayOrCategory:
        startDay, endDay, remainder = removeTo(dayOrCategory)

        if len(remainder) > 0:
            return "Invalid syntax"

        try:
            startDay = int(startDay)
            if startDay > 31 or startDay < 1:
                return "Invalid day"
        except ValueError:
            return "Invalid start day"

        try:
            endDay = int(endDay)
            if endDay > 31 or endDay < 1:
                return "Invalid day"
        except ValueError:
            return "Invalid end day"

        removeExpenses(startDay, endDay, undo, stepCount, category)
        return "Successfully removed"
    else:

        text, remainder = removeDayOrCategory(userInput)
        
        if len(remainder) > 0:
            return "Invalid syntax"
        try:
            day = int(text)
            if day > 31 or day < 1:
                return "Invalid day"
            removeExpenses(day, day, undo, stepCount, category)
            return "Successfully removed"
        except ValueError:
            if text in category:
                removeExpensesByCategory(text,undo, stepCount, category)
                return "Successfully removed"
            else:
                return "Invalid syntax"
            
def getCategoryAndValue(s):
    '''
    in: the user command
    out: the value, category and the remainder
    descr: extract the value and the category from the user command and the
    remainder if there is a one

    '''
    category = Sum = ''
    l = len(s)
    i = 0

    i = passSpaces(s, i, l) # passing the space before the command
    i = passText(s, i, l) # passing the command text 
    i = passSpaces(s, i, l) # passing the space after the command
    i, Sum = getText(s, i, l) 
    i = passSpaces(s, i, l)
    i, category = getText(s, i, l)
    i = passSpaces(s, i, l)

    remainder = s[i:]

    return Sum, category, remainder

def getDayCategoryAndValue(s):
    '''
    in: the user command
    out: the day, category, value and the remainder
    descr: extract the day, category, value and the remainder 
    '''
    day = category = Sum = ""
    l = len(s)
    i = 0

    i = passSpaces(s, i, l) # passing the space before the command text
    i = passText(s, i, l) # passing the command text
    i = passSpaces(s, i, l)
    i, day = getText(s, i, l)
    i = passSpaces(s, i, l)
    i, Sum = getText(s, i, l)
    i = passSpaces(s, i, l)
    i, category = getText(s, i, l)
    i = passSpaces(s, i, l)

    remainder = s[i:]

    return day,Sum, category, remainder

def getCommand(s):
    '''
    in: the user command
    out: extract the command 
    descr: extract the command from the user input
    '''
    l = len(s)
    i = 0

    cmd = ""
    i = passSpaces(s, i, l)
    i, cmd = getText(s, i, l)
    i - passSpaces(s, i, l)

    return cmd

def passSpaces(s, i, l):
    '''
    in: the user input, position and length of the string
    out: the first position that is not empty
    descr: pass all the empty spaces
    '''
    while i < l and s[i] == ' ':
        i = i + 1
    return i # the position which is not empty

def getText(s, i, l):
    '''
    in: the string, position and length of the string
    out: the command
    descr: extract the command
    '''
    text = ""
    while i < l and s[i] != ' ':
        text = text + s[i]
        i = i + 1
    return i, text

def passText(s, i, l):
    '''
    in: the string, position and lenght of the string
    out: the position in which the text is over
    descr: pass the text 
    '''
    while i < l and s[i] != ' ':
        i = i + 1
    return i # the position where the text is over

def getDay(s):
    '''
    in: the string
    out: the day and the reminder
    descr: extract the day from the user input
    '''
    l = len(s)
    i = 0

    i = passSpaces(s, i, l)
    i = passText(s, i, l)
    i = passSpaces(s, i, l)
    i, day = getText(s, i, l)
    i = passSpaces(s, i, l)

    remainder = s[i:]

    return day, remainder

def getDayOrCategory(s):
    l = len(s)
    i = 0

    i = passSpaces(s, i, l)
    i = passText(s, i, l) # passing the command
    i = passSpaces(s, i, l)
    i, text = getText(s, i, l)
    i = passText(s, i, l)

    remainder = s[i:]

    return text, remainder


def filter(userInput, category, undo, stepCount):
    '''
        create a list with some specific category
    '''

    remainderAfterCommand = getRemainder(userInput) # get the remaining characters after the <command>
    categorie = getCommand(remainderAfterCommand)

    remainderAfterCategory = getRemainder(remainderAfterCommand) # get the ramaining characters after the <category>

    if categorie not in category:
        return "   Invalid syntax"

    if len(remainderAfterCategory) == 0:
        '''
            This means that the user has entered only a category so we will delete everything from the
            files apart from the specified category
        '''
        deleteAllExcept(categorie, "", 0, undo, stepCount, category)
        return "   Data was filtered successfully!"

    else:
        '''
            The remaining case is the one with "<", ">" or "=" and then the <category>
        '''
        symbol = getCommand(remainderAfterCategory)
        remainderAftersymbol = getRemainder(remainderAfterCategory)

        value = getCommand(remainderAftersymbol)
        remainder = getRemainder(remainderAftersymbol)

        if symbol not in ["<", ">", "="] or len(remainder) > 0:
            return "Invalid syntax"

        try:
            value = int(value)
            deleteAllExcept(categorie, symbol, value, undo, stepCount, category)
            return "Data was filtered successfully!"

        except ValueError:
            return "Invalid value"
    
def getRemainder(s):
    '''
    in: the user input
    out: the remainder
    descr: the remainder after extracting all the values
    '''
    l = len(s)
    i = 0

    i = passSpaces(s, i, l)  # passing the spaces before the command
    i = passText(s, i, l)  # passing the command
    i = passSpaces(s, i, l)  # passing the spaces before the command

    remainder = s[i:]  # getting the rest of the text from the string

    return remainder

def removeTo(s):
    '''
    in: string - which is a part of the user input
    out: returns the <start day>, <end day> and if there are any other characters after the valid instruction
        the function returns it as well
    descr: the case in which the <remove> command was entered
        and also containg the string " to " in it
    
    '''
    start_day = end_day = ""
    i = 0
    l = len(s)

    i, start_day = getText(s, i, l)
    i = passSpaces(s, i, l)
    i = passText(s, i, l) # passing 'to'
    i = passSpaces(s, i, l)
    i, end_day = getText(s, i, l)
    i = passSpaces(s, i, l)

    remainder = s[i:]

    return start_day, end_day, remainder

def removeDayOrCategory(s):
    '''
    in: string - a part of the user input
    out: the day or category after the <remove> command followed by the remainder
                in case there are any characters after the day or category
    '''
    text = ""
    i = 0
    l = len(s)

    i = passText(s, i, l)
    i = passSpaces(s, i, l)
    i, text = getText(s, i, l)
    i = passSpaces(s, i, l)
   # i = passText(s, i, l)
    
    remainder = s[i:]

    return text, remainder

def removeExpenses(a, b, undo, stepCount, category):
    '''
    descr: remove a number of day from the dictionaries
    in: a is the start day and b is the end day
    out: dictionaries without the expenses for the interval [a, b]

    '''
    default = {"housekeeping" : 0, "food" : 0, "transport" : 0, "clothing" : 0, "internet" : 0, "others" : 0}

    for i in range(a, b+1):
        aux_dict = initializeDictionary(i, category)
        for key in aux_dict:
            if aux_dict[key] != 0:
                undo.append([stepCount, "insert " + str(i) + " " + str(aux_dict[key]) + " " + str(key)])
                # updating the undo list

        fileUpdate(i, default)

def removeExpensesByCategory(categorie, undo, stepCount, category):
    '''
    in: the category, list of categories
    descr: removes all the expenses for the category from day 1 to day 31
    (updates all the files with the default dictionary)
    '''
    for i in range(1, 32):
        aux_dict = initializeDictionary(i, category)

        if aux_dict[categorie] != 0:
            undo.append([stepCount, "insert " + str(i) + " " + str(aux_dict[categorie]) + " " + str(categorie)])            
            
        aux_dict[categorie] = 0
        fileUpdate(i, aux_dict)

def list(userInput, category):
    '''
    in: the user command and the list of catgories
    desc: all the cases of list instruction
    '''
    remainderAfterCommand = getRemainder(userInput)

    printList = []

    if len(remainderAfterCommand) == 0:
        # if the user has enterd only the <list> command 
        printList = listOfExpenses("", 1, "", -1, category)

    else:
        categorie = getCommand(remainderAfterCommand)
        remainderAfterCategory = getRemainder(remainderAfterCommand)

        if len(remainderAfterCategory) == 0:
        # if the user enterd the <list> <category> command
        
            if categorie not in category:
                printList.append("Wrong category")
                return printList

            printList = listOfExpenses(categorie, 2, "", -1, category)

        else:
            symbol = getCommand(remainderAfterCategory)
            remainderAftersymbol = getRemainder(remainderAfterCategory)

            if symbol in ['>', '<', '='] and len(remainderAftersymbol) > 0:
            # if the user has enterd a valid <, = or > 
                    
                value = getCommand(remainderAftersymbol)
                remainderAfterValue = getRemainder(remainderAftersymbol)

                if len(remainderAfterValue) == 0:
                    #if the user had entered corecty the command 
                        
                    try:
                        value = int(value)
                    except ValueError:
                        printList.append("Invalid syntax")
                        return printList

                    printList = listOfExpenses(categorie, 3, symbol, value, category)

                else:
                    printList.append("Invalid syntax")
                    return printList

            else:
                printList.append("Invalid syntax")
                return printList

    return printList

def updateExpensesList(dataList, emptyList, category, categ, t, symbol, value, ok, i, val):
    if t == 1 or (t == 2 and category == categ) or (symbol == '>' and value > val) or (symbol == '<' and value < val) or (symbol == '=' and value == val):
        if ok:
            dataList.append("day " + str(i))
            emptyList = False
            ok = 0
        dataList.append("     " + categ + " " + str(value) + " RON")
    return ok, emptyList

def listOfExpenses(categorie, t, symbol, val, category):
    '''
    in: the category that we want to print, in case that there is a one,
    the type of the operation, the symbol and the value for the 3rd operation
    descr: prints all the expenses from all the files in this format:
        DAY x
        internet y
        others z
        ...
      
    '''
    emptyList = True
    dataList = []
    for i in range(1, 32):
        ok = 1
        auxBool = True

        f = open("data/%s.txt" % i, "r")
        for line in f:
            categ, value, auxBool = getCategoryAndValueFromFile(line, category, auxBool)
            
            if value > 0 and t != 3:
                ok, emptyList = updateExpensesList(dataList, emptyList, categorie, categ, t, symbol, value, ok, i, val)

            elif value >= 0 and t == 3 and categorie == categ:
                ok, emptyList = updateExpensesList(dataList, emptyList, categorie, categ, t, symbol, value, ok, i, val)

    if emptyList:
        dataList.append("No results")

    return dataList

def undoCommand(userInput, category, undo, stepCount):

    if len(undo) == 0:
        return "Undo unavailable"

    undoSteps(userInput, category, undo, stepCount)

    return "Undo successful!"
def sum1(userInput, category):
    '''
    in: the user commmand and the list of categories
    out: sum of a category
    descr: returns the sum of a specific category for the entire month
    '''

    Sum = 0
    categorie = getRemainder(userInput)

    if categorie not in category:
        return("Invalid category") 
    
    for i in range(1, 32):
        ok = 1
        auxBool = True
        
        f = open("data/%s.txt" % i, "r")
        for line in f:
            categ, value, auxBool= getCategoryAndValueFromFile(line, category, auxBool)
            if categorie == categ:
                Sum = Sum + value
            
    return Sum

def max(userInput, category):
    '''
    in: the user input and the list of categories
    out: the day which has the maximum total of expenses
    descr: returns the day which has the maximum cost of expenses
    '''

    Maxim = -1
    Day = 0
    
    for i in range(1, 32):
        ok = 1
        Sum = 0
        auxBool = True 
        f = open("data/%s.txt" % i, "r")

        for line in f:
            categ, value, auxBool = getCategoryAndValueFromFile(line, category, auxBool)
            Sum = Sum + value
            
        if Sum > Maxim:
            Maxim = Sum
            Day = i

    return Day

def sort(userInput, category):
    '''
    in: the command and the list of categories
    descr: write the total daily expenses in ascending order by amount of money spent
    '''

    printList = []

    remainderAfterCommand = getRemainder(userInput)
    instruction = getCommand(remainderAfterCommand)

    remainder = getRemainder(remainderAfterCommand)

    if len(remainder) > 0 or (instruction != "day" and instruction not in category):
        printList.append("Invalid syntax")
        return printList

    if instruction == "day":
        '''
            Things to be done in case the user enters "sort day"
        '''
        entireExpenses = buildListOfExpenses("", 1, category)
                                                                       
        sortedExpenses = sorted(entireExpenses.items(), key = operator.itemgetter(1))
        printList.append("Sorting by day...")

        for t in sortedExpenses:
            printList.append("Expenses of day {0}: {1} ron".format(t[0], t[1]))

    else:
        '''
            Things to be done in case the user enters "sort <category>"
        '''

        entireExpenses = buildListOfExpenses(instruction, 0, category)

        sortedExpenses = sorted(entireExpenses.items(), key = operator.itemgetter(1))
        

        printList.append("Sorting by " + instruction + "...")

        for t in sortedExpenses:
            printList.append("Expenses for " + instruction + " on day {0}: are {1} ron ".format(t[0], t[1]))

    return printList

def getSum(categorie, category):
    '''
    in: category and the list of category
    descr: this function returns the sum of all the values corresponding to each day's category
    '''
    s = 0
    for i in range(1, 32):
        auxDict = initializeDictionary(i, category)
        s += auxDict[categorie]
    return s

def getExpensesForDay(auxDict):
    '''
    descr:this function returns the sum of all the expenses for this dictionary
    in: a dictionary containing categories and values
    out: the sum of all the values
    '''
    a = 0
    for key in auxDict:
        a += auxDict[key]
    return a

def updateMax(maxExp, auxExp, i, day):
    if auxExp > maxExp:
        return auxExp, i
    return maxExp, day

def maximumExpenses(category):
    '''
    descr: this function iterates thorugh all of the files, checks the expenses and memorizes the day with the most expenses
    It returns the the maximum expense + the day of the maximum expense
    '''
    maxExp, day = 0, 0

    for i in range(1, 32):
        auxExp = getExpensesForDay(initializeDictionary(i, category))
        maxExp, day = updateMax(maxExp, auxExp, i, day)

    return maxExp, day

def getSumForDay(dict):
    '''
    descr: returns the sum of expenses for a day
    in: the dictionary
    out: the sum of all categories
    '''
    sum = 0

    for category in dict:
        sum += dict[category]

    return sum
        
def buildCategList():
    '''
    in: -
    out: the list of categories
    descr: build the list of all categories 
    '''
    a = []
    a.extend(["housekeeping", "food", "internet", "transport", "clothing", "others"])
    return a

def buildListOfExpenses(categ, op, category):
    '''
    in: category, operation and the list of category 
    out: list of expenses sorted 

    '''

    valuesDictionary = {}

    for i in range(1, 32):
        sumOfValues = 0

        dictForDay = initializeDictionary(i, category)

        if op == 1:
            sumOfValues = getSumForDay(dictForDay)
        else:
            sumOfValues += dictForDay[categ]

        valuesDictionary[i] = sumOfValues

    return valuesDictionary

def stepCountUpdate(undo, Sum, category, day, stepCount):
    '''
    This function updates the undo_steps list with the most recent operation inserted by the user
    and at the same time the length of the list
    '''
    undo.append([stepCount, "insert " + str(day) + " " + str(-Sum) + " " + str(category)])

def undoSteps(userInput, category, undo, stepCount):
    current_step = int(undo[len(undo) - 1][0])
    userInput = str(undo[len(undo) - 1][1])

    insertExpense(userInput, category, undo, 0, stepCount)
    # 0 - means that there will be no UNDO update in the insert function
    undo.pop()

    if len(undo) > 0:
        next_step = int(undo[len(undo) - 1][0])

    while len(undo) > 0 and current_step == next_step:
        next_step = int(undo[len(undo) - 1][0])
        userInput = str(undo[len(undo) - 1][1])
        if current_step == next_step:
            insertExpense(userInput, category, undo, 0, stepCount)
            undo.pop()
def buildHelpList():
    '''
    descr: create a list with all the possible commands
    in:-
    out: a list with all the possible commands
    '''
    a = []
    a.extend(["add <sum> <category>", "insert <day> <sum> <category>", "remove <day>", "remove <start day> to <end day>"
                 ,"remove <category>", "list", "list <category>", "list <category> [ < | = | > ] <value>", "sum <category>",
              "max <day>", "sort <day>", "sort <category>", "filter <category>", "filter <category> [ < | = | > ] <value>", "undo", "clear", "exit"])
    return a

def initialize(i):
    '''
    descr: initializes file 'i.txt' with all categories and value 0
    in: the number i which represent the i-day 
    '''
    f = open("data/%s.txt" % i, "w")
    f.writelines("housekeeping 0\nfood 0\ntransport 0\nclothing 0\ninternet 0\nothers 0")
    f.close()

def getCategoryAndValueFromFile(s, category, ok):
    '''
     in: string from the command, list of categories and ok 
     out: return the category extract from the string, the value and ok 
     descr: extract the category and value from a line i
     checks if all the data is valid: if the category is valid and if the value is a number
    '''
    k = 0

    for i in s.split():
        if k == 0: # I get the category and the value
            categ = i
            k = 1
            if categ not in category:
                ok = False
        else: 
            value = i

    try:
        value = int(value)
    except ValueError:
        ok = False

    return categ, value, ok

def getFileDict(day, category, ok):
    '''
    in: the day, list of categories and ok
    out: the dictionary and ok 
    descr: returns the dictionary containing the categories and the values
    from the text 'day.txt'
    '''
    auxDictionary = {}

    f = open("data/%s.txt" % day, "r+")

    for line in f:
        categ, value, ok = getCategoryAndValueFromFile(line, category, ok)
        auxDictionary[categ] = value
        # inserting the category and sum into an auxiliary dictionary

    if not ok:
        initializeFile(day)

    f.close()

    return auxDictionary, ok

def fileUpdate(fileName, auxDictionary):
    '''
    in: the day, the aux dictionary
    out: the modified dictionary
    descr: updating the dictionary
    '''
    f = open("data/%s.txt" % fileName, "w")
    for key in auxDictionary:
        f.write(key + " " + "{0}\n".format(auxDictionary[key]))
    f.close()

def initializeDictionary(day, category):
    '''
    in: the day, the list of categories
    out: the dictionary for the day
    descr: returns the dictionary containing the categories and the values
        specific to the day <day>
    '''
    ok = True
    auxDictionary = {}

    f = open("data/%s.txt" % day, "r+")

    for line in f:
        categ, value, ok = getCategoryAndValueFromFile(line, category, ok)
        auxDictionary[categ] = value
        # inserting the category and sum into an auxiliary dictionary

    if not ok:
        initializeFile(day)

    f.close()

    return auxDictionary

