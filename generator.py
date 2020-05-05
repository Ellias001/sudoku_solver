import board_checker as bc
import math
import solver
import random
import time

class Generator:
    """Class that generates sudoku board.

    Class that intializes sudoku board with specified size and difficulty.
    Uses objects of Checker and Solver classes from board_checker and solver
    modules respectively.

    Attributes:
        board: incomplete sudoku board of intended size.
        solution: complete sudoku board.
        solver: object of Solver class, that is intended to solve sudoku problems.
        difficulty: number of non-zero numbers in incomplete sudoku.
        board_size: length and width of board.
    """

    def __init__(self, difficulty = 33, board_size = 9):
        """Constructor method.

        Initializes solver object, difficulty and board_size properties.

        Args:
            difficulty: number of non-zero numbers in incomplete sudoku.
                Default value: 33
            board_size: length and width of board.
                Default value: 9
        """
        self.difficulty = difficulty # at difficulty = 24 it becomes very slow
        self.board_size = board_size
        self.solver = solver.Solver()

    def generate_solved_board(self):
        """Method that creates solved sudoku board.

        Initializes empty board and calls init_first_line, shift and mix_board functions
        to generate complete solved sudoku board.
        """
        self.board = [[0 for i in range(self.board_size)] for j in range(self.board_size)]
        self.init_first_line()

        for i in range(1, self.board_size):
            if i % 3 == 0:
                self.shift(i - 1, 1)
            else:
                self.shift(i - 1, 3)
        
        self.mix_board()

    def init_first_line(self):
        """Initializes first line of sudoku board.

        Calls sample function from random module to create a line with non-repeated numbers
        in range from 1 to board_size + 1
        """
        self.board[0] = random.sample(range(1, self.board_size + 1), self.board_size)

    def shift(self, pos, shiftVal):
        """Fills intended board line by shifting previous line.

        Moves all values of line #pos in board by shiftVal value.

        Args:
            pos: index of line that will be created.
            shiftVal: number by which values of previous line will be moved.
        """
        for i in range(len(self.board[pos])):
            j = (i + shiftVal) % self.board_size
            self.board[pos + 1][i] = self.board[pos][j]

    def mix_board(self, swap_times = 15):
        """Mixes sudoku board by calling particular functions.

        Calls swap_rows, swap_sqr_rows, swap_cols, swap_sqr_cols methods to make board
        building algorithm less obvious for users.

        Args:
            swap_times: number of swaps that will be performed on sudoku board.
                Default value: 15
        """
        mix_functions = ["self.swap_rows()",
                         "self.swap_sqr_rows()",
                         "self.swap_cols()",
                         "self.swap_sqr_cols()"]
        
        for i in range(swap_times):
            id_func = random.randrange(0, len(mix_functions))
            eval(mix_functions[id_func])


    def swap_rows(self):
        """Swaps all values of two rows. 

        Generates random number to define square in which rows are selected and to define
        these rows. After what swaps them. In this case board stays valid.
        """
        right_border = int(self.board_size / 3)
        sqr = random.randrange(0, right_border, 1)
        row1 = random.randrange(0, right_border, 1)
        row2 = random.randrange(0, right_border, 1)

        pos1 = sqr * 3 + row1
        pos2 = sqr * 3 + row2
        self.board[pos1], self.board[pos2] = \
                         self.board[pos2], self.board[pos1]

    def swap_sqr_rows(self):
        """Swaps wide rows that consist of 3 board rows.

        Generates random number to define square rows and swap them.        
        """
        right_border = int(math.sqrt(self.board_size))
        sqr = random.randrange(0, right_border, 1)
        row1 = sqr * 3
        row2 = sqr * 3

        for i in range(int(math.sqrt(self.board_size))):
            self.board[row1], self.board[row2] = \
                self.board[row2], self.board[row1]
            row1 += 1
            row2 += 1

    def swap_cols(self):
        """Swaps all values of two columns. 

        Generates random number to define square in which columns are selected and to define
        these columns. After what swaps them. In this case board stays valid.
        """
        right_border = int(math.sqrt(self.board_size))
        sqr = random.randrange(0, right_border, 1)
        col1 = 3 * sqr + random.randrange(0, right_border, 1)
        col2 = 3 * sqr + random.randrange(0, right_border, 1)

        for i in range(self.board_size):
            self.board[i][col1], self.board[i][col2] = \
                self.board[i][col2], self.board[i][col1]

    def swap_sqr_cols(self):
        """Swaps wide columns that consist of 3 board columns.

        Generates random number to define square columns and swap them.        
        """
        right_border = int(math.sqrt(self.board_size))
        sqr = random.randrange(0, right_border, 1)
        col1 = 3 * sqr
        col2 = 3 * sqr

        for i in range(self.board_size):
            for j in range(3):
                self.board[j][col1], self.board[j][col2] = \
                    self.board[j][col2], self.board[j][col1]

    def generate_unsolved_board(self):
        """Method that creates unsolved sudoku board.

        Initializes empty board and fills it with numbers from solved sudoku
        while it stays solvable for solver object and until intended difficulty
        is reached.
        """
        try:
            self.board
        except AttributeError:
            self.generate_solved_board()
        
        self.solution = [[0 for i in range(self.board_size)] \
                               for j in range(self.board_size)]
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

    def is_solvable(self):
        """Checks if incomplete sudoku board is solvable.

        Solves sudokku problem using solver object and called solvable if
        it does not differ from original board.

        Returns:
            True: if board is solvable.
            False: if board is not solvable.
        """
        # it helps to keep original board unchanged in solve method
        full_board = self.solver.solve(self.list_to_tuple())
        
        for i in range(self.board_size):
            for j in range(self.board_size):
                if full_board[i][j] != self.board[i][j] and \
                   full_board[i][j] != self.solution[i][j]:
                    return False

        return True

    def list_to_tuple(self):
        """Converts list objects to tuple.

        Creates list object, that finally will contain tuples and converts
        every row of sudoku board from list to tuple objects. Afterwards
        converts this list to tuple.

        Returns:
            tuple_board: board attribute converted to tuple.
        """
        tuple_board = []
        for row in self.board:
            tuple_board.append(tuple(row))
        return tuple(tuple_board)
    
    def print_board(self):
        """Prints the board.

        Example:
            0 0 0  | 0 0 0  | 5 2 0 
            5 2 9  | 6 0 4  | 8 1 0 
            8 0 0  | 0 0 0  | 0 3 0 
            ------------------------
            3 0 0  | 0 4 0  | 0 7 0 
            0 7 8  | 3 0 5  | 0 0 6 
            1 0 6  | 0 0 0  | 0 0 5 
            ------------------------
            0 6 1  | 9 0 2  | 4 0 0 
            0 0 2  | 0 0 3  | 0 0 0 
            4 0 0  | 7 6 0  | 0 8 0 
        """
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
        """Getter method for board attribute.

        Returns:
            board: board attribute of the class.
        """
        return self.board

    def get_solution(self):
        """Getter method for solution attribute.

        Returns:
            solution: solution attribute of the class.
        """
        return self.solution

if __name__ == '__main__':
    start = time.time()
    generator = Generator()
    checker = bc.Checker()
    generator.generate_unsolved_board()
    end = time.time()
    generator.print_board()
    print("Spent time: %lf" % (end - start))
