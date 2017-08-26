# -*- coding: utf-8 -*-
import wx





class MyWindow(wx.Frame): 
    def __init__(self, parent=None, title=None, size=(640, 480)): 
        super().__init__(parent, title=title)
        self.SetClientSize(*size)
        

        
        
        self.Show()
        
        # define property of the ball
        self.x = 30
        self.y = 10
        self.vx = 7
        self.vy = 5
        
        self.dia = 20

        # Set Timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)       
        self.timer.Start(20)
        
    def OnTimer(self, event):
        # Graphics Update
        w, h = self.GetClientSize()
        bdc = wx.BufferedDC(wx.ClientDC(self))
        bdc.SetBackground(wx.Brush("white"))  
        bdc.Clear()
        
        # Update Circle Pos
        self.x += self.vx
        self.y += self.vy
        
        if self.x > w or self.x < 0:
            self.vx = - self.vx
        if self.y > h or self.y < 0:
            self.vy = - self.vy

        # Draw Circle
        bdc.SetPen(wx.Pen(wx.Colour(0,0,0)))
        bdc.SetBrush(wx.Brush(wx.Colour(112,146,190)))
        bdc.DrawCircle(self.x, self.y, self.dia/2)

        
        
        
        
        
def Main():
    app = wx.App()
    w = MyWindow(title="wxPython Animation Simple", size=(200, 200))
    app.MainLoop()

if __name__=="__main__":
    Main()
    