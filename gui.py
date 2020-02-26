########## THINGS TO IMPLEMENT ###########
# offer to start again if sudoku is completed

# COMPLETED:
# change values in unsolved board
# prevent underlining existing values
# make board adaptive (changing cube size will create appropriate table)
# implement representation of how many mistakes are done
# restart program if 3 mistakes are done

import tkinter
from generator import Generator
from board_checker import Checker
from solver import Solver

class Board:

    def __init__(self, master, unsolved_board, solved_board, cube_size = 50, mistakes_limit = 3):
        self.master = master
        self.unsolved_board = unsolved_board
        self.solved_board = solved_board
        self.cube_size = cube_size
        self.canvas_size = cube_size * 9 - 3
        self.canvas = tkinter.Canvas(self.master, width = self.canvas_size,\
                                     height = self.canvas_size + cube_size)
        self.sqrs = [[Cube(self.unsolved_board[i][j], i, j, self.cube_size, self.canvas) \
                      for i in range(9)] for j in range(9)]
        self.selected_rect = None
        self.clicked_cube = None
        self.mistakes = 0 # exits the program if mistakes
        self.mistakes_limit = mistakes_limit
        self.num_of_zeroes = self.count_zeroes() # exits the program when board is completed

        self.show_mistake()
        self.draw_lines()
        self.canvas.pack()

    def draw_lines(self):
        for i in range(1, 3):
            x = i * self.cube_size * 3
            self.canvas.create_line(x, 0, x, self.canvas_size + 3, width = 2.3)
            self.canvas.create_line(0, x, self.canvas_size + 3, x, width = 2.3)
        return

    def underline(self, event):
        if self.selected_rect != None:
            self.canvas.delete(self.selected_rect)
        pos1 = int(event.x / self.cube_size)
        pos2 = int(event.y / self.cube_size)
        self.clicked_cube = [pos1, pos2]
        
        if self.unsolved_board[pos2][pos1] != 0:
            return
        
        x1 = pos1 * self.cube_size
        y1 = pos2 * self.cube_size
        x2 = x1 + self.cube_size
        y2 = y1 + self.cube_size
        self.selected_rect = self.canvas.create_rectangle(x1, y1, x2, y2, outline = "red", width = 2.3)

    def change_val(self, event):
        try:
            val = int(event.char)
        except ValueError:
            val = 0
        if self.clicked_cube != None:
            x = self.clicked_cube[0]
            y = self.clicked_cube[1]
            if self.solved_board[y][x] == val:
                self.sqrs[x][y].change_val(val)
                self.num_of_zeroes -= 1
                self.canvas.delete(self.selected_rect)
                if self.num_of_zeroes == 0:
                    self.congrats()
            elif val != 0:
                self.mistakes += 1
                self.show_mistake()
                if self.mistakes == self.mistakes_limit:
                    self.restart()

    def show_mistake(self):
        if self.mistakes == 0:
            return
        for i in range(self.mistakes):
            y1 = self.canvas_size + self.cube_size / 10 + 3
            x1 = self.cube_size / 10 + i * self.cube_size + 3
            y2 = self.canvas_size + 9 * self.cube_size / 10 + 3
            x2 = 9 * self.cube_size / 10 + i * self.cube_size + 3
            self.canvas.create_rectangle(x1, y1, x2, y2, fill = "red")

    def restart(self):
        self.canvas.destroy()
        self.__init__(self.master, self.unsolved_board, self.solved_board)

    def count_zeroes(self):
        num_of_zeroes = 0
        for i in self.unsolved_board:
            for j in i:
                if j == 0:
                    num_of_zeroes += 1
        return num_of_zeroes

    def congrats(self):
        pass

class Cube:

    def __init__(self, val, row, col, size, canvas):
        self.val = val
        self.row = row
        self.col = col
        self.size = size
        self.is_selected = False
        self.canvas = canvas
        self.draw(self.canvas)

    def draw(self, canvas):
        x1 = self.col * self.size
        y1 = self.row * self.size
        x2 = x1 + self.size
        y2 = y1 + self.size
        canvas.create_rectangle(x1, y1, x2, y2)
        
        if self.val != 0:
            x1 = x1 + self.size / 2
            y1 = y1 + self.size / 2 
            canvas.create_text(x1, y1, text = self.val, font = ("Arial", 20))

    def change_val(self, val):
        self.val = val
        self.draw(self.canvas)


def main():
    unsolved_board_tuple = (
            (0, 2, 9, 0, 0, 6, 0, 0, 4),
            (0, 0, 7, 0, 0, 0, 1, 0, 5),
            (0, 6, 0, 0, 1, 3, 0, 0, 2),
            (6, 0, 3, 0, 2, 1, 9, 4, 7),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (9, 8, 1, 5, 4, 0, 6, 0, 3),
            (5, 0, 0, 1, 7, 0, 0, 8, 0),
            (2, 0, 6, 0, 0, 0, 4, 0, 0),
            (7, 0, 0, 3, 0, 0, 2, 5, 0)
    )

    root = tkinter.Tk()
    root.title("Sudoku")
    solver = Solver()
    unsolved_board = [list(line) for line in unsolved_board_tuple]
    solved_board = solver.solve([list(line) for line in unsolved_board_tuple])
    board = Board(root, unsolved_board, solved_board)

    board.master.bind("<Button-1>", board.underline)
    board.master.bind("<Key>", board.change_val)

    root.mainloop()

if __name__ == "__main__":
    main()
