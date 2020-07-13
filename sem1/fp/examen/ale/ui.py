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
		x = 5
		scor = self.__controller.nScore(lista[x][0])

		self.play(lista[x], scor)
		#command = input("give: ")
		#command, cuv1, poz1, cuv2, poz2 = self.citeste(lista)
		'''
		ok = self.checkPrimaUltima(poz1, poz2, lista)
		while ok == False:
			print("Try again")
			command, cuv1, poz1, cuv2, poz2 = self.citeste(lista)
			ok = self.checkPrimaUltima(poz1, poz2, lista)
		'''

	def citeste(self, lista):
		user = input("Give the command: ")
		i = 0
		l = len(user)

		i = self.__controller.passSpaces(user, i, l)
		i, command = self.__controller.getText(user, i, l)
		#print(command)
		'''
		while command not in ['undo', "swap"]:
			print('Try a correct one')
			user = input("Give the command: ")
			i = self.__controller.passSpaces(user, i, l)
			i, command = self.__controller.getText(user, i, l)
			'''
		
		if command == 'undo':
			return command,0,0,0,0
		elif command == 'swap':
		#	if l < 10:
		#		return False, 0,0,0,0
			if l < 12:
				return False, 0,0,0,0
			i = self.__controller.passSpaces(user, i, l)
			i, cuv1 = self.__controller.getText(user, i, l)
			cuv1 = int(cuv1)
			if cuv1 < 0:
				return False, 0, 0, 0, 0
			nrC = 0
			if cuv1 != 0 :
				index = 0 
				nrC = 0
				while cuv1 != 0:
					while lista[index] != ' ':
						nrC = nrC + 1
						index = index + 1
					cuv1 = cuv1 - 1
					nrC = nrC + 1
					index = index + 1
				#print(nrC)

			i = i + 1
			i, poz1 = self.__controller.getText(user, i, l)
			#print(poz1)
			try:
				poz1 = int(poz1)
			except ValueError:
				print("Invalid")
			if poz1 < 0:
				return False, 0, 0, 0, 0
			if nrC != 0:
				poz1 = poz1 + nrC
		#	print(poz1)
			i = i + 3
			i, cuv2 = self.__controller.getText(user, i, l)
			cuv2 = int(cuv2)
			if cuv2 < 0:
				return False, 0, 0, 0, 0
			nrC = 0
			if cuv2 != 0 :
				index = 0 
				nrC = 0
				while cuv2 != 0:
					while lista[index] != ' ':
						nrC = nrC + 1
						index = index + 1
					cuv2 = cuv2 - 1
					nrC = nrC + 1
					index = index + 1
			i = i + 1
			i, poz2 = self.__controller.getText(user, i, l)
			poz2 = int(poz2)
			if poz2 < 0:
				return False, 0, 0, 0, 0
			if nrC != 0:
				poz2 = poz2 + nrC
		#	print(poz2)
		#	print(cuv1, poz1, cuv2, poz2)
		#	print("A correct one")
			return command, cuv1, poz1, cuv2, poz2

	def checkPrimaUltima(self, poz1, poz2, lista):
		#print(len(lista))
		#print(poz1, poz2)
		if poz1 >= len(lista) or poz2 >= len(lista):
			return False
		if poz1 == 0 or poz2 == 0:
			return False
		if poz1 == len(lista)-1 or poz2 == len(lista)-1:
		#	print(len(lista))
		#	print('aici 1 ')
			return False
		for i in range(0, len(lista)-1):
			if i == poz1 and (lista[i+1] == ' ' or lista[i-1] == ' '):

				return False
			if i == poz2 and (lista[i+1] == ' ' or lista[i-1] == ' '):
				return False
		return True


	def play(self, lista, scor):
		for i in range(0, len(lista[1])):
			print(lista[1][i], end = "")
	#	print(lista[1])
		print("  [Your score is: ]", scor)
		command, cuv1, poz1, cuv2, poz2 = self.citeste(lista[1])
		'''
		while command == False:
			print("Try again")
			command, cuv1, poz1, cuv2, poz2 = self.citeste(lista[1])
			'''

		ok = self.checkPrimaUltima(poz1, poz2, lista[1])
		'''
		while ok == False:
			print("Try again")
			command, cuv1, poz1, cuv2, poz2 = self.citeste(lista[1])
			ok = self.checkPrimaUltima(poz1, poz2, lista[1])
		'''
		
		
	#	print(cuv1, poz1, cuv2, poz2)
		print(self.joc(lista, cuv1, poz1, cuv2, poz2, scor))

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

	def joc(self, lista, cuv1, poz1, cuv2, poz2, scor):
		nou = ""
		litere = []
		litereInitial = []
		initial = lista[0]
		nou = lista[1]
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

		#print('litere', litere, litereInitial, 'lit', litereVechi)
		ok, litere, litereVechi = self.__controller.joaca(litereInitial, litere, cuv1, poz1, cuv2, poz2)
		if ok == True:
			print("Your score is: ", scor)
			return ('Victory')
		while ok == False and scor > 1:
			scor = scor-1
			for i in range(0, len(litere)):
				print(litere[i], end =' ')
			print("Your score: ", scor)
			#print(command, cuv1, poz1, cuv2, poz2)
			print(lista[1])
			command, cuv1, poz1, cuv2, poz2 = self.citeste(lista[1])
			print(command, cuv1, poz1, cuv2, poz2)
			if command == 'swap':
				ok = self.checkPrimaUltima(poz1, poz2, lista[1])
				while ok == False and command != 'undo':
					print("Try again")
					command, cuv1, poz1, cuv2, poz2 = self.citeste(lista[1])
					ok = self.checkPrimaUltima(poz1, poz2, lista[1])

				ok, litere, litereVechi = self.__controller.joaca(litereInitial, litere, cuv1, poz1, cuv2, poz2)
				if ok == True:
					print("Your score is: ", scor)
					return ('Victory')
			elif command == 'undo':
				scor = scor + 1
				ok, litere, litereVechi = self.__controller.joaca(litereInitial, litereVechi, cuv1, poz1, cuv2, poz2)
			if scor == 1:
				return ('You lose! ')

repo = Repository()
controller = Controller(repo)
UI = UI(controller)
UI.mainMenu()
