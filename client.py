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

def send(client,msg):
    message=msg.encode(FORMAT)
    client.send(message)

# client=connect()
# send(client, "Testing")
# input()
# send(client,DISCONNECT_MESSAGE)

def start():
    answer=input('Would you like to connect(yes/no)?')
    if(answer.lower()!='yes'):
        return
    connection=connect()
    while True:
        msg=input("Message(q for quit): ")

        if msg == 'q':
            break
        send(connection,msg)
    send(connection,DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected')
start()
