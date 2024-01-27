""" Import modules. """
import socket
import random
import threading
import multiprocessing

""" Global variables. """
port = 5060
self_ip = socket.gethostbyname(socket.gethostname())

destination_ip = "192.168.2.167"

""" Port configuration. """
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp_sock.bind((self_ip, port))
udp_sock.connect((self_ip, port))
print(f"Connected to: {udp_sock.getsockname()}")