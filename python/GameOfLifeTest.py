import unittest

from src.GameOfLife import GameOfLife

transition_examples = [
    ([
        [ True, True, False ],
        [ False, True, False ],
        [ False, False, True ],
    ],
    [
        [ True, True, False ],
        [ True, True, True ],
        [ False, False, False]
    ]),
    ([
        [ False, True, False],
        [ True, False, False],
        [ False, False, True],
    ],
    [
        [ False, False, False ],
        [ False, True, False ],
        [ False, False, False ],
    ]),
    ([
        [ True, False, False ],
        [ True, False, False ],
        [ False, True, True ],
    ],
    [
        [ False, False, False ],
        [ True, False, False ],
        [ False, True, False ],
    ]),
    ([
        [ True, True, False, True ],
        [ False, True, False, True ],
        [ True, True, True, False ],
        [ False, True, False, True]
    ],
    [
        [ True, True, False, False ],
        [ False, False, False, True ],
        [ True, False, False, True ],
        [ True, True, False, False ]
    ]),
    ([
        [ True, False, False, True ],
        [ False, True, False, False ],
        [ False, False, True, False ],
        [ False, False, False, True ]
    ],
    [
        [ False, False, False, False ],
        [ False, True, True, False ],
        [ False, False, True, False ],
        [ False, False, False, False ]
    ])
]

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

    def test_the_board_correctly_counts_the_alive_neighbours_around_a_cell_that_is_not_at_an_edge(self):
        board = [
            [ True, True, False, False ],
            [ False, True, False, True ],
            [ True, True, True, False ],
            [ True, False, False, False ]
        ]
        x_pos = 1
        y_pos = 1

        actual = GameOfLife(board).board().alive_neighbours(x_pos, y_pos)
        expected = 5

        self.assertEqual(actual, expected)

    def test_the_board_correctly_applies_all_rules_when_transitioning_between_states(self):
        for board, expected in transition_examples:
            actual = GameOfLife(board).board().next_state().board

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
