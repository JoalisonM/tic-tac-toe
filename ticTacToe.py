class TicTacToe:
  def __init__(self):
    self.value = " "
    self.token = ["", "X", "O"]

  def createBoard(self):
    board = [
      [self.value, self.value, self.value],
      [self.value, self.value, self.value],
      [self.value, self.value, self.value]
    ]

    return board
  
  
  def printBoard(self, board):
      print("")
      for i in range(3):
         print("")
         print(" | ".join(board[i]))
         if(i<2):
           print("---------")


  def getInputValid(self, board):
    row = None
    column = None
  
    while True:
      try:
        row = int(input("Digite a linha: "))
        column = int(input("Digite a coluna: "))

        if (row  < 1 or row > 3 or column < 1 or column > 3):
          print("Número precisa estar entre 1 e 3\n")
          continue

        if (board[row-1][column-1] != self.value):
          print("Posição já preenchida\n")
          continue
        else:
          return row, column
      
      except:
        print("Digite um número inteiro")
        continue
  

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
