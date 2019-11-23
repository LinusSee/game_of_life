import unittest

from src.GameOfLife import GameOfLife


class GameOfLifeTest(unittest.TestCase):
    def test_the_board_correctly_counts_the_alive_neighbours_around_the_upper_left_cell(self):
        board = [
            [ True, True, False, False ],
            [ False, True, False, True ],
            [ True, True, True, True ],
            [ True, False, False, False ]
        ]
        x_pos = 0
        y_pos = 0

        actual = GameOfLife(board).board().alive_neighbours(x_pos, y_pos)
        expected = 2

        self.assertEqual(actual, expected)

    def test_the_board_correctly_counts_the_alive_neighbours_around_the_bottom_right_cell(self):
        board = [
            [ True, True, False, False ],
            [ False, True, False, True ],
            [ True, True, True, False ],
            [ True, False, False, False ]
        ]
        x_pos = 3
        y_pos = 3

        actual = GameOfLife(board).board().alive_neighbours(x_pos, y_pos)
        expected = 1

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
