from socket import AF_INET, SOCK_STREAM, socket
HOST = "0.0.0.0"
PORT = 5000


def chatServer(host, port):
    with socket (AF_INET, SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            client, client_address = s.accept() # retituisce la tupla del socket destinatario
            #3wh con il client
            msg = client.recv(1024).decode('utf-8') # resituisce null o bites (niente, interpretare)
            print(msg)
        
if __name__ == "__main__":
    chatServer(HOST, PORT)