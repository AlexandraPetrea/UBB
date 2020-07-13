class Square:
	def __init__(self, x, y):
		self._x = x
		self._y = y 
	def getX(self):
		return self._x

	def getY(self):
		return self._y


class Board:
	'''
	descr: constructor for the class Board
	'''
	def __init__(self):
		'''
		descr: Board is for the board in which the player put the planes
			Board1 is for the board in which the player has the hits position
		'''
		self._board = [[0 for x in range(1,12)] for y in range(1,12)]
		self._board1 = [[0 for x in range(1,12)] for y in range(1,12)]


	def printA(self):
		'''
		descr: the board printed
		'''
		#print(self._board)
		xLabel = " " * 3
		for i in range(1,11):           
			xLabel += str(i) + " "

		xLabel += "    "
		for i in range(1,11):           
			xLabel += str(i) + " "
		print(xLabel)
		for i in range(1,11):
				print(" " + chr(i + 64) +" " + str(self._board[i][1]) +" " + str(self._board[i][2]) + " "+  str(self._board[i][3]) +" " + str(self._board[i][4]) +" " + str(self._board[i][5]) + " "+  str(self._board[i][6]) +" " + str(self._board[i][7]) +" " + str(self._board[i][8]) + " "+  str(self._board[i][9]) + " "+  str(self._board[i][10]) + "   |" + chr(i + 64) +" " + str(self._board1[i][1]) +" " + str(self._board1[i][2]) + " "+  str(self._board1[i][3]) +" " + str(self._board1[i][4]) +" " + str(self._board1[i][5]) + " "+  str(self._board1[i][6]) +" " + str(self._board1[i][7]) +" " + str(self._board1[i][8]) + " "+  str(self._board1[i][9]) + " "+  str(self._board1[i][10]))
				
	def isFree(self, x, y):
		'''
		in:x, y - the coords
		out: True/False 
		descr: check if the position is free or not 
		'''
		return self._board[x][y] == 0

	def getFreeSquares(self):
		'''
		descr: get all the free squares from the board
		'''
		rez = []
		for i in range(1, 10):
			for j in range(1, 10):
				if self.isFree(i, j):
					rez.append((Square(i,j)))
		return rez 

	def __str__(self):
		for i in range(1, 10):
			for j in range(1, 10):
				print(self._board[i][j])

	def setGrid(self, x, y, poz):
		'''
		in: x, y - the coords, poz - the orientation
		out: board modified 
		descr: modify the board after it check if the coord are right and free
		'''
		if poz == 'S':
			ok = Board.checkCoord(self, x, y)
			#print("ok din tab", ok)
			if ok == True:
				self._board[x][y] = 'C'
				self._board[x+1][y] = 'X'
				self._board[x+2][y] = 'X'
				self._board[x+3][y] = 'X'
				self._board[x+1][y-1] = 'X'
				self._board[x+1][y-2] = 'X'
				self._board[x+1][y+2] = 'X'
				self._board[x+1][y+1] = 'X'
				self._board[x+1][y] = 'X'
				self._board[x+3][y+1] = 'X'
				self._board[x+3][y-1] = 'X'
				ok = "Succesful added"

		elif poz == 'J':
			ok = self.checkCord1(x, y)

			if ok == True:
				self._board[x][y] = 'C'
				self._board[x-1][y] = 'X'
				self._board[x-2][y] = 'X'
				self._board[x-3][y] = 'X'
				self._board[x-1][y-1] = 'X'
				self._board[x-1][y-2] = 'X'
				self._board[x-1][y+2] = 'X'
				self._board[x-1][y+1] = 'X'
				self._board[x-1][y] = 'X'
				self._board[x-3][y+1] = 'X'
				self._board[x-3][y-1] = 'X'

				ok = "Succesful added"
		elif poz == 'L':
			ok = self.checkCord2(x, y)

			if ok == True:
				self._board[x][y] = 'C'
				self._board[x][y-1] = 'X'
				self._board[x-1][y-1] = 'X'
				self._board[x-2][y-1] = 'X'
				self._board[x+1][y-1] = 'X'
				self._board[x+2][y-1] = 'X'
				self._board[x][y-2] = 'X'
				self._board[x][y-3] = 'X'
				self._board[x-1][y-3] = 'X'
				self._board[x][y-3] = 'X'
				self._board[x+1][y-3] = 'X'

				ok = "Succesful added"
		elif poz == 'R':
			ok = self.checkCord3(x, y)

			if ok == True:
				self._board[x][y] = 'C'
				self._board[x][y+1] = 'X'
				self._board[x-1][y+1] = 'X'
				self._board[x-2][y+1] = 'X'
				self._board[x+1][y+1] = 'X'
				self._board[x+2][y+1] = 'X'
				self._board[x][y+2] = 'X'
				self._board[x][y+3] = 'X'
				self._board[x-1][y+3] = 'X'
				self._board[x][y+3] = 'X'
				self._board[x+1][y+3] = 'X'

				ok = "Succesful added"
		return ok

	def getGrid(self, x, y):
		'''
		in: x, y - the coords 
		out: what is at that position
		descr: the value at the coords position
		'''
		return self._board[x][y]

	def setGrid1(self, x,y,char):
   		self._board1[x][y] = char
   			

	def checkCoord(self, x, y):
		'''
		in: x, y - the coords
		out: True/False if the position is right or not 
		descr: check if the position is free and on limits for the orientation Sus
		'''
		if(Board.isFree(self, x, y) == False):
			return("Is something there already")

		if (x+3 > 9 or y - 2 <= 0 or y +2 > 9):
			return ("Invalid coord")

		'''if(Board.isFree(self, x+3, y) == False or Board.isFree(self, x, y-2) == False or Board.isFree(self, x, y+2) == False):
			return ("Invalid")
		'''

		if(Board.isFree(self, x+1, y) == False or Board.isFree(self, x+2, y) == False or
		 Board.isFree(self, x+3, y) == False or Board.isFree(self, x+1, y-1) == False or
		  Board.isFree(self, x+1, y-2) == False or Board.isFree(self, x+1, y+2) == False or 
		  Board.isFree(self, x+1, y+1) == False or Board.isFree(self, x+3, y+1) == False or 
		  Board.isFree(self, x+3, y-1) == False):
			return ("Invalid")
		

		return True

	def checkCord1(self, x, y):
		'''
		descr: check coords for the orientation Jos
		'''
		if(Board.isFree(self, x, y) == False):
			return("Is something there already")

		if (x <= 3 or y - 2 <= 0 or y +2 > 9):
			return ("Invalid coord")
			
		if(Board.isFree(self, x-1, y) == False or Board.isFree(self, x-2, y) == False or 
			Board.isFree(self, x-3, y) == False or Board.isFree(self, x-1, y-1) == False or 
			Board.isFree(self, x-2, y-2) == False or Board.isFree(self, x-1, y+1) == False or 
			Board.isFree(self, x-1, y) == False or Board.isFree(self, x-3, y+1) == False or 
			Board.isFree(self, x-3, y-1) == False):
			return ("something there")
		

		return True

	def checkCord2(self, x, y):
		'''
		descr: check coord for the orientation Right
		'''
		if(Board.isFree(self, x, y) == False):
			return("Is something there already")

		if (x < 3 or x > 7 or y <= 3):
			return ("Invalid coord")

		if(Board.isFree(self, x-1, y-1) == False or Board.isFree(self, x-2, y-1) == False or 
			Board.isFree(self, x+1, y-1) == False or Board.isFree(self, x+2, y-1) == False or 
			Board.isFree(self, x, y-2) == False or Board.isFree(self, x, y-3) == False or 
			Board.isFree(self, x-1, y-3) == False or Board.isFree(self, x, y+3) == False or 
			Board.isFree(self, x+1, y-3) == False):
			return ("something there")

		return True

	def checkCord3(self, x, y):
		'''
		descr: check the coords for the Left 
		'''
		if(Board.isFree(self, x, y) == False):
			return("Is something there already")

		if (x < 3 or x > 7 or y >= 7):
			return ("Invalid coord")

		if(Board.isFree(self, x, y+1) == False or Board.isFree(self, x-1, y+1) == False or 
			Board.isFree(self, x-2, y+1) == False or Board.isFree(self, x+1, y+1) == False or 
			Board.isFree(self, x+2, y+1) == False or Board.isFree(self, x, y+2) == False or 
			Board.isFree(self, x, y+3) == False or Board.isFree(self, x-1, y+3) == False or 
			Board.isFree(self, x, y+3) == False):
			return ("something there")

		return True

	def isFull(self):
		'''
		descr: check if is some free squares
		'''
		return len(self.getFreeSquares()) == 0

	def getAll(self):
		'''
		descr: return the board 
		'''
		return self._board


class Game:
	def __init__(self):
		self._board = Board()



