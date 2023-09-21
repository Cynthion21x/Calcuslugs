import threading
import socket
import pickle
import Game.src.shared.constants as c

class Server:

    def __init__(self, port, game):

        self.port = int(port)

        self.running = True

        server_thread = threading.Thread(target=self.serverThread)
        server_thread.start()

        self.clients = []

    def threadded_client(self, con):

        con.send(str.encode("connected"))

        reply = ""
        
        while self.running:

            try:

                data = con.recv(2048)
                reply = data.decode("utf-8")

                if not data:

                    print("Disconnect")
                    break;

                else:

                    print("Recieved: ", reply)
                    print("Sending: ", reply)

                con.sendall(str.encode(reply))

            except:
    
                break

    def serverThread(self):

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server.bind((c.LOCALHOST, self.port))
        except socket.error as e:
            print(str(e))

        self.server.listen(4)

        print("Server hosted on port " + str(self.port) + " Waiting for players...")

        while self.running:
            
            client_socket, client_address = self.server.accept()
            print("Player connected:", client_address)

            self.clients.append(client_socket)
            threading.Thread(target=self.threadded_client, args=client_socket)


    def exit(self):

        self.running = False

        print("Shutting off the server")
        