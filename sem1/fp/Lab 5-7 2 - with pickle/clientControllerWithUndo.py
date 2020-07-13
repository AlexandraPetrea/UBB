from clientController import * 
from undoController import FunctionCall, Operation

class ClientControllerWithUndo(ClientController):
	def __init__(self, undoController, clientController, rentalController, repository):
		ClientController.__init__(self, repository)
		self.__undoController = undoController
		self.__rentalController = rentalController
		self.__clientController = clientController
		self.__repository = repository

	def addC(self, id, name):
		client1 = [id, name]
		client = ClientController.add(self, client1)
		redo = FunctionCall(self.add, client1)
		undo = FunctionCall(self.delete, id)
		operation = Operation(redo, undo)

		self.__undoController.recordOperation(operation)
		return client


	def deleteC(self, id):
		client = ClientController.delete(self, id)
		client = [client[0], client[1]]
		redo = FunctionCall(self.delete, id)
		undo = FunctionCall(self.add, client)
		operation = Operation(redo, undo)
		self.__undoController.newOperation()
		self.__undoController.recordOperation(operation)
		rentals = self.__rentalController.search(id)
		for rent in rentals:
			self.__rentalController.deleteR(rent[0])


	def updateC(self, client2, client):
		ClientController.update(self, client2)
		redo = FunctionCall(self.update, client)
		undo = FunctionCall(self.update, client2)
		operation = Operation(undo, redo)
		
		self.__undoController.recordOperation(operation)

