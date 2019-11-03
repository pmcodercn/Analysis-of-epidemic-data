from socket import *
import struct


addrHost = ''
fileName = ''
ackNum = 1

def getTftpInfo():
    global addrHost, fileName # 引用全局变量
    addrHost = input("请输入Tftp服务器IP：")
    fileName = input("请输入下载的文件名称：")
    pass

def main():
    getTftpInfo()
    global addrHost, fileName,ackNum
    udpSocket = socket(AF_INET, SOCK_DGRAM) # 创建udp套接字对象
    udpSocket.bind(("192.168.1.114", 8080)) # 绑定ip和端口号
    print("本机端口已绑定.....")

    sendData = struct.pack('!H%dsb5sb'%len(fileName),1, fileName.encode('gb2312'),0,'octet'.encode('gb2312'), 0 )
    #sendData = str((1, fileName,'octet', 0 ))
    sendAddr = (addrHost, 69)
    print("下载请求数据已封装.....")

    udpSocket.sendto(sendData, sendAddr) # 发送tftp请求
    print("下载请求已发送.....")
    print("等待数据中.....")


    localFileName = open("C:/Users/田海龙/Desktop/PyTest/"+fileName,'wb')
    print("创建本地文件...")

    while True:
        recvData, recvAddr = udpSocket.recvfrom(1024)
        print("获取数据.....")
        print(recvData)
        packetOpt = struct.unpack('!h', recvData[:2])
        packetNum = struct.unpack('!h', recvData[2:4])
        print(packetOpt)
        print(packetNum)
        print("解包...")
        # 判断当前接受数据类型
        if packetOpt[0] == 3: # 如果操作码为3，则开始下载
            
            if len(recvData) < 516:
                print("文件下载完毕.....")
                break
            else:
                if ackNum == packetNum[0]:
                    localFileName.write(recvData[4:])
                    print("保存数据中.....")
                    ackNum = ackNum + 1
                    sendAck = struct.pack("!HH", 4,packetNum[0])
                    udpSocket.sendto(sendAck,recvAddr)
                    print("返回ACK数据包...")
                if ackNum == 65536:
                    ackNum = 0
            # sendAck = str((4,recvData[0]))
                
            
        elif packetOpt[0] == 5: # 如果操作码为5，则表示文件不存在。
            print("没有您指定的文件.....")
            break
        else:
            print("其他错误.....")
            break

    localFileName.close()


if __name__ == "__main__":
    main()