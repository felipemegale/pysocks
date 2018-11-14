import socket
from Price import Price

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket created successfully")

port = 1234

udp.bind(('', port))
print("Socket bound to %s" %(port))

#udp.listen(1)
print("Socket is listening")

while True:
	msg, client = udp.recvfrom(1024)
	print client, msg
udp.close()