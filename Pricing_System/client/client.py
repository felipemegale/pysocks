import socket

def assemble_price(self):
    assembly_file = open("user_price.txt", "r")
    content = assembly_file.readlines()
    content = [line.strip() for line in content]
    assembly_file.close()

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter IP: ")
port = int(input("Enter port: "))

dest = (ip, port)

print("Para sair use CTRL+X\n")

msg = input()

while True:
    if msg != "stop":
        udp.sendto(bytes(msg, "utf-8"), dest)

        try:
            udp.settimeout(2)
            msg, server = udp.recvfrom(1024)
            print("Server: ",msg.decode("utf-8"))
        except socket.timeout:
            print("Timed out. Sending message again...")
            udp.sendto(bytes(msg, "utf-8"), dest)

        msg = input()
    else:
        udp.close()
        break
