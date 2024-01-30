""" Import modules. """
import socket
import random
import threading

""" Global variables. """

transmit_voice = False # Indicator for audio recording and playback.

r_port = 5060
t_port = 23456
self_ip = socket.gethostbyname(socket.gethostname())

destination_ip = "192.168.2.167"
destination_addr = (destination_ip, r_port)

""" Port configuration. """
receive_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive_sock.bind((self_ip, r_port))

transmit_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
transmit_sock.bind((self_ip, t_port))
