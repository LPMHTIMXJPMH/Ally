# server    # SOCKET    # server
 
import socket

# name = socket.gethostname()
# host_ip = socket.gethostbyname(name)

host_ip = '192.168.110.175'
port = 5049
print(f"TCP socket bind at: {host_ip} : {port}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host_ip, port))
server.listen(5)
print("Server start listening :)")
