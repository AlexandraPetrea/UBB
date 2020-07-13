import unittest 
from repository import * 
from controller import * 
from domain import * 
class Test(unittest.TestCase):
    def setUp(self):
        self._repo = Repository()

    def testRepo(self):
        controller = Controller(self._repo)
        controller.add(Word('ale', 'ale'))
        assert self._repo.getAll() == [['ale', 'ale']]
        controller.add(Word('alex', 'lexa'))
        assert self._repo.getAll() == [['ale', 'ale'], ['alex','lexa']]
        aux = 'alexandra'
        assert not controller.modificare2(aux) == ['a','l','e','x','a','n','d','r','a']
        aux = ['a','l','e','x']
        aux1 = ['a','e','l','x']
        assert controller.joaca(aux, aux1,0,1,0,2) == (True, ['a', 'l', 'e', 'x'], ['a', 'l', 'e', 'x'])
        aux = ['a','l','e','x','a']
        aux1 = ['a','e','x','l','a']
        assert controller.joaca(aux, aux1,0,3,0,1) ==(False, ['a', 'l', 'x', 'e', 'a'], ['a', 'l', 'x', 'e', 'a'])
        assert controller.joaca(aux, aux1,0,2,0,3) == (True, ['a', 'l', 'e', 'x', 'a'], ['a', 'l', 'e', 'x', 'a'])

'''
def testEverything(self):
       
    try:
        #self.testClientRepo()
        self.testRepo()
        # self.testRentalRepo()
        print("All tests passed!")
    except:
        print("Some test failed!")

    #testAll()
'''
if __name__ == '__main__':
    unittest.main()
   # Test().testEverything()
    

    