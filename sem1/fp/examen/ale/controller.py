from random import randint


class Controller:
	def __init__(self, repo):
		self.__repo = repo

	def add(self, new):
		'''
		in: new - the element to be added
		out: the repo with new element
		'''
		return self.__repo.add(new)

	def modificare2(self, now):
		'''
		in: now - the list read from the input
		out: listaBuna -a modified order of the letters 
		descr: take every letter from the initial string new and if is not a first or last one, it added it to the LITERE
		for every position which has a first or last letter from a word, the letter is saved on that postion 
		else if added a random letter from LITERE on that position 
		listaBuna - has the modified form of the initial string
		'''
		LITERE = []
		#print('aiic', now)
		for i in range(1, len(now)-1):
			#print(now[0][i])
			if now[i+1] != ' ' and now[i-1] != ' ' and i != len(now) and now[i] != ' ':
				LITERE.append(now[i])

		n = len(LITERE)-1
		listaBuna = []
		listaBuna.append(now[0])
		for i in range(1, len(now)-1):
			if now[i+1] == ' ' or now[i-1] == ' ' or now[i] == ' ':
				listaBuna.append(now[i])
			else:
				if n != 0:
					x = randint(0, n)
					#print(x, LITERE[x])
					listaBuna.append(LITERE[x])
					LITERE.pop(x)
					n = n -1
				else:
					listaBuna.append(LITERE[0])

		listaBuna.append(now[len(now)-1])

		return listaBuna

	def passSpaces(self,s, i, l):
		'''
		in: s - the string, i - index, l - len of s
		out: fist i where is no more space
		descr: pass the spaces between the words
		'''
		while i < l and s[i] == " ":
			i = i + 1 
		return i 

	def getText(self,s, i, l):
		'''
		in: s - string, i - index, l - len of s
		out: first i where is a space
		descr: pass the text between two spaces
		'''
		text = ""
		while i < l and s[i] != " ":
			text = text + s[i]
			i = i + 1
		#	if i == l-1:
		#		return i, 0
		#		break
		return i, text
		

	def joaca(self, litereInitial, litere, cuv1, poz1, cuv2, poz2):
		'''
		in: litereInitail - the corect array
		litere - the actual array 
		cuv1, poz1 - for the first word swap 
		cuv2, poz2 - for the seconf swap 
		out: the modified list 
		descr: return ok == True if the letters are corect orderd and False otherwise
		litere - the string with the letter from poz1 and poz2 swap
		litereVechi - the order of letter saved in case we do an undo next
		'''
		litereVechi = []
		ok = True	
		for i in range(0, len(litere)):
			litereVechi.append(litere[i])

		#litereVechi = litere
		litere[poz1], litere[poz2] = litere[poz2], litere[poz1]

		for i in range(0, len(litere)-1):
			if litereInitial[i] != litere[i]:		
				ok = False
		#print("in cont", litereVechi)
		return ok, litere, litereVechi
	'''
	def check(self, litere, poz1, poz2):
		if poz1 > len(litere) or poz2 >len(litere):
			return False
		if litere[poz1-1] ==' ' or litere[poz1+1] == ' ' or litere[poz2-1] == ' ' or litere[poz2+1] == ' ' or poz1 == 0 or poz2 == 0:
			return False
		return True
	'''

	def nScore(self, text):
		'''
		in: text - the text 
		out: the nr of character 
		descr: calculate the scor for a given text 
		'''
		nr = 0 
		for i in range(0, len(text)):
			if text[i] == " ":
				nr = nr + 1
		n = len(text) - nr 
		return n

	def constSir(self, lista):
		'''
		in: lista - the initial string
		out: litereInitial - the corect order of letters
			litere - the actual order of letters
		descr: construct 2 arrays with the given description 
		'''
		initial = lista[0]
		nou = lista[1]
		litere = []
		litereInitial = []
		aux1 = ""
		aux = ""

		for i in range(0, len(initial)):
			aux1 = initial[i]
			litereInitial.append(aux1)
			#litereInitial.append(' ')
		for i in range(0, len(nou)):
			aux = nou[i]
			for j in range(0, len(aux)):
				litere.append(aux[j])
		return litereInitial, litere

	def getAll(self):
		return self.__repo.getAll()