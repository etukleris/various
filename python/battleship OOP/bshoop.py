from random import randint

class game_board(object):
  def __init__(self):
    self.board = []
    for x in range(0, 5):
      self.board.append(["O"] * 5)

    #ship location in init 
    self.ship_row = randint(0, len(self.board) - 1)
    self.ship_col = randint(0, len(self.board) - 1)
    
  #check if ship got shot
  def check_ship_status(self, row, col):
    if self.ship_row == row and self.ship_col == col:
      return True
    else:
      return False
  def print_board(self):
    for row in self.board:
      print (" ".join(row))
  def change_board(self,status,row, col):
    if status == "Hit":
      self.board[row][col] = "V"
    if status == "Miss":
      self.board[row][col] = "X"
  def check_already_hit(self, row, col):
    if self.board[row][col] == "X":
      return True
  def clear_screen(self):
    print ("\n"*60)
    
#Attempt for a player
"""
class player(object):
  def __init__(self, name):
    
board = game_board()
print (board.ship_loc)
"""
board = game_board()
#maingame
game = 1
board.print_board()
print(board.ship_row)
print(board.ship_col)
while game == 1:
  ##checking for inputs
  try:
    guess_row = int(input("Guess Row: "))
  except ValueError:
    guess_row = 9999
  try:
    guess_col = int(input("Guess Col: "))
  except ValueError:
    guess_col = 9999
  ##checking for inputs done

  if guess_row == 9999 and guess_col == 9999: #in case non ints
    print ("You didn't enter numbers, you know")
  ##the -1 for rows/cols are to make the game feel like
  ##"1 to 5" grid rather than odd "0 to 4"
  elif board.check_ship_status(guess_row, guess_col):
    print("yup")
    board.change_board("Hit", guess_row, guess_col)
    board.print_board()
    #board[guess_row-1][guess_col-1] = "V"
    #print ("\n"*50)
    #print_board(board)
    print ("Congratulations! You sank my battleship!")
    
    game = 0
  else:
    if guess_row not in range(1,6) or guess_col not in range(1,6):
      print ("Oops, that's not even in the ocean.")
    elif board.check_already_hit(guess_row, guess_col):
      print ("You guessed that one already.")
    else:
      #print ("\n"*50)
      print ("You missed my battleship!")
      board.change_board("Miss", guess_row, guess_col)
      board.print_board()
#"""
