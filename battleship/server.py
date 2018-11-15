import socket
from Board import *

atks_performed = []

def main():
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket created successfully")

	port = 1234

	tcp.bind(('', port))
	print("Socket bound to %s" %(port))

	tcp.listen(1)
	print("Socket is listening")
	ship_qty = 30

	while ship_qty > 0:
		conn, addr = tcp.accept()
		print("Got connection from ", addr)

		s_board = Board()
		print("Assembled board")
		while True:
			msg_from_cli = conn.recv(2048).decode('utf-8') # waits for client to send something
			print(msg_from_cli)

			if not msg_from_cli:
				break
			
			msg_from_cli = msg_from_cli.split(',') # clients atk

			# if its the clients first atk
			if len(msg_from_cli) == 2:
				a_row = ord(msg_from_cli[0]) - 65
				a_col = int(msg_from_cli[1]) - 1

				# test clients atk on server's board
				# if that position in the board is not empty, means that the client has hit a ship
				if (s_board.board[a_row][a_col] != 'e'):
					s_board.board[a_row][a_col] = 'X'
					ship_qty -= 1

					_i,_j = random.randint(0,9), random.randint(0,9)
					atks_performed.append((_i,_j))

					s_atk = "hit," + str(chr(_i + 65)) + "," + str((_j+1))
					conn.send(bytes(s_atk,'utf-8'))
				# if the client missed
				else:
					_i,_j = random.randint(0,9), random.randint(0,9)
					atks_performed.append((_i,_j))

					s_atk = "miss," + str(chr(_i + 65)) + "," + str(_j+1)
					conn.send(bytes(s_atk,'utf-8'))

			# if its not the clients first atk
			else:
				# if the server hit a clients ship
				if (msg_from_cli[0] == 'hit'):
					# process clients atk
					a_row = ord(msg_from_cli[1]) - 65
					a_col = int(msg_from_cli[2]) - 1

					# if the client hits a servers ship
					if (s_board.board[a_row][a_col] != 'e'):
						s_board.board[a_row][a_col] = 'X'
						ship_qty -= 1
						
						if (_j != 9):
							s_atk = "hit," + str(chr(_i + 65)) + "," + str((_j+2))
							atks_performed.append((_i,_j+1))
							conn.send(bytes(s_atk,'utf-8'))
						
						else:
							_i,_j = random.randint(0,9), random.randint(0,9)
							while ((_i,_j) in atks_performed):
								_i,_j = random.randint(0,9), random.randint(0,9)
							
							s_atk = "hit," + str(chr(_i + 65)) + "," + str((_j+1))
							atks_performed.append((_i,_j))
							conn.send(bytes(s_atk,'utf-8'))
						
					# if the client missed
					else:
						if (_j != 9):
							s_atk = "miss," + str(chr(_i + 65)) + "," + str((_j+2))
							atks_performed.append((_i,_j+1))
							conn.send(bytes(s_atk,'utf-8'))
						
						else:
							_i,_j = random.randint(0,9), random.randint(0,9)
							while ((_i,_j) in atks_performed):
								_i,_j = random.randint(0,9), random.randint(0,9)
							
							s_atk = "miss," + str(chr(_i + 65)) + "," + str((_j+1))
							atks_performed.append((_i,_j))
							conn.send(bytes(s_atk,'utf-8'))
				
				# if the server missed
				else:
					#process clients atk
					a_row = ord(msg_from_cli[1]) - 65
					a_col = int(msg_from_cli[2]) - 1

					# if the client hits a servers ship
					if (s_board.board[a_row][a_col] != 'e'):
						s_board.board[a_row][a_col] = 'X'
						ship_qty -= 1

						_i,_j = random.randint(0,9), random.randint(0,9)
						while ((_i,_j) in atks_performed):
							_i,_j = random.randint(0,9), random.randint(0,9)
						
						s_atk = "hit," + str(chr(_i + 65)) + "," + str((_j+1))
						atks_performed.append((_i,_j))
						conn.send(bytes(s_atk,'utf-8'))

					# if the client missed
					else:
						_i,_j = random.randint(0,9), random.randint(0,9)
						while ((_i,_j) in atks_performed):
							_i,_j = random.randint(0,9), random.randint(0,9)
						
						s_atk = "miss," + str(chr(_i + 65)) + "," + str((_j+1))
						atks_performed.append((_i,_j))
						conn.send(bytes(s_atk,'utf-8'))

		print("End connection with", addr)	
		conn.close()

if __name__ == "__main__":
	main()