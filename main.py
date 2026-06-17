import socket
import threading
from queue import Queue

target = input("Enter the ip = ")
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False 

def fill_queue(from_port)