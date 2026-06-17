import socket 

target = input("Enter the ip = ")
    
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False 

for port in range(1, 1024):
    result = portscan(port)
    if result == True:
        print("Port " , port , " is open")
         