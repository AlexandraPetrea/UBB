class Word():
	def __init__(self, word, modificat):
		self._word = word
		self._modificat = modificat

	def getWord(self):
		return self._word

	def setWord(self, new):
		self._word= new

	def getDif(self):
		return self._modificat

	def setDif(self, new):
		self._modificat = new