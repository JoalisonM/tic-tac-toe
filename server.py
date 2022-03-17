from socket import *
import threading, json

players = 0
connections = []

HOST = 'localhost'
PORT = 50001

def receive(connection, client):
  global connections

  while (1):
    data = json.loads(connection.recv(1024).decode())
    connection, client = (0, 0)
    pack = {}

    if (data["player"] == 1):
      row = data["row"]
      column = data["column"]
      connection, client = connections[1]

      pack = {
        "row": row,
        "column": column,
      }
    else:
      row = data["row"]
      column = data["column"]
      connection, client = connections[0]

      pack = {
        "row": row,
        "column": column,
      }
  
    connection.send(json.dumps(pack).encode())


server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(2)

while(players < 2):
  connection, client = server.accept()
  nome = connection.recv(1024).decode()
  print("CONECTADO COM SUCESSO A <" + nome + ">.")
  connections.append((connection, client))
  players+=1

for i in range(len(connections)):
  connection, client = connections[i]

  sendPlayer = {
    "player": i+1
  }

  connection.send(json.dumps(sendPlayer).encode())
  connection.recv(1024).decode()

conn1, client1 = connections[0]
conn2, client2 = connections[1]

thread = threading.Thread(target=receive, args=(conn1, client1))
thread.start()
thread = threading.Thread(target=receive, args=(conn2, client2))
thread.start()