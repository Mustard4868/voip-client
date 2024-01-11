from utils import *

def create_call_id():   # Create 32bit call identifier.
    return random.getrandbits(32)

def create_branch():    # Create 8bit branch identifier.
    return str("z9hG4bK"+random.getrandbits(8))

def send_sip_request(destination_ip, destination_port):
    sip_request = (
        f"INVITE sip:destination@{destination_ip}:{port} SIP/2.0\r\n"
        f"Via: SIP/2.0/UDP {self_ip}:{port};branch={create_branch()}\r\n"
        f"Max-Forwards: 70\r\n"
        f"To: <sip:destination@{destination_ip}:{port}>\r\n"
        f"From: <sip:sender@{self_ip}:{port}>;tag=123456\r\n"
        f"Call-ID: {create_call_id()}@{self_ip}\r\n"
        f"CSeq: 1 INVITE\r\n"
        f"Contact: <sip:sender@{self_ip}:{port}>\r\n"
        f"Content-Type: application/sdp\r\n"
        f"Content-Length: 0\r\n\r\n"
    )
    try:
        udp_socket.sendto(sip_request.encode(), (destination_ip, destination_port))

        response, addr = udp_socket.recvfrom(4096)
        print(f"Received response from {addr}:\n{response.decode()}")
    
    except socket.error as e:
        print(f"Error: {e}")

def accept(client_address):
    reply = input(f"Incoming call from {client_address}. Accept? Y/N")
    if reply.capitalize() == "Y":
        return True
    elif reply.capitalize() == "N":
        return False
    else:   # Prompt user again if incorrect input was given.
        accept()

def receive_sip_request(self_ip, port):

    print(f"Listening to {self_ip}:{port}")

    while True:
        try:
            data, client_address = udp_socket.recvfrom(4096)
            print(f"Received SIP request from {client_address}:\n{data.decode()}")
            
            response = "SIP/2.0 200 OK\r\n...\r\n"
            udp_socket.sendto(response.encode(), client_address)

            x = accept(client_address)
            if x == True:
                response = "SIP/2.0 ACK\r\n...\r\n"
                udp_socket.sendto(response.encode(), client_address)
            elif x == False:
                response = "SIP/2.0 603 Decline\r\n...\r\n"
                udp_socket.sendto(response.encode(), client_address)

        except socket.error as e:
            print(f"Error: {e}")