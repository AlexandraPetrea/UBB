from repository import *
from controller.bookController import *
from domaine import * 

class UndoRepository:

    def __init__(self):
        self.__undo_repo = []
    # Functions add, update and remove for books
    def remove(self, book):
        self.__undo_repo.append(['b', 'remove', book])

    def add(self, book):
        self.__undo_repo.append(['b', 'add', book])

    def update(self, book):
        self.__undo_repo.append(['b', 'update', book])

    # Functions add, update and remove for clients
    def remove_client(self, client):
        self.__undo_repo.append(['c', 'remove', client])

    def add_client(self, client):
        self.__undo_repo.append(['c', 'add', client])

    def update_client(self, client):
        self.__undo_repo.append(['c', 'update', client])

    def undo(self, bookController, clientController, rentalController, redoController):
        '''
        descr: the undo function
        in: all the controllers 
        out: a specific message
        '''
        if len(self.__undo_repo) == 0:
            return 'Nothing to undo!'

        x = self.__undo_repo[len(self.__undo_repo) - 1]
        print("aici", x)

        if x[0] == 'b':
            # book
            if x[1] == 'remove':
                id = x[2]
                book = bookController._repo.find(x[2])
                bookController.delete(id)
                #redoController._repo.add_book(x[2])
                redoController.add(book)
            elif x[1] == 'add':
                id = x[2][0]
                x = bookController.add(x[2])
                redoController._repo.remove_book(id)
            else:
                # update
                
                #id = book[0]
                print('aici', x[2][0])
                book1 = bookController._repo.get(int(x[2][0]))
                print('book1', book1)
                book = x[2]
                x = bookController.update(x[2])
                
                redoController._repo.remove_book(book)
                redoController._repo.add_book(book1)
        else:
            # client
            if x[1] == 'remove':
                id = x[2]
                client = clientController._repo.find(x[2])
                clientController.delete(id)
                redoController.add_client(client)
            elif x[1] == 'add':
                x = clientController.add(x[2])
                redoController._repo.remove_client(x)
            else:
                # update
                x = clientController.update_client(x[2])

        self.__undo_repo.pop()

        return 'Undone!'
