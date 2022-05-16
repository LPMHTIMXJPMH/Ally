import socket


addr = "192.168.110.175"
port = 5051


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((addr, port))
s.listen(5)
print("python server start listening")


conn, addr = s.accept()
conn.send("welcome to socket server.".encode())
while True:
    try:
        from_client = conn.recv(1024).decode()
        if from_client:
            print("Message from client received:")
            print(from_client)
    except:
        continue
conn.close()
