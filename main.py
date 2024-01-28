from gui import Window
from maze import Cell

def main():
    test = Window(800, 600)
    cell = Cell(50, 100, 50, 100, test)
    cell2 = Cell(150, 100, 150, 100, test)
    cell.draw_walls()
    cell2.draw_walls()
    cell.draw_move(cell2)
    test.wait_for_close()

main()