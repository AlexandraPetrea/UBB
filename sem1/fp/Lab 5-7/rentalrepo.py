from domain import * 
class rentalRepository:
	def __init__(self):
		'''
		Constructor for the rental repository
		'''
		self._rentalRepo = []

	def add(self, rentData):
		'''
		Add a rental to repository 
		in: rentData - data to pe added
		'''
		self._rentalRepo.append(rental(rentData[0], rentData[1], rentData[2], rentData[3]))

	def returns(self, bookId):
		'''
		Returns a book to library 
		in: bookId - the Id of the book which was returned 
		'''
		i = -1
		j = len(self._rentalRepo) - 1
		ok = False

		for obj in self._rentalRepo:
			i += 1
			if obj.returnBookId() == bookId:
				ok = True
				break

		if ok == True:
			self._rentalRepo[i], self._rentalRepo[j] = self._rentalRepo[j], self._rentalRepo[i]
			self._rentalRepo.pop()
			print( "Return succesful!")

		else:
			print ("No results!")

	def getRaport(self):
		'''
		Raport for a year 
		'''
		v = copy.deepcopy(self._rentalRepo)
		reportDict = {}

		for obj in v:
			year = obj.returnDateYear()
			if year in reportDict:
				reportDict[year] += 1
			else:
				reportDict[year] = 1

		return reportDict

	def printAll(self):
		'''
		Print all the data from the rental repository 
		'''
		for obj in self._rentalRepo:
			obj.printObj()


	def getClientReport(self):
		
		l = []
		for obj in self._rentalRepo:
			l.append(obj.returnClientId())

		return l

	def getBookReport(self):
		l = []
		for obj in self._rentalRepo:
			l.append(obj.returnBookId())
		return l

