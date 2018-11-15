import socket
from Board import *

def main():
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket created successfully")

	port = 1234

	tcp.bind(('', port))
	print("Socket bound to %s" %(port))

	tcp.listen(1)
	print("Socket is listening")

	while True:
		conn, addr = tcp.accept()
		print("Got connection from ", addr)

		s_board = Board()
		while True:
			msg_from_cli = conn.recv(2048).decode('utf-8') # waits for client to send something

			if not msg_from_cli:
				break
			
			msg_from_cli = msg_from_cli.split(',') # clients atk
			a_row = ord(msg_from_cli[0])-65
			a_col = int(msg_from_cli[1])-1

			# test clients atk on server's board
			# if that position in the board is not empty, means that the client has hit a ship
			if (s_board.board[a_row][a_col] != 'e'):
				s_board.board[a_row][a_col] = 'X'
				_i = random.randint(0,9)
				_j = random.randint(0,9)
				s_atk = "hit" + "," + _i + "," + _j
				conn.send(bytes(s_atk,'utf-8'))
			else:
				_i = random.randint(0,9)
				_j = random.randint(0,9)
				s_atk = "miss" + "," + _i + "," + _j
				conn.send(bytes("miss",'utf-8'))

			#conn.send(bytes(msg_to_cli, 'utf-8')) # send something back to the client

		print("End connection with", addr)	
		conn.close()

if __name__ == "__main__":
	main()