import unittest 
from repository import * 
from controller import * 
from domain import * 
class Test(unittest.TestCase):
    def setUp(self):
        self._repo = Repository()

    def test(self):
        controller = Controller(self._repo)
        controller.add(Word('ale', 'ale'))
        assert self._repo.getAll() == [['ale', 'ale']]
        controller.add(Word('alex', 'lexa'))
        assert self._repo.getAll() == [['ale', 'ale'], ['alex','lexa']]
        aux = 'alexandra'
        assert not controller.modificare2(aux) == ['a','l','e','x','a','n','d','r','a']
        aux = 'maria'
        assert not controller.modificare2(aux) == ['m','a','r','i','a']
        aux = ['a','l','e','x']
        aux1 = ['a','e','l','x']
        assert controller.joaca(aux,aux1,0,1,0,2) == (True, ['a', 'l', 'e', 'x'], ['a', 'e', 'l', 'x'])
       #print(controller.joaca(aux,aux1,0,1,0,2))
        aux = ['a','l','e','x','a']
        aux1 = ['a','e','x','l','a']
        assert controller.joaca(aux, aux1,0,3,0,1) ==(False, ['a', 'l', 'x', 'e', 'a'], ['a', 'e', 'x', 'l', 'a'])
        assert controller.joaca(aux, aux1,0,2,0,3) == (True, ['a', 'l', 'e', 'x', 'a'], ['a', 'l', 'e', 'x', 'a'])
        aux = ['a','l','e','x','a','m']
        aux1 = ['a','e','x','l','a','m']
        assert controller.joaca(aux, aux1,0,3,0,1) ==(False, ['a', 'l', 'x', 'e', 'a','m'], ['a', 'l', 'x', 'e', 'a','m'])
        assert controller.joaca(aux, aux1,0,2,0,3) == (True, ['a', 'l', 'e', 'x', 'a','m'], ['a', 'l', 'e', 'x', 'a','m'])
        a = 'alex  are'
        assert controller.nScore(a) == 7
        a = 'alex'
        assert controller.nScore(a) == 4
        a = 'a a a a a'
        assert controller.nScore(a) == 5


if __name__ == '__main__':
    unittest.main()
