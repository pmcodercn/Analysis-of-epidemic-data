from socket import *


tcpSocket = socket(AF_INET,SOCK_STREAM)
# tcpSocket.bind("192.168.1.114",8686)
tcpSocket.connect(("192.168.1.125",8080))
tcpSocket.send("你好!".encode("gb2312"))
racvData = tcpSocket.recv(1024)
print(racvData)