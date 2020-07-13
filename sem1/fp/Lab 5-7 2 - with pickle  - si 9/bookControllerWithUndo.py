from controller.bookController import * 
from controller.undoController import FunctionCall, Operation

class BookControllerWithUndo(BookController):
	def __init__(self, undoController, bookController, rentalController, repository):
		BookController.__init__(self, repository)
		self.__undoController = undoController
		self.__rentalController = rentalController
		self.__bookController = bookController
		self.__repository = repository

	def addB(self, id, title, descr, author):
		book1 = [id, title, descr, author]
		book = BookController.add(self, book1)
		redo = FunctionCall(self.add, book1)
		undo = FunctionCall(self.delete, id)
		operation = Operation(redo, undo)

		self.__undoController.recordOperation(operation)
		return book


	def deleteB(self, id):
		book = BookController.delete(self, id)
		book = [book[0], book[1], book[2], book[3]]
		redo = FunctionCall(self.delete, id)
		undo = FunctionCall(self.add, book)
		operation = Operation(redo, undo)

		'''
		rentals = self.__rentalController.search(id)
		for rent in rentals:
			self.__rentalController.delete(rent[0])
			self.__undoController.recordOperation(operation)
		'''

	def updateB(self, book2, book):
		BookController.update(self, book2)
		redo = FunctionCall(self.update, book)
		undo = FunctionCall(self.update, book2)
		operation = Operation(undo, redo)
		
		self.__undoController.recordOperation(operation)

