from math import sqrt
from src.Sudoku.Sudoku import Sudoku
from time import time

"""

**** SUDOKU SOLVER ****
Author: Andrea Pollastro
Date: September 2018   

"""

class SudokuSolver:
    def solveSudoku(self, sudoku):
        """This function checks if 'sudoku' has a good structure and it solves 'sudoku' using a backtracking algorithm.
        'sudoku' must be a list."""
        if not isinstance(sudoku,list):
            return False
        validValues = self.__getSupportStructures(sudoku)
        if validValues is False:
            # wrong structure
            return False
        validValues = self.__solve(validValues)
        if validValues is False:
            return False
        for i in validValues.keys():
            sudoku[i] = int(validValues[i])

    def __solve(self, validValues):
        """This function works recursively solves Sudoku.
        'validValues' is a dictionary which contains all the possible values for any cell. This function searches for
        the cell with the minimum choice of values. Then it chooses one of them and tries if that is a good solution.
        If it is not, it goes to the last good solution."""
        if all(len(validValues[i]) == 1 for i in validValues.keys()):
            return validValues
        n, cell = min((len(validValues[i]), i) for i in validValues.keys() if len(validValues[i]) > 1)
        oldState = validValues.copy()
        for value in oldState[cell]:
            if self.__assign(validValues,cell,value):
                validValues = self.__solve(validValues)
                if validValues is not False:
                    return validValues
            validValues = oldState
        return False

    def __assign(self, validValues, cell, value):
        """This function assigns 'value' to 'cell'.
        Since solving a Sudoku is NP-complete problem, I used the constraint propagation technique to quickly come to a
        dead end, if there is. In this way I can quickly come to contradictions or to a good solution.

        The constrain used for the propagation is the basic rule of the Sudoku:
        - One number can stay only once in it's column, row and box.
        In this way, when a value is assigned to a cell, that value is removed from all the peers' values.
        If it takes to a contradiction, 'assign' returns False, else, it returns True."""
        if not self.__removeFromPeers(validValues,cell,value):
            return False
        validValues[cell] = value
        return True

    def __removeFromPeers(self, validValues, cell, value):
        """This function removes 'value' from all the 'cell' 's peers. If one of them remains with only one choice,
        'assign' is called on that cell."""
        for p in self.__peers[cell]:
            if value in validValues[p]:
                validValues[p] = validValues[p].replace(value,'')
                if len(validValues[p]) == 0:
                    return False
                if len(validValues[p]) == 1 and not self.__assign(validValues,p,validValues[p]):
                    return False
        return True

    def hasUniqueSolution(self, sudoku):
        """This function checks if 'sudoku' has a good structure and it checks if 'sudoku' has a unique solution.
        'sudoku' must be a list."""
        if isinstance(sudoku,Sudoku):
            sudoku = sudoku.getSudoku()
        validValues = self.__getSupportStructures(sudoku)
        if validValues is not False:
            return self.__checkUniqueSolution(validValues,[0])
        return False

    def __checkUniqueSolution(self, validValues, counter):
        """This function works recursively on 'validValues'. If it comes to 2 solutions, it returns False."""
        if all(len(validValues[i]) == 1 for i in validValues.keys()):
            counter[0] += 1
            if counter[0] > 1:
                return False
            return True
        n, cell = min((len(validValues[i]), i) for i in validValues.keys() if len(validValues[i]) > 1)
        oldState = validValues.copy()
        for value in oldState[cell]:
            if self.__assign(validValues,cell,value) and not self.__checkUniqueSolution(validValues,counter):
                return False
            validValues = oldState
        return True

    def __getSupportStructures(self, sudoku):
        """This function is used to create two main structures used for solving the sudoku:
        - peers: it contains all the peers for any cell
        - validValues: it contains all possible values for any cell"""
        DIM = int(sqrt(len(sudoku)))
        if DIM**2 != len(sudoku):
            return False
        BOXDIM = int(sqrt(DIM))
        # peers
        self.__peers = dict()
        for i in range(0,len(sudoku)):
            row = int(i / DIM)
            col = i % DIM
            rbox = int(row / BOXDIM) * BOXDIM
            cbox = int(col / BOXDIM) * BOXDIM
            self.__peers[i] = {j for j in range(row*DIM,row*DIM+DIM)}
            for j in range(0,DIM):
                self.__peers[i].add(col+DIM*j)
            for j in range(rbox,rbox+3):
                for k in range(cbox,cbox+3):
                    self.__peers[i].add(j*DIM+k)
            self.__peers[i] = self.__peers[i]-{i}
        # valid values
        validValues = {i:''.join(map(str,range(1,DIM+1))) for i in range(0,len(sudoku))}
        if not all(self.__assign(validValues,i,str(sudoku[i])) for i in range(0,len(sudoku)) if sudoku[i] != 0):
            return False
        return validValues