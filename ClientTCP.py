# Python TCP Client A
import socket

host = '192.168.0.12'
port = 6780
BUFFER_SIZE = 1024
MESSAGE = " "

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

tcpClientA.sendall("HELLO ClientA")

data = tcpClientA.recv(BUFFER_SIZE)
print " Server received data:", data
MESSAGE = raw_input("tcpClientA: ")
tcpClientA.sendall(MESSAGE)

data = tcpClientA.recv(BUFFER_SIZE)
print " Server received data:", data
MESSAGE = raw_input("tcpClientA: ")
tcpClientA.sendall(MESSAGE)

size = int(MESSAGE)
for i in range(0,size):

    data = tcpClientA.recv(BUFFER_SIZE)
    print data
    MESSAGE = raw_input("tcpClientA: ")
    tcpClientA.sendall(MESSAGE)
    data = tcpClientA.recv(BUFFER_SIZE)
    print data

tcpClientA.close()