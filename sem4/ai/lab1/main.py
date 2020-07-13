import sys
sys.path.insert(0, '/sem4/ai/lab1/Domain')
sys.path.insert(0, '/sem4/ai/lab1/Controller')
sys.path.insert(0, '/sem4/ai/lab1/UI')
from Domain.Puzzle import Puzzle 
from Controller.PuzzleCtrl import PuzzleCtrl
from UI.Console import Console


def readPuzzle():
    try:
        initialFilename = "D:\sem4\AI\lab1\Resources\\9initial" 
        finalFilename = "D:\sem4\AI\lab1\Resources\\9final"  

        initialState = []
        finalState = []

        with open(initialFilename) as f:
            for line in f:
                line.strip("\n")
                initialState.append(line.split())

        with open(finalFilename) as f:
            for line in f:
                line.strip("\n")
                finalState.append(line.split())

    except IOError:
        raise Exception("File is missing")

    emptySpaceX, emptySpaceY = findEmptySpace(initialState)
    return Puzzle(initialState, finalState, emptySpaceX, emptySpaceY)


def findEmptySpace(initialState):
    n = len(initialState[0])
    for i in range(n):
        for j in range(n):
            if initialState[i][j] == '*':
                return i, j


if __name__ == '__main__':
    puzzle = readPuzzle()
    controller = PuzzleCtrl(puzzle)
    console = Console(controller)
    console.run()