from socket import socket

client = socket(2, 1) ; client.connect(('5.161.102.38', 3293))
client.send(b'deez')