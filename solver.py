from unsolved_board_check import *
from solved_board_check import *

def solve(board):
    insertedValue = []
    while checkSolvedBoard(board):
        pos = findClosestZero(board)
        val = 1

        while not checkUnsolvedBoard(board, val, pos):
            val -=- 1
            if val >= 10:
                board = insertValue(board, 0, pos)
                pos = insertedValue[len(insertedValue) - 1][1]
                val = insertedValue[len(insertedValue) - 1][0]
                insertedValue.pop()
                continue

        board = insertValue(board, val, pos)
        insertedValue.append([val, pos])

    return board

def findClosestZero(board):
    length = range(len(board))
    for i in length:
        for j in length:
            if board[i][j] == 0:
                return [i, j]

def insertValue(board, val, pos: list):
    board[pos[0]][pos[1]] = val
    return board


unsolvedBoard = [
    [0, 0, 2, 3, 5, 0, 0, 0, 9],
    [5, 0, 0, 0, 4, 0, 2, 6, 0],
    [0, 0, 3, 0, 8, 0, 0, 7, 0],
    [0, 0, 0, 0, 9, 4, 0, 0, 0],
    [0, 2, 0, 7, 0, 6, 9, 5, 0],
    [4, 0, 0, 8, 1, 5, 0, 0, 0],
    [1, 7, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 8, 9, 0, 0, 6, 0, 0],
    [0, 0, 6, 4, 0, 0, 5, 8, 7]
]
solvedBoard = solve(unsolvedBoard)
printArr(solvedBoard)
