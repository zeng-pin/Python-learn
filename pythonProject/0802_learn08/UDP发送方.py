from socket import socket,AF_INET,SOCK_DGRAM

#创建socket对象
send_socket=socket(AF_INET,SOCK_DGRAM)
#2.准备发送数据
data=input('输入要发送的数据: ')
#指定接收方的IP地址与端口
ip_port=(('127.0.0.1',8888))
#4.发送数据
send_socket.sendto(data.encode('utf-8'),ip_port)
#5.接受回复数据
recv_data,addr=send_socket.recvfrom(1024)
print('接受的数据是: ',recv_data.decode('utf-8'))
#6.关闭socket对象
send_socket.close()