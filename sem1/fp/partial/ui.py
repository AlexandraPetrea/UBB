from operations import * 
from tests import * 
def start():

	db = []
	testInit(db)
	print(printMenu())
	test_Init()

	while True:
		print1(db)

		command = readCommand("Give the command: ")

		if command == '1':
			print(addCommand(db))
			
		elif command == '2':
			code = readCommand("Give the code: ")
			newDuration = readValue("Give the duration: ")
			print(update(db, code, newDuration))
			print1(db)
		elif command == '3':
			destination = readCommand("Give the destination: ")
			newDest = readCommand("Give the new dest:")
			if len(destination) < 3 or len(newDest) < 3:
				print("Invalid input")
			else:
				auxList = modi(db, destination, newDest)
				print1(auxList)
		elif command == '4':
			departure = readCommand("Give the departure city: ")
			auxList = filter(db, departure)
			aux = sort(auxList)
			print1(aux)
		else:
			return 0
		

def readCommand(s):
	aux = input("%s" % s)
	return aux

def readValue(s):
	aux = int(input("%s" % s))
	return aux

def addCommand(db):
	code = readCommand("Give the code: ")
	duration = readValue("Give the duration: ")
	departure = readCommand("Give the departure: ")
	destination = readCommand("Give the destination: ")


	if checkDuration(duration) == False:
		return("Cannot be added")

	try:
		if len(code) < 3 or len(departure) < 3 or len(destination) < 3:
			return ("Invalid")
	except ValueError:
		return("Invalid")

	ok = checkCode(db, code)
	if ok == False:
		return("Cannot be added")

	add(db, code, duration, departure, destination)
	return ("Added succesful!")

def print1(auxList):
    """
        This method builds a printable string from a list
    """
    s = ''
    for obj in auxList:
        s += str(obj[0]) + ' ' + str(obj[1]) + ' ' + str(obj[2]) + ' ' + str(obj[3]) + '\n'
    print(s)

def testInit(db):
	add(db, "1233", "26", "Cluj", "Londra")
	add(db, "0B3002", "45", "Cluj", "Londra")
	add(db,"12733", "60", "Milano", "Berlin")
	add(db, "127", "60", "Cluj", "Milano")
	add(db, "12345", "27", "Budapesta", "Londra")
	add(db, "1567", "56", "Cluj", "Bucuresti")
	add(db, "1257", "75", "Roma", "Paris")
	add(db, "1787", "620", "Budapesta", "New-York")
	add(db, "1787", "180", "Paris", "Bucuresti")
	add(db, "1679", "26", "Brasov", "Madrid")
 
   

   	
start()