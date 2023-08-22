import sys
from datetime import datetime
import socket

#set argument
if len(sys.argv) == 2:
    host= socket.gethostbyname(sys.argv[1]) #transfer host name into ip address
else:
    print("syntax error")
    print("syntax is: python3 scanner.py <Ip>")
print('\n')
#banner
print('*' * 50)
print('target IP: '+ host)
print(datetime.now())
print('*' * 50)
print('\n')

try:
    for port in range(20,1024):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result= s.connect_ex((host, port))
        if result == 0:
            print(f'port {port} is open')
        else:
            print(f"{port} close")
        s.close()
except KeyboardInterrupt:
    print('\nexiting')
    sys.exit()
except socket.gaierror:
    print("hostname not resdolved")
    sys.exit()
except socket.error:
    print("target host is offline")
    sys.exit()
