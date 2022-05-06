import socket

from zmq import STREAM

size = 64
port = 5050
format = 'utf-8'
disconnect_msg = 'disconnect'
server = "192.168.110.125"
addr = (server, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)
