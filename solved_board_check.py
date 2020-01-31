def isAllZeroes(arr):
    for i in arr:
        if i != 0:
            return 0
    return 1

def checkRows(arr):
    length = range(9)
    lst = [i + 1 for i in length]

    for i in length:
        for j in length:
            for k in length:
                if lst[k] == arr[i][j]:
                    lst[k] = 0

        if isAllZeroes(lst):
            lst = [i + 1 for i in length]
        else:
            return 0
    
    return 1

def checkCols(arr):
    length = range(9)
    lst = [i + 1 for i in length]

    for i in length:
        for j in length:
            for k in length:
                if lst[k] == arr[j][i]:
                    lst[k] = 0

        if isAllZeroes(lst):
            lst = [i + 1 for i in length]
        else:
            return 0
    return 1

def checkSqrs(arr):
    maxLength = range(9)
    sqrLength = range(3)
    lst = [i + 1 for i in maxLength]

    for numOfSqrs in maxLength:
        for i in sqrLength:
            for j in sqrLength:
                for k in maxLength:
                    if lst[k] == arr[i + (numOfSqrs % 3)*3][j + (numOfSqrs % 3)*3]:
                        lst[k] = 0

        if isAllZeroes(lst):
            lst = [i + 1 for i in maxLength]
        else:
            return 0
    return 1

def printArr(arr):
    for i in range(len(arr)):
        print(str(i) + " ", end="")
    print()

def checkSolvedBoard(arr):
    if not(checkRows(arr)):
        return -1
    if not(checkCols(arr)):
        return -2
    if not(checkSqrs(arr)):
        return -3
    return 0
