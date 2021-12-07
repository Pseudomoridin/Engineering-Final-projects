#from chess_board import board
import tkinter as tk
ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"

class bishop():
  def __init__(self, colour, position):
    self.colour = colour
    self.position = position
    self.ascii_lowercase = "abcdefgh"

  def set_position(self, position):
    self.position = position

  def get_type(self):
    return "b"

  def get_position(self):
    return self.position

  def get_colour(self):
    return self.colour

  def isCollision(self, move, board):
    self.num_diff = int(move[1]) - int(self.position[1])
    print(self.num_diff)
    self.alpha_diff = self.ascii_lowercase.index(move[0]) - self.ascii_lowercase.index(self.position[0])
    print(self.alpha_diff)
    self.alpha = self.position[0]
    self.alpha = self.ascii_lowercase.index(self.alpha)
    self.numeral = int(self.position[1])
    for x in range(self.num_diff, 2):
      self.test_alpha = self.alpha + x
      self.test_numeral = self.numeral + x
      self.test_move = self.ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      if self.test_move == self.position:
        continue
      if not (board.get_piece(self.test_move) == "-") and not (board.get_piece(self.test_move).get_colour() == self.get_colour()):
        print("err: unexpected collision at point " + self.test_move)
        return True
    for x in range(1, self.num_diff + 1):
      self.test_alpha = self.alpha + x
      self.test_numeral = self.numeral + x
      self.test_move = self.ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      if self.test_move == self.position:
        continue
      if not (board.get_piece(self.test_move) == "-") and not (board.get_piece(self.test_move).get_colour() == self.get_colour()):
        print("err: unexpected collision at point " + self.test_move)
        return True
    self.position = move
    return False

  def move_logic(self, move):
    self.move_list = []
    self.alpha = self.ascii_lowercase.index(move[0])
    self.numeral = int(move[1])
    for x in range(-8, 9):
      self.test_alpha = self.alpha + x
      self.test_alpha2 = self.alpha - x
      try:
        self.test_alpha = self.ascii_lowercase[self.test_alpha]
        self.test_alpha2 = self.ascii_lowercase[self.test_alpha2]
      except:
        continue
      self.test_numeral = self.numeral - x
      if self.test_numeral <= 0 or self.test_numeral > 8:
        continue
      self.test_move = self.test_alpha + str(self.test_numeral)
      self.test_move2 = self.test_alpha2 + str(self.test_numeral)
      self.move_list.append(self.test_move)
      self.move_list.append(self.test_move2)
    print(self.move_list)
    return self.move_list
  
  def move(self, move):
    self.moves = self.move_logic(move)
    if (move in self.moves) == True:
      return True
    else:
      return False
    
class king():
  def __init__(self, colour, position):
    self.colour = colour
    self.position = position
  
  def set_position(self, position):
    self.position = position

  def get_type(self):
    return "K"

  def get_position(self):
    return self.position

  def get_colour(self):
    return self.colour

  def isCollision(self, move, board):
    self.position = move
    return False

  def move_logic(self):
    self.move_list = []
    self.alpha = self.position[0]
    self.alpha = ascii_lowercase.index(self.alpha)
    self.numeral = int(self.position[1])
    for x in range(-1, 2):
      for y in range(-1, 2):
        self.test_alpha = self.alpha + x
        self.test_numeral = self.numeral + y
        self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
        self.move_list.append(self.test_move)
    return self.move_list
  
  def move(self, move):
    self.moves = self.move_logic()
    if (move in self.moves) == True:
      return True
    else:
      return False

class knight():
  def __init__(self, colour, position):
    self.colour = colour
    self.position = position
  
  def set_position(self, position):
    self.position = position

  def get_type(self):
    return "n"

  def get_position(self):
    return self.position

  def get_colour(self):
    return self.colour

  def isCollision(self, move, board):
    return False

  def move_logic(self, move):
    self.move_list = []
    self.alpha = self.position[0]
    self.alpha = ascii_lowercase.index(self.alpha)
    self.numeral = int(self.position[1])
    for x in range(-2, 3, 4):
      for y in range(-1, 2, 2):
        self.test_alpha = self.alpha + x
        self.test_numeral = self.numeral + y
        self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
        self.move_list.append(self.test_move)
    for y in range(-2, 3, 4):
      for x in range(-1, 2, 2):
        self.test_alpha = self.alpha + x
        self.test_numeral = self.numeral + y
        self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
        self.move_list.append(self.test_move)
    return self.move_list
  
  def move(self, move):
    self.moves = self.move_logic(move)
    if (move in self.moves) == True:
      self.position = move
      return True
    else:
      return False

class pawn():
  def __init__(self, colour, position):
    self.colour = colour
    self.position = position
    self.atStart = True

  def set_position(self, position):
    self.position = position

  def get_type(self):
    return "p"

  def get_position(self):
    return self.position

  def get_colour(self):
    return self.colour

  def isCollision(self, move, board):
    self.num_diff = int(move[1]) - int(self.position[1])
    if self.num_diff == 2:
      self.test_move = move[0] + str(int(move[1]) - 1)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    elif self.num_diff == -2:
      self.test_move = move[0] + str(int(move[1]) + 1)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    self.position = move
    self.atStart = False
    return False

  def move_logic(self, move):
    self.move_list = []
    self.alpha = self.position[0]
    self.alpha = ascii_lowercase.index(self.alpha)
    self.numeral = int(self.position[1])
    self.test_alpha = self.alpha
    if self.colour == "white":
      self.test_numeral = self.numeral + 1
      if self.atStart == True:
        self.test_numeral2 = self.numeral + 2
        self.test_move2 = ascii_lowercase[self.test_alpha] + str(self.test_numeral2)
        self.move_list.append(self.test_move2)
    elif self.colour == "black":
      self.test_numeral = self.numeral - 1
      if self.atStart == True:
        self.test_numeral2 = self.numeral - 2
        self.test_move2 = ascii_lowercase[self.test_alpha] + str(self.test_numeral2)
        self.move_list.append(self.test_move2)
    self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
    self.move_list.append(self.test_move)
    return self.move_list
  
  def take_logic(self, move):
    self.take_list = []
    self.alpha = self.position[0]
    self.alpha = ascii_lowercase.index(self.alpha)
    self.numeral = int(self.position[1])
    self.test_alpha = self.alpha
    if self.colour == "white":
      self.test_numeral = self.numeral + 1
    elif self.colour == "black":
      self.test_numeral = self.numeral - 1
    self.test_alpha -= 1
    self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
    self.take_list.append(self.test_move)
    self.test_alpha += 2
    self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
    self.take_list.append(self.test_move)
    return self.take_list


  def move(self, move):
    self.moves = self.move_logic(move)
    self.take = self.take_logic(move)
    if (move in self.moves) == True:
      return True
    elif (move in self.take) == True:
      return "take"
    else:
      return False

class queen():
  def __init__(self, colour, position):
    self.colour = colour
    self.position = position

  def set_position(self, position):
    self.position = position

  def get_type(self):
    return "Q"

  def get_position(self):
    return self.position

  def get_colour(self):
    return self.colour

  def rook_collision_logic(self, num_diff, alpha_diff, num, alpha, board):
    for x in range(self.num_diff, 2):
      if x == 0:
        continue
      if self.num_diff == 0:
        break
      self.test_alpha = self.alpha
      self.test_numeral = self.numeral + x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    for x in range(self.alpha_diff, 2):
      if x == 0:
        continue
      if self.alpha_diff == 0:
        break
      self.test_alpha = self.alpha + x
      self.test_numeral = self.numeral
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    for x in range(1, self.num_diff + 1):
      if x == 0:
        continue
      if self.num_diff == 0:
        break
      self.test_alpha = self.alpha
      self.test_numeral = self.numeral + x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    for x in range(1, self.alpha_diff + 1):
      if x == 0:
        continue
      if self.alpha_diff == 0:
        break
      self.test_alpha = self.alpha + x
      self.test_numeral = self.numeral
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    return False
  
  def bishop_collision_logic(self, num_diff, numeral, alpha, board):
    for x in range(num_diff, 2):
      if x == 0:
        continue
      self.test_alpha = alpha - x
      self.test_numeral = numeral + x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      print(self.test_move)
      if not (board.get_piece(self.test_move) == "-"):
        return True
      self.test_alpha = alpha + x
      self.test_numeral = numeral - x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      print(self.test_move)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    for x in range(1, num_diff + 1):
      if x == 0:
        continue
      self.test_alpha = alpha - x
      self.test_numeral = numeral - x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      print(self.test_move)
      if not (board.get_piece(self.test_move) == "-"):
        return True
      self.test_alpha = alpha + x
      self.test_numeral = numeral - x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      print(self.test_move)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    return False

  def isCollision(self, move, board):
    self.num_diff = int(move[1]) - int(self.position[1])
    self.alpha = self.position[0]
    self.alpha = ascii_lowercase.index(self.alpha)
    self.alpha_diff = ascii_lowercase.index(move[0]) - self.alpha
    self.numeral = int(self.position[1])
    if abs(self.alpha_diff) == abs(self.num_diff):
      print("bishop")
      if self.bishop_collision_logic(self.num_diff, self.numeral, self.alpha, board) == False:
        self.position = move
        return False
      else:
        return True
    elif self.alpha_diff == 0 or self.num_diff == 0:
      print("rook")
      if self.rook_collision_logic(self.num_diff, self.alpha_diff, self.numeral, self.alpha, board) == True:
        return True
      else:
        self.position = move
        return False

  def move_logic(self, move):
    self.move_list = []
    self.alpha = self.position[0]
    self.alpha = ascii_lowercase.index(self.alpha)
    self.numeral = int(self.position[1])
    for x in range(-8, 9):
      self.test_alpha = self.alpha + x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.numeral)
      self.move_list.append(self.test_move)
      self.test_numeral = self.numeral + x
      self.test_move = ascii_lowercase[self.alpha] + str(self.test_numeral)
      self.move_list.append(self.test_move)
      self.test_alpha = self.alpha + x
      self.test_numeral = self.numeral + x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      self.move_list.append(self.test_move)
      self.test_alpha = self.alpha - x
      self.test_numeral = self.numeral + x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      self.move_list.append(self.test_move)
    return self.move_list
  
  def move(self, move):
    self.moves = self.move_logic(move)
    if (move in self.moves) == True:
      return True
    else:
      return False

class rook():
  def __init__(self, colour, position):
    self.colour = colour
    self.position = position

  def set_position(self, position):
    self.position = position

  def get_type(self):
    return "r"

  def get_position(self):
    return self.position

  def get_colour(self):
    return self.colour

  def isCollision(self, move, board):
    self.num_diff = int(move[1]) - int(self.position[1])
    self.alpha = self.position[0]
    self.alpha = ascii_lowercase.index(self.alpha)
    self.alpha_diff = ascii_lowercase.index(move[0]) - self.alpha
    self.numeral = int(self.position[1])
    for x in range(self.num_diff, 2):
      if x == 0:
        continue
      if self.num_diff == 0:
        break
      self.test_alpha = self.alpha
      self.test_numeral = self.numeral + x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    for x in range(self.alpha_diff, 2):
      if x == 0:
        continue
      if self.alpha_diff == 0:
        break
      self.test_alpha = self.alpha + x
      self.test_numeral = self.numeral
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    for x in range(1, self.num_diff + 1):
      if x == 0:
        continue
      if self.num_diff == 0:
        break
      self.test_alpha = self.alpha
      self.test_numeral = self.numeral + x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    for x in range(1, self.alpha_diff + 1):
      if x == 0:
        continue
      if self.alpha_diff == 0:
        break
      self.test_alpha = self.alpha + x
      self.test_numeral = self.numeral
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
      if not (board.get_piece(self.test_move) == "-"):
        return True
    self.position = move
    return False
    
  def move_logic(self, move):
    self.move_list = []
    self.alpha = self.position[0]
    self.alpha = ascii_lowercase.index(self.alpha)
    self.numeral = int(self.position[1])
    for x in range(-8, 9):
      self.test_alpha = self.alpha + x
      self.test_move = ascii_lowercase[self.test_alpha] + str(self.numeral)
      self.move_list.append(self.test_move)
      self.test_numeral = self.numeral + x
      self.test_move = ascii_lowercase[self.alpha] + str(self.test_numeral)
      self.move_list.append(self.test_move)
    return self.move_list
  
  def move(self, move):
    self.moves = self.move_logic(move)
    if (move in self.moves) == True:
      return True
    else:
      return False

class board():
  def __init__(self):
    self.chessboard = {
      "a1":rook("white", "a1"),"a2":pawn("white", "a2"),"a7":pawn("black", "a7"),"a8":rook("black", "a8"),
      "b1":knight("white", "b1"),"b2":pawn("white", "b2"),"b7":pawn("black", "b7"),"b8":knight("black", "b8"),
      "c1":bishop("white", "c1"),"c2":pawn("white", "c2"),"c7":pawn("black", "c7"),"c8":bishop("black", "c8"),
      "d1":queen("white", "d1"), "d2":pawn("white", "d2"),"d7":pawn("black", "d7"),"d8":queen("black", "d8"),
      "e1":king("white", "e1"),"e2":pawn("white", "e2"),"e7":pawn("black", "e7"),"e8":king("black", "e8"),
      "f1":bishop("white", "f1"),"f2":pawn("white", "f2"),"f7":pawn("black", "f7"),"f8":bishop("black", "f8"),
      "g1":knight("white", "g1"),"g2":pawn("white", "g2"),"g7":pawn("black", "g7"),"g8":knight("black", "g8"),
      "h1":rook("white", "h1"),"h2":pawn("white", "h2"),"h7":pawn("black", "h7"),"h8":rook("black", "h8"),
    }

  def get_piece(self, position):
    try:
      return self.chessboard[position]
    except:
      return "-"

  def return_board(self):
    print_board = []
    for x in range(8):
      print_board.append([])
      for y in range(8):
        try:
          position = ascii_lowercase[y] + str(x+1)
          print_board[x].append([self.get_piece(position).get_type(), self.get_piece(position).get_colour()])
        except:
          print_board[x].append("-")
    return print_board

  def query_take_piece(self, position):
    if self.get_piece(position) == "-":
      return False
    else:
      return True

  def move_piece(self, move):
    self.start = move[:move.index(" to ")]
    self.end = move[move.index(" to ") + 4 :]
    self.bool_move = self.chessboard[self.start].move(self.end)
    if self.bool_move == "take":
      if self.query_take_piece(self.end) == True:
        self.bool_move = True
    #testing for piece collisions
    if self.chessboard[self.start].isCollision(self.end, self) == True and self.bool_move == True:
      print("bool_move changed")
      self.bool_move = False
    if self.bool_move == True:
      if self.query_take_piece(self.end) == False:
        self.store_piece = self.chessboard[self.start]
        self.chessboard[self.start] = "-"
        self.chessboard[self.end] = self.store_piece
      elif self.take_piece(self.start, self.end) == True:
        self.store_piece = self.chessboard[self.start]
        self.chessboard[self.start] = "-"
        self.chessboard[self.end] = self.store_piece
    else:
      print("invalid move")

  def take_piece(self, start, end):
    try:
      if not self.chessboard[start].get_colour() == self.chessboard[end].get_colour():
        return True
      else:
        return False
    except:
      return False


def handle_click_a1(event):
  input_chess.append("a1")
def handle_click_b1(event):
  input_chess.append("b1")
def handle_click_c1(event):
  input_chess.append("c1")
def handle_click_d1(event):
  input_chess.append("d1")
def handle_click_e1(event):
  input_chess.append("e1")
def handle_click_f1(event):
  input_chess.append("f1")
def handle_click_g1(event):
  input_chess.append("g1")
def handle_click_h1(event):
  input_chess.append("h1")

def handle_click_a2(event):
  input_chess.append("a2")
def handle_click_b2(event):
  input_chess.append("b2")
def handle_click_c2(event):
  input_chess.append("c2")
def handle_click_d2(event):
  input_chess.append("d2")
def handle_click_e2(event):
  input_chess.append("e2")
def handle_click_f2(event):
  input_chess.append("f2")
def handle_click_g2(event):
  input_chess.append("g2")
def handle_click_h2(event):
  input_chess.append("h2")

def handle_click_a3(event):
  input_chess.append("a3")
def handle_click_b3(event):
  input_chess.append("b3")
def handle_click_c3(event):
  input_chess.append("c3")
def handle_click_d3(event):
  input_chess.append("d3")
def handle_click_e3(event):
  input_chess.append("e3")
def handle_click_f3(event):
  input_chess.append("f3")
def handle_click_g3(event):
  input_chess.append("g3")
def handle_click_h3(event):
  input_chess.append("h3")

def handle_click_a4(event):
  input_chess.append("a4")
def handle_click_b4(event):
  input_chess.append("b4")
def handle_click_c4(event):
  input_chess.append("c4")
def handle_click_d4(event):
  input_chess.append("d4")
def handle_click_e4(event):
  input_chess.append("e4")
def handle_click_f4(event):
  input_chess.append("f4")
def handle_click_g4(event):
  input_chess.append("g4")
def handle_click_h4(event):
  input_chess.append("h4")

def handle_click_a5(event):
  input_chess.append("a5")
def handle_click_b5(event):
  input_chess.append("b5")
def handle_click_c5(event):
  input_chess.append("c5")
def handle_click_d5(event):
  input_chess.append("d5")
def handle_click_e5(event):
  input_chess.append("e5")
def handle_click_f5(event):
  input_chess.append("f5")
def handle_click_g5(event):
  input_chess.append("g5")
def handle_click_h5(event):
  input_chess.append("h5")

def handle_click_a6(event):
  input_chess.append("a6")
def handle_click_b6(event):
  input_chess.append("b6")
def handle_click_c6(event):
  input_chess.append("c6")
def handle_click_d6(event):
  input_chess.append("d6")
def handle_click_e6(event):
  input_chess.append("e6")
def handle_click_f6(event):
  input_chess.append("f6")
def handle_click_g6(event):
  input_chess.append("g6")
def handle_click_h6(event):
  input_chess.append("h6")

def handle_click_a7(event):
  input_chess.append("a7")
def handle_click_b7(event):
  input_chess.append("b7")
def handle_click_c7(event):
  input_chess.append("c7")
def handle_click_d7(event):
  input_chess.append("d7")
def handle_click_e7(event):
  input_chess.append("e7")
def handle_click_f7(event):
  input_chess.append("f7")
def handle_click_g7(event):
  input_chess.append("g7")
def handle_click_h7(event):
  input_chess.append("h7")

def handle_click_a8(event):
  input_chess.append("a8")
def handle_click_b8(event):
  input_chess.append("b8")
def handle_click_c8(event):
  input_chess.append("c8")
def handle_click_d8(event):
  input_chess.append("d8")
def handle_click_e8(event):
  input_chess.append("e8")
def handle_click_f8(event):
  input_chess.append("f8")
def handle_click_g8(event):
  input_chess.append("g8")
def handle_click_h8(event):
  input_chess.append("h8")

def initialize():
  global input_chess, chessboard, root, window, buttons_list, input_chess
  input_chess = []
  chessboard = board()
  root = tk.Tk()
  root.withdraw()
  window = tk.Toplevel(root)
  frame_1 = tk.Frame(master = window)
  frame_2 = tk.Frame(master = window)
  frame_3 = tk.Frame(master = window)
  frame_4 = tk.Frame(master = window)
  frame_5 = tk.Frame(master = window)
  frame_6 = tk.Frame(master = window)
  frame_7 = tk.Frame(master = window)
  frame_8 = tk.Frame(master = window)

  a1 = tk.Button(master = frame_1, height = 2, width = 3)
  a1.pack(side = tk.LEFT)
  a1.bind('<Button-1>', handle_click_a1)
  b1 = tk.Button(master = frame_1, height = 2, width = 3)
  b1.pack(side = tk.LEFT)
  b1.bind('<Button-1>', handle_click_b1)
  c1 = tk.Button(master = frame_1, height = 2, width = 3)
  c1.pack(side = tk.LEFT)
  c1.bind('<Button-1>', handle_click_c1)
  d1 = tk.Button(master = frame_1, height = 2, width = 3)
  d1.pack(side = tk.LEFT)
  d1.bind('<Button-1>', handle_click_d1)
  e1 = tk.Button(master = frame_1, height = 2, width = 3)
  e1.pack(side = tk.LEFT)
  e1.bind('<Button-1>', handle_click_e1)
  f1 = tk.Button(master = frame_1, height = 2, width = 3)
  f1.pack(side = tk.LEFT)
  f1.bind('<Button-1>', handle_click_f1)
  g1 = tk.Button(master = frame_1, height = 2, width = 3)
  g1.pack(side = tk.LEFT)
  g1.bind('<Button-1>', handle_click_g1)
  h1 = tk.Button(master = frame_1, height = 2, width = 3)
  h1.pack(side = tk.LEFT)
  h1.bind('<Button-1>', handle_click_h1)


  a2 = tk.Button(master = frame_2, height = 2, width = 3)
  a2.pack(side = tk.LEFT)
  a2.bind('<Button-1>', handle_click_a2)
  b2 = tk.Button(master = frame_2, height = 2, width = 3)
  b2.pack(side = tk.LEFT)
  b2.bind('<Button-1>', handle_click_b2)
  c2 = tk.Button(master = frame_2, height = 2, width = 3)
  c2.pack(side = tk.LEFT)
  c2.bind('<Button-1>', handle_click_c2)
  d2 = tk.Button(master = frame_2, height = 2, width = 3)
  d2.pack(side = tk.LEFT)
  d2.bind('<Button-1>', handle_click_d2)
  e2 = tk.Button(master = frame_2, height = 2, width = 3)
  e2.pack(side = tk.LEFT)
  e2.bind('<Button-1>', handle_click_e2)
  f2 = tk.Button(master = frame_2, height = 2, width = 3)
  f2.pack(side = tk.LEFT)
  f2.bind('<Button-1>', handle_click_f2)
  g2 = tk.Button(master = frame_2, height = 2, width = 3)
  g2.pack(side = tk.LEFT)
  g2.bind('<Button-1>', handle_click_g2)
  h2 = tk.Button(master = frame_2, height = 2, width = 3)
  h2.pack(side = tk.LEFT)
  h2.bind('<Button-1>', handle_click_h2)


  a3 = tk.Button(master = frame_3, height = 2, width = 3)
  a3.pack(side = tk.LEFT)
  a3.bind('<Button-1>', handle_click_a3)
  b3 = tk.Button(master = frame_3, height = 2, width = 3)
  b3.pack(side = tk.LEFT)
  b3.bind('<Button-1>', handle_click_b3)
  c3 = tk.Button(master = frame_3, height = 2, width = 3)
  c3.pack(side = tk.LEFT)
  c3.bind('<Button-1>', handle_click_c3)
  d3 = tk.Button(master = frame_3, height = 2, width = 3)
  d3.pack(side = tk.LEFT)
  d3.bind('<Button-1>', handle_click_d3)
  e3 = tk.Button(master = frame_3, height = 2, width = 3)
  e3.pack(side = tk.LEFT)
  e3.bind('<Button-1>', handle_click_e3)
  f3 = tk.Button(master = frame_3, height = 2, width = 3)
  f3.pack(side = tk.LEFT)
  f3.bind('<Button-1>', handle_click_f3)
  g3 = tk.Button(master = frame_3, height = 2, width = 3)
  g3.pack(side = tk.LEFT)
  g3.bind('<Button-1>', handle_click_g3)
  h3 = tk.Button(master = frame_3, height = 2, width = 3)
  h3.pack(side = tk.LEFT)
  h3.bind('<Button-1>', handle_click_h3)


  a4 = tk.Button(master = frame_4, height = 2, width = 3)
  a4.pack(side = tk.LEFT)
  a4.bind('<Button-1>', handle_click_a4)
  b4 = tk.Button(master = frame_4, height = 2, width = 3)
  b4.pack(side = tk.LEFT)
  b4.bind('<Button-1>', handle_click_b4)
  c4 = tk.Button(master = frame_4, height = 2, width = 3)
  c4.pack(side = tk.LEFT)
  c4.bind('<Button-1>', handle_click_c4)
  d4 = tk.Button(master = frame_4, height = 2, width = 3)
  d4.pack(side = tk.LEFT)
  d4.bind('<Button-1>', handle_click_d4)
  e4 = tk.Button(master = frame_4, height = 2, width = 3)
  e4.pack(side = tk.LEFT)
  e4.bind('<Button-1>', handle_click_e4)
  f4 = tk.Button(master = frame_4, height = 2, width = 3)
  f4.pack(side = tk.LEFT)
  f4.bind('<Button-1>', handle_click_f4)
  g4 = tk.Button(master = frame_4, height = 2, width = 3)
  g4.pack(side = tk.LEFT)
  g4.bind('<Button-1>', handle_click_g4)
  h4 = tk.Button(master = frame_4, height = 2, width = 3)
  h4.pack(side = tk.LEFT)
  h4.bind('<Button-1>', handle_click_h4)


  a5 = tk.Button(master = frame_5, height = 2, width = 3)
  a5.pack(side = tk.LEFT)
  a5.bind('<Button-1>', handle_click_a5)
  b5 = tk.Button(master = frame_5, height = 2, width = 3)
  b5.pack(side = tk.LEFT)
  b5.bind('<Button-1>', handle_click_b5)
  c5 = tk.Button(master = frame_5, height = 2, width = 3)
  c5.pack(side = tk.LEFT)
  c5.bind('<Button-1>', handle_click_c5)
  d5 = tk.Button(master = frame_5, height = 2, width = 3)
  d5.pack(side = tk.LEFT)
  d5.bind('<Button-1>', handle_click_d5)
  e5 = tk.Button(master = frame_5, height = 2, width = 3)
  e5.pack(side = tk.LEFT)
  e5.bind('<Button-1>', handle_click_e5)
  f5 = tk.Button(master = frame_5, height = 2, width = 3)
  f5.pack(side = tk.LEFT)
  f5.bind('<Button-1>', handle_click_f5)
  g5 = tk.Button(master = frame_5, height = 2, width = 3)
  g5.pack(side = tk.LEFT)
  g5.bind('<Button-1>', handle_click_g5)
  h5 = tk.Button(master = frame_5, height = 2, width = 3)
  h5.pack(side = tk.LEFT)
  h5.bind('<Button-1>', handle_click_h5)


  a6 = tk.Button(master = frame_6, height = 2, width = 3)
  a6.pack(side = tk.LEFT)
  a6.bind('<Button-1>', handle_click_a6)
  b6 = tk.Button(master = frame_6, height = 2, width = 3)
  b6.pack(side = tk.LEFT)
  b6.bind('<Button-1>', handle_click_b6)
  c6 = tk.Button(master = frame_6, height = 2, width = 3)
  c6.pack(side = tk.LEFT)
  c6.bind('<Button-1>', handle_click_c6)
  d6 = tk.Button(master = frame_6, height = 2, width = 3)
  d6.pack(side = tk.LEFT)
  d6.bind('<Button-1>', handle_click_d6)
  e6 = tk.Button(master = frame_6, height = 2, width = 3)
  e6.pack(side = tk.LEFT)
  e6.bind('<Button-1>', handle_click_e6)
  f6 = tk.Button(master = frame_6, height = 2, width = 3)
  f6.pack(side = tk.LEFT)
  f6.bind('<Button-1>', handle_click_f6)
  g6 = tk.Button(master = frame_6, height = 2, width = 3)
  g6.pack(side = tk.LEFT)
  g6.bind('<Button-1>', handle_click_g6)
  h6 = tk.Button(master = frame_6, height = 2, width = 3)
  h6.pack(side = tk.LEFT)
  h6.bind('<Button-1>', handle_click_h6)


  a7 = tk.Button(master = frame_7, height = 2, width = 3)
  a7.pack(side = tk.LEFT)
  a7.bind('<Button-1>', handle_click_a7)
  b7 = tk.Button(master = frame_7, height = 2, width = 3)
  b7.pack(side = tk.LEFT)
  b7.bind('<Button-1>', handle_click_b7)
  c7 = tk.Button(master = frame_7, height = 2, width = 3)
  c7.pack(side = tk.LEFT)
  c7.bind('<Button-1>', handle_click_c7)
  d7 = tk.Button(master = frame_7, height = 2, width = 3)
  d7.pack(side = tk.LEFT)
  d7.bind('<Button-1>', handle_click_d7)
  e7 = tk.Button(master = frame_7, height = 2, width = 3)
  e7.pack(side = tk.LEFT)
  e7.bind('<Button-1>', handle_click_e7)
  f7 = tk.Button(master = frame_7, height = 2, width = 3)
  f7.pack(side = tk.LEFT)
  f7.bind('<Button-1>', handle_click_f7)
  g7 = tk.Button(master = frame_7, height = 2, width = 3)
  g7.pack(side = tk.LEFT)
  g7.bind('<Button-1>', handle_click_g7)
  h7 = tk.Button(master = frame_7, height = 2, width = 3)
  h7.pack(side = tk.LEFT)
  h7.bind('<Button-1>', handle_click_h7)


  a8 = tk.Button(master = frame_8, height = 2, width = 3)
  a8.pack(side = tk.LEFT)
  a8.bind('<Button-1>', handle_click_a8)
  b8 = tk.Button(master = frame_8, height = 2, width = 3)
  b8.pack(side = tk.LEFT)
  b8.bind('<Button-1>', handle_click_b8)
  c8 = tk.Button(master = frame_8, height = 2, width = 3)
  c8.pack(side = tk.LEFT)
  c8.bind('<Button-1>', handle_click_c8)
  d8 = tk.Button(master = frame_8, height = 2, width = 3)
  d8.pack(side = tk.LEFT)
  d8.bind('<Button-1>', handle_click_d8)
  e8 = tk.Button(master = frame_8, height = 2, width = 3)
  e8.pack(side = tk.LEFT)
  e8.bind('<Button-1>', handle_click_e8)
  f8 = tk.Button(master = frame_8, height = 2, width = 3)
  f8.pack(side = tk.LEFT)
  f8.bind('<Button-1>', handle_click_f8)
  g8 = tk.Button(master = frame_8, height = 2, width = 3)
  g8.pack(side = tk.LEFT)
  g8.bind('<Button-1>', handle_click_g8)
  h8 = tk.Button(master = frame_8, height = 2, width = 3)
  h8.pack(side = tk.LEFT)
  h8.bind('<Button-1>', handle_click_h8)

  buttons_list = [[a1,b1,c1,d1,e1,f1,g1,h1],[a2,b2,c2,d2,e2,f2,g2,h2],[a3,b3,c3,d3,e3,f3,g3,h3],[a4,b4,c4,d4,e4,f4,g4,h4],[a5,b5,c5,d5,e5,f5,g5,h5],[a6,b6,c6,d6,e6,f6,g6,h6],[a7,b7,c7,d7,e7,f7,g7,h7],[a8,b8,c8,d8,e8,f8,g8,h8]]

  frame_1.pack()
  frame_2.pack()
  frame_3.pack()
  frame_4.pack()
  frame_5.pack()
  frame_6.pack()
  frame_7.pack()
  frame_8.pack()

def update():
  return_board = chessboard.return_board()
  x = 0
  for row in return_board:
    y = 0
    for item in row:
      buttons_list[x][y]['text'] = item[0]
      try:
        if item[1] == "white":
          buttons_list[x][y]['bg'] = "white"
          buttons_list[x][y]['fg'] = "black"
        if item[1] == "black":
          buttons_list[x][y]['bg'] = "black"
          buttons_list[x][y]['fg'] = "white"
      except:
        buttons_list[x][y]['bg'] = "white"
        buttons_list[x][y]['bg'] = "white"
      y += 1
    x +=1

def go():
  global input_chess
  if len(input_chess) == 2:
    try:
      input_fin = input_chess[0] + " to " + input_chess[1]
      chessboard.move_piece(input_fin)
    except:
      print("failure")
    input_chess = []
    update()
#  window.after(1000, go())

def chessmain():
  initialize()
  update()
  while True:
    window.update()
    window.after(0, go())

  window.mainloop()