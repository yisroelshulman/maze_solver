from gui import Line, Point, Window

class Cell:
    def __init__(self, win: Window=None) -> None:
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._win = win

    def _draw_wall(self, wall: Line, has_wall: bool) -> None:
        if has_wall:
            self._win.draw_line(wall)
        else:
            self._win.draw_line(wall, '#d9d9d9') # the default tkinter background color on windows

    # The 4 parameters have the following correspondence
    # x1 = left most x position
    # y1 = top most y position
    # x2 = right most x position
    # y2 = bottom most y position
    # this is because the windows top left corner has coords (0, 0)
    def draw_walls(self, x1: float, y1: float, x2: float , y2: float) -> None:
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)
        left_wall = Line(top_left, bottom_left)
        right_wall = Line(top_right, bottom_right)
        top_wall = Line(top_left, top_right)
        bottom_wall = Line(bottom_left, bottom_right)
        self._draw_wall(left_wall, self.has_left_wall)
        self._draw_wall(right_wall, self.has_right_wall)
        self._draw_wall(top_wall, self.has_top_wall)
        self._draw_wall(bottom_wall, self.has_bottom_wall)

    def _center(self) -> Point:
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    # undo represents backtracking on a path
    def draw_move(self, to_cell: 'Cell', undo=False) -> None:
        if self._win is None:
            return
        color = 'red'
        if undo:
            color = 'white'
        self._win.draw_line(Line(self._center(), to_cell._center()), color)