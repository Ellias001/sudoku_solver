class Checker:

    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]
    
    def check_solved_board(self, board):
        self.board = board
        if self.check_solved_rows():
            return 0
        if self.check_solved_cols():
            return 0
        if self.check_solved_sqrs():
            return 0
        return 1

    def check_unsolved_board(self, board, num, pos: list):
        self.board = board
        if self.check_unsolved_row(num, pos):
            return 0
        if self.check_unsolved_col(num, pos):
            return 0
        if self.check_unsolved_sqr(num, pos):
            return 0
        return 1

    def check_solved_rows(self):
        length = range(9)
        lst = [i + 1 for i in length]

        for i in length:
            for j in length:
                for k in length:
                    if lst[k] == self.board[i][j]:
                        lst[k] = 0

            if self.is_all_zeroes(lst):
                lst = [i + 1 for i in length]
            else:
                return 0

        return 1

    def check_solved_cols(self):
        length = range(9)
        lst = [i + 1 for i in length]

        for i in length:
            for j in length:
                for k in length:
                    if lst[k] == self.board[j][i]:
                        lst[k] = 0

            if self.is_all_zeroes(lst):
                lst = [i + 1 for i in length]
            else:
                return 0
        return 1

    def check_solved_sqrs(self):
        max_length = range(9)
        sqr_length = range(3)
        lst = [i + 1 for i in max_length]

        for num_of_sqrs in max_length:
            for i in sqr_length:
                for j in sqr_length:
                    for k in max_length:
                        it1 = i + (num_of_sqrs % 3)*3
                        it2 = j + (num_of_sqrs % 3)*3
                        if lst[k] == self.board[it1][it2]:
                            lst[k] = 0

            if self.is_all_zeroes(lst):
                lst = [i + 1 for i in max_length]
            else:
                return 0
        return 1

    def is_all_zeroes(self, lst):
        for i in self.board:
            if i != 0:
                return 0
        return 1

    def check_unsolved_col(self, num, pos: list):
        length = range(len(self.board))
        j = pos[1]
        for i in length:
            if self.board[i][j] == num:
                return 1
        return 0

    def check_unsolved_row(self, num, pos: list):
        length = range(len(self.board))
        j = pos[0]
        for i in length:
            if self.board[j][i] == num:
                return 1
        return 0

    def check_unsolved_sqr(self, num, pos: list):
        length = range(3)
        sqr_row = int(pos[0] / 3)
        sqr_col = int(pos[1] / 3)
        for i in length:
            i += sqr_row * 3
            for j in length:
                j += sqr_col * 3
                if self.board[i][j] == num:
                    return 1
        return 0
