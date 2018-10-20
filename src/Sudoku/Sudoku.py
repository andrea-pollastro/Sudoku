from math import sqrt

"""

**** SUDOKU ****
Author: Andrea Pollastro
Date: September 2018   

"""

class Sudoku:
    def __init__(self, sudoku):
        if isinstance(sudoku,str):
            sudoku = sudoku.replace(".","0")
            self.__sudoku = list(map(int,sudoku))
        else:
            self.__sudoku = sudoku
        self.__DIMENSION = int(sqrt(len(sudoku)))
        self.__BOXDIMENSION = int(sqrt(self.__DIMENSION))
        self.__blanks = self.__sudoku.count(0)

    def getBlanks(self):
        return self.__blanks

    def getDimension(self):
        return self.__DIMENSION

    def getSudoku(self):
        return self.__sudoku

    def printSudoku(self):
        tmpr = 0
        tmpc = 0
        self.__printRow()
        for i in range(0,self.__DIMENSION):
            print("|", end=" ")
            for j in range(0, self.__DIMENSION):
                print(self.__sudoku[(i * self.__DIMENSION) + j], end=" ")
                tmpc += 1
                if tmpc == self.__BOXDIMENSION:
                    tmpc = 0
                    print("|", end=" ")
            print()
            tmpr += 1
            if tmpr == self.__BOXDIMENSION:
                self.__printRow()
                tmpr = 0

    def __printRow(self):
        tmp = 0
        print("+", end=" ")
        for j in range(0, self.__DIMENSION):
            print("-", end=" ")
            tmp += 1
            if tmp == self.__BOXDIMENSION:
                tmp = 0
                print("+", end=" ")
        print()

    def isSolved(self):
        rows = [set() for x in range(0, self.__DIMENSION)]
        for i in range(0,len(self.__sudoku)):
            if self.__sudoku[i] != 0:
                rows[int(i / self.__DIMENSION)].add(self.__sudoku[i])
        return all(len(rows[i]) == self.__DIMENSION for i in range(0, len(rows)))