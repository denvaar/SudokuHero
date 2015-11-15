import numpy
import sys
from math import sqrt

from PyQt5.QtCore import QThread, pyqtSignal

class AbstractSudoku(object):
   
    EMPTY_CELL = '_'

    def __init__(self):
        self.puzzle = None
    
    def getEmptyCells(self):
        methodName = sys._getframe().f_code.co_name
        msg = "Must provide an implementation of '%s' method." % methodName
        raise NotImplementedError(msg)
    
    def validate(self, sudoku, x, y):
        methodName = sys._getframe().f_code.co_name
        msg = "Must provide an implementation of '%s' method." % methodName
        raise NotImplementedError(msg)

    def isGui(self):
        # A hook for gui implementations.
        return False

    def updateGui(self, x, y, c):
        methodName = sys._getframe().f_code.co_name
        msg = "Must provide an implementation of '%s' method." % methodName
        raise NotImplementedError(msg)

    def solveSudoku(self):
        # Do not override this method.
        empty = self.getEmptyCells()
        if empty == [(-1,-1)]:
            return False
        if not empty:
            return True
        if not self.validate(empty[0][1], empty[0][0]):
            return False
        answerMaybe = self.getPossibleAnswers(empty[0][1], empty[0][0])
        for possibleAnswer in answerMaybe:
            self.puzzle[empty[0][0]][empty[0][1]] = possibleAnswer
            if self.isGui():
                self.updateGui(empty[0][0], empty[0][1], possibleAnswer)
            if self.solveSudoku():
                return True
            self.puzzle[empty[0][0]][empty[0][1]] = AbstractSudoku.EMPTY_CELL
        return False

class SudokuSolverOne(AbstractSudoku, QThread):

    EMPTY_CELL = '_'
    trigger = pyqtSignal(int, int, str)
    finished = pyqtSignal(str)

    def __init__(self):
        AbstractSudoku.__init__(self)
        QThread.__init__(self)
    
    def run(self):
        if self.solveSudoku():
            self.finished.emit("SOLVED")
            print(self.puzzle)
        else:
            self.finished.emit("IMPOSSIBLE")
            print(self.puzzle)

    def isGui(self):
        # A hook for gui implementations.
        return True

    def updateGui(self, x, y, c):
        self.trigger.emit(y, x, c)

    def setData(self, tup): 
        self.puzzleSize = tup[0]
        self.puzzleValues = tup[1]
        self.puzzle = numpy.array(tup[2])

    def getEmptyCells(self):
        print(self.puzzleSize)
        emptyCells = []
        x = y = 0
        for row in self.puzzle:
            for cell in row:
                if cell == SudokuSolverOne.EMPTY_CELL:
                    emptyCells.append((y, x))
                x = x + 1
            y = y + 1
            x = 0
        return emptyCells
    
    def getBox(self, x, y):
        # Uses some fancy math to get all of the
        # values in the same box as cell(x,y)
        p = (x,y)
        boxSize = int(sqrt(self.puzzleSize))
        relBox = [(row,col) for col in range(0, boxSize) \
            for row in range(0, boxSize)]
        absBox = [(p[0]+(i[0]-p[0]%boxSize),p[1]+(i[1]-p[1]%boxSize)) \
            for i in relBox]
        return set([self.puzzle[cell[1]][cell[0]] for cell in absBox \
            if self.puzzle[cell[1]][cell[0]] != SudokuSolverTwo.EMPTY_CELL])
    '''
    def getBox(self, x, y):
        return self._getBox(x, y, set())

    def _getBox(self, x, y, setOfCells):
        if x%self.puzzleSize < self.puzzleSize and y%self.puzzleSize < self.puzzleSize:
            setOfCells.update([self.puzzle[x][y]])
            self._getBox(x+1, y, setOfCells)
        return setOfCells
    '''
    def validate(self, x, y): 
        horizontal = set(self.puzzle[:,x]) - set([SudokuSolverOne.EMPTY_CELL])
        vertical = set(self.puzzle[y]) - set([SudokuSolverOne.EMPTY_CELL])
        return len(list(\
            filter(lambda a: a != SudokuSolverOne.EMPTY_CELL, self.puzzle[:,x]))) \
            == len(horizontal) and \
            len(list(\
            filter(lambda a: a != SudokuSolverOne.EMPTY_CELL, self.puzzle[y]))) \
            == len(vertical)

    def getPossibleAnswers(self, x, y):
        l = set()
        l.update([i for i in self.puzzle[:,x] if i != SudokuSolverOne.EMPTY_CELL])
        l.update([i for i in self.puzzle[y] if i != SudokuSolverOne.EMPTY_CELL])
        l.update(self.getBox(x-x%int(sqrt(len(self.puzzle))),
                               y-y%int(sqrt(len(self.puzzle)))))
        return set(self.puzzleValues) - l

class SudokuSolverTwo(AbstractSudoku, QThread):

    EMPTY_CELL = '_'
    trigger = pyqtSignal(int, int, str)
    finished = pyqtSignal(str)

    def __init__(self):
        AbstractSudoku.__init__(self)
        QThread.__init__(self)
    
    def run(self):
        if self.solveSudoku():
            self.finished.emit("SOLVED")
        else:
            self.finished.emit("IMPOSSIBLE")

    def isGui(self):
        # A hook for gui implementations.
        return True

    def updateGui(self, x, y, c):
        self.trigger.emit(y, x, c)

    def setData(self, tup): 
        self.puzzleSize = tup[0]
        self.puzzleValues = tup[1]
        self.puzzle = numpy.array(tup[2])
    
    
    def getEmptyCells(self):
        # Uses recursion to gather all of the
        # empty cell values.
        l = []
        e = self._getEmptyCells(emptyCells=l)
        return e
        #return self._getEmptyCells()

    def _getEmptyCells(self, row=0, emptyCells=[]):
        try:
            if row == self.puzzleSize-1:
                [emptyCells.append((row,i)) for i, letter in enumerate(self.puzzle[row]) \
                    if letter == SudokuSolverTwo.EMPTY_CELL]
                return emptyCells
            [emptyCells.append((row,i)) for i, letter in enumerate(self.puzzle[row]) \
                if letter == SudokuSolverTwo.EMPTY_CELL]
            return self._getEmptyCells(row+1, emptyCells)
        except IndexError:
            return [(-1,-1)]
    
    def getBox(self, x, y):
        # Uses some fancy math to get all of the
        # values in the same box as cell(x,y)
        p = (x,y)
        boxSize = int(sqrt(self.puzzleSize))
        relBox = [(row,col) for col in range(0, boxSize) \
            for row in range(0, boxSize)]
        absBox = [(p[0]+(i[0]-p[0]%boxSize),p[1]+(i[1]-p[1]%boxSize)) \
            for i in relBox]
        return set([self.puzzle[cell[1]][cell[0]] for cell in absBox \
            if self.puzzle[cell[1]][cell[0]] != SudokuSolverTwo.EMPTY_CELL])

    def validate(self, x, y): 
        horizontal = set(self.puzzle[:,x]) - set([SudokuSolverTwo.EMPTY_CELL])
        vertical = set(self.puzzle[y]) - set([SudokuSolverTwo.EMPTY_CELL])
        return len(list(\
            filter(lambda a: a != SudokuSolverTwo.EMPTY_CELL, self.puzzle[:,x]))) \
            == len(horizontal) and \
            len(list(\
            filter(lambda a: a != SudokuSolverTwo.EMPTY_CELL, self.puzzle[y]))) \
            == len(vertical)

    def getPossibleAnswers(self, x, y):
        l = set()
        l.update([i for i in self.puzzle[:,x] if i != SudokuSolverTwo.EMPTY_CELL])
        l.update([i for i in self.puzzle[y] if i != SudokuSolverTwo.EMPTY_CELL])
        l.update(self.getBox(x-x%int(sqrt(len(self.puzzle))),
                               y-y%int(sqrt(len(self.puzzle)))))
        return set(self.puzzleValues) - l
