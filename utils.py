import socket
import threading

self_ip = socket.gethostbyname(socket.gethostname())
self_port = 5061
destination_port = 5060