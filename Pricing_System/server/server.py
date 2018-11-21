import socket
from math import sqrt, pow
#from Price import Price

stations = []
new_data = []

# when the server starts, load data to the memory
def load_stations():
	f = open("server_data.txt", "r")
	stations = f.readlines()
	stations = [data.strip() for data in stations]
	f.close()

# helper function that calculates euclidian distance between two points
def get_distance(_from, to):
	fx = _from[0]
	fy = _from[1]
	tx = to[0]
	ty = to[1]
	
	result = sqrt(pow((fx-tx), 2) + pow((fy-ty), 2))
	
	return result

# gets the lowest price for a fuel type within a points range
# searches on the data in the file previous to new additions
def get_lowest_price_old_data(fuel_type,radius,orig):
	lowest_price = 99999

	for station in stations:
		st_data = station.split("-")
		st_fuel_type = st_data[0]
		st_price = st_data[1]
		destination = (st_data[2],st_data[3])

		dist = get_distance(orig, destination)

		if dist < radius and st_fuel_type == fuel_type and st_price < lowest_price:
			lowest_price = st_price
	
	return lowest_price

# gets the lowest price for a fuel type within a points range
# searches on the newest, unrecorded data
def get_lowest_price_new_data(fuel_type,radius,orig):
	lowest_price = 99999
	
	for station in new_data:
		st_data = station.split("-")
		st_fuel_type = st_data[0]
		st_price = st_data[1]
		destination = (st_data[2],st_data[3])

		dist = get_distance(orig, destination)

		if dist < radius and st_fuel_type == fuel_type and st_price < lowest_price:
			lowest_price = st_price
	
	return lowest_price

load_stations()
print("Loaded data to memory")

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket created successfully")

port = int(input("Enter port: "))

udp.bind(('', port))
print("Socket bound to %s" %(port))

print("Socket is listening")

# open server data file again, but with append permission
data_file = open("server_data.txt", "a")
print("Opened data file as append to store incoming new data")

while True:
	# message is data (D) or search (P)
	msg, client = udp.recvfrom(1024)
	msg_decode = msg.decode("utf-8") 
	msg_split = msg_decode.split("-")
	d_or_p = msg_split[0].upper()

	# if client is not disconnecting...
	if msg_split[0] != "stop":
		
		# if user is inputting data...
		if d_or_p == "D":
			udp.sendto(bytes(True, "utf-8"), client)
			data_file.write(msg_decode)
			new_data.append(msg_decode)
		
		# if the user is searching, need to look into old and new data
		elif d_or_p == "P":
			fuel_type = msg_split[1]
			radius = msg_split[2]
			orig = (msg_split[3],msg_split[4])

			lowest_price_old = get_lowest_price_old_data(fuel_type,radius,orig)
			lowest_price_new = get_lowest_price_new_data(fuel_type,radius,orig)

			if lowest_price_old < lowest_price_new:
				udp.sendto(bytes("Lowest price is "+str(lowest_price_old), "utf-8"), client)
			else:
				udp.sendto(bytes("Lowest price is "+str(lowest_price_new)+" for selected fuel tye", "utf-8"), client)

	else:
		udp.close()
		break

data_file.close()