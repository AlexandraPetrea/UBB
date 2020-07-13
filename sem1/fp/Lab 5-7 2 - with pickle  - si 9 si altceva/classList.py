class List:
	def __init__(self, *par):
		self.index = 0
		self.data = [*par]

	def __setitem__(self, indx, item):
		self.data[indx] = item

	def __iter__(self):
		return self

	def __next__(self):
		self.index +=1
		try:
			return self.data[self.index-1]
		except IndexError:
			self.index = 0 
			raise StopIteration
		#item = self.data[self.index]
		#return item

	def __delitem__(self, index):
		del self.data[index]

	def idx(self, element):
		return self.data.index(element)

	def append(self, item):
		return self.data.append(item)

	def remove(self, item):
		return self.data.remove(item)

	def insert(self, index, item):
		return self.data.insert(indx, item)

	def extend(self, lengthNew):
		return self.data.extend(lengthNew - len(self.data))


	def __len__(self):
		'''
		descr: return the length of the repository
		'''
		return len(self.data)

def shellSort(lista,*, cmpfunction=lambda x:x[1]):
 
    # Start with a big gap, then reduce the gap
    n = len(lista)
    gap = n/2
 
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped 
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
 
        for i in range(int(gap),n):
 
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = lista[i]
 
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            #while j >= int(gap) and cmp(lista[j-int(gap)][1], temp[1]) == True:
            while j >= int(gap) and cmpfunction(lista[j-int(gap)]) < cmpfunction(temp):
                lista[j] = lista[j-int(gap)]
                j -= int(gap)
            # put temp (the original a[i]) in its correct location
            lista[j]= temp
        gap /= 2
    '''
    if cmp == '<':
        return lista
    else:
        for i in range(0, int(n/2)):
            lista[i][1], lista[n-i-1][1] = lista[n-i-1][1], lista[i][1]
    '''
    return lista

def Filter(lista, key):
    n=len(lista)-1
    lista1=[]
    for i in range (0,n):
        if functie(lista[i], key) ==True:
            lista1.append(lista[i])
    return lista1 

def functie(element, key):
    if element[3]== key:
        return True
    else:
        return False