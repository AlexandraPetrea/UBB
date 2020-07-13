from tab import * 
from random import randint

class UI:
	def __init__(self):
		self._game = Game()

	def GameUI(self):
		print("Start Game")
		b = Board()
		Board.printA(b)
		
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



