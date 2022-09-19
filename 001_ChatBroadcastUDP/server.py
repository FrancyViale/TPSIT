from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE =1024

mystr = "ciao" # str
# bytes

HOST = "0.0.0.0"
PORT = 5000
# possibilità
# localhost 127.0.0.1

def chatServer():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        msg = s.recvfrom(BUFFER_SIZE)
        print(msg)
        msg = msg.decode('utf8')
        print(msg)
        

if __name__ == "__main__":
        chatServer()