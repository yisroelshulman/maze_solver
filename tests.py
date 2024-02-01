import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_columns = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_columns, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_columns)

    def test_maze_break_entrance_and_exit(self):
        num_columns = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_columns, 10)
        m1._mark_start_and_end()
        self.assertFalse(m1._start is None)
        self.assertFalse(m1._end is None)

    def test_wall_break(self):
        num_columns = 30
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_columns, 10)
        count_4_walls = 0
        for row in m1._cells: 
            for cell in row:
                if cell.has_top_wall and cell.has_bottom_wall and cell.has_left_wall and cell.has_right_wall:
                    count_4_walls += 1
        self.assertEqual(count_4_walls, 0)

    def test_reset_cells_visited(self):
        num_columns = 30
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_columns, 10)
        for row in m1._cells:
            for cell in row:
                self.assertEqual(cell.visited, False)

    def test_solve(self):
        num_columns = 30
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_columns, 10)
        self.assertEqual(m1._solve(), True)

if __name__ == "__main__":
    unittest.main()