import sqlite3
import threading
import socket
import random

self_ip = socket.gethostbyname(socket.gethostname())

con = sqlite3.connect("voip-database.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS calls (call_id PRIMARY KEY INT, data BLOB)
""")

def create_call_id():
    return random.randbytes(32)

def transmit(data, dest_ip):
    transmit_socket.sendto(data, (dest_ip, 5060))
    
def receive():
    data, client_addr = receive_socket.recvfrom(4096)
    
    decoded_data = data.decode()
    fields = decoded_data.split()

    dest_ip = fields[1]
    t_data = fields[2]

    transmit(t_data.encode(), dest_ip)

# HEADER = "IP_ADDRESS|DATA"
    
transmit_thread = threading.Thread(target=transmit)
receive_thread = threading.Thread(target=receive)

transmit_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

receive_port = 5060
transmit_port = 23456

receive_socket.bind((self_ip, receive_port))
transmit_socket.bind((self_ip, transmit_port))