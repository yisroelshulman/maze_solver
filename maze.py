from cell import Cell
from gui import Window
import time
import random


class Maze:
    def __init__(self,
                 x: int,
                 y: int,
                 num_rows: int,
                 num_columns: int,
                 cell_size: float,
                 win: Window=None,
                 seed: int=None
                 ) -> None:
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size = cell_size
        self._win = win
        random.seed(seed)
        self._cells = []
        self._create_cells()
        self._mark_start_and_end()
        self._break_walls_r(self._start_row, self._start_column)
        self._reset_cells_visited()

    # loops through twice even though it is slower so the computation for the cell walls can be
    # done in its own method
    def _create_cells(self) -> None:
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_columns):
                row.append(Cell(self._win))
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_columns):
                self._draw_cell(i, j)

    def _draw_cell(self, row: int, column: int) -> None:
        x1 = column * self._cell_size + self._x
        x2 = (column + 1) * self._cell_size + self._x
        y1 = row * self._cell_size + self._y
        y2 = (row + 1) * self._cell_size + self._y
        self._cells[row][column].draw_walls(x1, y1, x2, y2)
        self._animate(0.00625)

    def _animate(self, delay: float) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(delay)

    # breaks the top wall of the top-left corner cell (the start position)
    # then breaks the bottom of the button-right corner cell (the end position)
    def _mark_start_and_end(self) -> None:
        self._start_row = self._start_column = None
        self._end_row = self._end_column = None
        while self._start_row == self._end_row and self._start_column == self._end_column:
            self._start_row = random.randrange(0, self._num_rows)
            self._start_column = random.randrange(0, self._num_columns)
            self._end_row = random.randrange(0, self._num_rows)
            self._end_column = random.randrange(0, self._num_columns)
        self._start = self._cells[self._start_row][self._start_column]
        self._end = self._cells[self._end_row][self._end_column]

        # checking here because we need a start and end even if we are not drawing it
        if self._win is None:
            return
        self._start.fill(self._win.canvas(), 'green')
        self._draw_cell(self._start_row, self._start_column)
        self._end.fill(self._win.canvas(), 'blue')
        self._draw_cell(self._end_row, self._end_column)

    # builds the maze using a depth first approach
    # we start at the top left cell mark it as visited
    # compile a list of adjacent (up, down, left, right) unvisited cells
    # if there are no unvisted cells to move to we are at the furthest depth on this path and return
    # randomly choose a cell from the list, break the walls connecting the cells and move there
    # mark the cell as visited and repeat (from compiling a list step)
    def _break_walls_r(self, row: int, column: int) -> None:
        self._cells[row][column].visited = True

        # only one way to reach the end
        if self._cells[row][column] == self._end:
            return

        # repeats until all adjacent cells where visited
        while True:
            # compiling the list of the adjacent visitable cells
            visitable = []
            if row > 0 and not self._cells[row - 1][column].visited:
                visitable.append(('up', row - 1, column))
            if column > 0 and not self._cells[row][column - 1].visited:
                visitable.append(('left', row, column - 1))
            if row + 1 < len(self._cells) and not self._cells[row + 1][column].visited:
                visitable.append(('down', row + 1, column))
            if column + 1 <  len(self._cells[0]) and not self._cells[row][column + 1].visited:
                visitable.append(('right', row, column + 1))

            # no visitable cells
            if len(visitable) == 0:
                return

            # randomly select a cell break the walls between and move there
            visit = visitable[random.randrange(0, len(visitable))]
            if visit[0] == 'up':
                self._cells[row][column].has_top_wall = False
                self._cells[row - 1][column].has_bottom_wall = False
            elif visit[0] == 'left':
                self._cells[row][column].has_left_wall = False
                self._cells[row][column - 1].has_right_wall = False
            elif visit[0] == 'down':
                self._cells[row][column].has_bottom_wall = False
                self._cells[row + 1][column].has_top_wall = False
            else:
                self._cells[row][column].has_right_wall = False
                self._cells[row][column + 1].has_left_wall = False
            self._draw_cell(row, column)
            self._break_walls_r(visit[1], visit[2])

    def _reset_cells_visited(self) -> None:
        for i in range(self._num_rows):
            for j in range(self._num_columns):
                self._cells[i][j].visited = False

    def _solve(self) -> bool:
        random.seed(None)
        return self._solve_r(self._start_row, self._start_column)

    # solves the maze with a DFS algorithm
    # creates a list of adjacent (up, down, left, right) cells from this cell, randomly moves to one
    # and walks the path drawing a line until the end or there are no adjacent visitable cells.
    # then we backtrack to the last cell with adjacent visitable cells and repeat graying out the
    # drawn line. if the current cell is the end then we return True
    def _solve_r(self, row: int, column: int) -> bool:
        self._animate(0.025)
        current = self._cells[row][column]
        current.visited = True
        if current == self._end: 
            return True
        # repeats until all adjacent cells are visited
        while True:
            visitable = [] # list of visitable adjacent cells
            if row > 0 and not self._cells[row - 1][column].visited and not current.has_top_wall:
                visitable.append('up')
            if column > 0 and not self._cells[row][column - 1].visited and not current.has_left_wall:
                visitable.append('left')
            if row + 1 < len(self._cells) and not self._cells[row + 1][column].visited and not current.has_bottom_wall:
                visitable.append('down')
            if column + 1 <  len(self._cells[0]) and not self._cells[row][column + 1].visited and not current.has_right_wall:
                visitable.append('right')

            # no visitable adjacent cells
            if len(visitable) == 0:
                return False

            # randomly select a cell to move to
            rand = random.randrange(0, len(visitable))
            if visitable[rand] == 'up':
                current.draw_move(self._cells[row - 1][column])
                if self._solve_r(row - 1, column):
                    return True
                current.draw_move(self._cells[row - 1][column], True)
            elif visitable[rand] == 'left':
                current.draw_move(self._cells[row][column - 1])
                if self._solve_r(row, column - 1):
                    return True
                current.draw_move(self._cells[row][column - 1], True)
            elif visitable[rand] == 'down':
                current.draw_move(self._cells[row + 1][column])
                if self._solve_r(row + 1, column):
                    return True
                self._cells[row][column].draw_move(self._cells[row + 1][column], True)
            else:
                current.draw_move(self._cells[row][column + 1])
                if self._solve_r(row, column + 1):
                    return True
                current.draw_move(self._cells[row][column + 1], True)