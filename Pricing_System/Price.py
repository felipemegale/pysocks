from math import radians, cos, sin, asin, sqrt


class Posto(object):
    def __init__(self, fuel, price, lat, long):
        self.fuel = fuel
        self.price = price
        self.lat = lat
        self.long = long

class Price(object):

    def __init__(self):
        self._list = []
        # self.posto = Posto()
        self.tratamento_dados()

    def tratamento_dados(self):
        assembly_file = open("user_price.txt", "r")

        content = assembly_file.readlines()
        content = [line.strip() for line in content]
        #str = "D-099-1-3299-P399251-N747292"

        for n in content:
            """i = 0
            D09913299P399251N747292
            type = [:0]
            id_msg = [1:3]
            fuel = [4:4]
            price = [5:8]
            lat = [9:15]
            long = [16:22]"""

            line = n

            if (line[:0] == 'D'):
                arquivo = open('dados.txt', 'w')
                arquivo.write(line)
                arquivo.close()

                (_type, id_msg, fuel, price, lat, long) = line.split("-")
                self._list.append(Posto(fuel, (price/1000), (lat/10000), (long/10000)))

            else :
                (type, id_msg, fuel, raio, lat, long) = str.split("-")
                self.pricing_system(fuel, raio, (lat/10000), (long/10000))

        assembly_file.close()


    def pricing_system(self, fuel, raio, lat, long):

        menor_preco = 0
        
        for n in self._list:
            if (fuel == self._list[n].fuel) :
                area = area_abrangencia(lat, self._list[n].lat, long, self._list[n].long)

                if (area <= raio) :
                    if(self._list[n].price < menor_preco) :
                        menor_preco = self._list[n].price

        print(menor_preco)
            
            
    def area_abrangencia(self, lat1, lat2, long1, long2):
        lat1, lat2, long1, long2 = map(radians[lat1, lat2, long1, long2]) #converte em rad

        dist_lat = lat2 - lat1
        dist_long = long2 - long1
        area = sin(dist_lat/2)**2 + cos(lat1) * cos(lat2) * sin(dist_long/2)**2
        aux = 2 * asin(sqrt(area))
        r = radius # 6371 km
        resp = aux * r

        return resp

