""" Import modules. """
import socket
import random
import threading
import wave
import numpy as np
import sounddevice as sd

""" Global variables. """

receive_thread = threading.Thread(target=receive_data)
voice_thread = threading.Thread(target=transmit_voice)

samplerate = 44100

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
