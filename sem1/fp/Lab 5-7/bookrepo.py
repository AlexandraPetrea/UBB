from domain import * 
class bookRepository:
	def __init__(self):
			'''			
			Constructor for bookRepository class
			'''
			self._bookRepo = []

	def addBook(self, newBook):
		'''
		Add a book to the repository 
		in: newBook - book to be added 
		'''
		self._bookRepo.append(book(newBook[0], newBook[1], newBook[2], newBook[3]))

	def removeBook(self, bookId):
		'''
		Remove a book from the repository
		in: bookId - book to be removed 
		out: a message proper for the actione done 
		'''
		ok = self.checkExistance(bookId)

		if ok == False:
			return "Inexistent Id!"
		
		i = self.positionOfId(bookId)
		j = len(self._bookRepo) - 1

		self._bookRepo[i], self._bookRepo[j] = self._bookRepo[j], self._bookRepo[i]
		self._bookRepo.pop()

		return "Removal succesful!"

	def positionOfId(self, bookId):
		'''
		Find the position of a book in list 
		in: bookId - book to be found 
		out: the position in the list 
		'''
		i = - 1
		for obj in self._bookRepo:
			i += 1
			if bookId == obj.returnBookId():
				return i

	def checkExistance(self, bookId):
		'''
		Check if a book exist in the repository 
		in: bookId - book to be found 
		out: True if exist, False otherwise
		'''
		for obj in self._bookRepo:
			if bookId == obj.returnBookId():
				return True
		return False

	def update(self, book):
		'''
		Update a book from the repository 
		book - book to be updated 
		'''
		ok = False
		for obj in self._bookRepo:
			if obj.returnBookId() == book[0]:
				obj.update(book)
				ok = True
		if ok == False:
			print("Inexistent Id!")
		else:
			print("Inserted succesful!")

	def getBook(self, bookTitle):
		'''
		Return a book searched by the title
		'''

		for obj in self._bookRepo:
			if obj.returnBookTitle() == bookTitle:
				return str(obj.returnBookId()) + " " + str(obj.returnBookTitle()) + " " + str(obj.returnBookDesc()) + " " + str(obj.returnBookAuthor())
		return "No results!"

	def printAll(self):
		'''
	 	Return all the data from repository 
     	Returns the live list of the repository
    	'''
		for obj in self._bookRepo:
			obj.printObj()

	def getAuthorReport(self):
		'''
		The report for every author
		'''
		authorDict = {}
		for obj in self._bookRepo:
			a = obj.returnBookAuthor()
			if a in authorDict:
				authorDict[a] += 1
			else:
				authorDict[a] = 1
		
		return authorDict

	def printBook(self, iD):
		'''
		Return a book by the Id
		'''
		for obj in self._bookRepo:
			if obj.returnBookId() == iD:
				obj.printObj()
