
from datetime import datetime 
from datetime import date
#import datetime
import time
from shell import * 


class BookController:
	'''
	descr: the Controller for the class book
	'''
	#def __init__(self, undoController, redoController, repo):
	def __init__(self, repo):
		self._repo = repo
		'''
		self._redoController = redoController
		self._undoController = undoController
	
		self._operations = []
		self._index = 0
		'''
		
	def add(self, item):
		'''
		descr: go to book repository and acces the add operations
		in: item 
		out: repository with new item
		'''
		#ok = Verify_name(item)
		#if ok == True:
		return self._repo.add(item)
		'''
		self._operations.append(AddOperation(book))
		self._index += 1
		self._undoController.remove(item)
		self._redoController.add(item)
		'''


	def delete(self, index):
		'''
		descr: delete a element from the repository 
		in: the index from the element 
		out: the repository without that element 
		'''	
		return self._repo.remove(index)
		#self._operations.append(RemoveOperation(index))
		#self._index += 1
		#self._undoController.recordUpdatedControllers([self])
		#self._redoController.recordUpdatedController([self])
        
	
	def update(self, object):
		'''
		descr: update a object from the repository
		in: new object
		out: the repository with a updated object
		'''
		self._repo.update(object)
		'''
		self._operations.append(UpdateOperation(id,id1))
		self._index+=1
		self._undoController.recordUpdatedControllers([self])    
		self._redoController.recordUpdatedControllers([self]) 
		'''

	def undo1(self):
		if self._index == 0:
			return False
		self._recorded = False
		for oper in self._operations[self._index]:
			oper.undo()
		self._recorded = True
		self._index -= 1
		return True


	def returns(self, id):
		index = self._repo.find(id)
		returnDate = datetime.today()
		self._repo[index].setDate(returnDate)

	def search(self, criteriu):
		'''
		descr: search using a special criteria
		in: the criteria
		out: the result of search
		'''
		return self._repo.search(criteriu)

	def find1(self, index):

		for e in range(0, len(self._repo)):
			#print(self._repo.get(e)[0])
			if self._repo.get(e)[0] == index:
				#print(self._repo.get(e)[0])
				return e
		return None

	
	def list1(self):
		'''
		descr: print all the data from the repository 
		'''
		return self._repo.__str__()

	def validity(self, id):
		'''
		descr: check if a id exist in repository
		in: the id
		out: True or False
		'''
		for i in range(0, len(self._repo)):
			if self._repo.get(i)[0] == id:
				return False
		return True

	def status(self, op):
		if op == '1':
			a, b = self.mostRented()
			return a, b
		elif op == '2':
			client_list = self.getSortedClients()
			return client_list
		elif op == '3':
			rental_list = self.getSortedAuthors()
			return rental_list
		else:
			late_rentals = self.getLateRentals()
			return late_rentals


	def mostRented(self):
		mostRentedDict = []
		mostRentedByNumberOfDays = []

		for i in range(0, len(self._repo)):
			mid = self._repo.get(i)[2]

			d1 = self._repo.get(i)[3]
			d2 = self._repo.get(i)[5]
		
			if d2 is None:
				d2 = self.todaysDate()


			number_of_days = days_between(d1, d2)

			ok = True

			for l in mostRentedDict:
				if l[0] == mid:
					l[1] += number_of_days
					ok = False

			if ok:
				mostRentedDict.append([mid, number_of_days])
			ok = True

			for l in mostRentedByNumberOfDays:
				if l[0] == mid:
					l[1] += number_of_days
					ok = False

			if ok:
				mostRentedByNumberOfDays.append([mid, number_of_days])

		'''
		for i in range(0, len(mostRentedDict) - 1):
			for j in range(i + 1, len(mostRentedDict) - 1):
				a = mostRentedDict[i][1]
				b = mostRentedDict[j][1]
				if a < b:
					mostRentedDict[i], mostRentedDict[j] = mostRentedDict[j], mostRentedDict[i]
		'''
		mostRentedDict = shellSort(mostRentedDict, '<')

		'''
		for i in range(0, len(mostRentedByNumberOfDays) - 1):
			for j in range(i + 1, len(mostRentedByNumberOfDays) - 1):
				a = mostRentedByNumberOfDays[i][1]
				b = mostRentedByNumberOfDays[j][1]
				if a < b:
					mostRentedByNumberOfDays[i], mostRentedByNumberOfDays[j] = mostRentedByNumberOfDays[j], mostRentedByNumberOfDays[i]
		'''
		mostRentedByNumberOfDays = shellSort(mostRentedByNumberOfDays, '<')
		return mostRentedDict, mostRentedByNumberOfDays

            
	def todaysDate(self):
		'''
		descr: return the today Date in a specific format
		'''
		today = datetime.now()
		year = today.year
		month = today.month
		day = today.day
		return date(year, month, day)

	def author(bookRepository):
		'''
		descr: a list of all authors
		'''
		mostRented = []
		ok = True
		for i in range(0, len(bookRepository._repo)):
			ok = True
			author = bookRepository._repo.get(i)[3]
			index = bookRepository._repo.get(i)[0]
			mostRented.append([author, index])

		return mostRented

	def getSortedAuthors(self):
		'''
		descr: sort authors 
		'''
		sorted_author = []

		for i in range(0, len(self._repo)):
			indexBook = self._repo.get(i)[2]
			sorted_author.append(indexBook)
		return sorted_author

	def Lista(self, author, author_list):
		'''
		descr: returns a list with the most rented authors
		in: author list - all the author
			author_list - all the author rented 
		out: the list with all author in orded 
		'''
		noua = []
		for i in range(0, len(author_list)):
			for j in range(0, len(author)):
				if author_list[i] == author[j][1]:
					ok = False
					for w in range(0, len(noua)):
						if noua[w][0] == author[j][0]:
							noua[w][1] += 1
							ok = True
					if ok == False:
						noua.append([author[j][0], 1])
		'''
		for i in range(0, len(noua)-1):
			for j in range(i+1, len(noua)):
				if noua[i][1] < noua[j][1]:
					noua[i], noua[j] = noua[j], noua[i]
		'''
		noua = shellSort(noua, '<')
		return noua

	def Verify_name(self,name):
		for i in range(0,len(name)):
			if ((ord(name[i])<65)or((ord(name[i])>90)and(ord(name[i])<97))or(ord(name[i])>122)):
				return False
		return True


def days_between(d1, d2):
	'''
	descr: number of days between d1 and d2
	in: d1 - start date, d2- end date
	out: delta - no of days
	'''
	d1 = datetime.strptime(d1, "%Y-%m-%d")
	d2 = datetime.strptime(d2, "%Y-%m-%d")
	delta = d2 - d1
	return delta.days

