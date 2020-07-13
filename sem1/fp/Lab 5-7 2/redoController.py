class RedoController:
	
	def __init__(self, repo, bookController, clientController, rentalController):
		self._repo = repo
		self._bookController = bookController
		self._clientController = clientController
		self._rentalController = rentalController
	'''
	def __init__(self, repo):
		self._repo = repo
	'''
	def redo1(self):
		self._repo.redo()

	def redo(self):
		return self._repo.redo(self._bookController, self._clientController, self._rentalController,)

	def add(self, book):
		self._repo.add_book(book)

	def remove(self, id):
		self._repo.remove_book(id)

	def add_client(self, client):
		self._repo.add_client(client)

	def remove_client(self, id):
		self._repo.remove_client(id)