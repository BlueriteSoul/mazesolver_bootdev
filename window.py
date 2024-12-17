from tkinter import Tk, BOTH, Canvas

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = 400
        self._x2 = 430
        self._y1 = 400
        self._y2 = 430
        self._win = window
    def draw(self, canvas, fillColor):
        if self.has_left_wall:
            canvas.create_line(
    self._x1, self._y1, self._x1, self._y2, fill=fillColor, width=2
)
        if self.has_right_wall:
            canvas.create_line(
    self._x2, self._y1, self._x2, self._y2, fill=fillColor, width=2
)
        if self.has_top_wall:
            canvas.create_line(
    self._x1, self._y1, self._x2, self._y1, fill=fillColor, width=2
)
        if self.has_bottom_wall:
            canvas.create_line(
    self._x1, self._y2, self._x2, self._y2, fill=fillColor, width=2
)
        
            
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        

    def draw(self, canvas, fillColor):
        canvas.create_line(
    self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fillColor, width=2
)


class Window:
    def __init__(self, width, height):
        # Create the main window
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fillColor):
        line.draw(self.canvas, fillColor)

    def draw_cell(self, cell, fillColor):
        cell.draw(self.canvas, fillColor)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False