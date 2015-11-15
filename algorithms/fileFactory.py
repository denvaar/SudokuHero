

class FileFactory(object):
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


