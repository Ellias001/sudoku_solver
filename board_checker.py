from math import sqrt

class Checker:

    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]

    def check_unsolved_board(self, board, num, pos: list):
        self.board = board
        if self.check_unsolved_row(num, pos):
            return 0
        if self.check_unsolved_col(num, pos):
            return 0
        if self.check_unsolved_sqr(num, pos):
            return 0
        return 1

    def check_unsolved_col(self, num, pos: list):
        length = len(self.board)
        j = pos[1]
        for i in range(length):
            if self.board[i][j] == num:
                return 1
        return 0

    def check_unsolved_row(self, num, pos: list):
        length = len(self.board)
        j = pos[0]
        for i in range(length):
            if self.board[j][i] == num:
                return 1
        return 0

    def check_unsolved_sqr(self, num, pos: list):
        length = int(sqrt(len(self.board)))
        sqr_row = int(pos[0] / length)
        sqr_col = int(pos[1] / length)
        for i in range(length):
            i += sqr_row * length
            for j in range(length):
                j += sqr_col * length
                if self.board[i][j] == num:
                    return 1
        return 0
