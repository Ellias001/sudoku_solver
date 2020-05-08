import numpy as np
import random

class BoardChecker:
    def __init__(self, board_size = 9):
        board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.board = np.array(board, dtype='int8')
        self.board_size = board_size
        self.arr = np.array([i+1 for i in range(self.board_size)], dtype='int8')

    def is_valid(self, board):
        self.board = board
        if not self.__is_valid_rows():
            return False
        if not self.__is_valid_cols():
            return False
        if not self.__is_valid_sqrs():
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
        pass

    def __is_true(self, arr):
        for el in arr:
            if el == False:
                return False
        return True

    def print_board(self):
        for i in range(self.board_size):
            if i % 3 == 0 and i != 0:
                print("------------------------")
            for j in range(self.board_size):
                if j % 3 == 0 and j != 0:
                    print(" | ", end = "")
                print(str(self.board[i][j]), end = " ")
            print()

if __name__ == "__main__":
    bc = BoardChecker()
    bc.print_board()
