class Controller:
	'''
	descr: the Controller for the class person
	'''

	def __init__(self, repo):
		self._repo = repo
	

	def vaccinate(self, id):
		'''
		descr: make the change to vaccinate a person
		'''
		return self._repo.vaccinate(id)

	def cure(self):
		'''
		descr: add one to the number of day if the person is ill
		if the number is 3 then the person is healty
		'''
		for e in self._repo._data:
			if e[2] == 'ill':
				e[3] = int(e[3]) + int(1)
			if e[3] == 3:
				e[2] = 'healty'
				e[3] = 0 

	def increase(self):
		'''
		descr: increase the number of day beeing sick
		'''
		return self._repo.increase()

	def bolnav(self, aux):
		'''
		descr: make a healty non vacc person ill
		'''
		while aux != 0:
			for e in self._repo._data:
				if e[2] == 'healty' and e[1] == 'non':
					e[2] = 'ill'
					aux = aux - 1

	def simulate(self):
		'''
		descr: simulate a day
		'''
		#print(self._repo.number())
		aux = self._repo.number()
		aux2 = len(self._repo)
		#print(aux2)

		if 2*aux >= aux2:
			return("All the persons is ill")
		else:
			self._repo.bolnav(aux)
		#print(self._repo.getAll())
	
	def list1(self):
		'''
		descr: print all the data from the repository 
		'''
		return self._repo.__str__()

