import numpy as np
import math

def print_board(board):
    """Prints Sudoku Board.

    Represents sudoku board in a format:
        2 1 6  | 4 9 7  | 3 5 8
        3 5 8  | 2 1 6  | 4 9 7
        4 9 7  | 3 5 8  | 2 1 6
        ------------------------
        6 4 9  | 7 3 5  | 8 2 1
        8 2 1  | 6 4 9  | 7 3 5
        7 3 5  | 8 2 1  | 6 4 9
        ------------------------
        9 7 3  | 5 8 2  | 1 6 4
        5 8 2  | 1 6 4  | 9 7 3
        1 6 4  | 9 7 3  | 5 8 2

    Args:
        board: sudoku board to be printed.
    """
    board_size = len(board)
    for i in range(board_size):
        if i % 3 == 0 and i != 0:
           print("------------------------")
        for j in range(board_size):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            print(str(board[i][j]), end = " ")
        print()

class BoardChecker:
    """Checks sudoku board for validity.

    Has two main purposes: to check solved board and 
    check if number may be added to a certain position.

    Attributes:
        board: sudoku board that is passed.
        board_size: length and width of sudoku board.
        arr: sequence of numbers [1, board_size)
    """
    def __init__(self, board_size = 9):
        """Initializes attributes.

        Creates board, board_size and arr attributes and
        assigns null values to them.

        Args:
            board_size: length and width of sudoku board.
                default value: 9
        """
        board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.board = np.array(board, dtype='int8')
        self.board_size = board_size
        self.arr = np.array([i+1 for i in range(self.board_size)], dtype='int8')

    def is_valid(self, board):
        """Checks if solved sudoku is valid.

        Calls __is_valid_rows(), __is_valid_cols() and __is_valid_sqrs()
        methods to check rows, columns and sudoku squares.

        Attr:
            board: solved sudoku board to be checked.
        
        Returns:
            True: if board is valid.
            False: if board is invalid.
        """
        self.board = board
        if not self.__is_valid_rows():
            return False
        if not self.__is_valid_cols():
            return False
        if not self.__is_valid_sqrs():
            return False
        return True

    def __is_valid_rows(self):
        """Checks every row in sudoku board for validity.

        Checks if a row has no duplicates or invalid (out of border) values.

        Returns:
            True: if all rows are valid.
            False: if at least one row is invalid.
        """
        for row in self.board:
            if not self.__is_true(np.sort(row) == self.arr):
                return False
        return True
    
    def __is_valid_cols(self):
        """Checks every column in sudoku board for validity.

        Checks if a column has no duplicates or invalid (out of border) values.

        Returns:
            True: if all columns are valid.
            False: if at least one column is invalid.
        """
        for col in self.board.T:
            if not self.__is_true(np.sort(col) == self.arr):
                return False
        return True

    def __is_valid_sqrs(self):
        """Checks every square in sudoku board for validity.

        Checks if a square has no duplicates or invalid (out of border) values.

        Returns:
            True: if all squares are valid.
            False: if at least one square is invalid.
        """
        num_of_sqrs = int(math.sqrt(self.board_size))
        for i in range(num_of_sqrs):
            for j in range(num_of_sqrs):
                sqr = self.__find_sqr(i, j)
                if not self.__is_true(np.sort(sqr) == self.arr):
                    return False
        return True

    def __find_sqr(self, a, b):
        """Returns an array made of particular square.

        Takes arguments that define square index and returns an array of
        all numbers in this square.

        Args:
            a: row number of square. (0, 1, 2 in 9x9 sudoku).
            b: column number of square. (0, 1, 2 in 9x9 sudoku).
        
        Returns:
            arr: array of numbers in defined square.
        """
        arr = np.array([0 for i in range(self.board_size)])
        num_of_sqrs = int(math.sqrt(self.board_size))
        k = 0
        for i in range(num_of_sqrs):
            for j in range(num_of_sqrs):
                arr[k] = self.board[a*3 + i][b*3 + j]
                k += 1
        return arr

    def __is_true(self, arr):
        """Checks if all values are true.

        Takes an array of boolean values and checks if all values are True.

        Args:
            arr: array of boolean values.

        Returns:
            True: if all values in an array are True.
            False: if at least on values in an array are False.
        """
        for el in arr:
            if el == False:
                return False
        return True

if __name__ == "__main__":
    bc = BoardChecker()
