import random
'''
Board is 10 x 10
Boats:
    Carrier: 5 blocks (1 per board)
    Tanker: 4 blocks (2 per board)
    Destroyer: 3 blocks (3 per board)
    Submarine: 2 blocks (4 per board)

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

    def verify_place(self, boat_type):
        # check if is possible to add boat
        print("verify_place")

    def place_carrier(self):
        # choose random row and column
        print("place_carrier")

        # generate random position on the board
        i = random.randint(0,9)
        j = random.randint(0,9)

        if self.board[i][j] == 'e':
            

    def place_tanker(self):
        # choose random row and column
        print("place_tanker")
    
    def place_destroyer(self):
        # choose random row and column
        print("place_destroyer")

    def place_submarine(self):
        # choose random row and column
        print("place_submarine")
    
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

def main():
    board = Board()
    board.print_board()
    board.assemble_random_board()

if __name__ == '__main__':
    main()