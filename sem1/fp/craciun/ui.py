from repository import * 
from domain import * 
from controller import *

class UI:
	def __init__(self, controller):
		self.__controller = controller
	
		#self.__redoController = redoController

	def printMenu(self):
		'''
		The available commands
		'''

		s =  'Available comands: \n'
		s+= '1. Simulate \n'
		s+= '2. Vaccinate\n'
		
		s+= '11. Exit \n'
		print(s)

	def mainMenu(self):
		print(self.__controller._repo.getAll())
		while True:
			print()
			#print(self.__controller._repo.getAll())
			self.printMenu()
			userInput = self.userInput("Insert a command:")

			category = ['1', '2']
			if userInput not in category:
				print("Command '%s' not recognized" % userInput)

			if userInput == "1":
				#self.__controller.increase()
				self.__controller.cure()
				aux = self.__controller._repo.number()
				if aux == 0:
					print("Not an ill")
				else:
					self.__controller.simulate()
				print(self.__controller._repo.getAll())
			elif userInput == "2":
				id = self.userInput("Give the id: ")
				print(self.__controller.vaccinate(id))
				print(self.__controller._repo.getAll())
			else:
				return


	def userInput(self, s):

		userInput = input(s)
		return userInput

