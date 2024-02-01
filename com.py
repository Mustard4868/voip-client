from utils import *
import socket

def recieve_data():
    data, addr = voipSockets.UDP_IN.recvfrom(4096)