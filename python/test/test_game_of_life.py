import unittest

from src.GameOfLife import GameBoard
from src.GameOfLife import GameOfLife


class GameOfLifeTest(unittest.TestCase):
    def test_game_returns_the_correct_board_after_creation(self):
        board = [
            [ True, True, False ],
            [ False, True, True ],
            [ False, True, False ]
        ]

        actual = GameOfLife(board).board().board
        expected = GameBoard(board).board

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
