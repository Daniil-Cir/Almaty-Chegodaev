import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.x = 0
        self.y = 0
        self.r = 0
        self.flag = False
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.dr)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.setBR()
            self.draw()
            self.qp.end()

    def dr(self):
        self.flag = True
        self.update()

    def draw(self):
        self.r = random.randint(5, 100)
        self.x = random.randint(self.r, 800 - self.r)
        self.y = random.randint(self.r, 600 - self.r)
        self.qp.drawEllipse(self.x, self.y, self.r, self.r)
        self.flag = False
        self.qp.end()

    def setBR(self):
        self.qp.setBrush(QColor(255, 255, 0))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
