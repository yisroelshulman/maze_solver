from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self._p1 = p1
        self._p2 = p2

    def draw(self, canvas: Canvas, fill_color='black') -> None:
        canvas.create_line(self._p1.x, self._p1.y, self._p2.x, self._p2.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__canvas = Canvas(self.__root, height=self.__height, width=self.__width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
        print('closing window')

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line: Line, fill_color='black') -> None:
        line.draw(self.__canvas, fill_color)