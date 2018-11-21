import random

used_coords = []
fil = open("server_data.txt", "w")

for i in range(0,5000):
    fuel_type = i % 3

    if fuel_type == 0: # diesel
        price = random.randint(2200,2800)
    elif fuel_type == 1: # E85
        price = random.randint(1500,2000)
    else: # gas
        price = random.randint(2100,2500)

    lat = random.randint(0,99)
    lon = random.randint(0,99)

    while (lat, lon) in used_coords:
        lat = random.randint(0,99)
        lon = random.randint(0,99)
    
    used_coords.append((lat, lon))

    data = str(fuel_type)+ "-" +str(price)+ "-" +str(lat)+ "-" +str(lon)+ "\n"

    fil.write(data)

fil.close()