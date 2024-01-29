from tkinter import Tk, BOTH, Canvas
from cell import Cell
import time
import random


class Maze:
    def __init__(self, x, y, num_rows, num_columns, cell_size, win=None, seed=None):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size = cell_size
        self._win = win
        random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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

    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        start.has_top_wall = False
        self._draw_cell(0, 0)
        end = self._cells[len(self._cells) - 1][len(self._cells[0]) - 1]
        end.has_bottom_wall = False
        self._draw_cell(len(self._cells) - 1, len(self._cells[0]) - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            visitable = []
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                visitable.append('up') #, self._cells[i - 1][j])
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                visitable.append('left') #, self._cells[i][j - 1])
            if i + 1 < len(self._cells) and not self._cells[i + 1][j].visited:
                visitable.append('down') #, self._cells[i + 1][j])
            if j + 1 <  len(self._cells[0]) and not self._cells[i][j + 1].visited:
                visitable.append('right') #, self._cells[i][j + 1])
            if len(visitable) == 0:
                self._draw_cell(i, j)
                return
            rand = random.randrange(0, len(visitable))
            if visitable[rand] == 'up':
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
                self._break_walls_r(i - 1, j)
            elif visitable[rand] == 'left':
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False
                self._break_walls_r(i, j - 1)
            elif visitable[rand] == 'down':
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
                self._break_walls_r(i + 1, j)
            else:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False
                self._break_walls_r(i, j + 1)