import numpy

class AbstractSaveInterface(object):
    '''
    Interface for saving a puzzle.
    '''
    def savePuzzle(self, puzzle, filename):
        '''
        Saves a solved puzzle to to a file.
        '''
        methodName = sys._getframe().f_code.co_name
        msg = "Must provide an implementation of '%s' method." % methodName
        raise NotImplementedError(msg)

class ComplicatedSaver(AbstractSaveInterface):
    '''
    One way of implementing the save method
    from AbstractSaveInterface.
    '''
    def savePuzzle(self, puzzle, filename):
        with open(filename, 'wb') as f:
            f.write(bytes(str(len(puzzle)), "UTF-8"))
            f.write(bytes("\n", "UTF-8"))
            values = sorted([i for i in puzzle[:,0]])
            [f.write(bytes(i+" ", "UTF-8")) \
                if values.index(i) < len(values)-1 \
                    else f.write(bytes(i, "UTF-8")) \
                        for i in values]
            f.write(bytes("\n", "UTF-8"))
            for row in puzzle:
                for col in row:
                    if row.tolist().index(col) == len(row)-1:
                        f.write(bytes(col, "UTF-8"))
                    else:
                        f.write(bytes(col+" ", "UTF-8"))
                f.write(bytes("\n", "UTF-8"))

class SimpleSaver(AbstractSaveInterface):
    '''
    A simpler way to save a puzzle. Implements
    the AbstractSaveInterface.
    '''
    def savePuzzle(self, puzzle, filename):
        size = [len(puzzle)]
        v = sorted([i for i in puzzle[:,0]])
        with open(filename,"w") as f:
            f.write("\n".join(" ".join(map(str, x)) \
                for x in (size,v)))
            f.write("\n")
            f.write("\n".join(" ".join(map(str, x)) \
                for x in (puzzle)))


