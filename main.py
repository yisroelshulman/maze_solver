from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color='red'):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack()

class Cell:
    def __init__(self, x1, x2, y1, y2, win): # x1 < x2, y1 < y2
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__win = win

    def draw_walls(self, canvas: Canvas, fill_color="black"):
        if self.has_left_wall:
            canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill=fill_color, width=2)
        if self.has_right_wall:
            canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill=fill_color, width=2)
        if self.has_top_wall:
            canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill=fill_color, width=2)
        if self.has_bottom_wall:
            canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill=fill_color, width=2)

    def center(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw_move(self, to_cell, undo=False):
        self.__win.draw_line(Line(self.center(), to_cell.center()))

class Window:
    def __init__(self, w, h):
        self.__width = w
        self.__height = h
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, height=self.__height, width=self.__width)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("closing window")

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color="red"):
        line.draw(self.__canvas, fill_color)

    def draw_cell(self, cell: Cell, fill_color="black"):
        cell.draw_walls(self.__canvas, fill_color)


def main():
    test = Window(800, 600)
    cell = Cell(50, 100, 50, 100, test)
    cell2 = Cell(150, 100, 150, 100, test)
    test.draw_cell(cell)
    test.draw_cell(cell2)
    cell.draw_move(cell2)
    test.wait_for_close()

main()