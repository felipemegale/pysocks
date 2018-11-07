# import socket lib to work with sockets
import socket

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully")

# reserve a port
port = 1234

# bind. Empty IP is used so server can
# listen to requests coming from other
# computers on the network
s.bind(('', port))
print("Socket bound to %s" %(port))

# put the socket into listening mode
# 1 connection only is allowed. More
# incoming connections will be refused
s.listen(1)
print("Socket is listening")

# run server forever until manually
# stopped or an error occurs
while True:
	# establish connection with client
	c, addr = s.accept()
	print("Got connection from ", addr)

	# send a thank you msg to the client
	c.send(bytes('Thank you for connecting\n', 'utf-8'))

	# close the connection with the client
	c.close()
