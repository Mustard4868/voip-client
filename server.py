from utils import socket, sqlite3, self_ip, port, udp_socket
import sqlite3
from datetime import datetime

#udp_socket.listen(1)
print(f"Server listening on: {self_ip}:{port}.")

class database():
    def __init__(self):

        self.insert_data = insert_data()

        con = sqlite3.connect("voip-database.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS voip-data (call_id INTEGER PRIMARY KEY, timestamp TEXT, payload BLOB, filtered INTEGER)""")

        def insert_data(data):
            query = """INSERT INTO voip-data (call_id, timestamp, payload, filtered) VALUES (?, ?, ?, ?)"""
            cur.execute(query, data)

def main():
    while True:
        try:
            data, client_addr = udp_socket.recvfrom(4096).decode
            print(data)

            dest_addr = "127.0.0.1" # Get destination IP from SIP header.

            """ !!! EXTRACT RTP PAYLOAD AND INSERT INTO DB !!! """

            call_id = () # Extract call_id from SIP header
            timestamp = datetime.now() # Log only on start (and potentially end for duration calculations.)
            payload = () # Payload from RTP.
            filtered = False # Check if filtered or unfiltered for statistics.

            db_data = (call_id, timestamp, payload, filtered)
            database.insert_data(db_data)

            udp_socket.sendto(data, dest_addr)

        except socket.error as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()