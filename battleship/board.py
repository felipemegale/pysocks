import random
'''
Board is 10 x 10
Boats:
    Carrier: 5 blocks (1 per board) - vertical
    Tanker: 4 blocks (2 per board) - horizontal
    Destroyer: 3 blocks (3 per board) - vertical
    Submarine: 2 blocks (4 per board) - horizontal

e e e e e e e e e e
e e e e e e e e e e
e e e e e e e e e e
e e e e e e e e e e
e e e e e e e e e e
e e e e e e e e e e
e e e e e e e e e e
e e e e e e e e e e
e e e e e e e e e e
e e e e e e e e e e
'''
class Board:

    def print_board(self):
        for _list in self.board:
            for el in _list:
                print("%c " %(el), end = '')
            print("")

    def get_origin(self):
        return random.randint(0,9), random.randint(0,9)

    # doesnt need as much logic as the other ships
    # because it is the first one to be placed
    def place_carrier(self):
        i,j = self.get_origin()

        if i >= 5:
            for _i in range(5, 10):
                self.board[_i][j] = 'c'
        else:
            for _i in range(i, i+5):
                self.board[_i][j] = 'c'
    
    def place_tanker(self):
        i,j = self.get_origin()
        valid_j = False

        # if origin position is not free
        while self.board[i][j] != 'e':
            i,j = self.get_origin()

        # cant know if ship actually fits
        while not valid_j:
            # if can place to the right
            if j <= 6:
                # if there is space to place to the right
                if (self.board[i][j+1] == 'e') and (self.board[i][j+2] == 'e') and (self.board[i][j+3] == 'e'):
                    for _j in range(j, j+4):
                        self.board[i][_j] = 't'
                    valid_j = True
                else:
                    j = random.randint(0,9)
                    while self.board[i][j] != 'e':
                        j = random.randint(0,9)
            # if can place to the left
            else:
                # if there is space to place to the left
                if (self.board[i][j-1] == 'e') and (self.board[i][j-2] == 'e') and (self.board[i][j-3] == 'e'):
                    for _j in range(j, j-4, -1):
                        self.board[i][_j] = 't'
                    valid_j = True
                else:
                    j = random.randint(0,9)
                    while self.board[i][j] != 'e':
                        j = random.randint(0,9)

    def place_destroyer(self):
        i,j = self.get_origin()
        valid_i = False

        # if origin position is not free
        while self.board[i][j] != 'e':
            i,j = self.get_origin()

        # cant know if ship actually fits
        while not valid_i:
            # if can place down
            if i <= 7:
                # if there is space to place down
                if (self.board[i+1][j] == 'e') and (self.board[i+2][j] == 'e'):
                    for _i in range(i, i+3):
                        self.board[_i][j] = 'd'
                    valid_i = True
                else:
                    i = random.randint(0,9)
                    while self.board[i][j] != 'e':
                        i = random.randint(0,9)
            # if can place up
            else:
                # if there is space to place up
                if (self.board[i-1][j] == 'e') and (self.board[i-2][j] == 'e'):
                    for _i in range(i, i-3, -1):
                        self.board[_i][j] = 'd'
                    valid_i = True
                else:
                    i = random.randint(0,9)
                    while self.board[i][j] != 'e':
                        i = random.randint(0,9)
    
    def place_submarine(self):
        i,j = self.get_origin()
        valid_j = False

        # if origin position is not free
        while self.board[i][j] != 'e':
            i,j = self.get_origin()

        # cant know if ship actually fits
        while not valid_j:
            # if can place to the right
            if j <= 8:
                # if there is space to place to the right
                if (self.board[i][j+1] == 'e'):
                    for _j in range(j, j+2):
                        self.board[i][_j] = 's'
                    valid_j = True
                else:
                    j = random.randint(0,9)
                    while self.board[i][j] != 'e':
                        j = random.randint(0,9)
            # if can place to the left
            else:
                # if there is space to place to the left
                if (self.board[i][j-1] == 'e'):
                    for _j in range(j, j-2, -1):
                        self.board[i][_j] = 's'
                    valid_j = True
                else:
                    j = random.randint(0,9)
                    while self.board[i][j] != 'e':
                        j = random.randint(0,9)

    # server's board assembly
    def assemble_random_board(self):
        self.place_carrier()
        self.place_tanker()
        self.place_tanker()
        self.place_destroyer()
        self.place_destroyer()
        self.place_destroyer()
        self.place_submarine()
        self.place_submarine()
        self.place_submarine()
        self.place_submarine()

    def __init__(self):
        self.board = [['e' for i in range(10)] for j in range(10)]
        self.assemble_random_board()