import numpy as np
import board_checker as bc
import generator as bg

class SudokuSolver:
    def __init(self, board):
        self.board = board.copy()
        self.board_size = board.shape[0]
        self.arr = np.array([i+1 for i in range(self.board_size)], dtype='int8')
        
        # zero_pos[0][i] - row position of ith element.
        # zero_pos[1][i] - column position of ith element.
        self.zero_pos = np.where(self.board == 0)

    def solve(self, board):
        self.__init(board)
        checker = bc.BoardChecker()
        values = np.ones(len(self.zero_pos[0]), dtype='int8')
        cur_pos = 0

        while not checker.is_valid(self.board) or cur_pos == len(values) - 1:
            val = values[cur_pos]
            pos = np.array([self.zero_pos[0][cur_pos], self.zero_pos[1][cur_pos]])
            
            while not checker.can_insert(self.board, pos, val):
                val += 1
                if val > self.board_size:
                    self.board[pos[0]][pos[1]] = 0
                    values[cur_pos] = 0
                    cur_pos -= 1
                    val = values[cur_pos]
                    pos = np.array([self.zero_pos[0][cur_pos], self.zero_pos[1][cur_pos]])
            
            values[cur_pos] = val
            cur_pos += 1
            self.board[pos[0]][pos[1]] = val
        
        return self.board

if __name__ == "__main__":
    ss = SudokuSolver()
    board = [
        [2, 6, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 5, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 4, 6],
        [0, 5, 6, 4, 0, 8, 7, 3, 0],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 3, 6, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 6, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 7, 9]
    ]
    board = np.array(board)
    bc.print_board(ss.solve(board))