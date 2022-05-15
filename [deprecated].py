import socket
import threading

port = 5050
size = 64

ip = "192.168.110.125"
host = socket.gethostbyaddr(socket.gethostname())
print(host)
addr = (ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

def client(conn, addr):
    print(f"Connection {addr} connected!")
    connected = True
    while connected:
        msg = conn.recv(size).decode('utf-8')
        print(f"{addr} {msg}")
        if msg == "Disconnected":
            connected = False
    conn.close()


def run():
    server.listen()
    print(f"Server is listening at {ip}!")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = client, \
            args = (conn, addr))
        thread.start()
        print(f"Connections {threading.activeCount() - 1}")

run()
