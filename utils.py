""" Import modules. """
import socket
import random
import threading

""" Global variables. """
port = 5060
self_ip = socket.gethostbyname(socket.gethostname())

""" Port configuration. """
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp_sock.bind((self_ip, port))
udp_sock.connect((self_ip, port))
print(f"Connected to: {udp_sock.getsockname()}")