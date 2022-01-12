import socket
import time
# build a socket

PORT=443
SERVER="localhost" 
ADDR=(SERVER,PORT)
FORMAT="utf-8"
DISCONNECT_MESSAGE="!DISCONNECT"

def connect():
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def start():
    connection=connect()
    while True:
        msg=connection.recv(1024).decode(FORMAT)
        print(msg)

start()
