from send import send_sip_request
from receive import receive_sip_request

from utils import *

send_thread = threading.Thread(send_sip_request())
receive_thread = threading.Thread(receive_sip_request())

send_thread.start()
receive_thread.start()

send_thread.join()
receive_thread.join()