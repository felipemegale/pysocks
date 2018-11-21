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

print("To add information: ")
print("D-<fuel type>-<price * 1000>-<latitude>-<longitude>\n")

print("To add information: ")
print("P-<fuel type>-<search radius>-<center latitude>-<center longitude>\n\n")

msg = input("Enter the desired operation and data: ")

while True:
    if msg == 'h' or msg == 'H':
        print("To add information: ")
        print("D-<fuel type>-<price * 1000>-<latitude>-<longitude>\n")
        print("To add information: ")
        print("P-<fuel type>-<search radius>-<center latitude>-<center longitude>\n\n")

    elif msg != "stop":
        udp.sendto(bytes(msg, "utf-8"), dest)

        try:
            udp.settimeout(2)
            msg, server = udp.recvfrom(1024)
            print("Server: ",msg.decode("utf-8"))
        except socket.timeout:
            print("Timed out. Sending message again...")
            udp.sendto(bytes(msg, "utf-8"), dest)

        msg = input("Enter the desired operation and data: ")
        
    else:
        udp.close()
        break
