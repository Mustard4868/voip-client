import socket
import threading
import sqlite3
import sounddevice as sd
import numpy as np
import random

samplerate = 44100

self_ip = socket.gethostbyname(socket.gethostname())
destination_ip = "192.168.0.100"
server_ip = "192.168.1.254"
port = 5000

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((self_ip, port))
#udp_socket.settimeout(5)