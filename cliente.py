import threading
from socket import *

from ticTacToe import TicTacToe

def main():
  HOST = "localhost"
  PORT = 65110
  client = socket(AF_INET, SOCK_STREAM)
  
  try:
    client.connect((HOST, PORT))
  except:
    return print("Não foi possícel se conectar ao servidor!\n")
  
  username = input("Usuário: ")
  print("\nConectado")

def receiveMessage(client):
  pass

def sendMessage(client, username):
  while True:
    try:
      message = input("\n")
      client.send(f"{username} > {message}")
    except:
      return

ttt = TicTacToe()
players = 0
board = ttt.createBoard()
winner = ttt.verifyWinner(board)

# sock = socket(AF_INET, SOCK_STREAM)
# sock.connect((HOST, PORT))


while True:
  print('Faça a sua jogada:')
  print('------------------')

  data = sock.recv(4096)
  print(data.decode())


  while (not winner):
    line = ttt.getInputValid("Digite a linha: ")
    column = ttt.getInputValid("Digite a coluna: ")
    
    if (ttt.verifyMovement(board, line, column)):
      ttt.makeMovement(board, line, column, players)
      players = (players + 1) % 2
    else:
      print("A posição informada já está ocupada")
    
    winner = ttt.verifyWinner(board)

    ttt.printBoard(board)

  sock.close()
  break