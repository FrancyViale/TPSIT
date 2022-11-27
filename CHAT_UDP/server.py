#from Packet import packet
from socket import socket, AF_INET, SOCK_DGRAM

MAX_SIZE = 7000

def chat_server():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind(("0.0.0.0", 5000))
        print("In ascolto")
        msg = s.recvfrom(MAX_SIZE)
        msg = msg.decode('utf-8')
        print(msg)        
        
if _name_ == "_main_":
    chat_server()