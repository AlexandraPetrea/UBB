from repository import *
from domaine import *

class BookCSVRepo(Repository):
    def __init__(self, fileName="books.txt"):
        Repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def add(self, book):
        Repository.add(self, book)
        self.__storeToFile()
    
    def delete(self, clientId):
        Repository.delete(self, clientId)
        self.__storeToFile()        
    
    def update(self, newClient):
        Repository.update(self, newClient)
        self.__storeToFile()
    
    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                book1 = [attrs[0], attrs[1], attrs[2], attrs[3]]
                Repository.add(self, book1)
                line = f.readline().strip()
        except IOError:
            print("Error")#raise RepositoryException("Error saving file")
        #finally:
         #   f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        books = Repository.getAll(self)
        for book in books:
            strf = str(book[0] + "," + book[1] + "," + book[2] + "," + book[3] + "\n")
            f.write(strf)
        f.close()