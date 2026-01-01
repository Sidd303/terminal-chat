import socket
import threading
import os

# ===== COLORS =====
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"

HOST = "127.0.0.1"  # later → global tunnel
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def clear():
    os.system("clear" if os.name == "posix" else "cls")


def banner():
    print(CYAN + BOLD)
    print("████████╗███████╗██████╗ ███╗   ███╗")
    print("╚══██╔══╝██╔════╝██╔══██╗████╗ ████║")
    print("   ██║   █████╗  ██████╔╝██╔████╔██║")
    print("   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║")
    print("   ██║   ███████╗██║  ██║██║ ╚═╝ ██║")
    print("   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝")
    print("        TERMINAL CHAT CLIENT v1.0")
    print(RESET)


clear()
banner()


def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "USERNAME":
                username = input(f"{MAGENTA}Choose username → {RESET}")
                client.send(username.encode())
                print(f"{GREEN}✔ Connected as {username}{RESET}\n")
            else:
                print(message, end="")
        except:
            print(f"{RED}[ERROR]{RESET} Connection lost")
            client.close()
            break


def write():
    while True:
        msg = input()
        if msg.lower() == "/quit":
            client.close()
            break
        client.send(msg.encode())


threading.Thread(target=receive, daemon=True).start()
write()
