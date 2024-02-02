import socket
self_ip = socket.gethostbyname(socket.gethostname())

class voipSockets(object):

    TCP_IN = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_OUT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    UDP_IN = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_OUT = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self):
        self.TCP_IN.bind((self_ip, 1234))
        self.TCP_OUT.bind((self_ip, 1235))
        self.UDP_IN.bind((self_ip, 1236))
        self.UDP_OUT.bind((self_ip, 1237))

while True:
    voipSockets.TCP_OUT.sendto("HELLO".encode(), ((self_ip, 1234)))
    data, addr = voipSockets.TCP_IN.recvfrom(0)
    print(data.decode())