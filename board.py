# Imports
import numpy as np
import random
from tile import tile

class board:    
    # Constructors
    def initialize(self, board, mines):
        for x in range(int(mines * len(board))):
            randint = random.randint(0,len(board)-1)
            if self.board[randint] != 1:
                self.board[randint] = 1
            else:
                x -= 1
        for x in range(len(self.board)):
            if self.board[x] == 0:
                self.board[x] = tile(False)
            elif self.board[x] == 1:
                self.board[x] = tile(True)
            else: raise Exception("Something went wrong!")
    def __init__(self, xsize, ysize, mines):
        self.board = [0] * (xsize*ysize)
        self.initialize(self.board, mines)
        self.board = np.reshape(self.board, (ysize,xsize))
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                for i in range(-1,2,1):
                    for j in range(-1,2,1):
                        try:
                            if self.board[x+i][y+j].getIsMine() and (i != 0 or j != 0) and not (x+i < 0 or y+j < 0):
                                self.board[x][y].set_value(self.board[x][y].get_value() + 1)
                        except:
                            continue
    
    # Calling tile-specific functions based on tile
    def excavate(self, inputcoords):
        xcoord = len(self.board) - 1 - int(inputcoords[1])
        ycoord = int(inputcoords[0])
        self.board[xcoord][ycoord].excavate()
    
    # Getters and Setters
    def get_board(self): return self.board
