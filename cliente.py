import socket

HOST = '127.0.0.1'
PORT = 50000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.listen()
