import threading

class voipThreads(object):

    def __init__(self):

        self.recieve = threading.Thread(target = receive_data)
        self.transmit = threading.Thread(target = transmit_data)
