class TicTacToe:
  def __init__(self):
    self.value = " "
    self.token = ["X", "O"]

  def createBoard(self):
    board = [
      [self.value, self.value, self.value],
      [self.value, self.value, self.value],
      [self.value, self.value, self.value]
    ]

    return board

  def printBoard(self, board):
    for line in board:
      return line

  def getInputValid(self, menssage):
    try:
      number = int(input(menssage))

      if (number >= 1 and number <= 3):
        return number - 1
      else:
        print("Número precisa estar entre 1 e 3")
        return self.getInputValid(menssage)
    except:
      print("Número não válido")
      return self.getInputValid(menssage)

  def verifyMovement(self, board, line, column):
    if(board[line][column] == self.value):
      return True
    else:
      return False

  def makeMovement(self, board, line, column, player):
    board[line][column] = self.token[player]

  def verifyWinner(self, board):
    for i in range(3):
      if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != self.value ):
        return board[i][0]

      if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != self.value ):
        return board[0][i]

    if(board[0][0]!= self.value and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
      return board[0][0]

    if(board[0][2]!= self.value and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
      return board[0][2]

    for line in board:
      for column in line:
        if (column == self.value):
          return False

    return "Empate"
  
  def randomPlayer(self,token):
    pass
