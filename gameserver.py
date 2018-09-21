import socket, _thread, os, sys, json
from character import Character

class GameServer():
    def __init__(self, port):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.port = port  
        self.clients = {}

    def start(self):
        # start the server listening
        self.s.bind(("127.0.0.1", self.port))
        
        while True:
            data, addr = self.s.recvfrom(1024)

            # create a dict for the connecting socket
            if addr[1] not in self.clients.keys():
                self.clients[addr[1]] = {}
            
            self.clients[addr[1]] = json.loads(data.decode())

            print(self.clients)
    