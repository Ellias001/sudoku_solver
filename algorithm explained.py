def generateBoard():
    
    return arr

def boardPrint(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(str(arr[i][j]) + " ", end = "")
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
        print()
        if i % 3 == 0 and i != 0:
            print("-----------")

def solver():



board = generateBoard()

# First line is a random array of 9 elements that do not repeat
# Other lines are formed by shifting principle (3, 3, 1)
# Swap random lines and rows


# print function is too slow
