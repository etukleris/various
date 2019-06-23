from random import randint
board = []
game = 1
for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row+1)
print (ship_col+1)

#maingame
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
  elif (guess_row-1) == ship_row and (guess_col-1) == ship_col:
    board[guess_row-1][guess_col-1] = "V"
    print ("\n"*50)
    print_board(board)
    print ("Congratulations! You sank my battleship!")
    
    game = 0
  else:
    if guess_row not in range(1,6) or guess_col not in range(1,6):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row-1][guess_col-1] == "X":
      print ("You guessed that one already.")
    else:
      print ("\n"*50)
      print ("You missed my battleship!")
      board[guess_row-1][guess_col-1] = "X"
      print_board(board)

