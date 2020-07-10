# Sudoku Game

Author: Oborotov Iliya.

An application used to generate sudoku problems and play sudoku.

# Project Screen Shot

???

## Installation and setup instruction

Clone down this repository. You will need `numpy` installed globally on your machine.
Make sure you installed pip while python installation.

Installation:

`pip install numpy`

To run the program double-click `gui.py` file.

## Reflection

This project is a personal project. It was developed to learn basic numpy array features and functions, to realize backtracking algorithm and to practice python programming skills.

I aimed to make useful program with graphical user interface, realize different algorithms of different difficulties and learn new python module.

The main challenge to create project was decomposing a solved sudoku board to make sudoku problem. Eventually I came with a solution to take out random parts of a board until it remains solvable (original board and board solved by solver are the same). Also it was difficult to pick up board cells that need to be deleted, since random number pickers after some time started to repeat and pick up same points, what drastically slowed down program execution. So it was decided to create an array of all possible cell locations and shuffle it. That decision noticeably increased performance.

Unexpectidly I found a lot of sudoku solving algorithms and it was decided to use backtracking algorithm due to it's simplicity and wide use. Also it was decided to make GUI with tkinter instead of using other modules is that it is more widely used and I didn't need such powerfull tools as Qt or wx.