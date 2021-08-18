import sys
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.layout1()
        
    def layout1(self):
        grid = QGridLayout()
        grid.setContentsMargins(10,10,10,10)

        btn = QPushButton("1-3",self)
        grid.addWidget(btn,0,0,1,3)

        btn = QPushButton("4,7",self)
        grid.addWidget(btn,1,0,-2,1)

        btn = QPushButton("4",self)
        grid.addWidget(btn,1,1)

        btn = QPushButton("5",self)
        grid.addWidget(btn,1,2)

        btn = QPushButton("7",self)
        grid.addWidget(btn,2,1)

        btn = QPushButton("8",self)
        grid.addWidget(btn,2,2)

        self.setLayout(grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    ex = Example()

    ex.setGeometry(100,100,350,100)
    ex.setWindowTitle("Basic Grid Layout")
    ex.show()
    sys.exit(app.exec_())