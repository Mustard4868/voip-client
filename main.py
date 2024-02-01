from utils import *

def receive_data():
    # create function to receive data using socket
    print("Data")

class voipThreads(object):

    def __init__(self):

        self.recieve = threading.Thread(target = receive_data)


def main():

    voipThreads().recieve.start()

if __name__ == "__main__":
    main()