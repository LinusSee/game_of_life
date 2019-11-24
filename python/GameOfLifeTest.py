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

    def test_the_board_extends_upwards_if_a_cell_is_brought_to_life_on_its_top(self):
        board = [
            [ True, True, True ],
            [ True, False, False ],
            [ False, False, False ]
        ]

        actual = GameOfLife(board).board().next_state().board
        expected = [
            [ False, True, False ],
            [ True, True, False ],
            [ True, False, False ],
            [ False, False, False]
        ]

        self.assertEqual(actual, expected)


    def test_the_board_extends_leftwards_if_a_cell_is_brought_to_life_on_its_left(self):
        board = [
            [ True, True, False ],
            [ True, False, False ],
            [ True, False, False ]
        ]

        actual = GameOfLife(board).board().next_state().board
        expected = [
            [ False, True, True, False ],
            [ True, True, False, False ],
            [ False, False, False, False ]
        ]

        self.assertEqual(actual, expected)


    def test_the_board_extends_rightwards_if_a_cell_is_brought_to_life_on_its_right(self):
        board = [
            [ True, False, True ],
            [ False, True, True ],
            [ True, False, True ]
        ]

        actual = GameOfLife(board).board().next_state().board
        expected = [
            [ False, False, True, False ],
            [ True, False, True, True ],
            [ False, False, True, False ]
        ]

        self.assertEqual(actual, expected)


    def test_the_board_extends_downwards_if_a_cell_is_brought_to_life_on_its_down(self):
        board = [
            [ True, False, True ],
            [ False, True, False ],
            [ True, True, True ]
        ]

        actual = GameOfLife(board).board().next_state().board
        expected = [
            [ False, True, False ],
            [ False, False, False ],
            [ True, True, True ],
            [ False, True, False ]
        ]

        self.assertEqual(actual, expected)


    def test_the_board_extends_top_and_right_if_a_cell_is_brought_to_life_on_both_sides(self):
        board = [
            [ True, True, True ],
            [ False, False, True ],
            [ True, False, True ]
        ]

        actual = GameOfLife(board).board().next_state().board
        expected = [
            [ False, True, False, False ],
            [ False, True, True, False ],
            [ True, False, True, True ],
            [ False, True, False, False ]
        ]

        self.assertEqual(actual, expected)

    def test_the_board_extends_bot_and_right_if_a_cell_is_brought_to_life_on_both_sides(self):
        board = [
            [ True, False, True ],
            [ False, False, True ],
            [ True, True, True ]
        ]

        actual = GameOfLife(board).board().next_state().board
        expected = [
            [ False, True, False, False ],
            [ True, False, True, True ],
            [ False, True, True, False ],
            [ False, True, False, False ]
        ]

        self.assertEqual(actual, expected)

    def test_the_board_extends_bot_and_top_if_a_cell_is_brought_to_life_on_both_sides(self):
        board = [
            [ True, True, True ],
            [ False, True, False ],
            [ True, True, True ]
        ]

        actual = GameOfLife(board).board().next_state().board
        expected = [
            [ False, True, False],
            [ True, True, True ],
            [ False, False, False ],
            [ True, True, True ],
            [ False, True, False ]
        ]

        self.assertEqual(actual, expected)

    def test_the_board_extends_left_and_right_if_a_cell_is_brought_to_life_on_both_sides(self):
        board = [
            [ True, False, True ],
            [ True, True, True ],
            [ True, False, True ]
        ]

        actual = GameOfLife(board).board().next_state().board
        expected = [
            [ False, True, False, True, False ],
            [ True, True, False, True, True ],
            [ False, True, False, True, False ],
        ]

        self.assertEqual(actual, expected)

    def test_the_board_extends_left_and_top_if_a_cell_is_brought_to_life_on_both_sides(self):
        board = [
            [ True, True, True ],
            [ True, False, False ],
            [ True, False, True ]
        ]

        actual = GameOfLife(board).board().next_state().board
        expected = [
            [ False, False, True, False ],
            [ False, True, True, False ],
            [ True, True, False, True ],
            [ False, False, True, False ],
        ]

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
