# _*_ coding: utf-8 _*_
import socket
import sys

s =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
host = 'localhost'
port = 8000

message= raw_input(">")

s.sendto(message,(host,port))

print 'socket created'
data = s.recv(2014)
print 'Received from server:'+ str(data)
	
s.close()



