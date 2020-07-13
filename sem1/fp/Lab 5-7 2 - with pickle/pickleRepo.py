import pickle

from repository import Repository

class PickleFileRepository(Repository):
    def __init__(self, fileName):
        Repository.__init__(self)
        self._fName = fileName
        self.__loadFromFile()
    
    def add(self, client):
        Repository.add(self, client)
        self.__storeToFile()
     
    def remove(self, clientId):
        Repository.remove(self, clientId)
        self.__storeToFile()        
 
    def update(self, client):
        Repository.update(self, client)
        self.__storeToFile()

    def readAllLines(self):
        f = open(self._fName, "rb")

        """
        You cannot unpickle an empty file
            - EOFError means the file is empty
            - Exception means no file, not accessible and so on...
            - finally makes sure we close the input file, regardless of error
        """
        try:
            self._data = pickle.load(f)
        except EOFError:
            self._data = {} 
        except Exception as e:
            raise e
        finally:
            f.close()

    def __loadFromFile(self):
        f = open(self._fName, "rb")
        
        """
        You cannot unpickle an empty file
            - EOFError means the file is empty
            - Exception means no file, not accessible and so on...
            - finally makes sure we close the input file, regardless of error
        """
        try:
            self._data = pickle.load(f)
        except EOFError:
            self._data = []
        except Exception as e:
            raise e
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "wb")
        pickle.dump(self._data, f)
        f.close()