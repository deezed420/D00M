from socket import socket

class dataBeam:
    def __init__(self): self.client = socket(2, 1) ; self.client.connect(('127.0.0.1', 42069))
    def send(self, data: bytes): self.client.send(data)
    def destroy(self): self.client.close()