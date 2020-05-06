import board_checker
import generator

class Solver:
    """Class that is intended to solve sudoku problems.

    Attributes:
        board: sudoku board.
        size: length and width of sudoku board.
    """
    def solve(self, board):
        """Solves sudoku board.

        This method uses backtracking method. While board is not solved, it
        puts a number in empty slot and if board becomes invalid, goes back
        and puts another number on previous position untill board is valid and
        solved.

        Args:
            board: unsolved sudoku board.

        Returns:
            board: solved sudoku board.
        """
        if isinstance(board, tuple):
            self.board = self.tuple_to_list(board)
        else:
            self.board = board

        self.size = len(board)
        inserted_value = []
        checker = board_checker.Checker(self.size)
        while checker.check_solved_board(self.board):
            pos = self.find_closest_zero()
            if pos[0] == -1:
                return self.board
            val = 1

            while not checker.check_unsolved_board(self.board, val, pos):
                val += 1
                if val >= self.size + 1:
                    board = self.insert_value(0, pos)
                    pos = inserted_value[len(inserted_value) - 1][1]
                    val = inserted_value[len(inserted_value) - 1][0]
                    inserted_value.pop()
                    continue

            self.board = self.insert_value(val, pos)
            inserted_value.append([val, pos])

        return self.board

    def find_closest_zero(self):
        """Finds first zero that meets in sudoku board.

        Traverses the whole sudoku board while zero is reached.

        Returns:
            [i, j]: position of closest zero.
            [-1, -1]: if there are no zeroes in sudoku board.
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return [i, j]
        return [-1, -1]

    def insert_value(self, val, pos: list):
        """Assigns value at particular position in sudoku board.

        Args:
            val: value to be inserted.
            pos: array defines position in the board.

        Returns:
            board: sudoku board with inserted value
        """
        self.board[pos[0]][pos[1]] = val
        return self.board

    def tuple_to_list(self, board):
        """Converts two-dimensional tuple into list.

        Args:
            board: two-dimensional tuple sudoku board.

        Returns:
            list_board: two-dimensional list sudoku  board.
        """
        list_board = []
        for row in board:
            list_board.append(list(row))
        return list_board

    def print_board(self):
        """Prints the board attribute.

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
        for i in range(self.size):
            if i % 3 == 0 and i != 0:
                print("------------------------")
            for j in range(self.size):
                if j % 3 == 0 and j != 0:
                    print(" | ", end = "")
                print(str(self.board[i][j]) + " ", end = "")
            print()

if __name__ == '__main__':
    solver = Solver()
    generator = generator.Generator()
    unsolved_board = [
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
    solver.solve(unsolved_board)
    solver.print_board()
