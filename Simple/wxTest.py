# -*- coding: utf-8 -*-
import wx

class MyWindow(wx.Frame): 
    def __init__(self, parent=None, title=None, size=(640, 480)): 
        super().__init__(parent, title=title)
        
        self.SetClientSize(*size)
        
        self.Bind(wx.EVT_PAINT, self.OnPaint) 
        self.Show(True)
		
    def OnPaint(self, event=None): 
        # Graphics Update
        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush("white"))  
        dc.Clear()
        
        # Draw Circle
        dia = 100
        centerX, centerY = 100, 100
        dc.SetPen(wx.Pen(wx.Colour(0,0,0)))
        dc.SetBrush(wx.Brush(wx.Colour(112,146,190)))
        dc.DrawCircle(centerX, centerY, dia/2)

def Main():
    app = wx.App()
    w = MyWindow(title="wxPython Window Simple", size=(200, 200))

    # Call Main loop
    app.MainLoop()

if __name__=="__main__":
    Main()
    