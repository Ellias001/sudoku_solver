# Need to work on:
# 1) mixBoard()
# 2) isSolvable()
# 3) generateUnsolvedBoard()

#from solved_board_check import checkSolvedBoard
#from solver import solve
import random
import time

class Generator:
    
    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]

    def generateSolvedBoard(self):
        self.initFirstLine()

        for i in range(1, 9):
            if i % 3 == 0:
                self.shift(i - 1, 1)
            else:
                self.shift(i - 1, 3)
        
        self.mixBoard()

    def initFirstLine(self):
        self.board[0] = random.sample(range(1, 10), 9)

    def shift(self, pos, shiftVal):
        for i in range(len(self.board[pos])):
            j = (i + shiftVal) % len(self.board)
            self.board[pos + 1][i] = self.board[pos][j]

    def mixBoard(self):
        # need to find real random function to excuse pattern
        # need to add swapCols method
        # need to add swapSqrRows & swapSqrCols method
        for i in range(3):
            row1 = int((time.time() * 1000) % 3)
            row2 = int((time.time() * 1000) % 3)
            
            while row1 == row2:
                row2 = int((time.time() * 1000) % 3)
                
            self.swapRows(row1, row2, i)

    def swapRows(self, row1, row2, sqr):
        self.board[sqr*3 + row1], self.board[sqr*3 + row2] = \
                         self.board[sqr*3 + row2], self.board[sqr*3 + row1]


    #def generateUnsolvedBoard(self):
        #removed = [1, [1, 2]]
        #while isSolvable(board):
            # ------------can be placed in class method------------ #
            #pos = [random.sample(range(1, 10), 2)]

            #while True:
                #isChanged = 0
               # for i in removed[1]:
                   # if i == pos:
                  #      pos = [random.sample(range(1, 10), 2)]
                 #       isChanged = 1
                #        break
               # if isChanged == 1:
              #      continue
             #   else:
            #        break

           # val = board[pos[0]][pos[1]]
          #  removed.append([val, pos])
            # ------------can be placed in class method------------ #
            
            
         #   board = removeElement(board, pos)
        #return board
        # Algorithm:
        # 1) Pick random position at the board
        # 2) Remove it and check weather solver can solve it
        # 3) Continue removing numbers until you get board
        #    with certain number of elements
        # Q: How to check if this table is solvable?

    def isSolvable(self):
        # check if the board can be solved
        return

    def boardPrint(self):
        length  = range(len(self.board))
        for i in length:
            if i % 3 == 0 and i != 0:
                print("------------------------")
            for j in length:
                if j % 3 == 0 and j != 0:
                    print(" | ", end = "")
                print(str(self.board[i][j]) + " ", end = "")
            print()
        
generator = Generator()
generator.generateSolvedBoard()
generator.boardPrint()
