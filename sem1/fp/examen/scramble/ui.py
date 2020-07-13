from repository import * 
from controller import *
from domain import *
from random import randint 


class UI:
	def __init__(self, controller):
		self.__controller = controller

	def mainMenu(self):
		text = self.__loadFromFile()
		lista = self.__controller.getAll()

		x = randint(0, len(lista)-1)
		#x = 1
		self.play(lista[x])
		#self.__controller.modificare2(lista[x])

	def citesteDate(self, lista):
		caractere = 0
		index = 0
		user = input("Give the swap: ")
		i = 0 
		l = len(user)
		s = user
		while i < l and s[i] != ' ':
			i = i + 1 
		i = i + 1
		cuv1 = int(s[i])
		nr = 10
		if cuv1 != 0:
			index = 0 
			while cuv1 != 0:
				while lista[index] != ' ':
					caractere = caractere + 1
					index = index + 1
					if index == len(lista):
						eroare = True
						break
				cuv1 = cuv1 - 1 
				index = index + 1 
				caractere = caractere + 1

			#caractere = caractere + 1


		i = i+1
		poz1 = int(s[i])
		if s[i+1] != '-':
			poz1 = poz1 * 10 + int(s[i+1])
			nr = nr + 1
			i = i + 1
		poz1 = caractere + poz1
		i = i + 2
		cuv2 = int(s[i])

		index = 0
		caractere = 0
		if cuv2 != 0:
			while cuv2 != 0:
				while lista[index] != ' ':
					caractere = caractere + 1
					index = index + 1
					if index == len(lista):
						break
				cuv2 = cuv2 - 1 
				index = index + 1 
				caractere = caractere + 1

			#caractere = caractere + 1

		poz2 = int(s[i+1])
		if (l > nr):
			if s[i+2] != ' ':
				poz2 = poz2 * 10 + int(s[i+2])

		poz2 = poz2+caractere
		#print('poz1', poz1, poz2, caractere)
		return cuv1, poz1, cuv2, poz2

	def play(self, lista):
		print(lista[1])
		cuv1, poz1, cuv2, poz2 = self.citesteDate(lista[1])
		
	#	print(cuv1, poz1, cuv2, poz2)
		print(self.joc(lista, cuv1, poz1, cuv2, poz2))

	def __loadFromFile(self):
		try:
			f = open('input.txt', "r")
			line = f.readline().strip()
			while line != "":
				attrs = line.split(",")
				lista = attrs[0]
				listaMod = self.__controller.modificare2(lista)
				#print(listaMod)
				
				#listaMod = self.__controller.modificare(lista)
				obj = Word(lista, listaMod)
				self.__controller.add(obj)
				line = f.readline().strip()
		except IOError:
			print("Error")

	def joc(self, lista, cuv1, poz1, cuv2, poz2):
		nou = ""
		litere = []
		litereInitial = []
		initial = lista[0]
		nou = lista[1]
		aux1 = ""
		aux = ""

		scor = len(initial)
		for i in range(0, len(initial)):
			aux1 = initial[i]
			litereInitial.append(aux1)
			#litereInitial.append(' ')
		for i in range(0, len(nou)):
			aux = nou[i]
			for j in range(0, len(aux)):
				litere.append(aux[j])

	#	print('litere', litere, litereInitial)
		
		ok, litere, litereVechi = self.__controller.joaca(litereInitial, litere, cuv1, poz1, cuv2, poz2)
		if ok == True:
			return('Victory')
		while ok == False and scor > 1:
			scor = scor-1
			for i in range(0, len(litere)):
				print(litere[i], end =' ')
			print("Your score: ", scor)
			user = input("Give the action: ")
			i, cmd = self.__controller.getText(user, 0, len(user))
			if cmd == 'swap':
				cuv1, poz1, cuv2, poz2 = self.citesteDate1(initial, user)
				#print('pozitiile', cuv1, poz1, cuv2, poz2)

				ok, litere, litereVechi = self.__controller.joaca(litereInitial, litere, cuv1, poz1, cuv2, poz2)
				if (ok == False and litere ==-1 and litereVechi == -1):
					return("Something wrong")
				if ok == True:
					return ('Victory')
			elif cmd == 'undo':
				scor = scor + 1
				ok, litere, litereVechi = self.__controller.joaca(litereInitial, litereVechi, cuv1, poz1, cuv2, poz2)
			if scor == 1:
				return ('You lose! ')

	def citesteDate1(self, lista, user):
		caractere = 0
		index = 0
		#user = input("Give the swap: ")
		i = 0 
		l = len(user)
		s = user
		while i < l and s[i] != ' ':
			i = i + 1 
		i = i + 1
		cuv1 = int(s[i])
		nr = 10
		if cuv1 != 0:
			index = 0 
			while cuv1 != 0:
				while lista[index] != ' ':
					caractere = caractere + 1
					index = index + 1
					if index == len(lista):
						break
				cuv1 = cuv1 - 1 
				index = index + 1 
				caractere = caractere + 1

			#caractere = caractere + 1


		i = i+1
		poz1 = int(s[i])
		if s[i+1] != '-':
			poz1 = poz1 * 10 + int(s[i+1])
			nr = nr + 1
			i = i + 1
		poz1 = caractere + poz1
		i = i + 2
		cuv2 = int(s[i])

		index = 0
		caractere = 0
		if cuv2 != 0:
			while cuv2 != 0:
				while lista[index] != ' ':
					caractere = caractere + 1
					index = index + 1
					if index == len(lista):
						break
				cuv2 = cuv2 - 1 
				index = index + 1 
				caractere = caractere + 1

			#caractere = caractere + 1

		poz2 = int(s[i+1])
		if (l > nr):
			if s[i+2] != ' ':
				poz2 = poz2 * 10 + int(s[i+2])

		poz2 = poz2+caractere
		#print('poz1', poz1, poz2, caractere)
		return cuv1, poz1, cuv2, poz2



repo = Repository()
controller = Controller(repo)
UI = UI(controller)
UI.mainMenu()

