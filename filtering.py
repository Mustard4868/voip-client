from pydub import AudioSegment
import numpy as np
from utils import *

def captured_audio():
    chunksize = 4096
    #sampling rate is 44100
    pydubaudio = pyaudo.PyAudio()
    stream = pydubaudio.open(format=pyaudio.paInt16,
                channels=1,
                samplerate=samplerate,
                input=True,
                frames_per_buffer=chunksize)
    
    audio_data = []
    captureactivity = True

    while captureactivity:
            data = recorddata.read(chunksize)
            audio_data.append(np.frombuffer(data, dtype=np.int16)

                  
    stream = stop_stream()
    stream.close()
    pydubaudio.terminate()
    captured_audio = np.concatenate(audio_data)
    audio_segment = AudioSegment(captured_audio.tobytes(), sample_width=captured_audio.dtype.itemsize, frame_rate=samplerate, channels=1)

    
    ####APPLYING LOWPASS FILTER
    filtered_audio = audio_segment.low_pass_filter(1000)
    filtered_audionump = np.array(filtered_audio.get_array_of_samples(), dtype=np.int16)
    return filtered_audioumnp


CAPTURED_FILTERED = captured_audio()
