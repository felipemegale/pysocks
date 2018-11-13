import socket

class client(object):

    def print_board(self):
        for _list in self.board:
            for el in _list:
                print("%c " %(el), end = '')
            print("")

    def assemble_board(self):
        assembly_file = open("user_board.txt", "r")

        content = assembly_file.readlines()
        content = [line.strip() for line in content]

        assembly_file.close()

    def __init__(self):
        self.board = [['e' for i in range(10)] for j in range(10)]
        self.assemble_board()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1234

tcp.connect(('127.0.0.1', port))
print("Conectou ao servidor")

print("Para sair use CTRL+X\n")

msg = input()

while msg != 'stop':
    tcp.send(bytes(msg, 'utf-8'))
    msg_from_server = '<server> ' + tcp.recv(2048).decode('utf-8')
    print(msg_from_server)
    msg = input()

tcp.close()