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

        if start_x <= x_pos <= end_x and start_y <= y_pos <= end_y:
            if self.board[y_pos][x_pos] == True:
                count -= 1

        return count

    def next_state(self):
        next_board = self.__next_board_without_extending()

        top_changed, top = self.__top_extension()
        left_changed, left = self.__left_extension()
        right_changed, right = self.__right_extension()
        down_changed, down = self.__down_extension()

        if top_changed:
            next_board.insert(0, top)

        if left_changed:
            for y, status in enumerate(left):
                next_board[y].insert(0, status)

        if right_changed:
            right = [False] + right if top_changed else right

            for y, status in enumerate(right):
                next_board[y].insert(len(next_board[y]), status)

        if down_changed:
            next_board.insert(len(next_board), down)

        return GameBoard(next_board)

    def __next_board_without_extending(self):
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
        return next_board

    def __top_extension(self):
        top_changed = False
        top = []
        for x in range(0, len(self.board)):
            cell_status = False
            alive_neighbours = self.alive_neighbours(x, -1)
            if RevivalRule(cell_status, alive_neighbours).applies():
                top.append(True)
                top_changed = True
            else:
                top.append(False)

        return top_changed, top

    def __left_extension(self):
        left_changed = False
        left = []
        for y in range(0, len(self.board)):
            cell_status = False
            alive_neighbours = self.alive_neighbours(-1, y)
            if RevivalRule(cell_status, alive_neighbours).applies():
                left.append(True)
                left_changed = True
            else:
                left.append(False)

        return left_changed, left

    def __right_extension(self):
        right_changed = False
        right = []
        for y in range(0, len(self.board)):
            cell_status = False
            alive_neighbours = self.alive_neighbours(len(self.board[0]), y)
            if RevivalRule(cell_status, alive_neighbours).applies():
                right.append(True)
                right_changed = True
            else:
                right.append(False)

        return right_changed, right

    def __down_extension(self):
        down_changed = False
        down = []
        for x in range(0, len(self.board)):
            cell_status = False
            alive_neighbours = self.alive_neighbours(x, len(self.board))
            if RevivalRule(cell_status, alive_neighbours).applies():
                down.append(True)
                down_changed = True
            else:
                down.append(False)

        return down_changed, down
