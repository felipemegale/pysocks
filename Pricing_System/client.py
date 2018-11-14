import socket

class client(object):

    #def print_price(self):
    #    for _list in self.price:
    #        for el in _list:
    #            print("%c " %(el), end = '')
    #        print("")

    def assemble_price(self):
        assembly_file = open("user_price.txt", "r")

        content = assembly_file.readlines()
        content = [line.strip() for line in content]

        assembly_file.close()

    def __init__(self):
        self.assemble_price()

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 1234

udp.connect(('127.0.0.1', port))
print("Conectou ao servidor")

print("Para sair use CTRL+X\n")

msg = input()

while msg != 'stop':
    udp.send(bytes(msg, 'utf-8'))
    msg = input()

udp.close()