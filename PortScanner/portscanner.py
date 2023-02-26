import socket

hedef = '127.0.0.1'
min_port = 1
max_port = 65535

for port in range(min_port, max_port+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)  
    sonuc = sock.connect_ex((hedef, port))
    if sonuc == 0:
        print(f"Port {port} açık")
    sock.close()