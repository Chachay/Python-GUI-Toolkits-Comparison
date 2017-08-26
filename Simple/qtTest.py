# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.Qt import QColor

class MyWindow(QWidget): 
    def __init__(self, parent=None, title=None, size=(640, 480)): 
        super().__init__()
        
        self.resize(*size)
        self.setWindowTitle(title)
        self.setStyleSheet("background-color : white;"); 
        
        self.show()
        
    def paintEvent(self, QPaintEvent):
        # Graphics Update
        qp = QPainter(self)
        
        # Draw Circle
        dia = 100
        centerX, centerY = 100, 100
        qp.setPen(QColor(0,0,0))
        qp.setBrush(QColor(112,146,190))
        qp.drawEllipse(centerX - dia/2, centerY - dia/2, dia, dia)
        
def Main():
    app  = QApplication(sys.argv)
    w    = MyWindow(title="PyQt5 Window Simple", size=(200, 200))
    sys.exit(app.exec_())

if __name__=="__main__":
    Main()
    