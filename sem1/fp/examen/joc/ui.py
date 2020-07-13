from tab import * 
from random import randint

class UI:
	def __init__(self):
		self._game = Game()

	def GameUI(self):
		print("Start Game")
		b = Board()
		Board.printA(b)
		x = int(0)
		y = int(0)
		nr = 0
		while(True):
			x, y = UI.Read(self,x, y)
			poz = input("Give the orientation: S - for sus, J - for jos, R - for right, L - for left: ")
			while poz not in ['S','J','R','L']:
				print("Try something right! ")
				poz = input("Give the orientation: S - for sus, J - for jos, R - for right, L - for left: ")

			ok = Board.setGrid(b,x,y, poz)
			Board.printA(b)
			print(ok)
			if (ok == "Succesful added"):
				nr = nr + 1
				#print(nr)
			if nr == 2:
				print("Your board: ")
				Board.printA(b)
				break

		c = Board()
		print("\n")         	
		
		nr = 0
		nrIncercari = 0 
		while(True):
			x = randint(1,6)
			y = randint(3,7)
			nrIncercari = nrIncercari + 1
			#print(x, y)
			#print("nr", nr)
			nr1 = randint(1, 4)
			if nr1 == '1':
				poz = 'S'
			elif nr1 == '2':
				poz = 'R'
			elif nr1 == '3':
				poz = 'J'
			else:
				poz = 'L'
			ok = Board.setGrid(c, x, y, poz)
			#print(ok)

			if (ok == "Succesful added"):
				nr = nr + 1

			if nr == 2:
				#print("Start to play:")
				#print("Computer board: ")
				#Board.printA(c)
				break
			
			if nrIncercari > 40 and nr < 2:
				c =  Board()
				Board.setGrid(c, 1, 7, 'S')
				Board.setGrid(c, 5, 2, 'R')
				print("Start to play: ")
				break
			
		
		
		cap = 0
		cap2 = 0
		player = True
		x1 = 0
		y1 = 0
		while(True):
			if cap == 2 and cap2 == 1:
				x1 = randint(1,10)
				y1 = randint(1,10)
				if(Board.getGrid(b,x1, y1) == 'C'):
					print("Warning! Cap hit by the computer!")
					Board.setGrid1(c, x1, y1, 'C')
					cap2 = cap2 + 1
				elif Board.getGrid(b,x1, y1) == 'X':
					print("Warning! Hit by the computer!")
					Board.setGrid1(c, x1, y1, 'H')
				else:
					Board.setGrid1(c, x1, y1, 'M')
				if cap2 == 2:
					print("Is draw!")
					break
					
			if cap == 2:
				print("You win")
				break
			if cap2 == 2:
				print("Computer win")
				break

			if player == True:
				x1, y1 = UI.Read(self,x1, y1)
				if(Board.getGrid(c,x1, y1) == 'C'):
					print("You hit the cap!")
					Board.setGrid1(b, x1, y1, 'C')
					
					cap  = cap + 1
				elif Board.getGrid(c,x1, y1) == 'X':
					print("Hit! ")
					ok = Board.setGrid1(b, x1, y1, 'H')
				else:
					Board.setGrid1(b, x1, y1, 'M') 
				#print("Computer board:")
				#Board.printA(c)
			
				player = False
			else:
				x1 = randint(1,10)
				y1 = randint(1,10)
				if(Board.getGrid(b,x1, y1) == 'C'):
					print("Warning! Cap hit by the computer!")
					Board.setGrid1(c, x1, y1, 'C')
					cap2 = cap2 + 1
				elif Board.getGrid(b,x1, y1) == 'X':
					print("Warning! Hit by the computer!")
					Board.setGrid1(c, x1, y1, 'H')
				else:

					Board.setGrid1(c, x1, y1, 'M') 
				print("Your board:")
				Board.printA(b)
				player = True


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



