import unittest

from src.Rules import PopulationRule
from src.Rules import SurvivalRule
from src.Rules import RevivalRule
from src.Rules import OverpopulationRule


class GameOfLifeTest(unittest.TestCase):
    def test_an_alive_cell_with_0_neighbours_dies(self):
        cell_status = True
        alive_neighbours = 0

        actual = PopulationRule(cell_status, alive_neighbours).applies()

        self.assertTrue(actual)

    def test_an_alive_cell_with_1_neighbour_dies(self):
        cell_status = True
        alive_neighbours = 1

        actual = PopulationRule(cell_status, alive_neighbours).applies()

        self.assertTrue(actual)


    def test_an_alive_cell_with_2_neighbours_stays_alive(self):
        cell_status = True
        alive_neighbours = 2

        actual = SurvivalRule(cell_status, alive_neighbours).applies()

        self.assertTrue(actual)

    def test_an_alive_cell_with_3_neighbours_stays_alive(self):
        cell_status = True
        alive_neighbours = 3

        actual = SurvivalRule(cell_status, alive_neighbours).applies()

        self.assertTrue(actual)


    def test_a_dead_cell_with_exactely_3_neighbours_becomes_alive(self):
        cell_status = False
        alive_neighbours = 3

        actual = RevivalRule(cell_status, alive_neighbours).applies()

        self.assertTrue(actual)


    def test_an_alive_cell_with_4_neighbours_dies(self):
        cell_status = True
        alive_neighbours = 4

        actual = OverpopulationRule(cell_status, alive_neighbours).applies()

        self.assertTrue(actual)

if __name__ == "__main__":
    unittest.main()
