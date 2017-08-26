# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.Qt import QColor, QTimer

class MyWindow(QWidget): 
    def __init__(self, parent=None, title=None, size=(640, 480)): 
        super().__init__()
        
        self.resize(*size)
        self.setWindowTitle(title)
        self.setStyleSheet("background-color : white;"); 
        
        self.show()
    
        # define property of the ball
        self.x = 30
        self.y = 10
        self.vx = 7
        self.vy = 5
        
        self.dia = 20
        
        # Set Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.OnTimer)
        self.timer.start(20)

    def OnTimer(self):
        h = self.height()
        w = self.width()
    
        # Update Circle Pos
        self.x += self.vx
        self.y += self.vy
        
        if self.x > w or self.x < 0:
            self.vx = - self.vx
        if self.y > h or self.y < 0:
            self.vy = - self.vy
        
        # Paint Event
        self.update()
        
    def paintEvent(self, QPaintEvent):
        # Graphics Update
        qp = QPainter(self)
        
        # Draw Circle
        qp.setPen(QColor(0,0,0))
        qp.setBrush(QColor(112,146,190))
        qp.drawEllipse(self.x - self.dia/2, self.y - self.dia/2, self.dia, self.dia)
        
        
def Main():
    app  = QApplication(sys.argv)
    w    = MyWindow(title="PyQt5 Window Simple", size=(200, 200))
    sys.exit(app.exec_())

if __name__=="__main__":
    Main()
    