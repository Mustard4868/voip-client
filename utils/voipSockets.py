import socket

class voipSockets(object):

    def __init__(self):

        self.UDP_IN = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.UDP_OUT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.TCP_IN = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.TCP_OUT = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def set_destination(sock: object, ip: str, port: int):
        if sock not in voipSockets:
            raise Exception({sock}," does not exist.")
        else:
            sock.bind((ip, port))
