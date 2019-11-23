class PopulationRule:
    def __init__(self, cell_status, alive_neighbours):
        self.cell_status = cell_status
        self.alive_neighbours = alive_neighbours

    def applies(self):
        if self.cell_status == True and self.alive_neighbours == 0:
            return True
        return False
