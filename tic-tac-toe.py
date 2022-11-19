#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# update the gameboard with the user input
def markBoard(position, mark):

    board[position]= mark.upper()
    return
    


# print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
  
  printboard = ["","","","","","","","",""] #initialize a list with 9 values
  i = 1 
  k = 10 
  for i in range (1,k):
    if (board[i] == " "):
      printboard[i-1] = str(i)  
    elif (board[i] == "X"):
      printboard[i-1] = "X"
    elif (board[i] == "O"):
      printboard[i-1] = "O"
 
  print (printboard[0]+" | "+printboard[1]+" | "+printboard[2])
  print ("---------")
  print (printboard[3]+" | "+printboard[4]+" | "+printboard[5])
  print ("---------")
  print (printboard[6]+" | "+printboard[7]+" | "+printboard[8])
  print ("---------")
  
  return 



# check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):

    newPos = int(position)
    if newPos >= 1 and newPos <= 9:
        if (board[newPos] == "X" or board[newPos] == "O"):
            print("The position is occupied")
            return False

        else:
            print("Prompt accepted")
            return True
      
    elif (newPos < 1):
        print("The number is too small, please enter number between     1 to 9")
        return False
    
    elif (newPos > 9):
        print("The number is too big, please enter number between     1 to 9")
        return False
    
    else:
        print("Please enter a NUMBER!")
        return False

# list out all the combinations of winning

winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9], 
    [1, 4, 7],
    [2, 5, 8], 
    [3, 6, 9], 
    [1, 5, 9], 
    [3, 5, 7]

]

# implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):

  i = 0
  k = len(winCombinations)
  for i in range (0,k):
    if (board[winCombinations[i][0]] == player and
        board[winCombinations[i][1]] == player and
        board[winCombinations[i][2]] == player):
      return True

  return False

#implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():

  i = 1
  k = 10
  for i in range (1,k):
    if board[i] == " ":
      return False
  
  return True


def currentPlayer(player,input):
  #if player x, then check if he wins, if not, return "0"
  
  global gameEnded 
  gameEnded = False
  proof = False
  if player == 'X':
    positionX = 0
    if proof == False:
      positionX = int(input)
      proof = validateMove(positionX)
      markX = 'X'
      markBoard(positionX, markX)
      printBoard()
      game_win = checkWin(player)
      fullBoard = checkFull()
      # check both for tie and win
      # if win is true, return win condition
      # elif fullboard is true, return tie condition
      if game_win is True:
        gameEnded = True
        return "X",gameEnded
        
      elif fullBoard is True:
        gameEnded = True
        return "Tie", gameEnded
        
      return  "O",gameEnded

  elif player == 'O':
    positionO = 0
    while proof == False:
      positionO = int(input)
      proof = validateMove(positionO)
      markO = 'O'
      markBoard(positionO, markO)
      printBoard()
      fullBoard = checkFull()
      game_win = checkWin(player)
      if game_win is True:
        gameEnded = True
        return "O",gameEnded
        
      elif fullBoard is True:
        gameEnded = True
        return "Tie", gameEnded
      
      return "X",gameEnded

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')


# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
while not gameEnded:
  move = input(currentTurnPlayer + "'s turn, input: ")
  if move.isdigit() == False:
    print("INSERT NUMBER!")
    continue
  currentTurnPlayer,gameEnded = (currentPlayer(currentTurnPlayer, move))
  
if currentTurnPlayer == "O" or currentTurnPlayer == "X":
  print(currentTurnPlayer + " win")
elif currentTurnPlayer == "Tie":
  print("It's a Tie")





