# import socket module
import socket

# create a socket object
s = socket.socket()

# define the port
port = 1234

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server
print(s.recv(1024).decode('utf-8'))

# close the connection
s.close()
