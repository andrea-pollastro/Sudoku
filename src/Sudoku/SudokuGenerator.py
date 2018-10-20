from random import shuffle
from math import sqrt
from enum import Enum
from src.Sudoku.SudokuSolver import SudokuSolver
from src.Sudoku.Sudoku import Sudoku

"""

**** SUDOKU GENERATOR ****
Author: Andrea Pollastro
Date: September 2018   

"""

class SudokuGenerator:
    __solver = SudokuSolver()

    def createSudoku(self, dimension, difficulty):
        """This method returns a Sudoku with a unique solution. Parameters are used to specify the dimension and the
        difficulty."""
        if not isinstance(dimension, SudokuDimension) and not isinstance(difficulty, SudokuDimension):
            return False
        sudoku = list() # grid
        self.__fillSudoku(sudoku,0,_SupportStructures(dimension.value))
        blanksIndexes = [i for i in range(0,len(sudoku))]
        shuffle(blanksIndexes)
        sudoku = self.__createBlanks(sudoku, difficulty.value, blanksIndexes, 0)
        return Sudoku(sudoku)

    def __fillSudoku(self, sudoku, cell, supportStructures):
        """This functions works recursively to create a complete Sudoku. It randomly assigns a value to cells. If
        a contradiction comes (specifically, when there aren't values to assign to a cell), it comes back to the last
        valid configuration."""
        values = supportStructures.getValidValues(cell)
        if(len(values) == 0):
            return False
        shuffle(values)
        for n in values:
            sudoku.append(n)
            supportStructures.addValue(n,cell)
            if((len(sudoku) == supportStructures.getSudokuDimension()**2) # sudoku is complete
                    or self.__fillSudoku(sudoku,cell+1,supportStructures)):
                return True
            sudoku.pop()
            supportStructures.removeValue(n,cell)
        return False

    def __createBlanks(self, sudoku, blanks, validValues, idx):
        """This functions creates blanks into 'sudoku' to make it playable. For any blanks, it checks if there's
        a unique solution. If it's not, it restores the last blank and chooses another cell."""
        if blanks == 0:
            return sudoku
        for i in range(idx,len(validValues)):
            index = validValues[i]
            oldValue = sudoku[index]
            sudoku[index] = 0
            if self.__solver.hasUniqueSolution(sudoku) and self.__createBlanks(sudoku, blanks-1, validValues, i+1):
                return sudoku
            sudoku[index] = oldValue
        return False


class SudokuDifficulties(Enum):
    EASY = 43
    MEDIUM = 50
    HARD = 58
    EXPERT = 61


class SudokuDimension(Enum):
    CLASSIC = 9


class _SupportStructures:
    def __init__(self, dimension):
        self.__DIM = dimension
        self.__BOXDIM = int(sqrt(dimension))
        self.__rows = [set() for x in range(0, dimension)]
        self.__cols = [set() for x in range(0, dimension)]
        self.__boxes = [set() for x in range(0, dimension)]

    def getValidValues(self, cell):
        values = {x for x in range(1, self.__DIM +1)}
        r, c, b = self.__getCoordinates(cell)
        return list(values - (self.__rows[r] | self.__cols[c] | self.__boxes[b]))

    def addValue(self, value, cell):
        r, c, b = self.__getCoordinates(cell)
        self.__rows[r].add(value)
        self.__cols[c].add(value)
        self.__boxes[b].add(value)

    def removeValue(self, value, cell):
        r, c, b = self.__getCoordinates(cell)
        self.__rows[r].remove(value)
        self.__cols[c].remove(value)
        self.__boxes[b].remove(value)

    def __getCoordinates(self, cell):
        r = int(cell / self.__DIM)
        c = cell % self.__DIM
        b = int(r / self.__BOXDIM) * self.__BOXDIM + int(c / self.__BOXDIM)
        return r,c,b

    def getSudokuDimension(self):
        return self.__DIM