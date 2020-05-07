import numpy as np
import board_checker as bc
import random

class SudokuGenerator(bc.BoardChecker):
    def __init__(self, board_size = 9):
        if board_size % 3 != 0:
            raise ValueError
        board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.board = np.array(board)
        self.board_size = board_size

    def generate(self):
        self.__generate_first_line()
        
        for i in range(1, self.board_size):
            if i % 3 == 0:
                self.__shift_line(i, 1)
            else:
                self.__shift_line(i, 3)

        self.__mix()

    def __generate_first_line(self):
        nums = range(1, self.board_size + 1)
        line = random.sample(nums, self.board_size)
        self.board[0] = np.array(line)

    def __shift_line(self, pos, shiftVal):
        for i in range(self.board_size):
            j = (shiftVal + i) % self.board_size
            self.board[pos][i] = self.board[pos - 1][j]

    def __mix(self, swap_times = 15):
        mix_functions = ["__transpose()",
                         "__swap_rows()",
                         "__swap_cols()",
                         "__swap_sqr_rows()",
                         "__swap_sqr_cols()"]
        list_len = len(mix_functions)

        while swap_times != 0:
            swap_times -= 1
            id_func = random.randrange(0, list_len)
            getattr(self, mix_functions[id_func])

    def __transpose(self):
        self.board = self.board.T

    def __swap_rows(self):
        pos = self.__find_random_position()
        self.board[pos] = self.board[reversed(pos)]

    def __swap_cols(self):
        pos = self.__find_random_position()
        self.board[:,pos] = self.board[:,reversed(pos)]
    
    def __swap_sqr_rows(self):
        pos = self.__find_random_position()
        pos %= 3

        for i in range(int(self.board_size / 3)):
            self.board[pos + i] = self.board[reversed(pos + i)]

    def __swap_sqr_cols(self):
        pos = self.__find_random_position()
        pos %= 3

        for i in range(int(self.board_size / 3)):
            self.board[:,pos + i] = self.board[:,reversed(pos + i)]

    def __find_random_position(self):
        right_border = int(self.board_size / 3)
        sqr = random.randrange(0, right_border, 1)
        i = random.randrange(0, right_border, 1)
        j = random.randrange(0, right_border, 1)

        pos1 = sqr * 3 + i
        pos2 = sqr * 3 + j
        return np.array([pos1, pos2], dtype='int8')

if __name__ == '__main__':
    bg = SudokuGenerator()
    bg.generate()
    bg.print_board()