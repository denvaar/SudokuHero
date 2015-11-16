import sys
from PyQt5 import QtWidgets, QtCore, QtGui, Qt

from src.widgets.puzzleWidget import PuzzleWidget
from src.algorithms.sudokuTemplate import SudokuSolverOne, SudokuSolverTwo
#from src.algorithms.saveStrategy import ComplicatedSaver, SimpleSaver
from src.algorithms.fileFactory import FileFactory

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.fileFactory = FileFactory()
        self.setWindowTitle("Sudoku Hero")
        self.resize(1000,700)
        self.initUI()

    def initUI(self):
        '''
        Set up the controls for the window.
        '''
        layout = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        vbox2 = QtWidgets.QVBoxLayout()
        vbox3 = QtWidgets.QVBoxLayout()
        vbox = QtWidgets.QVBoxLayout()
        
        self.btnLoad = QtWidgets.QPushButton("Load Puzzles", self)
        self.btnSolve = QtWidgets.QPushButton("Solve", self)
        self.btnSave = QtWidgets.QPushButton("Save Result", self)
        self.btnSolve.setEnabled(False)
        self.btnSave.setEnabled(False)
        self.puzzleList = QtWidgets.QListWidget(self)
        self.puzzleList.setViewMode(Qt.QListView.IconMode)
        self.graphicsView = PuzzleWidget(self)
        self.combo = QtWidgets.QComboBox(self)
        self.combo.addItem("SudokuSolverOne")
        self.combo.addItem("SudokuSolverTwo")
        self.comboSave = QtWidgets.QComboBox(self)
        self.comboSave.addItem("Joins & Maps")
        self.comboSave.addItem("Row-based")
        label = QtWidgets.QLabel("Select <i>solving</i> method:", self)
        lblSave = QtWidgets.QLabel("Select <i>saving</i> method:", self)
        self.puzzleList.setFixedHeight(80) 
        self.puzzleList.setMinimumWidth(700) 
        
        hbox.addWidget(self.puzzleList)
        vbox2.addWidget(self.btnLoad)
        vbox3.addWidget(label)
        vbox3.addWidget(self.combo)
        vbox3.addWidget(lblSave)
        vbox3.addWidget(self.comboSave)
        hbox.addStretch(1)
        hbox.addLayout(vbox3)
        vbox2.addWidget(self.btnSolve)
        vbox2.addWidget(self.btnSave)
        
        vbox.addWidget(self.graphicsView)
        vbox.addLayout(hbox)
        hbox.addLayout(vbox2)
        layout.addLayout(vbox)
        self.setLayout(layout)
       
        # Event handlers
        self.btnLoad.clicked.connect(self.onClick)
        self.btnSolve.clicked.connect(self.onSolve)
        self.btnSave.clicked.connect(self.onSave)
        self.puzzleList.clicked.connect(self.onPuzzleClick)

    def onSolve(self):
        '''
        Happens when the "Solve" button is clicked.
        '''
        self.solver.trigger.connect(self.graphicsView.updateCell)
        self.solver.finished.connect(self.graphicsView.finished)
        self.solver.finished.connect(self.finished)
        self.solver.start()

    def onSave(self):
        '''
        Happens when the "Save" button is clicked.
        '''
        #if str(self.comboSave.currentText()) == "Joins & Maps":
        #    self.saver = SimpleSaver()
        #else:
        #    self.saver = ComplicatedSaver()
        
        filename = QtWidgets.QFileDialog.getSaveFileName( \
            self, 'Save puzzle as...', '', 'Text Files (*.txt)')
        #self.saver.savePuzzle(self.solver.puzzle, filename[0])
        
        saveObject = self.fileFactory.saveFile(\
            str(self.comboSave.currentText()))
        saveObject.savePuzzle(self.solver.puzzle, filename[0])

    def onClick(self):
        '''
        Happens when the "Load Puzzles" button is clicked.
        '''
        filenames = QtWidgets.QFileDialog.getOpenFileNames( \
            self, 'Select puzzles', '', 'Text Files (*.txt)')
        print(type(filenames))
        for _file in filenames[0]:
            listItem = QtWidgets.QListWidgetItem(_file)
            self.puzzleList.addItem(listItem)

    
    def onPuzzleClick(self, index):
        '''
        Happens when a puzzle is selected from the list.
        '''
        print(index.data())
        if str(self.combo.currentText()) == "SudokuSolverOne":
            self.solver = SudokuSolverOne()
        else:
            self.solver = SudokuSolverTwo()

        fileObject = self.fileFactory.getFile(index.data())
        tup = fileObject.load(index.data())
        self.solver.setData(tup)

        self.graphicsView.scene.clear()
        self.graphicsView.setPuzzle(self.solver.puzzle)
        self.btnSolve.setEnabled(True)
        self.btnSave.setEnabled(False)
    
    def finished(self, msg):
        '''
        Happens when a puzzle is finished being solved.
        '''
        if msg == "SOLVED":
            self.btnSave.setEnabled(True)        


# Application entry point
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
