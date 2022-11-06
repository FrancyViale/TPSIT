from socket import AF_INET, SOCK_DGRAM, socket
from packet import Packet
import time

def run_client():
    receiver = ("127.0.0.1", 5000)
    with socket(AF_INET, SOCK_DGRAM) as s:
        with open("input.pdf", "rb") as f:
            s.sendto(Packet(Packet.NEW_FILE, b))
            