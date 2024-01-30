from utils import *

transmit_voice = False
duration = 10

def prompt(client_addr):
    accept = input(f"Incoming call from: {client_addr} \nAccept? Y/N: ").capitalize()
    if accept == "Y": return True
    elif accept == "N": return False

def transmit_data(t_data):
    transmit_sock.sendto(t_data.encode(), destination_addr)

def receive_data():
    r_data, client_addr = receive_sock.recvfrom(4096)

    if "HELLO" in r_data:
        if prompt(client_addr) == True:
            transmit_data("OKAY")
        else: transmit_data("BYE")

    if "OKAY" in r_data:
        transmit_voice = True
        transmit_data("OKAY")

    if "BYE" in r_data:
        transmit_voice = False
        transmit_data("BYE")

while transmit_voice == True:
    audio = sd.rec(
        int(duration * samplerate),
        samplerate = samplerate,
        channels = 1,
        dtype = "int16"
    )
    sd.wait()
