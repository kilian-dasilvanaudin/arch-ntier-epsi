import socket
import pickle
import time

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 12345  # Arbitrary non-privileged port

class Server:
    def __init__(self, menu) -> None:
        self._menu = menu

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            print(f'Server listening on port {PORT}...')
            while True:
                conn, addr = s.accept()
                with conn:
                    print(f'Connected by {addr}')
                    while True:
                        time.sleep(10)
                        data = conn.recv(1024)
                        if not data:
                            break
                        parameters = pickle.loads(data)
                        result = self._menu._main_entries[parameters['action']](parameters)
                        self._menu._application.save()
                        conn.sendall(result.encode())
