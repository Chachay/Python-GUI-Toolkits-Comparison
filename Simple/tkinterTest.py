# -*- coding: utf-8 -*-
import tkinter as tk

def Main():
    root = tk.Tk()
    root.title("Tkinter Window Simple")
    root.geometry("200x200")

    # Define Canvas
    canvas = tk.Canvas(root, width = 200, height = 200, bg="#fff")
    canvas.place(x=0, y=0)

    # Draw Circle on Canvas
    dia = 100
    centerX, centerY = 100, 100
    id = canvas.create_oval(centerX - dia/2, centerY - dia/2,
                            centerX + dia/2, centerY + dia/2,
                            fill="#7092be")

    # Call Main loop
    root.mainloop()

if __name__=="__main__":
    Main()
    