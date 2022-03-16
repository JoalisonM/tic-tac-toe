import json
from socket import *
from ticTacToe import TicTacToe

player = 0
ttt = TicTacToe()
board = ttt.createBoard()
winner = ttt.verifyWinner(board)
player_waiting = False

def responding():
  global player

  while(1):
    row = int(input("Digite a linha: "))
    column = int(input("Digite a coluna: "))

    pack = {
      "player":player,
      "row": row,
      "column": column
    }

    client.send(json.dumps(pack).encode())
    data = json.loads(client.recv(1024).decode())

def main():
  global player
  global client
  global player_waiting
  global board
  global winner


  HOST = 'localhost'
  PORT = 65111

  name = ""
  while(len(name) < 1 or len(name) > 10):
    print("Maximo de caracteres: 10")
    print("Minimo de caracteres: 1")
    name = input("Digite seu nome de jogador: ")
  
  client = socket(AF_INET, SOCK_STREAM)
  client.connect((HOST, PORT))
  client.send(name.encode())

  print("CONECTADO...")
  print("AGUARDANDO OUTROS JOGADORES...")

  message = client.recv(1024).decode()
  print(message)
  message = json.loads(message)
  client.send("{}".encode())

  player = int(message["player"])
  if (player == 1):
    player_waiting = False
  else:
    player_waiting = True

  while (not winner):
    if (not player_waiting):
      row, column = ttt.getInputValid(board)
      
      ttt.makeMovement(board, row-1, column-1, player)
    
      pack = {
        "player":player,
        "row": row,
        "column": column
      }

      client.send(json.dumps(pack).encode())
      player_waiting = True

      ttt.printBoard(board)
    else:
      response = client.recv(1024).decode()
      response = json.loads(response)

      ttt.makeMovement(board, response['row']-1, response['column']-1, (player % 2) + 1)
      print("Jogada do player %s" % ((player % 2) + 1))
      ttt.printBoard(board)
      player_waiting = False

    

    winner = ttt.verifyWinner(board)
  
  print("Ganhador: ", winner)

main()