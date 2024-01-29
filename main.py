from gui import Window
from maze import Maze
import time

def main():
    test = Window(800, 600)
    maze = Maze(5, 5, 20, 20, 20, test, 0)
    
    test.wait_for_close()

main()