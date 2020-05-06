import math

class Checker:
    """A class to check sudoku board validity.

    Attributes:
        board: Two dimensional list of sudoku board.
    """

    def __init__(self, size = 9):
        """Initializes empty board.

        Args:
            size: number of columns and rows in board.
        """
        self.board = [[0 for i in range(size)] for j in range(size)]

    def check_unsolved_board(self, board, num, pos: list):
        """Checks if board stays valid as new number is added.

        Calls check_unsolved_row, check_unsolved_col and check_unsolved_sqr
        functions and if one of them returns False, returns False, in other case
        returns True.

        Args:
            board: valid sudoku board to what number is added.
            num: number to be added.
            pos: position where this number is added.

        Returns:
            False: if the board becomes invalid.
            True: if the board stays valid.
        """
        self.board = board
        if not self.check_unsolved_row(num, pos[0]):
            return False
        if not self.check_unsolved_col(num, pos[1]):
            return False
        if not self.check_unsolved_sqr(num, pos):
            return False
        return True

    def check_unsolved_col(self, num, col):
        """Checks if sudoku remains valid after adding a number to a particular
           column.

        Traverses particular column in sudoku board and checks if certain number
        appears in that column.

        Args:
            num: number to be added.
            col: column number that is checked.

        Returns:
            False: if board becomes invalid.
            True: if board stays valid.
        """
        length = len(self.board)
        for i in range(length):
            if self.board[i][col] == num:
                return False
        return True

    def check_unsolved_row(self, num, row):
        """Checks if sudoku remains valid after adding a number to a particular
           row.

        Traverses particular row in sudoku board and checks if certain number
        appears in that row.

        Args:
            num: number to be added.
            row: row number that is checked.

        Returns:
            False: if board becomes invalid.
            True: if board stays valid.
        """
        length = len(self.board)
        for i in range(length):
            if self.board[row][i] == num:
                return False
        return True

    def check_unsolved_sqr(self, num, pos: list):
        """Checks if sudoku remains valid after adding a number to a particular
           position.

        Finds square to be checked and goes through sudoku square and checks
        if certain number appears in that square.

        Args:
            num: number to be added.
            pos: list of two integers that defines position where number is addedd.

        Returns:
            False: if board becomes invalid.
            True: if board stays valid.
        """
        length = int(math.sqrt(len(self.board)))
        sqr_row = int(pos[0] / length)
        sqr_col = int(pos[1] / length)
        for i in range(length):
            i += sqr_row * length
            for j in range(length):
                j += sqr_col * length
                if self.board[i][j] == num:
                    return False
        return True


    def check_solved_board(self, board):
        """Checks if solved board is valid.

        Calls check_solved_row, check_solved_col and check_solved_sqr
        functions and if one of them returns False, returns False, in other case
        returns True.

        Args:
            board: valid sudoku board to what number is added.

        Returns:
            False: if the board is invalid.
            True: if the board is valid.
        """
        self.board = board
        if self.check_solved_rows():
            return False
        if self.check_solved_cols():
            return False
        if self.check_solved_sqrs():
            return False
        return True


    def check_solved_rows(self):
        """Checks if all rows in sudoku table are valid.

        Traverses whole sudoku board row by row and checks if numbers repeat.

        Returns:
            False: if a number repeats in a row.
            True: if a number repeats in a row.
        """
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
                return False

        return True

    def check_solved_cols(self):
        """Checks if all columns in sudoku table are valid.

        Traverses whole sudoku board column by columb and checks if
        numbers repeat.

        Returns:
            False: if a number repeats in a column.
            True: if a number repeats in a column.
        """
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
        """Checks if all squares in sudoku table are valid.

        Traverses whole sudoku board square by square and checks if
        numbers repeat.

        Returns:
            False: if a number repeats in a square.
            True: if a number repeats in a square.
        """
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
                return False
        return True

    def is_all_zeroes(self, lst):
        """Checks if list has non-zero numbers.

        Args:
            lst: list to be checked.

        Returns:
            True: if all numbers are 0
            False: if list has at least one non-zero number
        """
        for i in self.board:
            if i != 0:
                return False
        return True
