# _*_ coding:utf-8 _*_
import socket
import sys

host = 'localhost'
port = 8000
	
	
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 括号内变量分别为地址族及UDP传输控制协议
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

s.bind((host,port)) #绑定端口
print '创建中...'

f = open('diary.txt','a+')
print f.read()
	
data = s.recvfrom(1024)
print "sending:"+str(data)
s.sendto(str(data),(host,port))
s.close()
	





	


	

