from domain import *
class Repository:
	'''
	Repository for all the items
	'''
	def __init__(self):
		self._data = []

	def add(self, new):
		'''
		descr: add a new item to repository
		in: new - the item to be added
		'''
		self._data.append(new)


	def remove(self, id):
		'''
		descr: delete a item give by id 
		in: id 
		out: the item that has been deleted
		'''
		index = self.find(id)
		if index == None:
			return 'No element'
		self._data.remove(index)
		return index


	def getAll(self):
		'''
		descr: return all the data from the repository
		'''
		return self._data

	def __len__(self):
		'''
		descr: return the length of the repository
		'''
		return len(self._data)

	def __str__(self):
		'''
		descr: printable format
		'''
		s = ''
		for e in self._data:
			s += str(e)
			s += "\n"
		return s


