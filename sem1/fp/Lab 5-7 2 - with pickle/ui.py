from repository import * 
from domaine import * 
from bookController import *
from clientController import * 
from rentalController import * 
from datetime import datetime 
from datetime import date
#from undoController import * 
from undoRepo import * 
from undo import *
from Validator import *

class UI:
	def __init__(self, bookController, clientController, rentalController, undoController, validator):
		self.__bookController = bookController
		self.__clientController = clientController
		self.__rentalController = rentalController
		self.__undoController = undoController
		self.__validator = validator
		#self.__redoController = redoController

	def printMenu(self):
		'''
		The available commands
		'''

		s =  'Available comands: \n'
		s+= '1. Add (books or clients)\n'
		s+= '2. Remove(books or clients)\n'
		s+= '3. Update(books or clients)\n'
		s+= '4. List(books or clients)\n'
		s+= '5. Rent a book\n'
		s+= '6. Return a book\n'
		s+= '7. Search \n'
		s+= '8. Statistics \n'
		s+= '9. Undo \n'
		s+= '11. Exit \n'
		print(s)

	def mainMenu(self):

		while True:
			print()
			self.printMenu()
			userInput = self.userInput("Insert a command:")

			category = ['1', '2', '3', '4', '5', '6', '7', '8','9', '10']
			if userInput not in category:
				print("Command '%s' not recognized" % userInput)

			if userInput == "1":
				opType =''
				while opType not in ['1','2']:
					opType = self.userInput("What would you like to add? \n 1. Book\n 2.Client\n ~:")
				
				if opType == '1':
					book = self.getDataForBook('')
					id = book[0]
					title = book[1]
					descr = book[2]
					author = book[3]
					ok = self.__validator.Verify_name(book[1])
					while(ok == False):
						print("Invalid input")
						book = self.getDataForBook('')
						ok = self.__validator.Verify_name(book[1])
					self.__undoController.newOperation()
					self.__bookController.addB(id, title, descr, author)
					
					
					#elf.__bookController.create(id, title, descr, author)
					#self.__undoController.remove(book)
					#self.__redoController.add(book)

				else:
					client = self.getDataForClient('')
					ok = self.__validator.Verify_name(client[1])
					while(ok != True):
						print("Invalid input")
						client = self.getDataForClient('')
						ok = self.__validator.Verify_name(client[1])
						
					self.__undoController.newOperation()
					self.__clientController.addC(client[0], client[1])
					#self.__undoController.removeC(client)
					

				print ("Addition successful!")
			elif userInput == "2":
				opType = ''
				while opType not in ['1', '2']:
					opType = self.userInput("What would you like to remove? \n 1. Book \n 2. Client\n")

				if opType == '1':
					bookId = self.getBookId()
					#book = self.__bookController._repo.find(bookId)
					#print(book)
					#print(self._bookController.find(bookId))
					self.__undoController.newOperation()
					self.__bookController.deleteB(bookId)
					#self.__undoController.add(book)
				else:
					clientId = self.getClientId()
					client = self.__clientController._repo.find(clientId)
					print(client)
					self.__undoController.newOperation()
					self.__clientController.deleteC(clientId)
					#self.__undoController.addC(client)

				print('Deleted successful!')
				
			elif userInput == "3":
				opType =''
				while opType not in ['1', '2']:
					opType = self.userInput("What would you like to update ?\n 1. Book \n 2. Client \n")

				if opType == '1':
					book2 = self.getDataForBook('new')
					book = self.__bookController._repo.find(book2[0])
					self.__undoController.newOperation()
					message = self.__bookController.updateB(book2, book)
					#self.__undoController.update(book)
				else:
					client2 = self.getDataForClient('new')
					client = self.__clientController._repo.find(client2[0])
					self.__undoController.newOperation()
					message = self.__clientController.updateC(client2, client)
					#self.__undoController.updateClient(client)
					
				print(" Updated succesful")
				
			elif userInput == "4":
				opType =''
				while opType not in ['1','2']:
					opType = self.userInput("What would you like to list? \n 1. Book\n 2.Client\n ~:")

				if opType == '1':
					print(self.__bookController.list1())
				else:
					print(self.__clientController.list1())

			elif userInput == "5":
				id = self.userInput("Give the rental ID: ")
				clientId = self.userInput("Give the client ID:")
				bookId = self.userInput("Insert the book ID:")

				opType =''
				while opType not in ['1','2']:
					opType = self.userInput("What would you like to use ?\n 1. Today date \n 2. Custom date\n")

				if opType == '1':
					today = datetime.now()
					day = today.day
					month = today.month
					year = today.year
					date = str(year) + '-' + str(month) + '-' + str(day)
				else:
					day = self.userInput("Insert the day:")
					month = self.userInput("Insert the month:")
					year = self.userInput("Insert the year:")
					date = str(year) + '-' + str(month) + '-' + str(day)

				print("Insert the due date")
				day = self.userInput("Insert the day:")
				month = self.userInput("Insert the month:")
				year = self.userInput("Insert the year:")
				returnDate = str(year) + '-' + str(month) + '-' + str(day)

				numberOfDays = days_between(date, returnDate)
				
				rentData = [id, clientId, bookId, date, numberOfDays, returnDate]
				ok = self.__rentalController.validity(bookId)
				if ok == True:
					self.__rentalController.add(rentData)
					print("Rental successful")
				else:
					print('Book already rented!')
				print(self.__rentalController.list1())

				

			elif userInput == '6':
				rentalId = self.userInput("Insert the book Id:")
				self.__rentalController.delete(rentalId)
				#print(self.__rentalController.list1())

				print("Return succesful!")

			elif userInput == '7':
				self.__bookController.list1()
				opType =''
				while opType not in ['1', '2']:
					opType = self.userInput("What would you like to search ?\n 1. Book \n 2. Client \n")

				if opType == '1':
					criteriu = self.userInput('Book search: ').lower()
					print('Book search result: \n')
					print(self.__bookController.search(criteriu))

				else:
					criteriu = self.userInput('Client search: ').lower()
					print('Client search result: \n')
					print(self.__clientController.searchC(criteriu))

			elif userInput == '8':
				s = ''
				opType = ''
				while opType not in ['1','2','3','4']:
					opType = self.userInput("What statistics do you want ?\n 1. Most rented books \n 2. Most active clients\n 3. Most rented author \n 4. Late rentals\n")
				
				if opType == '1':
					op = self.userInput("What would you like to filter by?\n  1. Number of rents\n  2. Number of days rented\n")
					while op not in ['1','2']:
						print('Invalid command')
						op = self.userInput('Command:')
					a, b = self.__rentalController.status(opType)
					
					if op == '1':
						print (a)
						#s = self.getPrintableBookFormat(a)
					else:
						#s = self.getPrintableBookFormat(b)
						print(b)
				elif opType == '2':
					client_list = self.__rentalController.status(opType)
					print(client_list)
					#s = self.getPrintableClientFormat(client_list)
				elif opType == '3':
					author = ''
					author = self.__bookController.author()
					author_list = self.__rentalController.status(opType)
					lista = self.__rentalController.Lista(author, author_list)
					print(lista)
					#s = self.getPrintableRentalFormat.status(rental_list)
				else:
					lateRentals = self.__rentalController.status(opType)
					print(lateRentals)
					#s = self.getPrintableRentalFormat(late_renatls)
			elif userInput == '9':
				path =''
				print ('What would you like to do?\n  1. Undo\n  2. Redo')
				while path not in ['1','2']:
					path = self.userInput('Give the command:')
				if path == '1':
					self.__undoController.undo()
				else:
					self.__undoController.redo()
			elif userInput == '10':
				print(self.__rentalController.list1())


	def userInput(self, s):

		userInput = input(s)
		return userInput


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


	def getDataForClient(self, aux):
		'''
		Read the data for a new client 
		in: aux - the new client 
		'''
		ID = self.userInput("Insert the client ID:")
		name = self.userInput("Insert the %s client name:" % aux)

		return [ID, name]

	def getBookId(self):
		'''Read the book Id
		'''
		bookId = self.userInput("Insert the book Id:")
		return bookId

	def getClientId(self):
		'''
		Read the client Id
		'''
		clientId = self.userInput("Insert the client ID:")
		return clientId

	def getPrintableRentalList(self, rental_list):
		s = ''
		i = 1
		for rental in rental_list:
			s += str(i) + '. ' + str(str(self.__bookController.returnBookId(rental))) + '\n'
			i += 1
		return s

	def getPrintableBookFormat(self, x):
		s = ''
		k = 1
		for i in x:
			s += str(k) + '. ' + '\n'
			k += 1

		return s

	def getPrintableClientFormat(self, x):
		s = ''
		k = 1
		for i in x:
			s += str(k) + '. ' + str(self.__clientController.getClientId()) + '\n'
			k += 1

		return s

	def getPrintableRentalFormat(self, x):
		s = ''
		k = 1
		for i in x:
			s += str(k) + '. ' + str(self.__rentalController.getId(i[0])) + '\n'
			k += 1

		return s
def days_between(d1, d2):
	'''
	descr: number of days between d1 and d2
	in: d1 - start date, d2- end date
	out: delta - no of days
	'''
	d1 = datetime.strptime(d1, "%Y-%m-%d")
	d2 = datetime.strptime(d2, "%Y-%m-%d")
	delta = d2 - d1
	return delta.days