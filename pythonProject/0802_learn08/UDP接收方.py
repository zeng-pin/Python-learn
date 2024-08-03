from socket import socket,AF_INET,SOCK_DGRAM
#1.创建socket对象
recv_socket=socket(AF_INET,SOCK_DGRAM)
#2.绑定IP与端口
recv_socket.bind(('127.0.0.1',8888))
#3.接受发送方数据
recv_data,address=recv_socket.recvfrom(1024)
print('接受到的数据是: ',recv_data.decode('utf-8'))
#准备回复数据
data=input('输入回复数据: ')
recv_socket.sendto(data.encode('utf-8'),address)
#关闭socket对象
recv_socket.close()
