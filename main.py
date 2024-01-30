from gui import Window
from maze import Maze
import time

def main():
    test = Window(800, 600)
    maze = Maze(5, 5, 25, 25, 20, test, 0)

    time.sleep(5)
    print(maze._solve())
    
    test.wait_for_close()

main()