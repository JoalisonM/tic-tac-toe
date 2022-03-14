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
      print(line)

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
      return "Número não válido"

  def verifyMovement(self, board, line, column):
    if(board[line][column] == self.value):
      return True
    else:
      return False

  def makeMovement(self, board, line, column, player):
    board[line][column] = self.token[player]

  def verifyWinner(self, board):
    return False