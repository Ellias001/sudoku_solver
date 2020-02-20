########## THINGS TO IMPLEMENT ###########
# prevent underlining existing values
# implement representation of how many mistakes are done
# restart program if 3 mistakes are done
# change values in unsolved board
# offer to start again if sudoku is completed
import tkinter
from generator import Generator
from board_checker import Checker
from solver import Solver

class Board:

    def __init__(self, master, unsolved_board, solver, cube_size = 50):
        self.master = master
        self.unsolved_board = unsolved_board
        self.solved_board = solved_board
        self.cube_size = cube_size
        canvas_size = cube_size * 9 - 3
        self.canvas = tkinter.Canvas(self.master, width = canvas_size, height = canvas_size)
        self.sqrs = [[Cube(self.unsolved_board[i][j], i, j, self.cube_size, self.canvas) \
                      for i in range(9)] for j in range(9)]
        self.selected_rect = None
        self.clicked_cube = None
        self.mistakes = 0
        self.draw_lines()
        self.canvas.pack()

    def draw_lines(self):
        for i in range(1, 3):
            x = i * 150
            self.canvas.create_line(x, 0, x, 450, width = 2.3)
            self.canvas.create_line(0, x, 450, x, width = 2.3)
        return

    def underline(self, event):
        if self.selected_rect != None:
            self.canvas.delete(self.selected_rect)
        pos1 = self.cube_size * int(event.x / self.cube_size)
        pos2 = self.cube_size * int(event.y / self.cube_size)
        cube_pos = [pos1, pos2]
        self.clicked_cube = [int(pos1 / self.cube_size), int(pos2 / self.cube_size)]
        x1 = cube_pos[0]
        y1 = cube_pos[1]
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
                self.canvas.delete(self.selected_rect)
            else:
                self.mistakes += 1
                if self.mistakes == 3:
                    self.restart()
                    
    def restart(self):
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



unsolved_board_tuple = (
        (2, 6, 0, 0, 0, 0, 0, 0, 0),
        (1, 0, 5, 0, 0, 7, 0, 0, 0),
        (0, 0, 0, 1, 8, 0, 0, 0, 0),
        (0, 0, 8, 0, 0, 0, 0, 4, 6),
        (0, 5, 6, 4, 0, 8, 7, 3, 0),
        (4, 3, 0, 0, 0, 0, 8, 0, 0),
        (0, 0, 0, 0, 3, 6, 0, 0, 0),
        (0, 0, 0, 7, 0, 0, 6, 0, 4),
        (0, 0, 0, 0, 0, 0, 0, 7, 9)
)

root = tkinter.Tk()
root.title("Sudoku")
solver = Solver()
unsolved_board_list = [list(line) for line in unsolved_board_tuple]
solved_board = solver.solve(unsolved_board_list)
unsolved_board = [list(line) for line in unsolved_board_tuple]
board = Board(root, unsolved_board, solved_board)

board.canvas.bind("<Button-1>", board.underline)
board.master.bind("<Key>", board.change_val)

root.mainloop()


