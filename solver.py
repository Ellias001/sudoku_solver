import numpy as np
import board_checker as bc
import generator as bg

class SudokuSolver:
    """Class made to solve sudoku problems.

    SudokuSolver class uses an instance of BoardChecker in board_checker module
    to solve sudoku problems using backtracking method. Method: add valid numbers
    to a board and if there is no valid number to insert, goes back to previous
    position and inserts another valid value until sudoku becomes solved.

    Attr:
        board: copy of unsolved sudoku board that needs to be solved.
        board_size: number of rows/columns in sudoku.
        zero_pos: positions of all zero values in board.
            zero_pos[0][i] - row position of ith element.
            zero_pos[1][i] - column position of ith element.
    """
    def __init__(self, board=0):
        """Constructor for SudokuSolver.

        Initializes board, board_size and zero_pos attributes. If there
        are no arguments passed exits the function.

        Args:
            board: unsolved sudoku board.
                default: 0.
        """
        if isinstance(board, int):
            return
        self.board = board.copy()
        self.board_size = board.shape[0]
        self.zero_pos = np.where(self.board == 0)

    def solve(self, board):
        """Solves sudoku board using backtracking method.

        Uses board_checker module to solve sudoku problems. Backtracking method: add
        valid numbers to a board and if there is no valid number to insert, goes back 
        to previous position and inserts another valid value until sudoku becomes solved.

        Args:
            board: unsolved sudoku board.
        """
        self.__init__(np.array(board))
        checker = bc.BoardChecker()
        values = np.ones(len(self.zero_pos[0]), dtype='int8')
        cur_pos = 0

        while not checker.is_valid(self.board) or cur_pos == len(values) - 1:
            val = values[cur_pos]
            pos = np.array([self.zero_pos[0][cur_pos], self.zero_pos[1][cur_pos]])
            
            while not checker.can_insert(self.board, pos, val):
                val += 1
                if val > self.board_size:
                    self.board[pos[0], pos[1]] = 0
                    values[cur_pos] = 0
                    cur_pos -= 1
                    val = values[cur_pos]
                    pos = np.array([self.zero_pos[0][cur_pos], self.zero_pos[1][cur_pos]])
            
            values[cur_pos] = val
            cur_pos += 1
            self.board[pos[0], pos[1]] = val

        return self.board.copy()

if __name__ == "__main__":
    ss = SudokuSolver()
    board = [
        [3, 2, 0, 0, 1, 4, 9, 0, 0],
        [0, 0, 0, 0, 6, 3, 0, 0, 0],
        [4, 6, 0, 0, 0, 8, 0, 0, 7],
        [2, 0, 0, 0, 0, 6, 4, 0, 3],
        [0, 3, 8, 0, 2, 0, 5, 7, 0],
        [6, 0, 4, 1, 0, 0, 0, 0, 9],
        [8, 0, 0, 9, 0, 0, 0, 5, 2],
        [0, 0, 0, 3, 8, 0, 0, 0, 0],
        [0, 0, 2, 6, 7, 0, 0, 8, 4]
    ]
    board = np.array(board)
    bc.print_board(ss.solve(board))