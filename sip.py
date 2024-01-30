from utils import *

def create_call_id():   # Create 32bit call identifier.
    return random.getrandbits(32)

def create_branch():    # Create 8bit branch identifier.
    return "z9hG4bK"+str(random.getrandbits(8))

def send_sip(destination_ip:str, destination_port:int):
    print("...")
    sip_request = (
        f"INVITE sip:destination@{destination_ip}:{r_port} SIP/2.0\r\n"
        f"Via: SIP/2.0/UDP {self_ip}:{r_port};branch={create_branch()}\r\n"
        f"Max-Forwards: 70\r\n"
        f"To: <sip:destination@{destination_ip}:{r_port}>\r\n"
        f"From: <sip:sender@{self_ip}:{t_port}>;tag=123456\r\n"
        f"Call-ID: {create_call_id()}@{self_ip}\r\n"
        f"CSeq: 1 INVITE\r\n"
        f"Contact: <sip:sender@{self_ip}:{port}>\r\n"
        f"Content-Type: application/sdp\r\n"
        f"Content-Length: 0\r\n\r\n"
    )
    try:
        transmit_sock.sendto(sip_request.encode(), (destination_ip, r_port))
        response, addr = receive_sock.recvfrom(4096)
        print(f"Received response from {addr}:\n{response.decode()}")
    
    except socket.error as e:
        print(f"Error: {e}")

def receive_sip():
    while True:
        try:
            data, client_address = receive_sock.recvfrom(4096)
            print(f"Received SIP request from {client_address}:\n{data.decode()}")
            
            responses = [
                "SIP/2.0 100 Trying\r\n...\r\n",
                "SIP/2.0 180 Ringing\r\n...\r\n",
                "SIP/2.0 200 OK\r\n...\r\n"
            ]
            
            for response in responses:
                transmit_sock.sendto(response.encode(), client_address)

        except socket.error as e:
            print(f"Error: {e}")
