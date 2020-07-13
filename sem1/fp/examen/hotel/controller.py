from domain import * 
class Controller:

	def __init__(self, repo):
		self._repo = repo

	def add(self, item):
		return self._repo.add(item)
	

	def delete(self, index):
		return self._repo.remove(index)

	def getAll(self):
		'''
		lista = []
		data = self._repo.getAll()
		for obj in data:
			lista.append([obj.getNumber(), obj.getType()])
		return lista
		'''
		return self._repo.getAll()
