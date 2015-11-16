
class FileFactory(object):
    '''
    Factory for loading puzzle files.
    '''
    def getFile(self, filename):
        with open(filename, 'rb') as f:
            pos = f.tell()
            lineEndingTest = f.readline().decode('UTF-8')
            if lineEndingTest.endswith('\r\n'):
                print("DOS line-endings")
                return DOSFile()
            elif lineEndingTest.endswith('\n'):
                print("UNIX line-endings")
                return UNIXFile()
            f.seek(pos)
    
    def saveFile(self, method):
        if method == "Joins & Maps":
            return SimpleSaver()
        if method == "Row-based":
            return ComplicatedSaver()
        return None

class SaveInterface(object):
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

class ComplicatedSaver(SaveInterface):
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

class SimpleSaver(SaveInterface):
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

class FileInterface(object):
    def load(self, filename):
        methodName = sys._getframe().f_code.co_name
        msg = "Must provide an implementation of '%s' method." % methodName
        raise NotImplementedError(msg)

class DOSFile(FileInterface):
    '''
    Provides file operations for a file with
    DOS line endings.
    '''
    def load(self, filename):
        with open(filename, 'rb') as f:
            # DOS line endings.
            puzzleSize = int(f.readline())
            print(puzzleSize)

            puzzleValues = f.readline().decode('UTF-8').\
                rstrip('\r\n').split(' ')

            print(puzzleValues)
            _puzzle = [['_' if cell == '-' \
                else cell for cell in list(filter(None, row))] \
                for row in \
                    [i.split(' ') for i in \
                        f.read().decode('UTF-8').split('\r\n')]]
            puzzle = list(filter(None, _puzzle))
            
            return tuple((puzzleSize, puzzleValues, puzzle))

class UNIXFile(FileInterface):
    '''
    Provides file operations for a file with
    UNIX line endings.
    '''
    def load(self, filename):
        with open(filename, 'rb') as f:
            # DOS line endings.
            puzzleSize = int(f.readline())
            print(puzzleSize)

            puzzleValues = f.readline().decode('UTF-8').\
                rstrip('\n').split(' ')

            print(puzzleValues)
            _puzzle = [['_' if cell == '-' \
                else cell for cell in list(filter(None, row))] \
                for row in \
                    [i.split(' ') for i in \
                        f.read().decode('UTF-8').split('\n')]]
            puzzle = list(filter(None, _puzzle))
            
            return tuple((puzzleSize, puzzleValues, puzzle))


