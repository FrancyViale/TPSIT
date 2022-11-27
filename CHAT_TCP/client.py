#from Packet import packet
from socket import socket, AF_INET, SOCK_STREAM

def chat_client():
    receiver = ("127.0.0.1", 5000)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)
        running = True
        while running:
            messaggio = input('Inserisci il messaggio che vuoi inviare: ')
            s.send(messaggio.encode())
            if messaggio == "fine":
                running = False
            else:
                print("Messaggio inviato")

if __name__ == "__main__":
    chat_client()