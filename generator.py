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

def swapRows(arr, row1, row2, sqr):
    arr[sqr*3 + row1], arr[sqr*3 + row2] = arr[sqr*3 + row2], arr[sqr*3 + row1]
    return arr

def mixBoard(arr):
    random.seed(1)
    for i in range(3):
        row1 = random.randint(0, 2)
        row2 = random.randint(0, 2)
        
        while row1 == row2:
            row2 = random.randint(0, 2)
            
        arr = swapRows(arr, row1, row2, i)

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
    
    board = mixBoard(board)

    end = time.time()
    print("Spent time is " + str(end - start) + " secs")
    return board

def generateUnsolvedBoard(board):
    
    
solvedBoard = generateSolvedBoard()
boardPrint(solvedBoard)
print(checkBoard(solvedBoard))
