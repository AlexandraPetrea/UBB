from repository import *
from domaine import *

class RentalCSVRepo(Repository):
    def __init__(self, bookRepo, clientRepo, fileName="rentals.txt"):
        Repository.__init__(self)
        self.__fName = fileName
        self.__bookRepo = bookRepo
        self.__clientRepo = clientRepo
        self.__loadFromFile()
    
    def store(self, book):
        Repository.add(self, rental)
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
                rent1 = [attrs[0], attrs[1], attrs[2], attrs[3], attrs[4], attrs[5]]
                Repository.add(self, rent1)
                line = f.readline().strip()
        except IOError:
            print("Error")#raise RepositoryException("Error saving file")
        finally:
            f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        rentals = Repository.getAll(self)
        for rental in rentalss:
            strf = str(rental[0] + "," + rental[1] + "," + rental[2] + "," + rental[3] + "," + rental[4] + "," + rental[5]+ "\n")
            f.write(strf)
        f.close()