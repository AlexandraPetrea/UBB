from texttable import * 

def mainM():
	#a = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
	a = __loadFromFile()
	#for i in range(0, len(a)):
	#	print(a[i])
	'''
	a[1].pop()
	a[1].append('X')
	a[2].pop()
	a[2].append('O')
	'''
	return a
	
def __loadFromFile():
	lista1 = []
	LISTA = []
	try:
		f = open('a.txt', "r")
		line = f.readline().strip()
		while line != "":
			attrs = line.split("\n")
			for i in range(0, len(attrs)):
				lista = attrs[i]
				lista1.append(attrs[i])
			line = f.readline().strip()
		return lista1
	except IOError:
		print("Error")

def buildResultTable(a):
	lista = []
	table = Texttable()
	for term in range(0, len(a)):
		lista = []
		for j in range(0, len(a[term])):
			if a[term][j] != ',' and a[term][j] != " " and a[term][j] != '[' and a[term][j] != ']':
				lista.append(a[term][j])
		table.add_row(lista)
	return table

def __storeToFile(lista):
    f = open('a.txt', "w")
    for obj in lista:
    	strf = str(obj)+'\n'
    	f.write(strf)
    f.close()

if __name__ == "__main__": 
	a = mainM()
	table = buildResultTable(a)
	print(buildResultTable(a).draw())
	__storeToFile(a)