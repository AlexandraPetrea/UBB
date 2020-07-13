from texttable import * 
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
		self._board = [[0 for x in range(1,8)] for y in range(1,8)]
		#for i in range(1,5):
		#	self._board[1][i] = 'X'
		self._board1 = [[0 for x in range(1,7)] for y in range(1,7)]


	def printA(self):
		'''
		descr: the board printed
		'''
		#print(self._board)
		#print(self._board)
		table = Texttable()
		for i in range(0, 6):
			table.add_row([self._board[i][1], self._board[i][2], self._board[i][3], self._board[i][4], self._board[i][5], self._board[i][6]])
		print(table.draw())

		#xLabel = " " * 6
		#for i in range(1,8):           
			#xLabel += str(i) + " "

		#for i in range(1,7):
				#print(str(self._board[i][1]) +" " + str(self._board[i][2]) + " "+  str(self._board[i][3]) +" " + str(self._board[i][4]) +" " + str(self._board[i][5]) + " "+  str(self._board[i][6])) 
				
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
		for i in range(1, 7):
			for j in range(1,7):
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
		return ok
		'''
		pass
	def getGrid(self, x, y):
		'''
		in: x, y - the coords 
		out: what is at that position
		descr: the value at the coords position
		'''
		return self._board[x][y]

	def checkWin(self):
		ok = False
		for i in range(1, 6):
			if self._board[i][1] == self._board[i][2] == self._board[i][3] == self._board[i][4] == self._board[i][5] and self._board[i][1] in ['X', 'O']:
				ok = True
			if self._board[i][2] == self._board[i][3] == self._board[i][4] == self._board[i][5] == self._board[i][6] and self._board[i][2] in ['X', 'O']:
				ok = True
		for i in range(0, 6):
			if self._board[1][i] == self._board[2][i] == self._board[3][i] == self._board[4][i] == self._board[5][i] and self._board[1][i] in ['X', 'O']:
				ok = True
			if self._board[2][i] == self._board[3][i] == self._board[4][i] == self._board[5][i] == self._board[6][i] and self._board[2][i] in ['X', 'O']:
				ok = True
		if self._board[1][1] == self._board[2][2] == self._board[3][3] == self._board[4][4] == self._board[5][5] and self._board[1][1] in ['X', 'O']:
				ok = True
		if self._board[2][2] == self._board[3][3] == self._board[4][4] == self._board[5][5] == self._board[6][6] and self._board[1][i] in ['X', 'O']:
			ok = True
		if self._board[1][6] == self._board[2][5] == self._board[3][4] == self._board[4][3] == self._board[5][2] and self._board[1][6] in ['X', 'O']:
				ok = True
		if self._board[2][5] == self._board[3][4] == self._board[4][3] == self._board[5][2] == self._board[5][2] and self._board[1][i] in ['X', 'O']:
				ok = True
		return ok

	def checkPoz(self):
		ok = False
		x = 0 
		y = 0
		char = ""
		for i in range(1, 6):
			if self._board[i][1] == self._board[i][2] == self._board[i][3] == self._board[i][4] and self._board[i][1] in ['X', 'O']:
				ok = True
				if self.isFree(i, 5) == True:
					x, y = i, 5
					char = self._board[i][1]
					break 

			if self._board[i][2] == self._board[i][3] == self._board[i][4] == self._board[i][5] and self._board[i][2] in ['X', 'O']:
				ok = True
				if self.isFree(i,6):
					x, y = i, 6
					break
			if self._board[i][3] == self._board[i][4] == self._board[i][5] == self._board[i][6] == self._board[i][2] in ['X', 'O']:
				ok = True
				if self.isFree(1,2):
					x, y = 1, 2
					break
		for i in range(0, 6):
			if self._board[1][i] == self._board[2][i] == self._board[3][i] == self._board[4][i] == self._board[5][i] and self._board[1][i] in ['X', 'O']:
				ok = True
			if self._board[2][i] == self._board[3][i] == self._board[4][i] == self._board[5][i] == self._board[6][i] and self._board[2][i] in ['X', 'O']:
				ok = True
		if self._board[1][1] == self._board[2][2] == self._board[3][3] == self._board[4][4] == self._board[5][5] and self._board[1][1] in ['X', 'O']:
				ok = True
		if self._board[2][2] == self._board[3][3] == self._board[4][4] == self._board[5][5] == self._board[6][6] and self._board[1][i] in ['X', 'O']:
			ok = True
		if self._board[1][6] == self._board[2][5] == self._board[3][4] == self._board[4][3] == self._board[5][2] and self._board[1][6] in ['X', 'O']:
				ok = True
		if self._board[2][5] == self._board[3][4] == self._board[4][3] == self._board[5][2] == self._board[5][2] and self._board[1][i] in ['X', 'O']:
				ok = True
		return x, y, char
	def setGrid1(self, x,y,char):
   		self._board[x][y] = char
   			

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
