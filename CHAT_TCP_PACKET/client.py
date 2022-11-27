from Packet import packet
from socket import socket, AF_INET, SOCK_STREAM

def chat_client():
    receiver = ("127.0.0.1", 5000)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)
        msg = input('Inserisci il messaggio che vuoi inviare')
        s.send(packet.to_bytes(msg))
        print("Messaggio inviato")

if __name__ == "__main__":
    chat_client()