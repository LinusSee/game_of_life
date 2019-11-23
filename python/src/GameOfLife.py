class GameOfLife:
    def __init__(self, inital_board):
        self.__board = GameBoard(initial_board=inital_board)

    def board(self):
        return self.__board

class GameBoard:
    def __init__(self, initial_board):
        self.board = initial_board

    def alive_neighbours(self, x, y):
        return 2
