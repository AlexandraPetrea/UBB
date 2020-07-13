class controller:
    def __init__(self, bookController, clientController, rentalController):
        self._bookController = repository
        self._clientController = repository
        self._rentalController = repository

  

    def userInput(self, message):
        """
            Reads the user input and returns it as a string
        """
        data = input("%s" % message)
        return str(data)

    # ADD ########################################################################################

    def add1(self):
        

        opType = ''
        while opType not in ['1', '2']:
            opType = self.userInput("What would you like to add?\n   1. Book\n   2. Client\n ~: ")

    
        if opType == '1':
            newBook = self.getBookData('')
            
            self._bookController.add(newBook)
        elif opType == '2':
            newClient = self.getClientData('')
            
            self._clientController.add(newClient)

        print("Addition successful!")

    def getBookData(self, aux):
        bookId = self.userInput("Insert the movie id: ")
        bookTitle = self.userInput("Insert the%s movie title: " % aux)

        return [bookId, bookTitle, bookDesc, book]

    def getClientData(self, aux):
        clientId = self.userInput("Insert the client id: ")
        clientName = self.userInput("Insert the%s client name: " % aux)

        return [clientId, clientName]

    # REMOVE #####################################################################################

    def remove1(self):
       
        opType = ''
        while opType not in ['1', '2']:
            opType = self.userInput("What would you like to remove?\n   1. Book\n   2. Client\n ~: ")

        

        if opType == '1':
            movieBook = self.userInput("Insert book title: ")
            index = self._bookController.find(bookTitle)
            message = self._bookController.delete(index)
        elif opType == '2':
            clientName = self.userInput("Insert client name: ")
            index = self._bookController.find(clientName)
            message = self._clientController.delete(index)

        print (message)

    