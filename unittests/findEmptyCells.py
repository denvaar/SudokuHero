import unittest
import numpy
from src.algorithms.sudokuTemplate \
    import SudokuSolverOne, SudokuSolverTwo

class TestFindEmptyCells(unittest.TestCase):
    def testFindEmptyCells(self):
        self.grid2 = numpy.array([['1', '1', '_', '4', '5', '6'],
                                 ['_', '2', '_', '4', '5', '6'],
                                 ['_', '2', '3', '4', '5', '6'],
                                 ['_', '2', '3', '4', '5', '6'],
                                 ['1', '2', '3', '4', '5', '6'],
                                 ['_', '_', '_', '_', '5', '6']])
        self.grid = numpy.array([['4', '2', '_', '1'],
                                  ['_', '_', '_', '2'],
                                  ['3', '_', '2', '_'],
                                  ['_', '4', '_', '3']])
        print(self.grid)
        self.solver2 = SudokuSolverTwo()
        self.solver1 = SudokuSolverOne()
        self.solver1.puzzleSize = 4
        self.solver2.puzzleSize = 4
        self.solver1.puzzle = self.grid
        self.solver2.puzzle = self.grid
        result2 = self.solver2.getEmptyCells()
        result1 = self.solver1.getEmptyCells()
        
        print(result1)
        print(result2)
        
        self.assertEqual(result1, result2)
        
        print(self.grid2)
        self.solver2 = SudokuSolverTwo()
        self.solver1 = SudokuSolverOne()
        self.solver1.puzzleSize = 6
        self.solver2.puzzleSize = 6
        self.solver1.puzzle = self.grid2
        self.solver2.puzzle = self.grid2
        result2 = self.solver2.getEmptyCells()
        result1 = self.solver1.getEmptyCells()
        
        print(result1)
        print(result2)
        
        self.assertEqual(result1, result2)
        
        self.grid = numpy.array([['4', '2', '5', '1'],
                                  ['6', 'q', '5', '2'],
                                  ['3', '5', '2', '0'],
                                  ['_', '4', '%', '3']])
        print(self.grid)
        self.solver2 = SudokuSolverTwo()
        self.solver1 = SudokuSolverOne()
        self.solver1.puzzleSize = 4
        self.solver2.puzzleSize = 4
        self.solver1.puzzle = self.grid
        self.solver2.puzzle = self.grid
        result2 = self.solver2.getEmptyCells()
        result1 = self.solver1.getEmptyCells()
        self.assertEqual(result1, result2)
        print(result1)
        print(result2)

if __name__ == '__main__':
    unittest.main()
