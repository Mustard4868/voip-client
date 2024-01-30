from pydub import AudioSegment
import numpy as np
from utils import *

def capturing_audio():
    chunksize = 4096
    #sampling rate is 44100
    Paudio = pyaudo.PyAudio()
    recorddata = Paudio.open(format=pyaudio.paInt16,
                channels=1,
                rate=sample_rate,
                input=True,
                frames_per_buffer=chunk_size)
    

data = []
data.append(np.random.rand(44100))
i = 0
def filter_audio(data):
    filtered_data = []
    for audio_segment in data:
        audio_segment = AudioSegment(audio_segment.tobytes(), sample_width=audio_segment.dtype.itemsize, frame_rate=44100, channels=1)
        filtered_audio = audio_segment.low_pass_filter(1000)
        filteredaudionump = np.array(filtered_audio.get_array_of_samples(), dtype=np.float32)
        filtered_data.append(filteredaudionump)
    return filtered_data

filtered_data = filter_audio(data)
 #print(filtered_data)

