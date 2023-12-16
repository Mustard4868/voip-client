from utils import *

def receive_sip_request(self_ip, self_port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    udp_socket.bind((self_ip, self_port))

    print(f"Server listening on {self_ip}:{self_port}")

    while True:
        try:
            data, client_address = udp_socket.recvfrom(4096)
            print(f"Received SIP request from {client_address}:\n{data.decode()}")
            
            response = "SIP/2.0 200 OK\r\n...\r\n"
            udp_socket.sendto(response.encode(), client_address)

        except socket.error as e:
            print(f"Error: {e}")

    udp_socket.close()

receive_sip_request(self_ip, self_port)