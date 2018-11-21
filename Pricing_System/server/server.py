import socket
import math

class stations(object):
	def __init__(self):
		self.stations = []

	# when the server starts, load data to the memory
	def load_stations(self, _file):
		f = open(_file, "r")
		self.stations = f.readlines()
		self.stations = [data.strip() for data in self.stations]
		f.close()

	# helper function that calculates euclidian distance between two points
	def get_distance(self, _from, to):
		fx = int(_from[0])
		fy = int(_from[1])
		tx = int(to[0])
		ty = int(to[1])
		
		result = math.sqrt(math.pow((fx-tx), 2) + math.pow((fy-ty), 2))
		
		return result

	# gets the lowest price for a fuel type within a points range
	# searches on the data in the file previous to new additions
	def get_lowest_price_old_data(self, fuel_type, radius, orig):
		lowest_price = 99999

		for station in self.stations:
			st_data = station.split("-")

			st_fuel_type = int(st_data[0])
			st_price = int(st_data[1])
			destination = (int(st_data[2]), int(st_data[3]))

			if st_fuel_type != fuel_type:
				pass
			else:
				dist = self.get_distance(orig, destination)

				if dist <= radius:
					if st_price <= lowest_price:
						lowest_price = st_price
		
		return lowest_price

new_data = []

# helper function that calculates euclidian distance between two points
def euc_distance(_from, to):
	fx = int(_from[0])
	fy = int(_from[1])
	tx = int(to[0])
	ty = int(to[1])
	
	result = math.sqrt(math.pow((fx-tx), 2) + math.pow((fy-ty), 2))
	
	return result

# gets the lowest price for a fuel type within a points range
# searches on the newest, unrecorded data
def get_lowest_price_new_data(fuel_type,radius,orig):
	lowest_price = 99999
	
	if new_data:
		for station in new_data:
			print(station)
			st_data = station.split("-")
			st_fuel_type = int(st_data[0])
			st_price = int(st_data[1])
			destination = (int(st_data[2]),int(st_data[3]))

			if st_fuel_type != fuel_type:
				pass
			else:
				dist = euc_distance(orig, destination)

				if dist <= radius:
					if st_price < lowest_price:
						lowest_price = st_price
	
	return lowest_price

st_handler = stations()

st_handler.load_stations("server_data.txt")
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
	print("Client request: ",msg_decode)
	msg_split = msg_decode.split("-")
	d_or_p = msg_split[0].upper()

	# if client is not disconnecting...
	if msg_split[0] != "stop":
		
		# if user is inputting data...
		if d_or_p == "D":
			udp.sendto(bytes("New data received!", "utf-8"), client)
			to_write = msg_split[1]+"-"+msg_split[2]+"-"+msg_split[3]+"-"+msg_split[4]
			print("Writing '%s' to file..." %(to_write))
			data_file.write(to_write+"\n")
			data_file.close()
			new_data.append(to_write)
		
		# if the user is searching, need to look into old and new data
		elif d_or_p == "P":
			fuel_type = int(msg_split[1])
			radius = int(msg_split[2])
			orig = (int(msg_split[3]),int(msg_split[4]))

			print(client," is searching for ",fuel_type,radius,orig)

			lowest_price_old = st_handler.get_lowest_price_old_data(fuel_type,radius,orig)
			lowest_price_new = get_lowest_price_new_data(fuel_type,radius,orig)

			print("Old: %i -- New: %i" %(lowest_price_old,lowest_price_new))

			if lowest_price_old < lowest_price_new:
				udp.sendto(bytes("Lowest price is "+str(lowest_price_old)+" for selected fuel type", "utf-8"), client)
			else:
				udp.sendto(bytes("Lowest price is "+str(lowest_price_new)+" for selected fuel type", "utf-8"), client)

	else:
		udp.close()
		break