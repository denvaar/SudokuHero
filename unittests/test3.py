import unittest

import numpy

from src.algorithms.saveTemplate \
    import AbstractSaveTemplate

class TestBox(unittest.TestCase):
    def testSave(self):
        self.grid = numpy.array([['4', 'B', '3', '1'],
                                 ['1', '3', '4', 'B'],
                                 ['3', '1', 'B', '4'],
                                 ['B', '4', '1', '3']])
        print(self.grid)
        print(numpy.asarray(self.grid))
        saver = AbstractSaveTemplate()
        saver.savePuzzle2(self.grid, "foo.txt")

if __name__ == '__main__':
    unittest.main()
