class PopulationRule:
    def __init__(self, cell_status, alive_neighbours):
        self.cell_status = cell_status
        self.alive_neighbours = alive_neighbours

    def applies(self):
        if self.cell_status == True:
            if self.alive_neighbours == 0 or self.alive_neighbours == 1:
                return True
        return False


class SurvivalRule:
    def __init__(self, cell_status, alive_neighbours):
        self.cell_status = cell_status
        self.alive_neighbours = alive_neighbours

    def applies(self):
        if self.cell_status == True and self.alive_neighbours == 2:
            return True
        if self.cell_status == True and self.alive_neighbours == 3:
            return True
        return False
