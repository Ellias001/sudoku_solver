import tkinter
from generator import Generator

class Board:

    def __init__(self, master, board, cube_size = 50):
        self.board = board
        self.master = master
        self.cube_size = cube_size
        self.canvas = tkinter.Canvas(self.master, width = cube_size * 9, height = cube_size * 9)
        self.sqrs = [[Cube(self.board[i][j], i, j, cube_size) for i in range(9)] for j in range(9)]
        
        self.draw_lines()
        self.canv.pack()

    def draw_lines(self):
        for i in range(1, 4):
            x = i * 150
            self.canvas.create_line(x, 0, x, 450, width = 2.3)
            self.canvas.create_line(0, x, 450, x, width = 2.3)
        return

    def fill_sqrs(self):
        pass

class Cube:

    def __init__(self, val, row, col, size):
        self.val = val
        self.row = row
        self.col = col
        self.size = size
        self.is_selected = False

    def draw(self, canvas):
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap
        canvas.create_rectangle()
        
        if self.val == 0:
            
        else:
        
            
        
generator = Generator()
root = tkinter.Tk()
root.title("Sudoku")
Board(root, generator.get_board())
root.mainloop()
