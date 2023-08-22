#importing in python

import sys #system function and parameter
from datetime import datetime as dt #import with alias
print(sys.version)
print(dt.now())

import socket #importing socket module

host='192.168.1.129'
port= 1234
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET for ipv4 & SOCK_STREAM for TCP port number
s.connect((host, port)) #.connect is used to connect