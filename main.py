from sip import send_sip, receive_sip
from utils import *
import numpy as np
from noisereduce import reduce_noise


def filter_audio(input_audio):
    reduced_audio = reduce_noise(input_audio)
    return reduced_audio


def main():

    transmit = threading.Thread(target=send_sip)
    transmit.start()
    
    receive = threading.Thread(target=receive_sip)
    receive.start()

if __name__ == "__main__":
    main()
