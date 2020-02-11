from board_checker import *
import random
import time

class Generator:
    
    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]

    def generate_solved_board(self):
        self.init_first_line()

        for i in range(1, 9):
            if i % 3 == 0:
                self.shift(i - 1, 1)
            else:
                self.shift(i - 1, 3)
        
        self.mix_board()

    def init_first_line(self):
        self.board[0] = random.sample(range(1, 10), 9)

    def shift(self, pos, shiftVal):
        for i in range(len(self.board[pos])):
            j = (i + shiftVal) % len(self.board)
            self.board[pos + 1][i] = self.board[pos][j]

    def mix_board(self, swap_times = 10):
        mix_functions = ["self.swap_rows()",
                         "self.swap_sqr_rows()",
                         "self.swap_cols()",
                         "self.swap_sqr_cols()"]

        for i in range(swap_times):
            id_func = random.randrange(0, len(mix_functions))
            eval(mix_functions[id_func])


    def swap_rows(self):
        right_border = int(len(self.board) / 3)
        sqr = random.randrange(0, right_border, 1)
        row1 = random.randrange(0, right_border, 1)
        row2 = random.randrange(0, right_border, 1)

        pos1 = sqr*3 + row1
        pos2 = sqr*3 + row2
        self.board[pos1], self.board[pos2] = \
                         self.board[pos2], self.board[pos1]

    def swap_sqr_rows(self):
        right_border = int(len(self.board) / 3)
        sqr = random.randrange(0, right_border, 1)
        row1 = random.randrange(0, right_border, 1) * sqr
        row2 = random.randrange(0, right_border, 1) * sqr

        for i in range(3):
            self.board[row1], self.board[row2] = \
                self.board[row2], self.board[row1]
            row1 += 1
            row2 += 1

    def swap_cols(self):
        right_border = int(len(self.board) / 3)
        sqr = random.randrange(0, right_border, 1)
        col1 = random.randrange(0, right_border, 1) * sqr
        col2 = random.randrange(0, right_border, 1) * sqr

        for i in range(len(self.board[0])):
            self.board[i][col1], self.board[i][col2] = \
                self.board[i][col2], self.board[i][col1]

    def swap_sqr_cols(self):
        right_border = int(len(self.board) / 3)
        sqr = random.randrange(0, right_border, 1)
        col1 = random.randrange(0, right_border, 1) * sqr
        col2 = random.randrange(0, right_border, 1) * sqr

        for i in range(len(self.board)):
            for j in range(3):
                self.board[j][col1], self.board[j][col2] = \
                    self.board[j][col2], self.board[j][col1]

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

    def is_solvable(self):
        # check if the board can be solved
        return 1

    def board_print(self):
        length  = range(len(self.board))
        for i in length:
            if i % 3 == 0 and i != 0:
                print("------------------------")
            for j in length:
                if j % 3 == 0 and j != 0:
                    print(" | ", end = "")
                print(str(self.board[i][j]) + " ", end = "")
            print()

    def get_board(self):
        return self.board

if __name__ == '__main__':
    generator = Generator()
    checker = Checker()
    generator.generate_solved_board()
    print(checker.check_solved_board(generator.get_board()))
    generator.board_print()
