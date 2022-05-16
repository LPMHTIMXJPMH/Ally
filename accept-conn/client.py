import socket


addr = "192.168.110.175"
port = 5051
address = (addr, port)


s = socket.socket()
s.connect(address)


receive = s.recv(1024).decode()
print("message from server received:")
print(receive)


s.send("Sending message from client to server.".encode())
while True:
    s.send("Sending message from client to server.".encode())


s.close()
