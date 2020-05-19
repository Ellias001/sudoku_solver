import numpy as np
import solver as ss
import board_checker as bc
import math

class SudokuGenerator:
    """Designed to generate solved and unsolved sudoku problems.

    Attributes:
        solved: solved sudoku problem.
        unsolved: unsolved sudoku board.
        solver: SudokuSolver class instance from solver module.
                Dedicated to solve sudoku problems.
        board_size: length and width of sudoku board.
        sqr_size: length and width of sudoku squares.
        difficulty: represents how many non-zero numbers unsolved board should have.
    """
    def __init__(self, board_size = 9, difficulty = 33):
        """Initializes instance attributes.
        
        Args:
            difficulty: represents how many non-zero numbers unsolved board should have.
                default: 33.
            board_size: length and width of sudoku board.
                default: 9.

        Raises:
            ValueError: if board_size is invalid (has no integer square root).
        """
        self.sqr_size = int(math.sqrt(board_size))
        if board_size % self.sqr_size != 0:
            raise ValueError
        self.difficulty = difficulty
        self.solver = ss.SudokuSolver()
        self.solved = np.zeros((board_size, board_size), dtype="int8")
        self.board_size = board_size

    def generate(self):
        """Generates solved and unsolved sudoku.

        Creates solved sudoku problem and calls __generate_unsolved() method
        to create unsolved sudoku problem.
        """
        self.__generate_first_line()
        
        for i in range(1, self.board_size):
            if i % self.sqr_size == 0:
                self.__shift_line(i, 1)
            else:
                self.__shift_line(i, 3)

        self.__mix()
        self.__generate_unsolved()

    def get_solved(self):
        """Getter method for unsolved attribute.
        
        unsolved attribute represents unsolved sudoku board.

        Returns:
            unsolved.copy(): copy of unsolved board whith type np.arrray(dtype='int8').
        """
        return list(self.solved)

    def get_unsolved(self):
        """Getter method for unsolved attribute.
        
        solved attribute represents solved sudoku board.

        Returns:
            solved.copy(): copy of solved board whith type np.arrray(dtype='int8').
        """
        return list(self.unsolved)

    def __generate_unsolved(self):
        """Generates unsolved sudoku board.

        Removes random numbers from solved sudoku while it stays valid 
        until certain difficulty is reached.
        """
        self.unsolved = self.solved.copy()
        current_difficulty = self.board_size ** 2
        positions_list = self.__make_position_list()

        for i, j in positions_list:
            if self.__is_solvable():
                self.unsolved[i, j] = 0
                current_difficulty -= 1
            if current_difficulty == self.difficulty:
                break

    def __make_position_list(self):
        """Makes list of board positions.
        
        Creates a list of all possible board positions and shuffles it.

        Returns:
            res: shuffled list of all possible board positions.
        """
        res = list()
        for i in range(self.board_size):
            for j in range(self.board_size):
                res.append((i, j))
        np.random.shuffle(res)
        return res

    def __is_solvable(self):
        """Checks if unsolved board is solvable by solver.

        Solves unsolved sudoku board and creates temporary object for it.
        Compares original solved board and temporary, if they are different
        returns False, if they are same, returns True.

        Returns:
            True: if board is solvable.
            False: if board is not solvable.
        """
        tmp_board = self.solver.solve(self.unsolved)
        compare = tmp_board == self.solved
        if np.where(compare == False)[0].size == 0:
            return True
        return False

    def set_difficulty(self, difficulty):
        """Setter method for difficulty attribute.

        Args:
            difficulty: new difficulty to be assigned.
        
        Raises:
            ValueError: if difficulty is invalid (higher or less than possible values).
        """
        if difficulty > self.board_size ** 2 or difficulty <= 0:
            raise ValueError
        self.difficulty = difficulty

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
            self.solved[pos, i] = self.solved[pos - 1, j]

    def __mix(self, swap_times = 15):
        """Mixes sudoku board by calling particular functions.

        Calls swap_rows, swap_sqr_rows, swap_cols, swap_sqr_cols methods to make board
        building algorithm less obvious for users.

        Args:
            swap_times: number of swaps that will be performed on sudoku board.
                Default value: 15
        """
        while swap_times != 0:
            id_func = np.random.randint(0, 6, 1)
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

if __name__ == '__main__':
    bg = SudokuGenerator()
    checker = bc.BoardChecker()
    
    bg.generate()
    board = bg.get_unsolved()

    bc.print_board(board)
    print(checker.is_valid(board))
