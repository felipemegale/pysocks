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
    
    def place_tankers(self):
        print("placed tankers")
    
    # server's board assembly
    def assemble_random_board(self):
        self.place_carrier()
        self.place_tankers()

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