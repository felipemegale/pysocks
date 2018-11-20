import socket
#from Price import Price

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket created successfully")

port = int(input("Enter port: "))

udp.bind(('', port))
print("Socket bound to %s" %(port))

print("Socket is listening")

while True:
	msg, client = udp.recvfrom(1024)
	msg = msg.decode("utf-8")

	if msg != "stop":
		print (client, msg)
	else:
		udp.close()
		break