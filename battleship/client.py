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
hit_or_miss = ""

def print_server_board():
    for i in range(10):
        for j in range(10):
            print(s_board[i][j], end=' ')
        print()

def print_boards(cli):
    print("My Board:")
    cli.print_board()
    print("\nServer's Board:")
    print_server_board()

def print_help():
    print("Entre 'p' para ver o que aprendeu do servidor")
    print("Entre 'stop' para sair")
    print("Para atacar, informe <linha>,<coluna>. E.g. A,1")

def main():
    cli = client()
    print("Started client's board")

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 1234
    tcp.connect(('127.0.0.1', port))
    print("Conectou ao servidor")

    print("Para sair, digite 'stop'\n")
    print("Para ajuda, entre 'h'")

    msg = input("~ ")

    while cli.ship_qty > 0:

        len_msg_spl = len(msg.split(','))
        
        if len_msg_spl == 1:
            if msg == 'p' or msg == 'P':
                print_boards(cli)

            elif msg == 'h' or msg == 'H':
                print_help()

            msg = input("~ ")
            
        elif len_msg_spl > 1:
            if msg.split(',')[1] == 'p' or msg.split(',')[1] == 'P':
                print_boards(cli)

            elif msg.split(',')[1] == 'h' or msg.split(',')[1] == 'H':
                print_help()

            else:
                tcp.send(bytes(msg, 'utf-8'))
                
                msg_from_server = tcp.recv(2048).decode('utf-8')
                fmt_msg_serv = msg_from_server.split(',')
                
                # show servers response and atk
                print("You %s! I attack on position (%s,%s)" % (fmt_msg_serv[0], fmt_msg_serv[1], fmt_msg_serv[2]))

                msg_from_server = msg_from_server.split(',')

                if msg_from_server[0] == 'hit':
                    # process clients atk
                    msg = msg.split(',')

                    if len(msg) == 2:
                        row = ord(msg[0]) - 65
                        col = int(msg[1]) - 1
                    else:
                        row = ord(msg[1]) - 65
                        col = int(msg[2]) - 1

                    s_board[row][col] = 'H'

                    # process servers atk
                    row = ord(msg_from_server[1]) - 65
                    col = int(msg_from_server[2]) - 1

                    # if the server hit a clients ship
                    if (cli.board[row][col] != 'e'):
                        cli.board[row][col] = 'X'
                        cli.ship_qty -= 1
                        hit_or_miss = "hit,"

                    # if the server misses
                    else:
                        cli.board[row][col] = 'X'
                        hit_or_miss = "miss,"

                elif msg_from_server[0] == 'miss':
                    # process clients atk
                    msg = msg.split(',')

                    if len(msg) == 2:
                        row = ord(msg[0]) - 65
                        col = int(msg[1]) - 1
                    else:
                        row = ord(msg[1]) - 65
                        col = int(msg[2]) - 1

                    s_board[row][col] = 'm'

                    # process servers atk
                    row = ord(msg_from_server[1]) - 65
                    col = int(msg_from_server[2]) - 1

                    # if the server hit a clients ship
                    if (cli.board[row][col] != 'e'):
                        cli.board[row][col] = 'X'
                        cli.ship_qty -= 1
                        hit_or_miss = "hit,"
                    # if the server misses
                    else:
                        cli.board[row][col] = 'X'
                        hit_or_miss = "miss,"

            msg = hit_or_miss + input("~ ")
        
    tcp.close()

if __name__ == "__main__":
    main()