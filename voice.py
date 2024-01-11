from utils import *

def rec_audio():
    while True:
        voice = sd.rec(frames=None, samplerate=samplerate, blocking=False)
        return voice

def play_audio(audio):   # Get audio data from RTP.
    while True:
        sd.play(data=audio, samplerate=samplerate, blocking=False)