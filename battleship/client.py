# import socket module
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define the port
port = 1234

# connect to the server on local computer
s.connect(('127.0.0.1', port))

for _ in range(10):
    # send something to server
    s.send(bytes(input(), 'utf-8'))
    
# receive data from the server
print(s.recv(1024).decode('utf-8'))

# close the connection
s.close()
