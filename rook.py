from string import ascii_lowercase
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
