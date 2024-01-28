from tkinter import Tk, BOTH, Canvas
from cell import Cell
import time



class Maze:
    def __init__(self, x, y, num_rows, num_columns, cell_size, win):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size = cell_size
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_columns):
            row = []
            for j in range(self._num_rows):
                row.append(Cell(j * self._cell_size + self._y, (j + 1) * self._cell_size + self._y, i * self._cell_size + self._x, (i + 1) * self._cell_size + self._x, self._win))
            self._cells.append(row)
        for row in self._cells:
            for cell in row:
                self._draw_cell(cell)

    def _draw_cell(self, cell):
        cell.draw_walls()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)