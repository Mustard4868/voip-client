from utils import voipThreads, voipSockets

def main():

    voipThreads().recieve.start()

if __name__ == "__main__":
    main()
