from boardChecker import *
from generator import *
class Solver:
    
    def solve(self, board):
        self.board = board
        insertedValue = []
        checker = Checker()
        while checker.checkSolvedBoard(self.board):
            pos = self.findClosestZero()
            if pos[0] == -1:
                return self.board
            val = 1

            while not checker.checkUnsolvedBoard(self.board, val, pos):
                val -=- 1
                if val >= 10:
                    board = self.insertValue(0, pos)
                    pos = insertedValue[len(insertedValue) - 1][1]
                    val = insertedValue[len(insertedValue) - 1][0]
                    insertedValue.pop()
                    continue

            self.board = self.insertValue(val, pos)
            insertedValue.append([val, pos])

        return self.board

    def findClosestZero(self):
        length = range(len(self.board))
        for i in length:
            for j in length:
                if self.board[i][j] == 0:
                    return [i, j]
        return [-1, -1]

    def insertValue(self, val, pos: list):
        self.board[pos[0]][pos[1]] = val
        return self.board


solver = Solver()
generator = Generator()
unsolvedBoard = [
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
solvedBoard = solver.solve(unsolvedBoard)
