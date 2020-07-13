from repository import Repository
import pickle

class PickleFileRepository(Repository):
    def __init__(self, fileName):
        Repository.__init__(self)
        self.fileName = fileName
        self.loadFromFile()
    
    def add(self, client):
        el = Repository.add(self, client)
        self.storeToFile()
     
    def remove(self, clientId):
        st = Repository.remove(self, clientId)
        self.storeToFile()        
        return st
        
    def update(self, client):
        el = Repository.update(self, client)
        self.storeToFile()
        return el

    def loadFromFile(self):
        f = open(self.fileName, "rb")
        
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

    def storeToFile(self):
        f = open(self.fileName, "wb")
        pickle.dump(self._data, f)
        f.close()