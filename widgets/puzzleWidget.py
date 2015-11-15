from PyQt5 import QtWidgets, QtCore, QtGui, Qt

class PuzzleWidget(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(PuzzleWidget, self).__init__(parent)
        self.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.setScene(self.scene)
        self.rows = []
        self.itemDict = {}

    def drawBackground(self, painter, rect):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QColor(5,5,5, 50)) 
        gridSize = 200/4
        left = int(rect.left()) - (int(rect.left() % gridSize))
        top = int(rect.top()) - (int(rect.top() % gridSize))
        lines = []
        x = left
        y = top
        while x < rect.right():
            lines.append(QtCore.QLineF(x, rect.top(),
                x, rect.bottom()))
            x = x + gridSize
        while y < rect.bottom():
            lines.append(QtCore.QLineF(rect.left(), y,
                rect.right(), y))
            y = y + gridSize

        painter.drawLines([line for line in lines]) 
    
    def updateCell(self, x, y, c):
        gridSize = 200/4
        rect = self.sceneRect()
        left = int(rect.left()) - (int(rect.left() % gridSize))
        top = int(rect.top()) - (int(rect.top() % gridSize))
        left = left * x
        top = top * y
        if (left+50,top+50) in self.itemDict.keys():
            self.itemDict[(left+50,top+50)].setPlainText(c)
            self.itemDict[(left+50,top+50)].setDefaultTextColor(QtGui.QColor(0,0,0))
            self.scene.update()
    
    def finished(self, msg):
        color = None
        font = QtGui.QFont("Impact", self.sceneRect().width()/3)
        left = int(self.sceneRect().left()) - \
            (int(self.sceneRect().left() % (200/4)))
        solved = QtWidgets.QGraphicsTextItem(msg)
        solved.setFont(font)
        solved.setPos(left,
            self.sceneRect().height()/2)
        self.scene.addItem(solved)
        if msg == "SOLVED":
            color = QtGui.QColor(0,150,50)
        else:
            color = QtGui.QColor(200,0,0)
        #for item in self.items():
        #    item.setDefaultTextColor(color)
        solved.setDefaultTextColor(color)
        solved.setOpacity(0.3)

    def setPuzzle(self, values):
        self.scene.clear()
        self.scene = QtWidgets.QGraphicsScene(self)
        self.setScene(self.scene)
        self.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        self.itemDict = {}
        self.rows = values
        font = QtGui.QFont()
        font.setPointSize(36)

        gridSize = 200/4
        rect = self.sceneRect()
        left = int(rect.left()) - (int(rect.left() % gridSize))
        top = int(rect.top()) - (int(rect.top() % gridSize))
        for row in self.rows:
            for cell in row:
                item = QtWidgets.QGraphicsTextItem()
                #print("setting",(self.rows.tolist().index(row.tolist()),row.tolist().index(cell)),"to", cell)
                orig = cell
                if cell == '_':
                    cell = ' '
                item.setPlainText(cell)
                item.setFont(font)
                item.setPos(QtCore.QPointF(left+50,top+50))
                self.scene.addItem(item)
                self.itemDict[(left+50,top+50)]=item
                left = left + gridSize
            top = top + gridSize
            left = int(rect.left()) - (int(rect.left() % gridSize)) #+ gridSize


