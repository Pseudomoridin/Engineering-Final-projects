import tkinter as tk
from main import *
from tictactoe import *
from snake import *

# I know exec() is bad practice but be quiet it works
snake = False
chess = False
tictactoe = False
root = tk.Tk()

def snakegame(event):
    snakemain()
def chessgame(event):
    chessmain()
def tttgame(event):
    tttmain()

button_snake = tk.Button(master=root, height=20, width=100, text="Snake Game")
button_snake.pack()
button_snake.bind('<Button-1>', snakegame)
button_chess = tk.Button(master=root, height=20, width=100, text="Chess")
button_chess.pack()
button_chess.bind('<Button-1>', chessgame)
button_tictactoe = tk.Button(master=root, height=20, width=100, text="Tic Tac Toe")
button_tictactoe.pack()
button_tictactoe.bind('<Button-1>', tttgame)
root.mainloop()
