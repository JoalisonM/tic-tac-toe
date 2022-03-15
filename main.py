from socket import *
import time, _thread as thread, json

from ticTacToe import TicTacToe

HOST = 'localhost'
PORT = 65110

sock = socket(AF_INET, SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(2)

ttt = TicTacToe()

players = 0
connections = []
board = ttt.createBoard()
winner = ttt.verifyWinner(board)

while True:
  while (players < 2):
    print("Aguardando conexão com o cliente")
    connection, address = sock.accept()
    print('Server conectado por: ', address)
    connections.append((connection, address))
    players+=1

  data = connection.recv(4096)

  if not data: break

  connection.sendall(ttt.printBoard().encode("utf-8"))

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

  connection.close()
  break

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