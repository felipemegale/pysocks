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

        sepd = [string.split(',') for string in content]

        for _list in sepd:
            lin = ord(_list[0])-65
            col = int(_list[1])-1
            typ = _list[2]

            self.board[lin][col] = typ

        assembly_file.close()

    def __init__(self):
        self.board = [['e' for i in range(10)] for j in range(10)]
        self.assemble_board()
        self.ship_qty = 30

s_board = [['?' for i in range(10)] for j in range(10)]

def print_server_board():
    for i in range(10):
        for j in range(10):
            print(s_board[i][j], end=' ')
        print()

def main():
    cli = client()
    print("Started client's board")

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 1234
    tcp.connect(('127.0.0.1', port))
    print("Conectou ao servidor")

    print("Para sair digite 'stop'\n")
    print("Para ajuda, entre 'h'")

    msg = input("~ ")

    while msg != 'stop':
        if msg == 'p' or msg == 'P':
            print_server_board()
        elif msg == 'h' or msg == 'H':
            print("Entre 'p' para ver o que aprendeu do servidor")
            print("Entre 'stop' para sair")
            print("Para atacar, informe <linha>,<coluna>. E.g. A,1")
        else:
            tcp.send(bytes(msg, 'utf-8'))
            
            msg_from_server = tcp.recv(2048).decode('utf-8')
            print(msg_from_server)

            msg_from_server = msg_from_server.split(',')

            if msg_from_server[0] == 'hit':
                # process clients atk
                msg = msg.split(',')
                row = ord(msg[0]) - 65
                col = int(msg[1]) - 1

                s_board[row][col] = 'H'

                # process servers atk
                row = ord(msg_from_server[1]) - 65
                col = int(msg_from_server[2]) - 1

                if (cli.board[row][col] != 'e'):
                    cli.board[row][col] = 'X'
                    cli.ship_qty -= 1

            elif msg_from_server[0] == 'miss':
                msg = msg.split(',')
                s_board[ord(msg[0])-65][int(msg[1])-1] = 'm'

        msg = input("~ ")
        
    tcp.close()

if __name__ == "__main__":
    main()