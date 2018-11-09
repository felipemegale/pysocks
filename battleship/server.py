import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully")

port = 1234

tcp.bind(('', port))
print("Socket bound to %s" %(port))

tcp.listen(1)
print("Socket is listening")

while True:
	c, addr = tcp.accept()
	print("Got connection from ", addr)

	while True:
		msg_from_cli = c.recv(2048).decode('utf-8')
		msg_to_cli = msg_from_cli

		if not msg_from_cli: break
		print("<client>",msg_from_cli)
		c.send(bytes(msg_to_cli, 'utf-8'))

	print("End connection with", addr)	
	#c.send(bytes('Thank you for connecting\n', 'utf-8'))
	c.close()