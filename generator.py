from board_checker import *
from math import sqrt
import solver
import random
import time

class Generator:
    # at difficulty = 24 it becomes very slow
    def __init__(self, difficulty = 30, board_size = 3):
        self.difficulty = difficulty
        self.board_size = board_size ** 2
        self.solver = solver.Solver()

    def generate_solved_board(self):
        self.board = [[0 for i in range(self.board_size)] for j in range(self.board_size)]
        self.init_first_line()

        for i in range(1, self.board_size):
            if i % 3 == 0:
                self.shift(i - 1, 1)
            else:
                self.shift(i - 1, 3)
        
        self.mix_board()

    def init_first_line(self):
        self.board[0] = random.sample(range(1, 10), self.board_size)

    def shift(self, pos, shiftVal):
        for i in range(len(self.board[pos])):
            j = (i + shiftVal) % self.board_size
            self.board[pos + 1][i] = self.board[pos][j]

    def mix_board(self, swap_times = 15):
        mix_functions = ["self.swap_rows()",
                         "self.swap_sqr_rows()",
                         "self.swap_cols()",
                         "self.swap_sqr_cols()"]
        
        for i in range(swap_times):
            id_func = random.randrange(0, len(mix_functions))
            eval(mix_functions[id_func])


    def swap_rows(self):
        right_border = int(self.board_size / 3)
        sqr = random.randrange(0, right_border, 1)
        row1 = random.randrange(0, right_border, 1)
        row2 = random.randrange(0, right_border, 1)

        pos1 = sqr * 3 + row1
        pos2 = sqr * 3 + row2
        self.board[pos1], self.board[pos2] = \
                         self.board[pos2], self.board[pos1]

    def swap_sqr_rows(self):
        right_border = int(sqrt(self.board_size))
        sqr = random.randrange(0, right_border, 1)
        row1 = sqr * 3
        row2 = sqr * 3

        for i in range(int(sqrt(self.board_size))):
            self.board[row1], self.board[row2] = \
                self.board[row2], self.board[row1]
            row1 += 1
            row2 += 1

    def swap_cols(self):
        right_border = int(sqrt(self.board_size))
        sqr = random.randrange(0, right_border, 1)
        col1 = 3 * sqr + random.randrange(0, right_border, 1)
        col2 = 3 * sqr + random.randrange(0, right_border, 1)

        for i in range(self.board_size):
            self.board[i][col1], self.board[i][col2] = \
                self.board[i][col2], self.board[i][col1]

    def swap_sqr_cols(self):
        right_border = int(sqrt(self.board_size))
        sqr = random.randrange(0, right_border, 1)
        col1 = 3 * sqr
        col2 = 3 * sqr

        for i in range(self.board_size):
            for j in range(3):
                self.board[j][col1], self.board[j][col2] = \
                    self.board[j][col2], self.board[j][col1]

    def generate_unsolved_board(self):
        start = time.time()
        self.solution = [[0 for i in range(self.board_size)] \
                               for j in range(self.board_size)]
        it = 0
        current_difficulty = self.board_size ** 2

        while current_difficulty > self.difficulty:
            i = random.randrange(0, self.board_size, 1)
            j = random.randrange(0, self.board_size, 1)

            if self.solution[i][j] == 0:
                self.solution[i][j] = self.board[i][j]
                self.board[i][j] = 0

                current_difficulty -= 1

                if not self.is_solvable():
                    self.board[i][j] = self.solution[i][j]
                    self.solution[i][j] = 0
                    current_difficulty += 1

            end = time.time()

            #if (end - start) > 7:
             #   print("Something went wrong. Making new board.", end - start, sep = "\t")
              #  self.generate_solved_board()
               # self.generate_unsolved_board()
                #return

    def is_solvable(self):
        full_board = self.solver.solve(self.list_to_tuple()) # it helps to keep original board unchanged in solve method
        
        for i in range(self.board_size):
            for j in range(self.board_size):
                if full_board[i][j] != self.board[i][j] and \
                   full_board[i][j] != self.solution[i][j]:
                    return False

        return True

    def list_to_tuple(self):
        tuple_board = []
        for row in self.board:
            tuple_board.append(tuple(row))
        return tuple(tuple_board)
    
    def print_board(self):
        length  = range(len(self.board))
        for i in length:
            if i % 3 == 0 and i != 0:
                print("------------------------")
            for j in length:
                if j % 3 == 0 and j != 0:
                    print(" | ", end = "")
                print(str(self.board[i][j]) + " ", end = "")
            print()

    def get_board(self):
        return self.board

    def get_solution(self):
        return self.solution

if __name__ == '__main__':
    start = time.time()
    generator = Generator()
    checker = Checker()
    generator.generate_solved_board()
    generator.generate_unsolved_board()
    end = time.time()
    print(end - start)
