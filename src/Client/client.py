import socket
import pickle

HOST = 'localhost'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

class Client:
    def __init__(self) -> None:
        pass

    def send(self, action, parameters):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            parameters['action'] = action
            data = pickle.dumps(parameters)
            s.sendall(data)
            print(s.getsockname())
            data = s.recv(1024)
        print(f'Received: {data.decode()}')
