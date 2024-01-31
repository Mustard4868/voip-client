from utils import *

def transmit_voice():
    audio_data = sd.rec(
        int(duration * samplerate),
        samplerate = samplerate,
        channels = 1,
        dtype = "int16"
    )
    sd.wait()

    for i in range(0, len(audio_data), buffer):
        chunk = audio_data[i:i+buffer]
        transmit_sock.sendto(chunk.tobytes(), destination_addr)

transmit_voice_thread = threading.Thread(target=transmit_voice)

duration = 10
buffer = 4096

def prompt(client_addr):
    accept = input(f"Incoming call from: {client_addr} \nAccept? Y/N: ").capitalize()
    if accept == "Y": return True
    elif accept == "N": return False

def transmit_data(t_data):
    transmit_sock.sendto(t_data.encode(), destination_addr)

def receive_data():
    r_data, client_addr = receive_sock.recvfrom(4096)
    d_data = r_data.decode()

    if "HELLO" in d_data:
        print(f"@{client_addr}: {d_data}")
        if prompt(client_addr) == True:
            transmit_data("OKAY")
        else: transmit_data("BYE")

    elif "OKAY" in d_data:
        print(f"@{client_addr}: {d_data}")
        transmit_voice_thread.start()
        transmit_data("OKAY")

    elif "BYE" in d_data:
        print(f"@{client_addr}: {d_data}")
        transmit_voice_thread.join()
        transmit_data("BYE")
    
    else:
        play_audio(r_data)

def play_audio(data, samplerate):
    audio = np.frombuffer(data, dtype=np.int16)
    sd.play(audio, samplerate=samplerate)
    sd.wait()

if self_ip != "192.168.2.167":
    transmit_data("HELLO")
