class Word:
	def __init__(self, word, modificat):
		self.__word = word
		self.__modificat = modificat

	def getWord(self):
		return self.__word

	def getDif(self):
		return self.__modificat

	def setWord(self, new):
		self.__word = new

	def setDif(self, new):
		self.__modificat = new