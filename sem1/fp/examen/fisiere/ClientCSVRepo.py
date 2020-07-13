from repository import *
from domaine import *

class ClientCSVRepo(Repository):
    def __init__(self, fileName="clients.txt"):
        Repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def store(self, book):
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
                client1 = [attrs[0], attrs[1]]
                Repository.add(self, client1)
                line = f.readline().strip()
        except IOError:
            print("Error")#raise RepositoryException("Error saving file")
        finally:
            f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        clients = Repository.getAll(self)
        for client in clients:
            strf = str(client[0] + "," + client[1] + "," + client[2] + "," + client[3] + "\n")
            f.write(strf)
        f.close()