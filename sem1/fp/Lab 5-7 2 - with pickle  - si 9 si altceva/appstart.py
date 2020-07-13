from repository import * 
from domaine import * 
from tests import * 
from bookController import *
from clientController import * 
from rentalController import * 
from ui import * 
#from undoController import * 
from undoRepo import *
from undoController import *
from redoController import*
from redoRepository import * 
from Validator import *
from redoController import * 
from redoRepository import *
from bookControllerWithUndo import * 
from clientControllerWithUndo import * 
from rentalControllerWithUndo import *

from BookCSVFileRepository import *
from ClientCSVRepo import *
from RentalCSVRepo import * 
from PickleFileRepository import *
from shell import *

#from bookControllerWithUndo import*
'''
bookRepository= Repository()
clientRepository = Repository()
rentalRepository= Repository()
undoRepository = UndoRepository()
redoRepository = RedoRepository()

undoController = UndoController()
rentalController = RentalControllerWithUndo(undoController, RentalController, rentalRepository)
clientController = ClientControllerWithUndo(undoController, clientRepository, rentalController, clientRepository)
bookController = BookControllerWithUndo(undoController, bookController, rentalController, bookRepository)
validator = ValidatorException(Exception)
#redoController = RedoController(redoRepository, bookController, clientController, rentalController)

#bookController = BookController(undoController, redoController, bookRepository)
#bookController = BookControllerWithUndo(undoController,rentalController, bookRepository)

#book = BookControllerWithUndo.create(bookController,'2','3','4','5')
#print(bookRepository)


#controller = BookController(bookRepository) #clientController, rentalController)


bookController.add(["1","title","description","author"])
bookController.add(["2","Ana","are","author"])
bookController.add(["3","Morometii ","2 volume","author2"])
bookController.add(["5","Harry Potter","description4","author4"])
bookController.add(["4","Moara cu noroc","description3","Ion Slavici"])
bookController.add(["6","Adam si Eva","description5","Liviu Rebreanu"])
bookController.add(["7","Fluturi","description6","author6"])
bookController.add(["8","Inger si demon","description7","Dan Brown"])
bookController.add(["9","Codul lui DaVinci","description8","Dan Brown"])
bookController.add(["10","Simbolul pierdut","description9","author9"])
bookController.add(["11","Mmmm","description10","author10"])

clientController.add(["1","Ana"])
clientController.add(["2","Maria"])
clientController.add(["3","Magda"])
clientController.add(["4","Mirela"])
clientController.add(["5","Alex"])
clientController.add(["6","Andra"])
clientController.add(["7","Razvan"])
clientController.add(["8","Matei"])
clientController.add(["9","Vlad"])
clientController.add(["10","Carmen"])

rentalController.add(['1', '2', '1', '2017-11-21', '1', '2017-11-29'])
rentalController.add(['2', '3', '6', '2017-11-21', '2', '2017-11-30'])
rentalController.add(['3', '4', '9', '2017-11-21', '1', '2017-11-30'])
rentalController.add(['4', '3', '8', '2017-11-21', '1', '2017-11-30'])
rentalController.add(['5', '2', '11', '2017-11-21', '1', '2017-12-30'])

ui = UI(bookController, clientController, rentalController, undoController, validator )

	
#ui.mainMenu()
'''

tip = print("What would you like to use? \n 1. Pickle\n 2.Csv\n ~:")
userInput = input()

if userInput == '2':

    SETTINGS_FILE = "settings_text.txt"


    def readSettings():
        '''
        Reads the program's settings file
        output:
        A dictionary containing the program settings
        '''
        f = open(SETTINGS_FILE, "r")
        lines = f.read().split("\n")
        settings = {}
    
        for line in lines:
            setting = line.split("=")
            if len(setting) > 1:
                settings[setting[0]] = setting[1]
        f.close()
        return settings

    settings = readSettings()

    undoRepository = UndoRepository()
    redoRepository = RedoRepository()
    bookRepository = BookCSVRepo()
    clientRepository = ClientCSVRepo()
    rentalRepository = RentalCSVRepo(bookRepository, clientRepository)

    if 'CSV' == settings['repository']:
        bookRepo = BookCSVRepo(settings['books'])
        clientRepo = ClientCSVRepo(settings['clients'])
        rentalRepo = RentalCSVRepo(bookRepository, clientRepository, settings['rentals'])


    print('-' * 10 + " Clients " + '-' * 10)
    print(clientRepo)
    print('-' * 10 + " Books " + '-' * 10)
    print(bookRepo)
    print('-' * 10 + " Rentals " + '-' * 10)
    print(rentalRepo)

    readSettings()

    rentalRepository = RentalCSVRepo(bookRepository, clientRepository)

    undoController = UndoController()
    rentalController = RentalControllerWithUndo(undoController, RentalController, rentalRepository)
    clientController = ClientControllerWithUndo(undoController, clientRepository, rentalController, clientRepository)
    bookController = BookControllerWithUndo(undoController, bookController, rentalController, bookRepository)
    validator = ValidatorException(Exception)
else:
    SETTINGS_FILE = "settings_binary.properties.txt"

    def readSettings():
        '''
        Reads the program's settings file
        output:
        A dictionary containing the program settings
        '''
        f = open(SETTINGS_FILE, "r")
        lines = f.read().split("\n")
        settings = {}
    
        for line in lines:
            setting = line.split("=")
            if len(setting) > 1:
                settings[setting[0]] = setting[1]
        f.close()
        return settings

    settings = readSettings()
    bookRepository = None
    clientRepository = None
    rentalRepository = None

    if 'binary' == settings['repository']:
        bookRepository = PickleFileRepository(settings['books'])
        clientRepository = PickleFileRepository(settings['clients'])
        rentalRepository = PickleFileRepository(settings['rentals'])


    undoController = UndoController()
    rentalController = RentalControllerWithUndo(undoController, RentalController, rentalRepository)
    clientController = ClientControllerWithUndo(undoController, clientRepository, rentalController, clientRepository)
    bookController = BookControllerWithUndo(undoController, bookController, rentalController, bookRepository)
    validator = ValidatorException(Exception)

    print('-' * 10 + " Clients " + '-' * 10)
    print(clientRepository)
    print('-' * 10 + " Books " + '-' * 10)
    print(bookRepository)
    print('-' * 10 + " Rentals " + '-' * 10)
    print(rentalRepository)

#bookRepository.setitem(3, ['1', 'X', 'X', 'X'])

'''
print(bookRepository.__iter__())

print(bookRepository.__next__())
print(bookRepository.__next__())
print(bookRepository.__delItem__(0))
bookRepository.__setItem__(9, ['S','Ana','are','mere'])
print(bookRepository.__iter__())
lista = [1, 3, 8, 5]


def MaiMic(x, y):
    return(x < y )

print(shellSort(lista, MaiMic))
'''

ui = UI(bookController, clientController, rentalController, undoController, validator )

ui.mainMenu()
