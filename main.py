from sip import send_sip_request, receive_sip_request
from utils import *

def main():

    receive_sip_request_thread = threading.Thread(target=receive_sip_request(self_ip, port))
    receive_sip_request_thread.start()

if __name__ == "__main__":
    main()