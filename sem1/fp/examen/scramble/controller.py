from random import randint

class Controller:
	def __init__(self, repo):
		self.__repo = repo

	def add(self, new):
		return self.__repo.add(new)

	def modificare2(self, now):
		LITERE = []
		#print('aiic', now)
		for i in range(1, len(now)-1):
			#print(now[0][i])
			if now[i+1] != ' ' and now[i-1] != ' ' and i != len(now) and now[i] != ' ':
				LITERE.append(now[i])

		#print(LITERE)
		#print("now", now)
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
		while i < l and s[i] == " ":
			i = i + 1 
		return i 

	def getText(self,s, i, l):
		text = ""
		while i < l and s[i] != " ":
			text = text + s[i]
			i = i + 1
		return i, text
		

	def joaca(self, litereInitial, litere, cuv1, poz1, cuv2, poz2):
		ok = True	
		litereVechi = litere
		if self.check(litere, poz1, poz2) == False:
			return False, -1, -1
		'''
		if litere[poz1-1] ==' ' or litere[poz1+1] == ' ' or litere[poz2-1] == ' ' or litere[poz2+1] == ' ' or poz1 == 0 or poz2 == 0:
			print('Invalid')
			#print('litere', litere[poz1], litere[poz2])
			ok = False
			return ok, litere, litereVechi
		'''
		if self.check(litere, poz1, poz2) == True:
			litere[poz1], litere[poz2] = litere[poz2], litere[poz1]
		#print(litere)
			
			for i in range(0, len(litere)-1):
				if litereInitial[i] != litere[i]:
					ok = False
			return ok, litere, litereVechi

	def check(self, litere, poz1, poz2):
		if poz1 > len(litere) or poz2 >len(litere):
			return False
		if litere[poz1-1] ==' ' or litere[poz1+1] == ' ' or litere[poz2-1] == ' ' or litere[poz2+1] == ' ' or poz1 == 0 or poz2 == 0:
			return False
		return True

	def getAll(self):
		return self.__repo.getAll()