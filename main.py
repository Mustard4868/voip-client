from utils import *

class voipThreads(object):

    def __init__(self):

        self.recieve = threading.Thread(target = receive_data)
        self.transmit = threading.Thread(target = transmit_data)


def main():

    voipThreads().recieve.start()

if __name__ == "__main__":
    main()


