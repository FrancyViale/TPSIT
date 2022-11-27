#from Packet import packet
from socket import socket, AF_INET, SOCK_STREAM

MAX_SIZE = 7000

ADDRESS = (("0.0.0.0", 5000))

def chat_server():
            
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(ADDRESS)
        s.listen()
        print("In ascolto")
        client, client_address = s.accept()
        running = True
        while running:
            msg = client.recv(MAX_SIZE)
            msg = msg.decode('utf-8')
            if msg == "fine":
                running = False
            else:
                print(msg)        
        
if __name__ == "__main__":
    chat_server()