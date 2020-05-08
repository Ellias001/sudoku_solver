import numpy as np
import random

def print_board(board, board_size):
    for i in range(board_size):
        if i % 3 == 0 and i != 0:
           print("------------------------")
        for j in range(board_size):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            print(str(board[i][j]), end = " ")
        print()

class BoardChecker:
    def __init__(self, board_size = 9):
        board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.board = np.array(board, dtype='int8')
        self.board_size = board_size
        self.arr = np.array([i+1 for i in range(self.board_size)], dtype='int8')

    def is_valid(self, board):
        self.board = board
        if not self.__is_valid_rows():
            print("ROWS")
            return False
        if not self.__is_valid_cols():
            print("COLS")
            return False
        if not self.__is_valid_sqrs():
            print("SQRS")
            return False
        return True

    def __is_valid_rows(self):
        for row in self.board:
            if not self.__is_true(np.sort(row) == self.arr):
                return False
        return True
    
    def __is_valid_cols(self):
        for col in self.board.T:
            if not self.__is_true(np.sort(col) == self.arr):
                return False
        return True

    def __is_valid_sqrs(self):
        num_of_sqrs = int(self.board_size / 3)
        for i in range(num_of_sqrs):
            for j in range(num_of_sqrs):
                sqr = self.__find_sqr(i, j)
                if not self.__is_true(np.sort(sqr) == self.arr):
                    return False
        return True

    def __find_sqr(self, a, b):
        arr = np.array([0 for i in range(self.board_size)])
        num_of_sqrs = int(self.board_size / 3)
        k = 0
        for i in range(num_of_sqrs):
            for j in range(num_of_sqrs):
                arr[k] = self.board[a*3 + i][b*3 + j]
                k += 1
        return arr

    def __is_true(self, arr):
        for el in arr:
            if el == False:
                return False
        return True

if __name__ == "__main__":
    bc = BoardChecker()
