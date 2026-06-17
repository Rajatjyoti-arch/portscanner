import socket
import threading
from queue import Queue

target = input("Enter the ip = ")
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Add a timeout so it doesn't hang for minutes on closed/filtered ports
        sock.settimeout(1)
        sock.connect((target, port))
        return True
    except:
        return False
    finally:
        # Always close the socket
        sock.close()

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for i in range(50): 
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("The open ports are = ", open_ports)
