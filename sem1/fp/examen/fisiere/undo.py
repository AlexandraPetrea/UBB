class UndoController:

    def __init__(self, repo, bookController, clientController, rentalController, redoController):
        self._repo = repo
        self._bookController = bookController
        self._clientController = clientController
        self._rentalController = rentalController
        self._redoController = redoController

    def undo(self):
        return self._repo.undo(self._bookController, self._clientController, self._rentalController, self._redoController)
    # Functions add, update and remove for books
    def remove(self, book):
        bookId = book[0]
        self._repo.remove(bookId)

    def add(self, book):
        self._repo.add(book)

    def update(self, book):
        self._repo.update(book)

    # Functions add, update and remove for clients
    def removeC(self, client):
        clientId = client[0]
        print(clientId)
        self._repo.remove_client(clientId)

    def addC(self, client):
        self._repo.add_client(client)

    def updateClient(self, client):
        self._repo.update_client(client)