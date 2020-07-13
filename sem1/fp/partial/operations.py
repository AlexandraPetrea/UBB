def printMenu():
    """
        This method returns the menu list
    """
    s = 'Available commands:\n'
    s += '   1. Add (Adds a flight)\n'
    s += '   2. Modify the duration of a flight \n'
    s += '   3. Reroute all the flights \n'
    s += '   4. Show all the flights with a departure city sorted by duration\n'
    s += '   5. \'exit\' '
    return s

def add(db, code, duration, departure, destination):
	'''
	add a new fly
	in: code, duration, departure, dest
	out: db with a new fly
	'''
	new = [code, duration, departure, destination]
	db.append(new)

def update(db, code, duration):
	'''
	update the duration of fly given by code
	in: code, duration
	out: updated fly
	'''
	i = - 1
	for obj in db:
		i = i + 1
		if obj[0] == code:
			obj[1] = duration
			break

	return("Updated succesful!")

def modi(db, destination, newDest):
	'''
	modify all the fly with some destination with newDest
	in: destination, newDest
	out: modifed db
	'''
	auxList = db
	for obj in auxList:
		if obj[3] == destination:
			obj[3] = newDest

	return auxList

def filter(db, departure):
	'''
	in: departure - filter criteria
	out: all the flights with that departure
	'''
	aux =[]
	for obj in db:
		if obj[2] == departure:
			aux.append(obj)
	return aux

def sort(auxList):
    """
        This method returns a sorted list using bubble sort
    """
    n = len(auxList)

    for i in range(0, n):
        for j in range(i+1, n):
            if int(auxList[i][1]) > int(auxList[j][1]):
                auxList[i], auxList[j] = auxList[j], auxList[i]

    return auxList

def checkCode(db, code):
    """
    descr: checks whether or not a code is already in the code list
    in: code
    """
    for obj in db:
        if obj[0] == code:
            return False
    return True

def checkDuration(duration):
    """
     descr: returns True if the duration variable is greater than 20
       Otherwise it returns False
     in: duration
     out: True or False
    """
    if int(duration) < 20:
        return False
    return True

def checkLen(s):
    """
    descr: checks if the length of the given string is greater than 3
    in: s
    out: True or False
    """
    if len(s) < 3:
        return True
    return False