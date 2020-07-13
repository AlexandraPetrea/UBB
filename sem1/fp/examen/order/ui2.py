from tab import * 
from random import randint

class UI:
	def __init__(self):
		self._game = Game()

	def GameUI(self):
		print("Start Game")
		b = Board()
		Board.printA(b)
		ai = Board.getFreeSquares(b)
		#for i in range(0, len(ai)):
		#	print(ai[i].getX(), ai[i].getY())

		self.Game(b)
		Board.printA(b)


	def Game(self, b):
		ok = True
		OK = False
		while (len(Board.getFreeSquares(b)) !=0 and Board.checkWin(b) == False):
			if ok == True:
				while OK == False:
					try:
						x = int(input("Give the x: "))
						y = int(input("Give the y: "))
						user = input("Give the X or O: ")
						if x < 1 or x > 6 or y < 1 or y > 6 or user not in ['X', 'O']:
							raise ValueError
						else:
							OK = True
					except ValueError:
						print('Try altceva')
						OK = False
				Board.setGrid1(b, x, y, user)
				ok = False
				#Board.printA(b)
			else:
				x, y,char = Board.checkPoz(b)
				if char == 'X':
					char = 'O'
				else:
					char = 'X'
				if x == y == 0:
					ok1 = False
					while(ok1 == False):
						x = randint(1, 6)
						y = randint(1, 6)
						print(x, y)
						print(Board.isFree(b, x, y))
						if (Board.isFree(b, x, y) == True):
							Board.setGrid1(b,1, 2, 'X')
							#Board.printA(b)
							ok1 = True
				else:
					Board.setGrid1(b, x, y, char)
				ok = True
				Board.printA(b)
				#Board.printA(b)



	def Read(self, a, b):
		ok = 0

		while(ok == 0):
			a = input("Give the x: ")
			if a > "J" or a <"A" or len(a) != 1:
				print("Not good")
			else:
				ok = 1
		a = ord(a)-64
		ok = 0
		while (ok == 0):
			try:
				b = int(input("Give the y: "))
				if b >= 1 and b <= 10:
					ok = 1
			except ValueError:
				ok = 0
				print("Not good")
			if ok == 0:
				print("Try something else")
		
		return a, b

		
board = UI()
UI.GameUI(board)
Game()



