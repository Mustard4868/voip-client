from comm import receive_data, transmit_voice, play_audio
from utils import *

def main():

    receive_thread = threading.Thread(target=receive_data)
    voice_thread = threading.Thread(target=transmit_voice)
    playback_thread = threading.Thread(target=play_audio)

    receive_thread.start()
#   voice_thread.start() called by receive_data()
#   playback_thread.start() called by receive_data()

if __name__ == "__main__":
    main()
