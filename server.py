import socket
import threading


class Server:
    MAX_CONNECTIONS = 4

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sent = 0

    def start(self):
        self.socket_server.bind((self.ip, self.port))
        self.socket_server.listen(Server.MAX_CONNECTIONS)
        print(f"Server listening on {self.ip}:{self.port}")

        while True:
            client_socket, adrress = self.socket_server.accept()
            print("New client!")

            new_thread = threading.Thread(target=self.handle_request, args=(client_socket, adrress), daemon=True)

            new_thread.start()
            # new_thread.join()

    def handle_request(self, client_socket, adrress):
        data = client_socket.recv(1024).decode("UTF-8")
        print(f"data from client: {adrress}")

        headers = "HTTP/1.1 200 OK\r\nContent-type: text/html; charset=utf-8\r\n\r\n"
        answer = f"data is correct 200 already sent: {self.sent}".encode("UTF-8")
        client_socket.send(headers.encode("UTF-8") + answer)

        # close a client socket
        client_socket.close()

        self.sent += 1
