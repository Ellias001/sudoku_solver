from board_check import *
import random
import time

def boardPrint(arr):
    for i in range(len(arr)):
        if i % 3 == 0 and i != 0:
            print("------------------------")
        for j in range(len(arr[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            print(str(arr[i][j]) + " ", end = "")
        print()

def shift(arr, shiftVal):
    arr1 = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        arr1[i] = arr[(i + shiftVal) % len(arr)]
    return arr1

def swapRows(arr, row1, row2):
    arr[row1], arr[row2] = arr[row2], arr[row1]
    return arr

def swapCols(arr, col1, col2):
    tmp = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        tmp[i] = arr[i][col1]
        arr[i][col1] = arr[i][col2]
        arr[i][col2] = tmp[i]
    return arr

def mixArr(arr):
    random.seed(1)
    for i in range(4):
        a = random.randint(0, 8)
        b = random.randint(0, 8)

        while a == b:
            b = random.randint(0, 8)

        if i % 2 == 0:
            arr = swapRows(arr, a, b)
        else:
            arr = swapCols(arr, a, b)

    return arr

def generateSolvedBoard():
    start = time.time()
    board = [[0 for i in range(9)] for j in range(9)]
    board[0] = random.sample(range(1, 10), 9)

    for i in range(1, 9):
        if i % 3 == 0:
            board[i] = shift(board[i - 1], 1)
        else:
            board[i] = shift(board[i - 1], 3)
            
    board = mixArr(board)

    end = time.time()
    boardPrint(board)
    print("Spent time is " + str(end - start) + " secs")
    return board
    
generateSolvedBoard()
print(checkBoard(solvedBoard))
