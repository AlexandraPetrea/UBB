from repository import * 
from domain import * 
from CSVRepo import *
from controller import *
from ui import * 

repository = CSVRepo()
controller = Controller(repository)
ui = UI(controller)

ui.mainMenu()
