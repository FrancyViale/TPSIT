from Packet import packet
from socket import socket, AF_INET, SOCK_STREAM

MAX_SIZE = 7000

def chat_server():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 5000))
        s.listen()
        print("In ascolto")
        client, client_address = s.accept() #client_address valore 0 ip valore 1 porta 
        msg = client.recv(MAX_SIZE)
        msg = packet.from_bytes(msg)
        print(msg)        
        
if __name__ == "__main__":
    chat_server()