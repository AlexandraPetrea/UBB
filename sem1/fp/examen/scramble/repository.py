from domain import * 
class Repository:
	def __init__(self):
		self._data = []

	def add(self, new):
		self._data.append(new)

	def getAll(self):
		lista = []
		for obj in self._data:
			lista.append([obj.getWord(), obj.getDif()])
		return lista