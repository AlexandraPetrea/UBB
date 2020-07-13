from domain import * 

class clientRepository():
	def __init__(self):
		'''
		Constructor for the clientRepository
		'''
		self._clientRepo = []

	def addClient(self, newClient):
		'''
		Add a number to repository 
		in: newClient - the client to be added
		'''
		self._clientRepo.append(client(newClient[0], newClient[1]))

	def removeClient(self, clientId):
		'''
		Remove a client from the repository 
		in: clientId - the Id for the client to be removed
		'''
		ok = self.checkExistance(clientId)


		if ok == False:
			return "Inexistent ID!"

		i = self.positionOfId(clientId)
		j = len(self._clientRepo) - 1

		self._clientRepo[i], self._clientRepo[j] = self._clientRepo[j], self._clientRepo[i]

		return "Removal succesful!"

	def checkExistance(self, clientId):
		'''
		Check if a client exist in the repository 
		in: clientId- Id for the client to be searched
		out: True if exist, False otherwise
		'''
		for obj in self._clientRepo:
			if clientId == obj.returnClientId():
				return True
		return  False

	def positionOfId(self, clientId):
		'''
		Return the position of a client in repository 
		in: clientId - Id for the client 
		out: position in which it was found, -1 otherwise
		'''
		i = - 1
		for obj in self._clientRepo:
			i += 1
			if clientId == obj.returnClientId():
				return i 

	def update(self, client):
		'''
		Update the data for a client 
		in: client to be updated 
		'''
		ok = False
		for obj in self._clientRepo:
			if obj.returnClientId() == client[0]:
				obj.update(client)
				ok = True
		if ok == False:
			return "Inexistent Id!"
		else:
			return "Update succesful!"

	def getClient(self, clientName):
		'''
		Return all the atributs for a client
		in: clientName - the name of the client 
		'''
		for obj in self._clientRepo:
			if obj.returnClientName == clientName:
				return str(obj.returnClientId()) + " " + str(obj.returnClientName()) + " " + str(obj.returnClientCnp()) + " " + str(obj.returnClientAdd())
		return "No results!"

	def printAll(self):
		'''
		Print all repository data
		'''
		for obj in self._clientRepo:
			obj.printObj()

	def printClient(self, ID):
		'''
		Print a specifed client 
		in: clientId
		'''
		for obj in self._clientRepo:
			if obj.returnClientId() == ID:
				obj.printObj()

