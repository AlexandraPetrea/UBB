class book:
	'''
	Instances of this class represent the book with Id, title, descr and author
	'''
	def __init__(self, ID, title, descriere, author):
		'''
		Constructor for book class 
		in: Id, title, descr and author 
		'''
		self._id = ID
		self._title = title
		self._descriere = descriere
		self._author = author

	def getId(self):
		return self._id

	def setId(self, id):
		self._id = id

	def returnTitle(self):
		return self._title

	def setTitle(self, title):
		self._title = title

	def returnDescr(self):
		return self._descriere

	def setDescr(self, descr):
		self._descriere = descr

	def returnAuthor(self):
		return self._author

	def setAuthor(self, author):
		self._author = author

	def update(self, newBook):
		self._title = newBook[1]
		self._descriere = newBook[2]
		self._author = newBook[3]

	def printObj(self):
		print(str(self._id)+" " +str(self._title)+" "+ str(self._descriere)+" "+str(self._author))

class client:
	'''
	Instances of this class represent client with Id and name
	'''
	def __init__(self, ID, name):
		'''
		Constructor for the client class
		'''
		self._id = ID 
		self._name = name 

	def getId(self):
		return self._id

	def returnName(self):
		return self._name

	def update(self, new):
		self.__name = new[1]

	def printObj(self):
		print(str(self.__id)+" " +str(self.__name))

	def getAll(self):
		return self.__data


class rental:
	'''
	Instances of this class represent rental with clientId, bookId, date and days
	'''
	def __init__(self, id, clientId, bookId, date, dueDate, returnDate):
		'''
		Constructor for the rental class
		'''
		self.__id = id
		self.__book = bookId
		self.__client = clientId
		self.__date = date
		self.__dueDate = dueDate
		self.__returnDate = returnDate

	def getId(self):
		return self.__id

	def returnBookId(self):
		return self.__book

	def returnClientId(self):
		return self.__client

	def getDate(self):
		return self.__date

	def setDate(self, returnDate):
		self.__date = returnDate

	def getDueDate(self):
		return self.__dueDate

	def getReturnDate(self):
		return self.__returnDate


	def returnDateYear(self):
		return self.__date[0:4]

	def printObj(self):
		print (str(self.__client) + " " + str(self.__book) + " " + str(self.__date) + " " + str(self.__dueDate) + " " + str(self.__returnDate))