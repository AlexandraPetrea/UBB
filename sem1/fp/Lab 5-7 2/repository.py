from domaine import *
class Repository:
	'''
	Repository for all the items
	'''
	def __init__(self):
		self.__data = []

	def add(self, new):
		'''
		descr: add a new item to repository
		in: new - the item to be added
		'''
		self.__data.append(new)


	def remove(self, id):
		'''
		descr: delete a item give by id 
		in: id 
		out: the item that has been deleted
		'''
		index = self.find(id)
		if index == None:
			return 'No element'
		self.__data.remove(index)
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
		self.__data.remove(el)
		self.__data.append(item)

	def search(self, crt):
		'''
		descr: search in the list using a specific crt 
		in: crt
		out: the list of item
		'''
		s = []
		for obj in self.__data:
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
		for obj in self.__data:
			if crt in obj[1].lower():
				#print(obj)
				s.append(obj)
			if s == '':
			   	return 'No results! \n'
		return s

	def find(self, objectId):
		for e in self.__data:
			if objectId == e[0]:
				return e
		return None


	def get(self, index):
		'''
		descr: return the item which has the index - Index 
		in: index
		out: the element or Invalid msg 
		'''
		if int(index) < int(0) or int(index) >= len(self.__data):
			return 'Invalid'
		return self.__data[index]
		

	def getAll(self):
		'''
		descr: return all the data from the repository
		'''
		return self.__data

	def __len__(self):
		'''
		descr: return the length of the repository
		'''
		return len(self.__data)

	def __str__(self):
		'''
		descr: printable format
		'''
		s = ''
		for e in self.__data:
			s += str(e)
			s += "\n"
		return s

