from domain import *
#from classList import List
class Repository:
	'''
	Repository for all the items
	'''
	def __init__(self):
		self._data = []
		self.index = 0


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
	
	def update(self, item):
		'''
		descr: update a element in the list 
		in: the item to be updated 
		'''
		el = self.find(item[0])
		if el == None:
			return 'Element not found'
		index = el
		self._data.remove(el)
		self._data.append(item)

	def search(self, crt):
		'''
		descr: search in the list using a specific crt 
		in: crt
		out: the list of item
		'''
		s = []
		for obj in self._data:
			if crt in obj[1].lower() or crt in obj[2].lower() or crt in obj[3].lower():
				#print(obj)
				s.append(obj)
			if s == '':
			   	return 'No results! \n'
		return s


	def search1(self, crt):
		'''
		descr: search in the list using a specific crt 
		in: crt
		out: the list of item
		'''
		s = []
		for obj in self._data:
			if crt in obj[1].lower():
				#print(obj)
				s.append(obj)
			if s == '':
			   	return 'No results! \n'
		return s

	def find(self, objectId):
		for e in self._data:
			if objectId == e[0]:
				return e
		return None


	def get(self, index):
		'''
		descr: return the item which has the index - Index 
		in: index
		out: the element or Invalid msg 
		'''
		if int(index) < int(0) or int(index) >= len(self._data):
			return 'Invalid'
		return self._data[index]
		

	def getAll(self):
		'''
		descr: return all the data from the repository
		'''
		return self._data

	def vaccinate(self, id):
	 for e in self._data:
			if (e[0] == id):
				if (e[2] == 'healty'):
					e[1] = 'vac'
					return("Succesful")
				else:
					return ("Error")


	def bolnav(self, aux):
		while aux != 0:
			for e in self._data:
				if e[2] == 'healty' and e[1] == 'non':
					e[2] = 'ill'
					e[3] = 1
					aux = aux-1
			if aux  != 0:
				return


	def number(self):
		nr = 0
		for e in self._data:
			if (e[2] == 'ill'):
				nr = nr + 1

		return nr


	def cure(self):
		for e in self._data:
			if e[3] == '3':
				e[2] = 'healty'


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


