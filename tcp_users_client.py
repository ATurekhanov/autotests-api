import socket

for i in range(1, 6):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 12345)
    server_socket.connect(server_address)

    server_socket.send(f"{i} Привет, сервер!".encode())

    print(server_socket.recv(1024).decode())

    server_socket.close()