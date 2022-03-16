import threading
from socket import *

from ticTacToe import TicTacToe

ttt = TicTacToe()

def main():
  HOST = "localhost"
  PORT = 65111
  client = socket(AF_INET, SOCK_STREAM)
  
  try:
    client.connect((HOST, PORT))
  except:
    return print("Não foi possícel se conectar ao servidor!\n")
  
  username = input("Usuário: ")
  print("\nConectado")

  thread1 = threading.Thread(target=receiveMessage, args=[client])
  thread2 = threading.Thread(target=sendMessage, args=[client, username])

  thread1.start()
  thread2.start()

def receiveMessage(client):
  while True:
    try:
      message = client.recv(2048).decode("utf-8")
      print(message+"\n")
    except:
      print("\nNão foi possível permanecer conectado no servidor")
      print("Pressione ENTER para continuar...")
      client.close()
      break

def sendMessage(client, username):
  while True:
    try:
      print("Faça a sua jogada:\n")
      # message = input("\n")
      row = ttt.getInputValid("Digite a linha: \n")
      print("row: ", row)
      column = ttt.getInputValid("Digite a coluna: \n")
      print("column: ", column)

      coordinates = str(row)+"," + str(column)

      client.send(coordinates.encode("utf-8"))
    except:
      return

main()

# players = 0
# board = ttt.createBoard()
# winner = ttt.verifyWinner(board)


# while True:
#   print('Faça a sua jogada:')
#   print('------------------')

#   data = sock.recv(4096)
#   print(data.decode())


#   while (not winner):
#     line = ttt.getInputValid("Digite a linha: ")
#     column = ttt.getInputValid("Digite a coluna: ")
    
#     if (ttt.verifyMovement(board, line, column)):
#       ttt.makeMovement(board, line, column, players)
#       players = (players + 1) % 2
#     else:
#       print("A posição informada já está ocupada")
    
#     winner = ttt.verifyWinner(board)

#     ttt.printBoard(board)

#   sock.close()
#   break