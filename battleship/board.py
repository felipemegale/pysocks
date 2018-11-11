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

    def place_carrier(self):
        i,j = self.get_origin()

        if i >= 5:
            for _i in range(5, 10):
                self.board[_i][j] = 's'
        else:
            for _i in range(i, i+5):
                self.board[_i][j] = 's'
    
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
                        self.board[i][_j] = 's'
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
                        self.board[i][_j] = 's'
                    valid_j = True
                else:
                    j = random.randint(0,9)
                    while self.board[i][j] != 'e':
                        j = random.randint(0,9)

    def place_destroyer(self):
        
    
    # server's board assembly
    def assemble_random_board(self):
        self.place_carrier()
        self.place_tanker()
        self.place_tanker()

    def __init__(self):
        self.board = [['e' for i in range(10)] for j in range(10)]

def main():
    board = Board()
    board.print_board()
    board.assemble_random_board()
    print("\n")
    board.print_board()

if __name__ == '__main__':
    main()