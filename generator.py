import numpy as np
import board_checker as bc
import math

class SudokuGenerator:
    """Designed to generate solved and unsolved sudoku problems.

    Attributes:
        solved: solved sudoku problem.
        board_size: length and width of sudoku board.
        sqr_size: length and width of sudoku squares.
    """
    def __init__(self, board_size = 9):
        """Initializes instance attributes.
        
        Args:
            board_size: length and width of sudoku board.
                default: 9.

        Raises:
            ValueError: if board_size is invalid (has no integer square root).
        """
        self.sqr_size = int(math.sqrt(board_size))
        if board_size % self.sqr_size != 0:
            raise ValueError
        solved = [[0 for i in range(board_size)] for j in range(board_size)]
        self.solved = np.array(solved, dtype="int8")
        self.board_size = board_size

    def generate(self):
        """Generates solved and unsolved sudoku.

        Creates solved sudoku problem and decomposes it to get unsolved problem.
        """
        self.__generate_first_line()
        
        for i in range(1, self.board_size):
            if i % self.sqr_size == 0:
                self.__shift_line(i, 1)
            else:
                self.__shift_line(i, 3)

        self.__mix()

    def __generate_first_line(self):
        """Generates first line.

        Creates and array of valid values ([1, board_size] with no duplicates)
        and assigns it to the first line.
        """
        nums = range(1, self.board_size + 1)
        line = np.random.choice(nums, size=self.board_size, replace=False)
        self.solved[0] = np.array(line)

    def __shift_line(self, pos, shiftVal):
        """Fills intended board line by shifting previous line.

        Moves all values of line #pos in board by shiftVal value.

        Args:
            pos: index of line that will be created.
            shiftVal: number by which values of previous line will be moved.
        """
        for i in range(self.board_size):
            j = (shiftVal + i) % self.board_size
            self.solved[pos][i] = self.solved[pos - 1][j]

    def __mix(self, swap_times = 15):
        """Mixes sudoku board by calling particular functions.

        Calls swap_rows, swap_sqr_rows, swap_cols, swap_sqr_cols methods to make board
        building algorithm less obvious for users.

        Args:
            swap_times: number of swaps that will be performed on sudoku board.
                Default value: 15
        """
        while swap_times != 0:
            id_func = np.random.random_integers(0, 4)
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
        """Transposes current board."""
        self.solved = self.solved.T

    def __swap_rows(self):
        """Swaps two random rows in the same square."""
        pos = self.__find_random_position()
        self.solved[[pos[0], pos[1]]] = self.solved[[pos[1], pos[0]]]

    def __swap_cols(self):
        """Swaps two random columns in the same square."""
        pos = self.__find_random_position()
        self.solved[:,[pos[0], pos[1]]] = self.solved[:,[pos[1], pos[0]]]
    
    def __swap_sqr_rows(self):
        """Swaps two random square rows."""
        pos = self.__find_random_position()
        pos %= self.sqr_size; pos *= self.sqr_size

        for _ in range(self.sqr_size):
            self.solved[[pos[0], pos[1]]] = self.solved[[pos[1], pos[0]]]
            pos += 1

    def __swap_sqr_cols(self):
        """Swaps two random square columns."""
        pos = self.__find_random_position()
        pos %= self.sqr_size; pos *= self.sqr_size

        for _ in range(self.sqr_size):
            self.solved[:,[pos[0], pos[1]]] = self.solved[:,[pos[1], pos[0]]]
            pos += 1

    def __find_random_position(self):
        """Returns random position on the board.

        Uses np.random to choose the square row/column and find
        row/column in that square.

        Retrurns:
            pos: numpy array of coordinates of that position. 
        """
        sqr = np.random.randint(0, self.sqr_size)
        i = np.random.randint(0, self.sqr_size)
        j = np.random.randint(0, self.sqr_size)

        pos1 = sqr * self.sqr_size + i
        pos2 = sqr * self.sqr_size + j
        pos = np.array([pos1, pos2], dtype="int8")
        return pos
    
    def get_solved_board(self):
        """Getter method for solved sudoku.

        Returns:
            solved: solved attribute of an instance
        """
        return self.solved

if __name__ == '__main__':
    bg = SudokuGenerator()
    checker = bc.BoardChecker()
    
    bg.generate()
    board = bg.get_solved_board()

    bc.print_board(board)
    print(checker.is_valid(board))
