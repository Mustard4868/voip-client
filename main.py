from utils import *
from comm import receive_data, transmit_data, transmit_voice

receive_data_thread = threading.Thread(target=receive_data)
transmit_data_thread = threading.Thread(target=transmit_data)

def main():

    receive_data_thread.start()

if __name__ == "__main__":
    main()
