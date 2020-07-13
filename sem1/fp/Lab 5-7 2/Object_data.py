class Object:
    def __init__(self,id1,nr):
        self._id=id1
        self._apa=nr
    def getid(self):
        return self._id
    def getapa(self):
        return self._apa
    def setapa(self,p):
        self._apa=p
    def capa(self):
        self._apa+=1  
class AddOperation:
    def __init__(self, object):
        self._object = object
    def getObject(self):
        return self._object

class RemoveOperation:
 
    def __init__(self, object):
        self._object = object
    def getObject(self):
        return self._object

class UpdateOperation:
    def __init__(self, oldObject, updatedObject):
        self._oldObject = oldObject
        self._updatedObject = updatedObject
    def getOldObject(self):
        return self._oldObject
    def getUpdatedObject(self):
        return self._updatedObject               
    