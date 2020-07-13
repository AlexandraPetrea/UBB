import datetime
from domain import *
from tests import * 
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
			self.controller.add(book)
		else:
			client = self.getDataForClient('')
			self.controller.add(client)

		print ("Addition successful!")

######### Remove 
	

	def removeBook(self, bookId):
		'''
		Remove a book
		in: bookId - book to be removed 
		'''
		book = self.controller.find(bookId)
		return self.controller.remove(book)

	def removeClient(self, clientId):
		'''
		Remove a client
		id: clientId - client to be removed
		'''
		client = self._clientController.find(clientId)
		return self._clientController.removeClient(client)

###### Update


	def updateBook(self, book):
		'''
		Update a book 
		'''
		return self.controller.update(book)

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

		return self.contorller.returns(bookId)

### List 
	def listAll(self):
		'''
		Print all the data for books or clients
		'''

		opType =''
		while opType not in ['1','2']:
			opType = self.userInput("What would you like to list? \n 1. Book\n 2.Client\n ~:")

		if opType == '1':
			return self.controller.list(getAll())
		else:
			return self.controller.list(getAll())



