import socket
#from Price import Price

stations = []

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket created successfully")

port = int(input("Enter port: "))

udp.bind(('', port))
print("Socket bound to %s" %(port))

print("Socket is listening")

while True:
	msg, client = udp.recvfrom(1024) # message is data (D) or search (P)
	msg_decode = msg.decode("utf-8") 
	msg_split = msg_decode.split("-")
	d_or_p = msg_split[0].upper()

	# if client is not disconnecting...
	if msg_split[0] != "stop":
		
		# if user is inputting data...
		if d_or_p == "D":
			udp.sendto(bytes(True, "utf-8"), client)
			data_file = open("server_data.txt", "a")
			data_file.write(msg_decode)
			data_file.close()
		
		# if the user is searching...
		elif d_or_p == "P":
			msg_id = msg_split[1]
			fuel = msg_split[2]
			radius = msg_split[3]
			lat = msg_split[4]
			lon = msg_split[5]

		
	else:
		udp.close()
		break