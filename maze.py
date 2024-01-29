from tkinter import Tk, BOTH, Canvas
from cell import Cell
import time



class Maze:
    def __init__(self, x, y, num_rows, num_columns, cell_size, win=None):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size = cell_size
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_columns):
                row.append(Cell(self._win))
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_columns):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = j * self._cell_size + self._x
        x2 = (j + 1) * self._cell_size + self._x
        y1 = i * self._cell_size + self._y
        y2 = (i + 1) * self._cell_size + self._y
        self._cells[i][j].draw_walls(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)