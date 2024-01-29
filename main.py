from gui import Window
from maze import Maze
import time

def main():
    test = Window(800, 600)
    maze = Maze(5, 5, 10, 30, 15, test)
    time.sleep(1)
    maze._cells[9][10].draw_move(maze._cells[8][10])
    test.wait_for_close()

main()