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
