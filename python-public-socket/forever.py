import socket

import listen

s = listen.server
while True:
    connecter, addr = s.accept()
    print("Connection from client established!")

    connecter.send("Thank you! Now we are connected!".encode())

    s.close()

    break
