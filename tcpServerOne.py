from socket import *


tcpSocket = socket(AF_INET, SOCK_STREAM)
# mcAddr = ("127.0.0.1", 5656)
tcpSocket.bind(("127.0.0.1", 5656))
tcpSocket.listen(5)
print("服务器开启...")

try:
    while True:
        print("服务等待中...")
        conn,addr = tcpSocket.accept()
        print("服务正在进行...")
        while True:
            recvData = conn.recv(1024)
            if len(recvData) > 0:
                print(recvData.decode('gb2312'))
                sendData = input("请输入回复消息：")
                conn.send(sendData.encode("gb2312"))
            else:
                conn.close()
                print("本次服务关闭...")
except Exception:
    tcpSocket.close()
    print("服务器关闭...")