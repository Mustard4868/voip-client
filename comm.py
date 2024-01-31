from utils import *
import numpy as np

center_freq = 100
bandwidth = 10
class NotchFilter:
    def __init__(self, center_freq, bandwidth, sampling_rate):
        self.center_freq = center_freq
        self.bandwidth = bandwidth
        self.sampling_rate = sampling_rate

    def apply_filter(self, signal):
        # Calculate normalized frequency parameters
        center_freq_normalized = self.center_freq / (0.5 * self.sampling_rate)
        bandwidth_normalized = self.bandwidth / (0.5 * self.sampling_rate)
        # Generate frequency axis
        freq_axis = np.fft.fftfreq(len(signal), d=1.0 / self.sampling_rate)
        # Create a notch filter kernel
        filter_kernel = np.ones_like(freq_axis)
        notch_indices = np.where(np.abs(freq_axis - center_freq_normalized) < bandwidth_normalized)
        filter_kernel[notch_indices] = 0.0
        # Apply the notch filter in the frequency domain
        signal_spectrum = np.fft.fft(signal)
        filtered_spectrum = signal_spectrum * filter_kernel
        # Inverse transform to get the filtered signal
        filtered_signal = np.fft.ifft(filtered_spectrum).real
        return filtered_signal


def transmit_voice():
    audio_data = sd.rec(
        int(duration * samplerate),
        samplerate = samplerate,
        channels = 1,
        dtype = "int16"
    )
    sd.wait()


    notch_filter = NotchFilter(center_freq, bandwidth, samplerate)
    filtered_audio_data = notch_filter.apply_filter(audio_data.flatten())  #addednotch


    for i in range(0, len(filtered_audio_data), buffer):
        chunk = filtered_audio_data[i:i+buffer]
        transmit_sock.sendto(chunk.tobytes(), destination_addr)

transmit_voice_thread = threading.Thread(target=transmit_voice)

duration = 10
buffer = 4096

def prompt(client_addr):
    accept = input(f"Incoming call from: {client_addr} \nAccept? Y/N: ").capitalize()
    if accept == "Y": return True
    elif accept == "N": return False

def transmit_data(t_data, addr):
    dest_ip = list(addr)[0]
    dest_addr = (dest_ip, r_port)
    transmit_sock.sendto(t_data.encode(), dest_addr)

def receive_data():
    i = 0
    notch_filter = NotchFilter(center_freq, bandwidth, samplerate)

    while True:
        r_data, client_addr = receive_sock.recvfrom(4096)
        d_data = r_data.decode()

        if "HELLO" in d_data:
            print(f"@{client_addr}: {d_data}")
            if prompt(client_addr) == True:
                transmit_data("OKAY", client_addr)
            else:
                transmit_data("BYE", client_addr)

        elif "OKAY" in d_data:
            print(f"@{client_addr}: {d_data}")
            if i != 0:
                pass
            else:
                transmit_data("OKAY", client_addr)
                transmit_voice_thread.start()
                i = 1

        elif "BYE" in d_data:
            print(f"@{client_addr}: {d_data}")
            if i == 0:
                pass
            else:
                transmit_data("BYE", client_addr)
                transmit_voice_thread.join()
                i = 0

        else:
            #####################notchfilter
            filtered_audio_data = notch_filter.apply_filter(np.frombuffer(r_data, dtype=np.int16))

            ######filteredaudio
            play_audio(filtered_audio_data.tobytes(), samplerate)
def play_audio(data, samplerate):
    audio = np.frombuffer(data, dtype=np.int16)
    sd.play(audio, samplerate=samplerate)
    sd.wait()

if self_ip != destination_ip:
    msg = "HELLO"
    transmit_sock.sendto(msg.encode(), destination_addr)
