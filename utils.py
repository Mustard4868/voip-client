import socket
import threading
import sqlite3

self_ip = socket.gethostbyname(socket.gethostname())
self_port = 5061
destination_port = 5060