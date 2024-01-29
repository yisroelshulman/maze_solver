from gui import Window
from maze import Maze

def main():
    test = Window(800, 600)
    maze = Maze(5, 5, 10, 30, 15, test)
    test.wait_for_close()

main()