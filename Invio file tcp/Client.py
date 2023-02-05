from Packet import Packet
from socket import socket, AF_INET, SOCK_DGRAM

BUFSIZE = 10

def invia_file(sock):
    with open("miofile.txt", "rb") as f:
        finito = False
        sock.sendto(Packet(b'', Packet.INIZIO).to_bytes())
        while not finito:
            dati = f.read(BUFSIZE)
            if not dati:
                sock.sendto(Packet(dati, Packet.CONTINUA).to_bytes(), dest)
            else:
                finito = True
        sock.sendto(Packet(b'', Packet.FINE).to_bytes(), dest)

def main():
    dest = ('127.0.0.1', 5000)
    with socket(AF_INET, SOCK_DGRAM) as s:
        invia_file(s, dest)

if __name__ == "__main__":
    run_server()