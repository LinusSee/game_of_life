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


    def test_game_returns_the_correct_board_after_running_an_iteration(self):
        board = [
            [ True, True, False ],
            [ False, True, True ],
            [ False, True, False ]
        ]

        actual = GameOfLife(board).run().board().board
        expected = GameBoard(board).next_state().board

        self.assertEqual(actual, expected)

    def test_game_returns_the_correct_board_after_running_for_10_iterations(self):
        board = [
            [ True, True, False ],
            [ False, True, True ],
            [ False, True, False ]
        ]
        iterations = 10

        actual = GameOfLife(board).run_for(iterations=iterations).board().board
        game_board = GameBoard(board)
        for iteration in range(iterations):
            game_board = game_board.next_state()
        expected = game_board.board


        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
