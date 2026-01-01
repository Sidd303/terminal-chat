import socket
import threading

# ===== COLORS =====
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}  # socket : username


def banner():
    print(CYAN + BOLD)
    print("╔════════════════════════════════════════════╗")
    print("║      TERMINAL CHAT SERVER v1.0              ║")
    print("║      Secure • Fast • Python Powered         ║")
    print("╚════════════════════════════════════════════╝")
    print(RESET)


banner()
print(f"{GREEN}[SERVER STARTED]{RESET} Listening on {HOST}:{PORT}\n")


def broadcast(message, sender_socket=None):
    for client in list(clients):
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.pop(client, None)


def handle_client(client_socket):
    try:
        client_socket.send("USERNAME".encode())
        username = client_socket.recv(1024).decode().strip()

        clients[client_socket] = username
        print(f"{GREEN}[JOIN]{RESET} {username} connected")

        broadcast(f"{YELLOW}[SYSTEM]{RESET} {username} joined the chat\n".encode())

        while True:
            message = client_socket.recv(1024)
            if not message:
                break

            formatted = f"{CYAN}[{username}]{RESET} {message.decode()}"
            print(formatted.strip())
            broadcast((formatted + "\n").encode(), client_socket)

    except:
        pass
    finally:
        username = clients.get(client_socket, "Unknown")
        print(f"{RED}[LEAVE]{RESET} {username} disconnected")
        broadcast(f"{YELLOW}[SYSTEM]{RESET} {username} left the chat\n".encode())
        clients.pop(client_socket, None)
        client_socket.close()


while True:
    client_socket, addr = server.accept()
    print(f"{CYAN}[NEW CONNECTION]{RESET} {addr}")
    threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()
