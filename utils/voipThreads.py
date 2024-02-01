import threading

class voipThreads:

    def __init__(self):

        self.recieve = threading.Thread()
        self.transmit = threading.Thread()
