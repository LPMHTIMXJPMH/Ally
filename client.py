import socket

s = socket.socket()

port = 5049

s.connect(('192.168.110.175',port))

print(s.recv(1024).decode())
s.close()
