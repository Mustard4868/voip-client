from sip import send_sip_request, receive_sip_request

from utils import *

def main():

    send_thread = threading.Thread(send_sip_request())
    receive_thread = threading.Thread(receive_sip_request())

    send_thread.start()
    receive_thread.start()

    send_thread.join()
    receive_thread.join()

if __name__ == "__main__":
    main()