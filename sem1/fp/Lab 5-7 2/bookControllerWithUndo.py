from bookController import * 
from undoController import FunctionCall, Operation

class BookControllerWithUndo(BookController):
	def __init__(self, undoController, rentalController, repository):
		BookController.__init__(self, repository)
		self._undoController = undoController
		self._rentalController = rentalController
		self._repository = repository

	def create(self, id, title, descr, author):
		book1 = book(id, title, descr, author)
		BookController.add(self, book1)
		redo = FunctionCall(self.add, book1)
		undo = FunctionCall(self.delete, id)
		operation = Operation(redo, undo)

		self._undoController.recordOperation(operation)
		return Book


	def delete(self, id):
		book = bookController.delete(self, id)
		redo = FunctionCall(self.delete, id)
		undo = FunctionCall(self.create, book.getId())
		operation = Operation(redo, undo)

		rentals = self._rentalController.search(id)
		for rent in rentals:
			self._rentalController.delete(rent.getId())
		self._undoController.recordOperation(operation)