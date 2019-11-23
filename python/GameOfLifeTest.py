import unittest

from src.Rules import PopulationRule


class GameOfLifeTest(unittest.TestCase):
    def test_an_alive_cell_with_0_neighbours_dies(self):
        alive_neighbours = 0
        cell_state = True

        actual = PopulationRule(cell_state, alive_neighbours).applies()

        self.assertTrue(actual)

if __name__ == "__main__":
    unittest.main()
