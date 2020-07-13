class Operation:
	def __init__(self, functionDo, functionUndo):
		self._functionDo = functionDo
		self._functionUndo = functionUndo

	def undo(self):
		self._functionUndo.call()

	def redo(self):
		self._functionDo.call()


class FunctionCall():
	def __init__(self, functionRef, *parametrii):
		self._functionRef = functionRef
		self._paramaterii = parametrii

	def call(self):
		self._functionRef(*self._paramaterii)

class UndoController:
	def __init__(self):
		self._operations = []
		self._index = -1
		self._recorded = True
  
	def recordUpdatedControllers(self, controllers):
		self._operations.append(controllers)
		self._operations = self._operations[0:self._index+2]
		self._index = len(self._operations) - 1

	def newOperation(self):
		if self.isRecorded() == False:
			return 
		self._operations = self._operations[0:self._index+1]
		self._operations.append([])
		self._index += 1 

	def recordOperation(self, operation):
		if self.isRecorded() == True:
			self._operations[-1].append(operation)

	def isRecorded(self):
		return self._recorded

	def undo(self):
		if self._index < 0:
			return False
		self._recorded = False
		for oper in self._operations[self._index]:
			oper.undo()
		self._recorded = True
		self._index -= 1
		return True

	def redo(self):
		self._index += 1
		if self._index >= len(self._operations):
			return False
		self._recorded = False
		for oper in self._operations[self._index]:
			oper.redo()
		self._recorded = True
		return True

	def list(self):
		return self._operations.__str__

class CascadedOperation:
    def __init__(self, op=None):
        self._operations = []
        
        if op != None:
            self.add(op)
            
    def add(self, op):
        self._operations.append(op)

    def undo(self):
        for i in range(len(self._operations) - 1, -1, -1):
            self._operations[i].undo()

    def redo(self):
        for i in range(len(self._operations) - 1, -1, -1):
            self._operations[i].redo()
		
class RedoController:
    def __init__(self):
        self._operations=[]
        self._index=-1 
    def recordUpdatedControllers(self, controllers):
        self._operations.append(controllers)
        self._operations = self._operations[0:self._index + 2]
        self._index = len(self._operations) - 1
    def redo(self):
        if self._index < 0:
            return False
        for controller in self._operations[self._index]:
            controller.redo()
        self._index -= 1
        return True