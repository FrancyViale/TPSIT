#from Packet import packet
from socket import socket, AF_INET, SOCK_DGRAM

def chat_client():
    receiver = ("127.0.0.1", 5000)
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.sendto("ciao".encode(), receiver)
        print("Messaggio inviato")

if _name_ == "_main_":
    chat_client()