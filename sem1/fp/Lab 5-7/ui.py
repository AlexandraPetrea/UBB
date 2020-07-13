import datetime
#from bookrepo import *
from clientrepo import *
from rentalrepo import *
from domain import *
from tests import * 
#from bookrepo import bookRepository
from clientrepo import clientRepository
from rentalrepo import rentalRepository
from controller import * 
from repository import *

class UI:
	def __init__(self, bookController, clientController, rentalController):
		'''
		Constructor for the UI class
		'''
		self._bookController = bookController
		self._clientController = clientController
		self._rentalContorller = rentalController

	def printMenu(self):
		'''
		The available commands
		'''

		s =  'Available comands:'
		s+= '1. Add (books or clients)\n'
		s+= '2. Remove(books or clients)\n'
		s+= '3. Update(books or clients)\n'
		s+= '4. List(books or clients)\n'
		s+= '5. Rent a book\n'
		s+= '6. Return a book\n'
		s+= '7. Search \n'
		s+= '11. Exit \n'
		print(s)

	def mainMenu(self):


		while True:

			self.printMenu()
			userInput = self.userInput("Insert a command:")

			if not self.isValid(userInput):
				print("Command '%s' not recognized" % userInput)

			if userInput == "1":
				self.add()
			elif userInput == "2":
				self.remove()
			elif userInput == "3":
				self.update()
			elif userInput == "4":
				print(self.listAll())
			elif userInput == "5":
				self.rent()
			elif userInput == "6":
				self.returns()
	

	def userInput(self, s):

		userInput = input(s)
		return userInput

	def isValid(self, s):
		category = ['1', '2', '3', '4', '5', '6', '7']
		if s not in category:
			return False
		return True

######## Add 
	def add(self):
		'''
		Add book or client 
		'''
		

		opType =''
		while opType not in ['1','2']:
			opType = self.userInput("What would you like to add? \n 1. Book\n 2.Client\n ~:")

		if opType == '1':
			book = self.getDataForBook('')
			self._bookController.add(book)
		else:
			client = self.getDataForClient('')
			self._bookController.add(client)

		print ("Addition successful!")


	def getDataForBook(self, aux):
		'''
		Read the data for a book 
		in: aux - the new book 
		'''
		ID = self.userInput("Insert the book Id:")
		title = self.userInput("Insert the %s book title:" % aux)
		descr = self.userInput("Insert the %s book description:" % aux)	
		author = self.userInput("Insert the % s book author:" % aux)

		return [ID, title, descr, author]

	def addNewBook(self, book):
		'''
		Add a new book
		in: book - book to be added
		'''
		self._bookController.add(book)

	def getDataForClient(self, aux):
		'''
		Read the data for a new client 
		in: aux - the new client 
		'''
		ID = self.userInput("Insert the client ID:")
		name = self.userInput("Insert the %s client name:" % aux)

		return [ID, name]

	def addNewClient(self, client):
		'''
		Add a new client
		'''
		self._clientController.addClient(client)

######### Remove 
	def remove(self):
		'''
		Remove a book or a client 
		'''
		opType = ''
		while opType not in ['1', '2']:
			opType = self.userInput("What would you like to remove? \n 1. Book \n 2. Client\n")

		if opType == '1':
			bookId = self.getBookId()
			book1 = self._bookController.find(bookId)
			message = self._bookController.remove(book1)
		else:
			clientId = self.getClientId()
			message = self.removeClient(clientId)

		print("%s" % message)

	def getBookId(self):
		'''Read the book Id
		'''
		bookId = self.userInput("Insert the book Id:")
		return bookId

	def removeBook(self, bookId):
		'''
		Remove a book
		in: bookId - book to be removed 
		'''
		return self._bookController.remove(bookId)

	def getClientId(self):
		'''
		Read the client Id
		'''
		clientId = self.userInput("Insert the client ID:")
		return clientId

	def removeClient(self, clientId):
		'''
		Remove a client
		id: clientId - client to be removed
		'''
		return self._clientController.removeClient(clientId)

###### Update

	def update(self):
		'''
		Update a book or a client 
		'''

		opType =''
		while opType not in ['1', '2']:
			opType = self.userInput("What would you like to update ?\n 1. Book \n 2. Client \n")

		if opType == '1':
			book = self.getDataForBook('new')
			
			book2 = self.getDataForBook('old')
			message = self.updateBook(book, book2)
		else:
			client = self.getDataForClient('new')
			message = self.updateClient(client)

	def updateBook(self, oldBook, newBook):
		'''
		Update a book 
		'''
		return self._bookController.update(book)

	def updateClient(self, client):
		'''
		Update a client 
		'''
		return self._clientController.update(client)

#### Rent 

	def rent(self):
		'''
		Rent a book 
		'''

		rentData = self.getRentData()
		self._rentalContorller.add(rentData)

		print("Rental successful")

	def getRentData(self):
		'''
		Read the data for renting a book 
		'''

		clientId = self.userInput("Give the client ID:")
		bookId = self.userInput("Insert the book ID:")

		opType =''
		while opType not in ['1','2']:
			opType = self.userInput("What would you like to use ?\n 1. Today date \n 2. Custom date\n")

		if opType == '1':
			today = datetime.datetime.now()
			day = today.day
			month = today.day
			year = today.day
			date = str(year) + '.' + str(month) + '.' + str(day)
		else:
			day = self.userInput("Insert the day:")
			month = self.userInput("Insert the month:")
			year = self.userInput("Insert the year:")
			date = str(year) + '.' + str(month) + '.' + str(day)

		numberOfDays = self.userInput("Insert the number of days you want to rent it for:")

		return [clientId, bookId, date, numberOfDays]

### Return 	
	def returns(self):
		'''
		Return a book 
		'''
		bookId = self.userInput("Insert the book Id:")

		return self._rentalContorller.returns(bookId)

### List 
	def listAll(self):
		'''
		Print all the data for books or clients
		'''

		opType =''
		while opType not in ['1','2']:
			opType = self.userInput("What would you like to list? \n 1. Book\n 2.Client\n ~:")

		if opType == '1':
			return self._bookController.getAll()
		else:
			return self._clientController.getAll()



bookController = Repository()
clientController = Repository()
rentalController = Repository()

bookController.add(["1","title","description","author"])
bookController.add(["2","title1","description1","author1"])
bookController.add(["3","title2","description2","author2"])
bookController.add(["4","title3","description3","author3"])
bookController.add(["5","title4","description4","author4"])
bookController.add(["6","title5","description5","author5"])
bookController.add(["7","title6","description6","author6"])
bookController.add(["8","title7","description7","author7"])
bookController.add(["9","title8","description8","author8"])
bookController.add(["10","title9","description9","author9"])
bookController.add(["11","title10","description10","author10"])


clientController.add(["1","name","cnp","address"])
clientController.add(["2","name1","cnp1","address1"])
clientController.add(["3","name2","cnp2","address2"])
clientController.add(["4","name3","cnp3","address3"])
clientController.add(["5","name4","cnp4","address4"])
clientController.add(["6","name5","cnp5","address5"])
clientController.add(["7","name6","cnp6","address6"])
clientController.add(["8","name7","cnp7","address7"])
clientController.add(["9","name8","cnp8","address8"])
clientController.add(["10","name9","cnp9","address9"])


testAll()


ui = UI(bookController, clientController, rentalController)
ui.mainMenu()

