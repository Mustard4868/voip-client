from utils import *

def send_sip_request(destination_ip, destination_port):
    sip_request = (
        f"INVITE sip:destination@example.com SIP/2.0\r\n"
        f"Via: SIP/2.0/UDP {self_ip}:{self_port};branch=z9hG4bK123456\r\n"
        f"Max-Forwards: 70\r\n"
        f"To: <sip:destination@example.com>\r\n"
        f"From: <sip:sender@example.com>;tag=123456\r\n"
        f"Call-ID: 789@{self_ip}\r\n"
        f"CSeq: 1 INVITE\r\n"
        f"Contact: <sip:sender@{self_ip}:{self_port}>\r\n"
        f"Content-Type: application/sdp\r\n"
        f"Content-Length: 0\r\n\r\n"
    )

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(5)

    try:
        udp_socket.sendto(sip_request.encode(), (destination_ip, destination_port))

        response, addr = udp_socket.recvfrom(4096)
        print(f"Received response from {addr}:\n{response.decode()}")
    
    except socket.error as e:
        print(f"Error: {e}")

    finally:
        udp_socket.close()

destination_ip = input("IP: ")
send_sip_request(destination_ip, destination_port)
