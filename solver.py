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
                printArr(board)
                val = insertedValue[len(insertedValue) - 1][0]
                pos = insertedValue[len(insertedValue) - 1][1]
                insertedValue.pop()
                break

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
    [2, 5, 6, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 9],
    [0, 3, 0, 6, 0, 0, 0, 7, 0],
    [6, 0, 3, 1, 0, 8, 0, 0, 0],
    [8, 0, 7, 0, 5, 0, 1, 0, 4],
    [0, 0, 0, 4, 0, 3, 9, 0, 6],
    [0, 2, 0, 0, 0, 7, 0, 6, 0],
    [1, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 2, 5, 3]
]
solvedBoard = solve(unsolvedBoard)
printArr(solvedBoard)
