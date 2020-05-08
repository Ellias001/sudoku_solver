import numpy as np
import board_checker as bc
import random

class SudokuGenerator:
    def __init__(self, board_size = 9):
        if board_size % 3 != 0:
            raise ValueError
        solved = [[0 for i in range(board_size)] for j in range(board_size)]
        self.solved = np.array(solved, dtype="int8")
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
        self.solved[0] = np.array(line)

    def __shift_line(self, pos, shiftVal):
        for i in range(self.board_size):
            j = (shiftVal + i) % self.board_size
            self.solved[pos][i] = self.solved[pos - 1][j]

    def __mix(self, swap_times = 15):
        while swap_times != 0:
            id_func = np.random.random_integers(0, 5)
            if id_func == 1:
                self.__transpose()
            elif id_func == 2:
                self.__swap_rows()
            elif id_func == 3:
                self.__swap_cols()
            elif id_func == 4:
                self.__swap_sqr_rows()
            elif id_func == 5:
                self.__swap_sqr_cols()
            swap_times -= 1

    def __transpose(self):
        self.solved = self.solved.T

    def __swap_rows(self):
        pos = self.__find_random_position()
        self.solved[[pos[0], pos[1]]] = self.solved[[pos[1], pos[0]]]

    def __swap_cols(self):
        pos = self.__find_random_position()
        self.solved[:,[pos[0], pos[1]]] = self.solved[:,[pos[1], pos[0]]]
    
    def __swap_sqr_rows(self):
        pos = self.__find_random_position()
        pos %= 3; pos *= 3

        for _ in range(int(self.board_size / 3)):
            self.solved[[pos[0], pos[1]]] = self.solved[[pos[1], pos[0]]]
            pos += 1

    def __swap_sqr_cols(self):
        pos = self.__find_random_position()
        pos %= 3; pos *= 3

        for _ in range(int(self.board_size / 3)):
            self.solved[:,[pos[0], pos[1]]] = self.solved[:,[pos[1], pos[0]]]
            pos += 1

    def __find_random_position(self):
        right_border = int(self.board_size / 3)
        sqr = np.random.randint(0, right_border)
        i = np.random.randint(0, right_border)
        j = np.random.randint(0, right_border)

        pos1 = sqr * 3 + i
        pos2 = sqr * 3 + j
        return np.array([pos1, pos2], dtype="int8")
    
    def get_solved_board(self):
        return self.solved

if __name__ == '__main__':
    bg = SudokuGenerator()
    checker = bc.BoardChecker()
    
    bg.generate()
    board = bg.get_solved_board()

    bc.print_board(board, len(board))
    print(checker.is_valid(board))
