class Room:
	def __init__(self, number, type, ok):
		self._number = number 
		self._type = type
		self._ok = ok

	def getNumber(self):
		return self._number

	def getType(self):
		return self._type

	def getOk(self):
		return self._ok

	def setOk(self, new):
		self._ok = new
class Res:
	def __init__(self, id, rnr, name, guest, a, d, camera):
		self._id = id 
		self._rnr = rnr 
		self._name = name
		self._guest = guest 
		self._a = a
		self._d = d
		self._camera = camera

	def getId(self):
		return self._id

	def getType(self):
		return self._type

	def getRoom(self):
		return self._camera
