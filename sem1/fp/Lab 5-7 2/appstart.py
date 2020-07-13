from repository import * 
from domaine import * 
from tests import * 
from bookController import *
from clientController import * 
from rentalController import * 
from ui import * 
#from undoController import * 
from undoRepo import *
from undo import *
from redoController import*
from redoRepository import * 
from Validator import *
from redoController import * 
from redoRepository import *

#from bookControllerWithUndo import*

bookRepository= Repository()
clientRepository = Repository()
rentalRepository= Repository()
undoRepository = UndoRepository()
redoRepository = RedoRepository()


clientController = ClientController(clientRepository)
rentalController = RentalController(rentalRepository)
bookController = BookController(bookRepository)
validator = ValidatorException(Exception)
redoController = RedoController(redoRepository, bookController, clientController, rentalController)

undoController = UndoController(undoRepository, bookController, clientController, rentalController, redoController)
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

ui = UI(bookController, clientController, rentalController, undoController, validator, redoController)

	
ui.mainMenu()





