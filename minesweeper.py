from board import board
from game import game
import tkinter as tk

xlength = int(input("Please give the width of the minesweeper board: "))
ylength = int(input("Please give the height of the minesweeper board: "))
percentMines = float(input("Please enter the decimal portion of the tiles that will be mines: "))

def output():
    global mineSweeperBoard
    global notLost
    outputstring = ""
    board = mineSweeperBoard.get_board()
    for list in board:
        for item in list:
            outputstring += str(item) + " "
        outputstring += "\n"
    if "*" in outputstring:
        notLost = False
        #return
    print(outputstring)

root = tk.Tk()
mineSweeperBoard = board(xlength, ylength, percentMines)
output()

notWon = True
notLost = True
while notWon and notLost:
    nextCoord = tuple(input("Please give the coordinates of the next tile to excavate: "))
    mineSweeperBoard.excavate(nextCoord)
    output()
if not notWon:
    print("Congradulations! You excavated every safe tile!")
elif not notLost:
    print("You attempted to excavate a mine and blew up.")
else:
    raise Exception("Something went wrong!")
