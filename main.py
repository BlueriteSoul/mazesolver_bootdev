from tkinter import Tk, BOTH, Canvas
from window import *

def main():
    
    point1 = Point(5, 5)
    point2 = Point(90, 90)
    point3 = Point(330, 450)
    testLine = Line(point1, point2)
    testLine2 = Line(point2, point3)
    win = Window(800, 600)
    cell = Cell(win)
    win.draw_cell(cell, ("green"))
    win.draw_line(testLine, "black")
    win.draw_line(testLine2, "red")
    win.wait_for_close()



main()