from socket import *
import time, threading, json

from ticTacToe import TicTacToe

ttt = TicTacToe()
board = ttt.createBoard()
winner = ttt.verifyWinner(board)
waiting_player = []

def main():
  global clients, players, waiting_player

  HOST = 'localhost'
  PORT = 65111

  server = socket(AF_INET, SOCK_STREAM)

  try:
    server.bind((HOST,PORT))
    server.listen(2)
  except:
    return print("\nNão foi possível iniciar o servidor")
  
  while True:
    connection, address = server.accept()
    new_player = Player(connection)
    waiting_player.append(new_player)

    for i in waiting_player:
      print("count:",i.count)

    thread = threading.Thread(target=messagesTreatment, args=[connection])
    thread.start()

def messagesTreatment(client):
  global waiting_player, board
  while True:
    try:
      data = client.recv(2048)
      dataDecoded = data.decode("utf-8").split(",")

      row = int(dataDecoded[0])
      column = int(dataDecoded[1])
      print("row: ", row)
      print("column: ", column)

      message = ttt.printBoard(board)
      broadcast(message, client)

      if (ttt.verifyMovement(board, row, column)):
        for play in waiting_player:
          ttt.makeMovement(board, row, column, play.count)
      else:
        print("A posição informada já está ocupada")

    except Exception as e:
      print("erro: ", e)
      deleteClient(client)
      break

def broadcast(message, client):
  global waiting_player
  for clientItem in waiting_player:
    print("client: ", clientItem)
    if (clientItem != client):
      try:
        clientItem.connection.send(message)
      except Exception as e:
        print("erro: ", e)
        deleteClient(clientItem)

def deleteClient(client):
  global waiting_player

  waiting_player.remove(client)

class Player:
  count = 0

  def __init__(self, connection):
    Player.count = Player.count + 1
    self.id = Player.count
    self.connection = connection
    self.is_waitgin = True

main()
# ttt = TicTacToe()

# players = 0
# board = ttt.createBoard()
# winner = ttt.verifyWinner(board)

# while True:
#   while (players < 2):
#     print("Aguardando conexão com o cliente")
#     connection, address = sock.accept()
#     print('Server conectado por: ', address)
#     connections.append((connection, address))
#     players+=1

#   data = connection.recv(4096)

#   if not data: break

#   connection.sendall(ttt.printBoard().encode("utf-8"))

  #   line = ttt.getInputValid("Digite a linha: ")
  #   column = ttt.getInputValid("Digite a coluna: ")

  #   if (line == "Número não válido" or column == "Número não válido"):
  #     break
    
  #   if (ttt.verifyMovement(board, line, column)):
  #     ttt.makeMovement(board, line, column, players)
  #     players = (players + 1) % 2
  #   else:
  #     print("A posição informada já está ocupada")
    
  #   winner = ttt.verifyWinner(board)

  # ttt.printBoard(board)
  # print("Ganhador: ", winner)

  # connection.close()
  # break

# def timeNow():
#   return time.ctime(time.time())

# def client(connection):
#   time.sleep(1)

#   while True:
#     data = connection.recv(1024)

#     if not data: break

#     response = "Eco=> %s as %s" % (data, timeNow())
  
#     connection.send(response.encode())
  
#   connection.close()

# def despacha():
#   while True:
#     connection, address = sock.accept()
#     print("Server conectado por ", address, end="")
#     print("as", timeNow())

#     thread.start_new_thread(client, (connection,))

# despacha()