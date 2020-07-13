from rentalController import * 
from undoController import FunctionCall, Operation

class RentalControllerWithUndo(RentalController):
	def __init__(self, undoController, rentalController, repository):
		RentalController.__init__(self, repository)
		self.__undoController = undoController
		self.__rentalController = rentalController
		self.__repository = repository

	def addR(self, id, client, book, date, dueDate, returnDate):
		rental1 = [id, client, book, date, dueDate, returnDate]
		rental = RentalController.add(self, rental1)
		redo = FunctionCall(self.add, rental1)
		undo = FunctionCall(self.delete, id)
		operation = Operation(redo, undo)

		self.__undoController.recordOperation(operation)
		return rental


	def deleteR(self, id):
		rental = RentalController.delete(self, id)
		rental = [rental[0], rental[1], rental[2], rental[3], rental[4]]
		redo = FunctionCall(self.delete, id)
		undo = FunctionCall(self.add, rental)
		operation = Operation(redo, undo)

		self.__undoController.recordOperation(operation)

	def updateR(self, rental2, rental):
		RentalController.update(self, book2)
		redo = FunctionCall(self.update, book)
		undo = FunctionCall(self.update, book2)
		operation = Operation(undo, redo)
		
		self.__undoController.recordOperation(operation)
