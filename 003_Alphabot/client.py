from socket import AF_INET, SO_BROADCAST, SOCK_STREAM, socket

def chatClient():
    with socket (AF_INET, SOCK_STREAM) as s:
        s.connect(("192.168.0.129", 5000))
        s.send("avanti".encode('utf-8'))

if __name__ == "__main__":
    chatClient()