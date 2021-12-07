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