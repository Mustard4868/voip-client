import socket
import threading
import sqlite3
import sounddevice as sd
import numpy as np

self_ip = socket.gethostbyname(socket.gethostname())
destination_ip = "127.0.0.1"
port = 5000

samplerate = 48000