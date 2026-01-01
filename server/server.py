import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            break

    clients.remove(client)
    client.close()
    print(f"[DISCONNECTED] {addr}")

print("[SERVER STARTED] Waiting for connections...")

while True:
    client, addr = server.accept()
    clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client, addr))
    thread.start()
