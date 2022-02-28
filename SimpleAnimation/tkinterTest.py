# -*- coding: utf-8 -*-
import tkinter as tk





class MyWindow(tk.Tk): 
    def __init__(self, title=None, size=(640, 480)):
        super().__init__()
        self.title("Tkinter Window Simple")
        self.geometry("%dx%d"%(size))
                
        self.canvas  = tk.Canvas(self, width = size[0], height = size[1], bg="#fff")
        self.canvas.place(x=0, y=0)

        
        # define property of the ball
        self.x = 30
        self.y = 10
        self.vx = 7
        self.vy = 5
        
        self.dia = 20
        
        
        self.onTimer()
    
    def onTimer(self):
        # Clear Canvas
        h = self.winfo_height()
        w = self.winfo_width()
        self.canvas.delete('all')
        self.canvas.create_rectangle(0, 0, w, h, fill = 'white')
    
        # Update Circle Pos
        self.x += self.vx
        self.y += self.vy
        
        if self.x > w or self.x < 0:
            self.vx = - self.vx
        if self.y > h or self.y < 0:
            self.vy = - self.vy
    
    
        # Draw Circle on Canvas
        id = self.canvas.create_oval(self.x - self.dia/2, self.y - self.dia/2,
                                self.x + self.dia/2, self.y + self.dia/2,
                                fill="#7092be")
        self.after(20, self.onTimer)


def Main():
    w = MyWindow(title="PyQt5 Window Simple", size=(200, 200))

    # Call Main loop
    w.mainloop()

if __name__=="__main__":
    Main()
    
