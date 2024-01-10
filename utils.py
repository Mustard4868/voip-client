import socket
import threading
import sqlite3

self_ip = socket.gethostbyname(socket.gethostname())
destination_ip = "127.0.0.1"
port = 5000