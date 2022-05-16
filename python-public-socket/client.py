import socket

s = socket.socket()

s.connect(('5w308173f5.eicp.vip', 27284))

print(s.recv(1024).decode())
s.close()
