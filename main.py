from sip import send_sip, receive_sip
from utils import *

def main():

    transmit = threading.Thread(target=send_sip)
    transmit.start()
    
    receive = threading.Thread(target=receive_sip)
    receive.start()

if __name__ == "__main__":
    main()
