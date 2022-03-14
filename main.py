from ticTacToe import TicTacToe

ttt = TicTacToe()

player = 0
board = ttt.createBoard()
winner = ttt.verifyWinner(board)


while (not winner):
  print("")
  ttt.printBoard(board)
  print("")
  line = ttt.getInputValid("Digite a linha: ")
  column = ttt.getInputValid("Digite a coluna: ")

  if (line == "Número não válido" or column == "Número não válido"):
    break
  
  if (ttt.verifyMovement(board, line, column)):
    ttt.makeMovement(board, line, column, player)
    player = (player + 1) % 2
  else:
    print("A posição informada já está ocupada")
  winner = ttt.verifyWinner(board)

ttt.printBoard(board)
print("Ganhador: ",winner)