import socket

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = '1'
    s.sendall(data.encode())
    print(s.getsockname())
    data = s.recv(1024)

print(f'Received: {data.decode()}')