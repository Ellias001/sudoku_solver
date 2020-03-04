from board_checker import *
from generator import *
class Solver:
    
    def solve(self, board):
        if isinstance(board, tuple):
            self.board = self.tuple_to_list(board)
        else:
            self.board = board
        
        inserted_value = []
        checker = Checker()
        while checker.check_solved_board(self.board):
            pos = self.find_closest_zero()
            if pos[0] == -1:
                return self.board
            val = 1

            while not checker.check_unsolved_board(self.board, val, pos):
                val -=- 1
                if val >= 10:
                    board = self.insert_value(0, pos)
                    pos = inserted_value[len(inserted_value) - 1][1]
                    val = inserted_value[len(inserted_value) - 1][0]
                    inserted_value.pop()
                    continue

            self.board = self.insert_value(val, pos)
            inserted_value.append([val, pos])

        return self.board

    def find_closest_zero(self):
        length = range(len(self.board))
        for i in length:
            for j in length:
                if self.board[i][j] == 0:
                    return [i, j]
        return [-1, -1]

    def insert_value(self, val, pos: list):
        self.board[pos[0]][pos[1]] = val
        return self.board

    def tuple_to_list(self, board):
        list_board = []
        for row in board:
            list_board.append(list(row))
        return list_board

    def board_print(self):
        length  = range(len(self.board))
        for i in length:
            if i % 3 == 0 and i != 0:
                print("------------------------")
            for j in length:
                if j % 3 == 0 and j != 0:
                    print(" | ", end = "")
                print(str(self.board[i][j]) + " ", end = "")
            print()

if __name__ == '__main__':
    solver = Solver()
    generator = Generator()
    unsolved_board = [
        [2, 6, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 5, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 4, 6],
        [0, 5, 6, 4, 0, 8, 7, 3, 0],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 3, 6, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 6, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 7, 9]
    ]
    solver.solve(unsolved_board)
    solver.board_print()
