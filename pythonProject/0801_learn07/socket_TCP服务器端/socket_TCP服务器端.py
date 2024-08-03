from socket import socket,AF_INET,SOCK_STREAM
#AF_INET 用于Internet间的通信
#SOCK_STREAM表示的是TCP协议编程

#1.创建socket对象
server_socket=socket(AF_INET,SOCK_STREAM)
#2.绑定IP地址和端口
ip='127.0.0.1'
port=8888  #端口的范围
server_socket.bind((ip,port))
#3.使用listen()开始监听
server_socket.listen(5)
print('服务器已经启动')
#4.等待客户端的链接
client_socket,client_addr=server_socket.accept()#系列解包赋值
#5.接受客户端数据
date=client_socket.recv(1024)
print(type(date),'客户端发送的数据为: ',date.decode('utf-8'))#客户端的数据使用utf-8进行解码
#关闭服务器
server_socket.close()

