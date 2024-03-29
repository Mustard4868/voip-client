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

def transmit_data(t_data, addr):
    dest_ip = list(addr)[0]
    dest_addr = (dest_ip, r_port)
    transmit_sock.sendto(t_data.encode(), dest_addr)

def receive_data():
    i = 0
    while True:
        r_data, client_addr = receive_sock.recvfrom(4096)
        d_data = r_data.decode()

        if "HELLO" in d_data:
            print(f"@{client_addr}: {d_data}")
            if prompt(client_addr) == True:
                transmit_data("OKAY", client_addr)
            else: transmit_data("BYE", client_addr)

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
            play_audio(r_data)

def play_audio(data, samplerate):
    audio = np.frombuffer(data, dtype=np.int16)
    sd.play(audio, samplerate=samplerate)
    sd.wait()

if self_ip != destination_ip:
    msg = "HELLO"
    transmit_sock.sendto(msg.encode(), destination_addr)
