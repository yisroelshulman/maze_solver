from gui import Window
from maze import Maze
import time
import random

def _skip_one_line() -> None:
    print()

# input in range is inclusive
def _input_in_range(start: int, end: int, msg: str) -> int:
    u_input = float('-inf')
    while u_input < start or u_input > end:
        try:
            u_input = int(input(f'{msg}' ))
        except Exception:
            pass
    _skip_one_line()
    return u_input

# rows and columns have the restrictin of < 1000 because of recursion limits in python
def _num_row_and_column() -> None:
    rows = float('inf')
    columns = float('inf')
    while rows * columns > 1000 or  rows * columns < 2:
        print('Note: rows * columns must be less than 1000, and greater than 2')
        try:
            rows = int(input('Enter how many rows: '))
            columns = int(input('Enter the number of columns: '))
        except Exception:
            pass
        _skip_one_line()
    return rows, columns

def _min(x: float, y: float) -> float:
    if x < y:
        return x
    return y

def main():

    win_height = _input_in_range(100, 900, 'Enter the height, range(100, 900): ')
    win_width = _input_in_range(100, 1200, 'Enter the width, range(100, 1200): ')
    num_rows, num_columns = _num_row_and_column()
    cell_size = _min((win_height - 10) / num_rows, (win_width - 10) / num_columns)

    # not recoverable even though we can make it, it would add alot of logic
    if cell_size < 10:
        print(f'FATAL ERROR: cell size too small')
        return

    try:
        seed = int(input('Enter a seed number or hit enter to have the default set: '))
    except Exception:
        seed = 'default'

    print('Starting...')
    time.sleep(random.randrange(0, 2))
    _skip_one_line()
    print('Building Maze with')
    print(f'height: {win_height}, width: {win_width}')
    print(f'rows: {num_rows}, columns: {num_columns}')
    print(f'cell size: {cell_size}x{cell_size}')
    print(f'seed: {seed}')
    if seed == 'default':
        seed = 15
    window = Window(win_height, win_width)
    maze = Maze(5, 5, num_rows, num_columns, cell_size, window, seed)
    print('Build Done.')

    _skip_one_line()
    time.sleep(2)
    print('Solving...')
    if maze._solve():
        print('Done.')

    window.wait_for_close()
    return

main()