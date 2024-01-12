import socket
import threading
import sqlite3
import sounddevice as sd
import numpy as np
import random

samplerate = 44100

""""""

self_ip = socket.gethostbyname(socket.gethostname())
destination_ip = "192.168.0.99"# input("Destination IP: ")
server_ip = "192.168.1.254"

send_port = 5000
receive_port = 5100

port = receive_port # Contact information SIP

send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

send_socket.bind((self_ip, send_port))
print(f"Initialized {send_socket}.")

receive_socket.bind((self_ip, receive_port))
print(f"Initialized {receive_socket}.")

receive_socket.listen(1)
print("Succes.")