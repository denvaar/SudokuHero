import unittest

import numpy

from src.algorithms.fileFactory \
    import FileFactory

class TestBox(unittest.TestCase):
    def testSaveAndLoad(self):
        self.grid = numpy.array([['4', 'B', '3', '1'],
                                 ['1', '3', '4', 'B'],
                                 ['3', '1', 'B', '4'],
                                 ['B', '4', '1', '3']])
        print(self.grid)
        print(numpy.asarray(self.grid))
        fileFactory = FileFactory()
        saverObject = fileFactory.saveFile("Joins & Maps")
        saverObject.savePuzzle(self.grid, "foo.txt")

        loaderObject = fileFactory.getFile("foo.txt")
        tup = loaderObject.load("foo.txt")
        value = (self.grid == numpy.array(tup[2])).all()
        self.assertTrue(value)
    
    def testSaveAndLoadValues(self):
        self.grid = numpy.array([['4', '0', '3', '1'],
                                 ['1', '3', '4', '0'],
                                 ['3', '1', '0', '4'],
                                 ['0', '4', '1', '3']])
        print(self.grid)
        print(numpy.asarray(self.grid))
        fileFactory = FileFactory()
        saverObject = fileFactory.saveFile("Joins & Maps")
        saverObject.savePuzzle(self.grid, "foo.txt")

        loaderObject = fileFactory.getFile("foo.txt")
        tup = loaderObject.load("foo.txt")
        self.assertTrue(['0','1','3','4'] == tup[1])

    def testSaveAndLoadSize(self):
        self.grid = numpy.array([['4', '0', '3', '1'],
                                 ['1', '3', '4', '0'],
                                 ['3', '1', '0', '4'],
                                 ['0', '4', '1', '3']])
        print(self.grid)
        print(numpy.asarray(self.grid))
        fileFactory = FileFactory()
        saverObject = fileFactory.saveFile("Joins & Maps")
        saverObject.savePuzzle(self.grid, "foo.txt")

        loaderObject = fileFactory.getFile("foo.txt")
        tup = loaderObject.load("foo.txt")
        self.assertTrue(4 == tup[0])
    
    def testSaveAndLoad_Row(self):
        self.grid = numpy.array([['4', 'B', '3', '1'],
                                 ['1', '3', '4', 'B'],
                                 ['3', '1', 'B', '4'],
                                 ['B', '4', '1', '3']])
        print(self.grid)
        print(numpy.asarray(self.grid))
        fileFactory = FileFactory()
        saverObject = fileFactory.saveFile("Row-based")
        saverObject.savePuzzle(self.grid, "foo.txt")

        loaderObject = fileFactory.getFile("foo.txt")
        tup = loaderObject.load("foo.txt")
        value = (self.grid == numpy.array(tup[2])).all()
        self.assertTrue(value)
    
    def testSaveAndLoadValues_Row(self):
        self.grid = numpy.array([['4', '0', '3', '1'],
                                 ['1', '3', '4', '0'],
                                 ['3', '1', '0', '4'],
                                 ['0', '4', '1', '3']])
        print(self.grid)
        print(numpy.asarray(self.grid))
        fileFactory = FileFactory()
        saverObject = fileFactory.saveFile("Row-based")
        saverObject.savePuzzle(self.grid, "foo.txt")

        loaderObject = fileFactory.getFile("foo.txt")
        tup = loaderObject.load("foo.txt")
        self.assertTrue(['0','1','3','4'] == tup[1])

    def testSaveAndLoadSize_Row(self):
        self.grid = numpy.array([['4', '0', '3', '1'],
                                 ['1', '3', '4', '0'],
                                 ['3', '1', '0', '4'],
                                 ['0', '4', '1', '3']])
        print(self.grid)
        print(numpy.asarray(self.grid))
        fileFactory = FileFactory()
        saverObject = fileFactory.saveFile("Row-based")
        saverObject.savePuzzle(self.grid, "foo.txt")

        loaderObject = fileFactory.getFile("foo.txt")
        tup = loaderObject.load("foo.txt")
        self.assertTrue(4 == tup[0])

if __name__ == '__main__':
    unittest.main()
