class Checker:

    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]
    
    def checkSolvedBoard(self, board):
        self.board = board
        if self.checkSolvedRows():
            return 0
        if self.checkSolvedCols():
            return 0
        if self.checkSolvedSqrs():
            return 0
        return 1

    def checkUnsolvedBoard(self, board, num, pos: list):
        self.board = board
        if self.checkUnsolvedRow(num, pos):
            return 0
        if self.checkUnsolvedCol(num, pos):
            return 0
        if self.checkUnsolvedSqr(num, pos):
            return 0
        return 1

    def checkSolvedRows(self):
        length = range(9)
        lst = [i + 1 for i in length]

        for i in length:
            for j in length:
                for k in length:
                    if lst[k] == self.board[i][j]:
                        lst[k] = 0

            if self.isAllZeroes(lst):
                lst = [i + 1 for i in length]
            else:
                return 0

        return 1

    def checkSolvedCols(self):
        length = range(9)
        lst = [i + 1 for i in length]

        for i in length:
            for j in length:
                for k in length:
                    if lst[k] == self.board[j][i]:
                        lst[k] = 0

            if self.isAllZeroes(lst):
                lst = [i + 1 for i in length]
            else:
                return 0
        return 1

    def checkSolvedSqrs(self):
        maxLength = range(9)
        sqrLength = range(3)
        lst = [i + 1 for i in maxLength]

        for numOfSqrs in maxLength:
            for i in sqrLength:
                for j in sqrLength:
                    for k in maxLength:
                        it1 = i + (numOfSqrs % 3)*3
                        it2 = j + (numOfSqrs % 3)*3
                        if lst[k] == self.board[it1][it2]:
                            lst[k] = 0

            if self.isAllZeroes(lst):
                lst = [i + 1 for i in maxLength]
            else:
                return 0
        return 1

    def isAllZeroes(self, lst):
        for i in self.board:
            if i != 0:
                return 0
        return 1

    def checkUnsolvedCol(self, num, pos: list):
        length = range(len(self.board))
        j = pos[1]
        for i in length:
            if self.board[i][j] == num:
                return 1
        return 0

    def checkUnsolvedRow(self, num, pos: list):
        length = range(len(self.board))
        j = pos[0]
        for i in length:
            if self.board[j][i] == num:
                return 1
        return 0

    def checkUnsolvedSqr(self, num, pos: list):
        length = range(3)
        sqrRow = int(pos[0] / 3)
        sqrCol = int(pos[1] / 3)
        for i in length:
            i += sqrRow * 3
            for j in length:
                j += sqrCol * 3
                if self.board[i][j] == num:
                    return 1
        return 0
