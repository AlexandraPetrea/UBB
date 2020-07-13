class Repository:
	def __init__(self):
		self.__data = []

	def __len__(self):
		return len(self.__data)

	def __str__(self):
		s=''
		for e in self.__data:
			s += str(e) + "\n"
		return s

	def add(self, new):
		self.__data.append(new)

	def remove(self, index):
	
		return self.__data.pop(index)


	def update(self, oldIt, newIt):
		
		tmp = []
		for i in range(0, len(self.__data)):
			if self.get(i) != oldIt:
				tmp.append(self.__data[i])
			else:
				tmp.append(newIt)

		self.__data = tmp 

	def find(self, item):
		for i in range(0, len(self.__data)):
			if self.__data[i] == item:
				return i
		return -1

	def getAll(self):
		return self.__data

	def list(self):
	
		return(str(self))
