from sip import send_sip, receive_sip
from utils import *

def main():

    send = multiprocessing.Process(target=send_sip, args=(destination_ip, port))
    send.start()
    send.join()

    receive = multiprocessing.Process(target=receive_sip)
    receive.start()
    receive.join()

if __name__ == "__main__":
    main()