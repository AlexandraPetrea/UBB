import datetime
from bookrepo import *
from clientrepo import *
from rentalrepo import *
from domain import *
from tests import * 
from bookrepo import bookRepository
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
			self.add(book)
		else:
			client = self.getDataForClient('')
			self.addNewClient(client)

		print ("Addition successful!")


	def addNewBook(self, book):
		'''
		Add a new book
		in: book - book to be added
		'''
		self._bookController.addBook(book)

	def addNewClient(self, client):
		'''
		Add a new client
		'''
		self._clientController.addClient(client)

######### Remove 
	

	def removeBook(self, bookId):
		'''
		Remove a book
		in: bookId - book to be removed 
		'''
		return self._bookController.removeBook(bookId)

	def removeClient(self, clientId):
		'''
		Remove a client
		id: clientId - client to be removed
		'''
		return self._clientController.removeClient(clientId)

###### Update


	def updateBook(self, book):
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
			return self._bookController.printAll()
		else:
			return self._clientController.printAll()



bookController = bookRepository()
clientController = clientRepository()
rentalController = rentalRepository()

bookController.addBook(["1","title","description","author"])
bookController.addBook(["2","title1","description1","author1"])
bookController.addBook(["3","title2","description2","author2"])
bookController.addBook(["4","title3","description3","author3"])
bookController.addBook(["5","title4","description4","author4"])
bookController.addBook(["6","title5","description5","author5"])
bookController.addBook(["7","title6","description6","author6"])
bookController.addBook(["8","title7","description7","author7"])
bookController.addBook(["9","title8","description8","author8"])
bookController.addBook(["10","title9","description9","author9"])
bookController.addBook(["11","title10","description10","author10"])


clientController.addClient(["1","name","cnp","address"])
clientController.addClient(["2","name1","cnp1","address1"])
clientController.addClient(["3","name2","cnp2","address2"])
clientController.addClient(["4","name3","cnp3","address3"])
clientController.addClient(["5","name4","cnp4","address4"])
clientController.addClient(["6","name5","cnp5","address5"])
clientController.addClient(["7","name6","cnp6","address6"])
clientController.addClient(["8","name7","cnp7","address7"])
clientController.addClient(["9","name8","cnp8","address8"])
clientController.addClient(["10","name9","cnp9","address9"])

testAll()


ui = UI(bookController, clientController, rentalController)
ui.mainMenu()
