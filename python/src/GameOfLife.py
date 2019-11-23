from src.Rules import PopulationRule
from src.Rules import SurvivalRule
from src.Rules import RevivalRule
from src.Rules import OverpopulationRule


class GameOfLife:
    def __init__(self, inital_board):
        self.__board = GameBoard(initial_board=inital_board)

    def board(self):
        return self.__board


class GameBoard:
    def __init__(self, initial_board):
        self.board = initial_board

    def alive_neighbours(self, x_pos, y_pos):
        start_x = max(0, x_pos - 1)
        start_y = max(0, y_pos - 1)
        end_x = min(x_pos + 1, len(self.board[0]) - 1)
        end_y = min(y_pos + 1, len(self.board) - 1)

        count = 0
        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                if self.board[y][x] == True:
                    count += 1
        if self.board[y_pos][x_pos] == True:
            count -= 1

        return count

    def next_state(self):
        next_board = []
        for y in range(len(self.board)):
            next_board.append([])
            for x in range(len(self.board[0])):
                alive_neighbours = self.alive_neighbours(x, y)
                cell_status = self.board[y][x]
                if PopulationRule(cell_status, alive_neighbours).applies():
                    next_board[y].append(False)
                elif SurvivalRule(cell_status, alive_neighbours).applies():
                    next_board[y].append(True)
                elif RevivalRule(cell_status, alive_neighbours).applies():
                    next_board[y].append(True)
                elif OverpopulationRule(cell_status, alive_neighbours).applies():
                    next_board[y].append(False)
                else:
                    next_board[y].append(False)
                    #assert 1 == 2, "This case should not be able to occur (Cell status: {}, Alive neighbours: {})".format(cell_status, alive_neighbours)
        return GameBoard(next_board)
