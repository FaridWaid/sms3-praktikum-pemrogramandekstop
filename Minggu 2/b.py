import sys
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.layout1()
        
    def layout1(self):
        grid = QGridLayout()
        grid.setContentsMargins(10,10,10,10)

        btn = QPushButton("Cls",self)
        grid.addWidget(btn,0,0)

        btn = QPushButton("Bck",self)
        grid.addWidget(btn,0,1)

        btn = QPushButton("Close",self)
        grid.addWidget(btn,0,3)

        btn = QPushButton("7",self)
        grid.addWidget(btn,1,0)

        btn = QPushButton("8",self)
        grid.addWidget(btn,1,1)

        btn = QPushButton("9",self)
        grid.addWidget(btn,1,2)

        btn = QPushButton("/",self)
        grid.addWidget(btn,1,3)

        btn = QPushButton("4",self)
        grid.addWidget(btn,2,0)

        btn = QPushButton("5",self)
        grid.addWidget(btn,2,1)

        btn = QPushButton("6",self)
        grid.addWidget(btn,2,2)

        btn = QPushButton("*",self)
        grid.addWidget(btn,2,3)

        btn = QPushButton("1",self)
        grid.addWidget(btn,3,0)

        btn = QPushButton("2",self)
        grid.addWidget(btn,3,1)

        btn = QPushButton("3",self)
        grid.addWidget(btn,3,2)

        btn = QPushButton("-",self)
        grid.addWidget(btn,3,3)

        btn = QPushButton("0",self)
        grid.addWidget(btn,4,0)

        btn = QPushButton(".",self)
        grid.addWidget(btn,4,1)

        btn = QPushButton("=",self)
        grid.addWidget(btn,4,2)

        btn = QPushButton("+",self)
        grid.addWidget(btn,4,3)
        
        self.setLayout(grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    ex = Example()

    ex.setGeometry(100,100,200,100)
    ex.setWindowTitle("Calculator")
    ex.show()
    sys.exit(app.exec_())