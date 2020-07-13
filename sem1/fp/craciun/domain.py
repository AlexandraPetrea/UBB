class person:
	'''
	Instances of this class represent the book with Id, title, descr and author
	'''
	def __init__(self, id, imun, status, number):
		'''
		Constructor for person class 
		in: Id, imun, status and number
		'''
		self._id = id
		self._imun = imun 
		self._status = status
		self._number = number

	def getId(self):
		return self._id

	def setId(self, id):
		self._id = id

	def getStatus(self):
		return self._status

	def setStatus(self, status):
		self._status = status

	def getImnu(self):
		return self._imun

	def setImun(self, imun):
		self._imun = imun

	def getNumber(self):
		return self._number

	def setNumber(self, number):
		self._number = number
	