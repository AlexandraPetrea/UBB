from tab import * 


import unittest

class Test(unittest.TestCase):
   

    def testRepo(self):
        b = Board()
        
        self.assertEqual(Board.isFree(b,1,1), True)
        self.assertEqual(Board.isFree(b,9,9), True)

        self.assertEqual(Board.isFull(b), False)

        Board.setGrid(b,1,7,'S')
        self.assertEqual(Board.isFree(b,1,7), False)
        self.assertEqual(Board.isFree(b,2,7), False)
        self.assertEqual(Board.isFree(b,2,5), False)
        self.assertEqual(Board.isFree(b,2,9), False)

        self.assertEqual(Board.setGrid(b,1,1,'S'), 'Invalid coord')
        self.assertEqual(Board.setGrid(b,1,1,'R'), 'Invalid coord')
        self.assertEqual(Board.setGrid(b,1,1,'L'), 'Invalid coord')
        self.assertEqual(Board.setGrid(b,1,1,'J'), 'Invalid coord')

        self.assertEqual(Board.setGrid(b,1,2,'S'), 'Invalid coord')
        self.assertEqual(Board.setGrid(b,1,3,'S'), 'Invalid')
        self.assertEqual(Board.setGrid(b,1,7,'S'), 'Is something there already')
        self.assertEqual(Board.setGrid(b,2,7,'S'), 'Is something there already')
        self.assertEqual(Board.setGrid(b,1,1,'L'), 'Invalid coord')
        self.assertEqual(Board.setGrid(b,2,1,'R'), 'Invalid coord')
        self.assertEqual(Board.setGrid(b,8,2,'R'), 'Invalid coord')
        self.assertEqual(Board.setGrid(b,1,1,'J'), 'Invalid coord')
        self.assertEqual(Board.setGrid(b,8,3,'S'), 'Invalid coord')
        self.assertEqual(Board.setGrid(b,9,1,'S'), 'Invalid coord')
        self.assertEqual(Board.setGrid(b,2,3,'J'), 'Invalid coord')


        self.assertEqual(Board.checkCoord(b,1,7), 'Is something there already')
        self.assertEqual(Board.checkCoord(b,1,2), 'Invalid coord')
        self.assertEqual(Board.checkCoord(b,8,2), 'Invalid coord')
        self.assertEqual(Board.checkCoord(b,9,2), 'Invalid coord')


        self.assertEqual(Board.checkCord1(b,1,2), 'Invalid coord')
        self.assertEqual(Board.checkCord1(b,9,3), True)
        self.assertEqual(Board.checkCord1(b,4,3), True)
        self.assertEqual(Board.checkCord1(b,9,7), True)
        self.assertEqual(Board.checkCord1(b,9,8), 'Invalid coord')
        self.assertEqual(Board.checkCord3(b,1,7), 'Is something there already')


        self.assertEqual(Board.checkCord3(b,1,2), 'Invalid coord')
        self.assertEqual(Board.checkCord3(b,8,2), 'Invalid coord')
        self.assertEqual(Board.checkCord3(b,7,8), 'Invalid coord')
        self.assertEqual(Board.checkCord3(b,7,3), True)
        self.assertEqual(Board.checkCord3(b,7,7), 'Invalid coord')
        self.assertEqual(Board.checkCord3(b,1,7), 'Is something there already')


        self.assertEqual(Board.checkCord2(b,1,2), 'Invalid coord')
        self.assertEqual(Board.checkCord2(b,5,3), 'Invalid coord')
        self.assertEqual(Board.checkCord2(b,5,5), True)
        self.assertEqual(Board.checkCord2(b,5,9), 'something there')
        self.assertEqual(Board.checkCord3(b,1,7), 'Is something there already')


        Board.setGrid(b,7,2,'R')
        Board.setGrid(b,7,6,'L')
        Board.setGrid(b,5,5,'J')
       # print(Board.printA(b))
        
    
if __name__ == '__main__':
    unittest.main()