from controller import * 
from domain import * 
from repository import * 
from random import randint 
from controllerR import* 
class UI:
	def __init__(self, controller, controllerR):
		self.__controller = controller
		self.__controllerR = controllerR

	def main(self):
		self.__loadFromFile()
		aux = self.__controller.getAll()
		self.create(aux)
		print("aici")
		aux1 = self.__controllerR.getAll()

	def create(self, aux):
		name = input("Get the name: ")
		type = input("Get the type: ")
		nr = int(input("Get the nr of guests: "))
		day = input("Insert the day:")
		month =	input("Insert the month:")
		year = input("Insert the year:")

		dateA = str(year) + '.' + str(month) + '.' + str(day)
		day = input("Insert the day:")
		month =	input("Insert the month:")
		year = input("Insert the year:")

		dateD = str(year) + '.' + str(month) + '.' + str(day)


		id = randint(1000,9999)
		camera = 0

		for i in range(0, len(aux)):
			if aux[i].getType() == type and aux[i].getOk() == True:
				camera = aux[i].getNumber()
				aux[i].setOk = False
		if camera !=0 :
			Res = [id, name, type, nr,dateA, dateD, camera]
			self.__controllerR.add(Res)
			print(Res)
		else:
			print("Invalid")
		#print(Res)
	def __loadFromFile(self):
		try:
			f = open("a.txt", "r")
			line = f.readline().strip()
			while line != "":
				attrs = line.split(',')
				nr = attrs[0]
				type = attrs[1]
				room = Room(nr, type, True)
				self.__controller.add(room)
				
				line = f.readline().strip()
		except IOError:
			print("Error")
import datetime
dt = '02/02/2018'
day, month, year = (int(x) for x in dt.split('/'))    
ans = datetime.date(year, month, day)
print (ans.strftime("%B"))

repo = Repository()
repoR = Repository()
controller = Controller(repo)
controllerR = ControllerR(repoR)
UI= UI(controller, controllerR)
UI.main()

