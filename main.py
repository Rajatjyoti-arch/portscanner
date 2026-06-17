import socket 

target = input("Enter the ip = ")
    
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        sock.connect((target, port))
        return true