class book:
	'''
	Instances of this class represent the book with Id, title, descr and author
	'''
	def __init__(self, ID, title, descriere, author):
		'''
		Constructor for book class 
		in: Id, title, descr and author 
		'''
		self.__id = ID
		self.__title = title
		self.__descriere = descriere
		self.__author = author

	def returnBookId(self):
		return self.__id

	def returnBookTitle(self):
		return self.__title

	def returnBookDescr(self):
		return self.__descriere

	def returnBookAuthor(self):
		return self.__author

	def update(self, newBook):
		self.__title = newBook[1]
		self.__descriere = newBook[2]
		self.__author = newBook[3]

	def printObj(self):
		print(str(self.__id)+" " +str(self.__title)+" "+ str(self.__descriere)+" "+str(self.__author))

class client:
	'''
	Instances of this class represent client with Id and name
	'''
	def __init__(self, ID, name):
		'''
		Constructor for the client class
		'''
		self.__id = ID 
		self.__name = name 

	def returnClientId(self):
		return self.__id

	def returnClientName(self):
		return self.__name

	def update(self, new):
		self.__name = new[1]

	def printObj(self):
		print(str(self.__id)+" " +str(self.__name))

class rental:
	'''
	Instances of this class represent rental with clientId, bookId, date and days
	'''
	def __init__(self, clientId, bookId, date, days):
		'''
		Constructor for the rental class
		'''
		self.__book = bookId
		self.__client = clientId
		self.__date = date
		self.__days = days

	def returnId(self):
		return self.__id

	def returnBookId(self):
		return self.__book

	def returnClientId(self):
		return self.__client

	def returnDate(self):
		return self.__date

	def returnDays(self):
		return self.__days
	
	def returnDateYear(self):
		return self.__date[0:4]

	def printObj(self):
		print (str(self.__client) + " " + str(self.__book) + " " + str(self.__date) + " " + str(self.__days))