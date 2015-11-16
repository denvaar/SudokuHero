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
        result2 = self.solver2.getBox(5,5)
        result1 = self.solver1.getBox(5,5)
        print("Solver1 =>",result1)
        print("Solver2 =>",result2)
        self.assertEqual(result1, result2)

        print(self.grid2)
        self.solver2 = SudokuSolverTwo()
        self.solver1 = SudokuSolverOne()
        self.solver1.puzzleSize = 4
        self.solver2.puzzleSize = 4
        self.solver1.puzzle = self.grid2
        self.solver2.puzzle = self.grid2
        result2 = self.solver2.getBox(2,3)
        result1 = self.solver1.getBox(2,3)
        print("Solver1 =>",result1)
        print("Solver2 =>",result2)
        self.assertEqual(result1, result2)
        
        print(self.grid2)
        self.solver2 = SudokuSolverTwo()
        self.solver1 = SudokuSolverOne()
        self.solver1.puzzleSize = 4
        self.solver2.puzzleSize = 4
        self.solver1.puzzle = self.grid2
        self.solver2.puzzle = self.grid2
        result2 = self.solver2.getBox(3,3)
        result1 = self.solver1.getBox(3,3)
        print("Solver1 =>",result1)
        print("Solver2 =>",result2)
        self.assertEqual(result1, result2)
        
        print(self.grid2)
        self.solver2 = SudokuSolverTwo()
        self.solver1 = SudokuSolverOne()
        self.solver1.puzzleSize = 4
        self.solver2.puzzleSize = 4
        self.solver1.puzzle = self.grid2
        self.solver2.puzzle = self.grid2
        result2 = self.solver2.getBox(0,0)
        result1 = self.solver1.getBox(0,0)
        print("Solver1 =>",result1)
        print("Solver2 =>",result2)
        self.assertEqual(result1, result2)

        self.grid3 = numpy.array([['_', '_', '_', '_'],
                                  ['_', '_', '_', '_'],
                                  ['_', '_', '_', '_'],
                                  ['_', '_', '_', '_']])
        print(self.grid3)
        self.solver2 = SudokuSolverTwo()
        self.solver1 = SudokuSolverOne()
        self.solver1.puzzleSize = 4
        self.solver2.puzzleSize = 4
        self.solver1.puzzle = self.grid3
        self.solver2.puzzle = self.grid3
        result2 = self.solver2.getBox(1,1)
        result1 = self.solver1.getBox(3,3)
        print("Solver1 =>",result1)
        print("Solver2 =>",result2)
        self.assertEqual(result1, set())
        self.assertEqual(result2, set())
        
        self.grid4 = numpy.array([['X', '_', '_', '_'],
                                  ['_', '_', '_', '_'],
                                  ['Y', 'J', '_', 'T'],
                                  ['_', '_', '_', '_']])
        print(self.grid4)
        self.solver2 = SudokuSolverTwo()
        self.solver1 = SudokuSolverOne()
        self.solver1.puzzleSize = 4
        self.solver2.puzzleSize = 4
        self.solver1.puzzle = self.grid4
        self.solver2.puzzle = self.grid4
        result2 = self.solver2.getBox(1,1)
        result1 = self.solver1.getBox(0,3)
        print("Solver1 =>",result1)
        print("Solver2 =>",result2)
        self.assertEqual(result1, set(['Y','J']))
        self.assertEqual(result2, set(['X']))
        
        self.grid4 = numpy.array([['X', '_', '_', '_'],
                                  ['_', '_', '_', '_'],
                                  ['Y', 'J', '_', 'T'],
                                  ['_', '_', '_', '_']])
        print(self.grid4)
        self.solver2 = SudokuSolverTwo()
        self.solver1 = SudokuSolverOne()
        self.solver1.puzzleSize = 4
        self.solver2.puzzleSize = 4
        self.solver1.puzzle = self.grid4
        self.solver2.puzzle = self.grid4
        result2 = self.solver1.getBox(0,3)
        result1 = self.solver2.getBox(1,1)
        print("Solver1 =>",result1)
        print("Solver2 =>",result2)
        self.assertEqual(result2, set(['Y','J']))
        self.assertEqual(result1, set(['X']))


if __name__ == '__main__':
    unittest.main()
