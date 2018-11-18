class Price(object):

    def tratamento_dados(self):
        assembly_file = open("user_price.txt", "r")

        content = assembly_file.readlines()
        content = [line.strip() for line in content]
        #str = "D-099-1-3299-P399251-N747292"

        for n in content:
            #i = 0
            #D09913299P399251N747292
            #type = [:0]
            #id_msg = [1:3]
            #fuel = [4:4]
            #price = [5:8]
            #lat = [9:15]
            #long = [16:22]

            str = content[n]

            if (str[:0] == 'D'):
                arquivo = open('dados.txt', 'w')
                arquivo.write(str)

                (type, id_msg, fuel, price, lat, long) = str.split("-")
                list = []
                list.append(fuel, price, lat, long)

            else :
                (type, id_msg, fuel, raio, lat, long) = str.split("-")
                pricing_system(fuel, raio, lat, long)

        assembly_file.close()


    def pricing_system(self, fuel, raio, lat, long):
        pass


    def __init__(self):
        self.tratamento_dados()
        
