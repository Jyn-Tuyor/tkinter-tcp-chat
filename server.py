import threading
import socket
import random

port = 7878
host = 'localhost'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()
clients = []

def alert(message):
    for client in clients:
        try:
            client.send(message.encode('ascii'))
        except:
            print("Something went wrong idk")

def broadcast(message, addr):
    host, port = addr
    for client in clients:
        try:
            client.send("{}:{}> {}".format(host, port,message).encode('ascii'))
        except:
            print("Something went wrong idk")

def receive(client, addr):
    while True:
        try:
            message = client.recv(1024).decode()
            broadcast(message, addr)
        except:
            host, port = addr
            alert("{}{} disconnected from the server".format(host, port))
            clients.remove(client)
            # broadcast("{} disconnected from the server.".format(addr), addr)
            client.close()
            break
        # print(message.decode())

while True:
    client, addr = server.accept()

    client.send("Server: {}:{}".format(host, port).encode('ascii'))

    clients.append(client)
    threading.Thread(target=receive, args=(client, addr), daemon=True).start()

    print(f"{addr} connected.")