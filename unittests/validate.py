import unittest

import numpy

from src.algorithms.sudokuTemplate \
    import SudokuSolverOne, SudokuSolverTwo

class TestValidate(unittest.TestCase):
    def testValidate(self):
        self.grid = numpy.array([['_', '_', '_', '4', '5', '1'],
                                 ['_', '2', '3', '4', '5', '2'],
                                 ['_', '2', '3', '4', '5', '3'],
                                 ['_', '2', '3', '4', '5', '4'],
                                 ['_', '2', '3', '4', '5', '5'],
                                 ['_', '_', '_', '_', '5', '6']])
        self.grid2 = numpy.array([['1', '_', '_', '4'],
                                 ['_', '2', '3', '4'],
                                 ['1', '2', '3', '4'],
                                 ['_', '_', '_', '_']])
        print(self.grid)
        self.solver2 = SudokuSolverTwo()
        self.solver1 = SudokuSolverOne()
        self.solver1.puzzleSize = 6
        self.solver2.puzzleSize = 6
        self.solver1.puzzle = self.grid
        self.solver2.puzzle = self.grid
        
        self.assertTrue(self.solver2.validate(5,5))
        self.assertTrue(self.solver1.validate(5,5))
        
        self.assertFalse(self.solver2.validate(4,4))
        self.assertFalse(self.solver1.validate(4,4))
        
        self.assertTrue(self.solver2.validate(0,0))
        self.assertTrue(self.solver1.validate(0,0))

        self.assertFalse(self.solver2.validate(1,1))
        self.assertFalse(self.solver1.validate(1,1))

if __name__ == '__main__':
    unittest.main()
