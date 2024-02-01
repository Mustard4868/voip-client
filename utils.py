""" Import modules. """
import threading
import pyaudio
import socket

""" Global variables. """
self_ip = socket.gethostbyname(socket.gethostname())

""" Define sockets. """
class voipSockets(object):

    def __init__(self):
        self.UDP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.TCP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
