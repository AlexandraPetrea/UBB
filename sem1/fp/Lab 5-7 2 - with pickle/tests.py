from repository import * 
from domaine import * 
from tests import * 
from bookController import *

bookRepository= Repository()

bookController = BookController(bookRepository)


def testRentals():
    
    rental1 = rental("1", '2', '12', '2017-11-21', '1','2017-11-22')
    rental2 = rental('2', '2', '31', 'date1', '10','2017-11-22')
    rental3 = rental('3', '3', '32', 'date2', '14','2017-11-23')
    rental4 = rental('4', '4', '41', 'date3', '100','2017-11-30')

    assert rental1.returnClientId() == "2"
    assert rental2.returnClientId() == "2"
    assert rental3.returnClientId() == "3"
    assert rental4.returnClientId() == "4"

    assert rental1.returnBookId() == "12"
    assert rental2.returnBookId() == "31"
    assert rental3.returnBookId() == "32"
    assert rental4.returnBookId() == "41"

    assert rental1.getDate() == "2017-11-21"
    assert rental2.getDate() == "date1"
    assert rental3.getDate() == "date2"
    assert rental4.getDate() == "date3"


    assert rental1.returnDateYear() == "2017"
    assert rental2.returnDateYear() == "date"
    assert rental3.returnDateYear() == "date"
    assert rental4.returnDateYear() == "date"

def testClient():
    client1 = client("1","Ana")
    client2 = client("2","Maria")
    client3 = client("3","Dan")
    client4 = client("4","Vlad")

    assert client1.getId() == "1"
    assert client2.getId() == "2"
    assert client3.getId() == "3"
    assert client4.getId() == "4"

    assert client1.returnName() == "Ana"
    assert client2.returnName() == "Maria"
    assert client3.returnName() == "Dan"
    assert client4.returnName() == "Vlad"


def testBooks():
    book1 = book("1","12","date","10")
    book2 = book("2","31","date1","11")
    book3 = book("3","32","date2","14")
    book4 = book("4","41","date3","100")

    repo = Repository()

    bookNew= book("12","title","description","author")
    Repository.add(repo, bookNew)


    assert book1.getId() == "1"
    assert book2.getId() == "2"
    assert book3.getId() == "3"
    assert book4.getId() == "4"

    assert book1.returnTitle() == "12"
    assert book2.returnTitle() == "31"
    assert book3.returnTitle() == "32"
    assert book4.returnTitle() == "41"

    assert book1.returnDescr() == "date"
    assert book2.returnDescr() == "date1"
    assert book3.returnDescr() == "date2"
    assert book4.returnDescr() == "date3"

    assert book1.returnAuthor() == "10"
    assert book2.returnAuthor() == "11"
    assert book3.returnAuthor() == "14"
    assert book4.returnAuthor() == "100"


def testAll():
    ok = True
    try:
        testRentals()
    except AssertionError:
        ok = False
        return ("Invalid rentals test")
    try:
        testClient()
    except AssertionError:
        ok = False
        return("Invalid client test")

    try:
        testBooks()
    except AssertionError:
        ok = False
        return("Invalid books test")

    if ok == True:
        return("All test passed")

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self._repo = Repository()

    def testBookRepo(self):
       
        new_repo = bookRepository
        new_controller = bookController
       
        new_controller.add(('1', 'title1', 'description1', 'author1')) 
        #print(new_repo.getAll())
        assert new_repo.getAll() == [('1', 'title1', 'description1', 'author1')]
        #== ('1', 'title1', 'description1', 'author1')
        
        new_controller.add(('2', 'title2', 'description2', 'author2'))
        assert new_repo.getAll() == [('1', 'title1', 'description1', 'author1'),('2', 'title2', 'description2', 'author2')]

        new_controller.add(('3', 'title3', 'description3', 'author3')) 
        assert new_repo.getAll() == [('1', 'title1', 'description1', 'author1'),('2', 'title2', 'description2', 'author2'),('3', 'title3', 'description3', 'author3')]
        
        
        new_controller.update(('1', '1', '1', '1'))
        assert new_repo.getAll() == [('2', 'title2', 'description2', 'author2'),('3', 'title3', 'description3', 'author3'), ('1', '1', '1', '1'),]

        new_controller.update(('1', 'titlu', 'desc', 'aut')) 
        assert new_repo.getAll() == [('2', 'title2', 'description2', 'author2'),('3', 'title3', 'description3', 'author3'),('1', 'titlu', 'desc', 'aut'),]
        
    
        new_controller.delete('1') 
        assert new_repo.getAll()== [('2', 'title2', 'description2', 'author2'),('3', 'title3', 'description3', 'author3')]
        
        new_controller.delete('2') 
        assert new_repo.getAll() == [('3', 'title3', 'description3', 'author3')]
        new_controller.delete('3') 
        assert new_repo.getAll() == []

        self.assertEqual(len(self._repo), 0)
        z = book("1", "titlu", "descr", 'Ana')
        self._repo.add(z)
        self.assertEqual(len(self._repo), 1)
        z = book("2", "tile", "descr1", "Maria")
        self._repo.add(z)
        self.assertEqual(len(self._repo), 2)

        
        '''
    '''
    '''
    def testClientRepo(self):
        new_repo = ClientRepository()
        new_controller = ClientController(new_repo)

        assert new_controller.add(client('1', 'name1')) == 'Addition successful!'
        assert new_controller.add(client('2', 'name2')) == 'Addition successful!'
        assert new_controller.add(client('3', 'name3')) == 'Addition successful!'

        assert new_controller.remove('1') == 'Removal successful!'
        assert new_controller.remove('2') == 'Removal successful!'
        assert new_controller.remove('3') == 'Removal successful!'

    def testRentalRepo(self):
        new_repo = RentalRepository()
        new_controller = RentalController(new_repo)

        assert new_controller.rent(rental('1', '1', '1', date(2016, 4, 1), date(2017, 1, 1), None)) == 'Rental successful!'
        assert new_controller.rent(rental('2', '2', '1', date(2016, 5, 1), date(2016, 10, 1), None)) == 'Rental successful!'
        assert new_controller.rent(rental('3', '3', '2', date(2016, 6, 1), date(2017, 1, 1), None)) == 'Rental successful!'
    '''
    def testEverything(self):

       
        try:
            #self.testClientRepo()
            self.testBookRepo()
           # self.testRentalRepo()
            print("All tests passed!")
        except:
            print("Some test failed!")

        testAll()
if __name__ == '__main__':
    unittest.main()
    Test().testEverything()
    

    