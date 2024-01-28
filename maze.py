from tkinter import Tk, BOTH, Canvas
from gui import Line, Point

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

    def draw_walls(self, fill_color="black"):
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))

    def center(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw_move(self, to_cell, undo=False):
        self.__win.draw_line(Line(self.center(), to_cell.center()))


class Maze:
    def __init__(self, x, y, num_rows, num_columns, cell_size, win):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size = cell_size
        self._win = win
        self._create_cells()

        def _create_cells():
            self._cells = []
            
