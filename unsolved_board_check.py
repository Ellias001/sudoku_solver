def checkCol(board, num, pos: list):
    length = range(len(board))
    for i in length:
        if board[i][pos[1]] == num:
            return 1
    return 0

def checkRow(board, num, pos: list):
    length = range(len(board))
    for i in length:
        if board[pos[0]][i] == num:
            return 1
    return 0

def checkSqr(board, num, pos: list):
    length = range(3)
    sqrRow = int(pos[0] / 3)
    sqrCol = int(pos[1] / 3)
    for i in length:
        i += sqrRow * 3
        for j in length:
            j += sqrCol * 3
            if board[i][j] == num:
                return 1
    return 0

def checkUnsolvedBoard(board, num, pos: list):
    if checkCol(board, num, pos):
        return 0
    if checkRow(board, num, pos):
        return 0
    if checkSqr(board, num, pos):
        return 0
    return 1
