import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1234

tcp.connect(('127.0.0.1', port))

print("Para sair use CTRL+X\n")

msg = input()

while msg != 'stop':
    tcp.send(bytes(msg, 'utf-8'))
    msg_from_server = '<server> ' + tcp.recv(2048).decode('utf-8')
    print(msg_from_server)
    msg = input()

tcp.close()