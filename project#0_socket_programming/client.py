import socket

HOST='192.168.0.23'

PORT = 8000

BUFFER = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

sock.send('hello, tcpServer!'.encode())

recv = sock.recv(BUFFER)

print('[tcpServer said]: %s' % recv)

sock.close()
