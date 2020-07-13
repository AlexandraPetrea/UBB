from repository import * 
from domain import * 
from controller import *

repository= Repository()
controller = Controller(repository)

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self._repo = Repository()
        self._controller = Controller(self._repo)

    def testRepo(self):
       
        new_repo =  repository
        new_controller = controller


        new_repo.add(['1', 'non', 'ill', '0'])
        print(self._controller.vaccinate(1))
        self.assertEqual(new_repo.getAll(), [['1', 'non', 'ill', '0']])
        new_repo.add(['2', 'vac', 'healty', '0'])
        self.assertEqual(new_repo.getAll(), [['1', 'non', 'ill', '0'], ['2', 'vac', 'healty', '0']])
        new_repo.add(['3', 'non', 'healty', '0'])
        self.assertEqual(new_repo.getAll(),[['1', 'non', 'ill', '0'], ['2', 'vac', 'healty', '0'], ['3', 'non', 'healty', '0']])
        self.assertEqual(new_controller.vaccinate('1'), 'Error')
        self.assertEqual(new_controller.vaccinate('2'), 'Succesful')
        self.assertEqual(new_controller.vaccinate('3'), 'Succesful')
        self.assertEqual(new_controller._repo.number(), 1)

        self.assertEqual(len(self._repo), 0)
        z = person('1', 'name','a','b')
        self._repo.add(z)
        self.assertEqual(len(self._repo), 1)
        z = person("2", "name2", '1','2')
        self._repo.add(z)
        self.assertEqual(len(self._repo), 2)
        #print(self._repo)

if __name__ == '__main__':
    unittest.main()