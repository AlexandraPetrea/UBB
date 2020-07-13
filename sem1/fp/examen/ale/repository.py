from domain import * 
class Repository:
	def __init__(self):
		self._data = []

	def add(self, new):
		'''
		in: new - an element to be added
		out: the data with an element higher
		descr: add a new element
		'''
		self._data.append(new)

	def getAll(self):
		'''
		in: - 
		out: an elegant way of returning the object
		'''
		lista = []
		for obj in self._data:
			lista.append([obj.getWord(), obj.getDif()])
		return lista