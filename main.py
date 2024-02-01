from utils import *

class voipThreads:
    def __init__(self):

        receive = threading.Thread(target = receive_data).start()


def main():
    
    voipThreads.receive.start()

if __name__ == "__main__":
    main()