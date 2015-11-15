import unittest

import numpy

from src.algorithms.sudokuTemplate \
    import SudokuSolverOne, SudokuSolverTwo

class TestBox(unittest.TestCase):
    def testGetBox(self):
        self.grid = numpy.array([['1', '_', '_', '4', '5', '6'],
                                 ['_', '2', '3', '4', '5', '6'],
                                 ['_', '2', '3', '4', '5', '6'],
                                 ['_', '2', '3', '4', '5', '6'],
                                 ['1', '2', '3', '4', '5', '6'],
                                 ['_', '_', '_', '_', '5', '6']])
        #self.grid = numpy.array([['1', '_', '_', '4'],
        #                         ['_', '2', '3', '4'],
        #                         ['1', '2', '3', '4'],
        #                         ['_', '_', '_', '_']])
        print(self.grid)
        self.solver2 = SudokuSolverTwo()
        self.solver1 = SudokuSolverOne()
        self.solver1.puzzleSize = 3
        self.solver2.puzzleSize = 3
        self.solver1.puzzle = self.grid
        self.solver2.puzzle = self.grid
        result2 = self.solver2.getBox(5,5)
        result1 = self.solver1.getBox(5,5)
        print("Solver1 =>",result1)
        print("Solver2 =>",result2)
        self.assertEqual(result1, result2)

if __name__ == '__main__':
    unittest.main()
