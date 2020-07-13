class RedoRepository:

    def __init__(self):
        self.__redo_repo = []
    def getAll(self):
        return self.__redo_repo


    def remove_book(self, book):
        self.__redo_repo.append(['b', 'remove', book])

    def add_book(self, book):
        self.__redo_repo.append(['b', 'add', book])
        print("DA")
        print(self.__redo_repo)

    def update_book(self, book):
        self.__redo_repo.append(['b', 'update', book])

    def remove_client(self, client):
        self.__redo_repo.append(['c', 'remove', client])

    def add_client(self, client):
        self.__redo_repo.append(['c', 'add', client])

    def update_client(self, client):
        self.__redo_repo.append(['c', 'update', client])

    def redo(self,  bookController, clientController, rentalController,):
        '''
        descr: the undo function
        in: all the controllers 
        out: a specific message
        '''
        if len(self.__redo_repo) == 0:
            return 'Nothing to redo!'

        x = self.__redo_repo[len(self.__redo_repo) - 1]
        print("aici", x)

        if x[0] == 'b':
            # book
            if x[1] == 'remove':
                id = x[2]
                bookController._repo.remove(id)
            elif x[1] == 'add':
                id = x[2][0]
                bookController._repo.add(x[2])#(id)
            else:
                # update
                x = bookController.update_book(x[2])
        else:
            # client
            if x[1] == 'remove':
                id = x[2]
                clientController._repo.remove(x)
            elif x[1] == 'add':
                id = x[2][0]
                clientController._repo.add(x[2])
            else:
                # update
                x = clientController.update_client(x[2])

        self.__redo_repo.pop()

        return 'Redone!'