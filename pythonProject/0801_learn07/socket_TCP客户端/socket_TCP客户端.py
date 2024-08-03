import socket
#1.创建socket对象
client_socket=socket.socket()
#2.IP地址和主机接口
ip='127.0.0.1'
port=8888
client_socket.connect((ip,port))
print('------与服务器端链接成功------')
#3.发送数据
client_socket.send('Welcome to python'.encode('utf-8'))
#4.关闭
client_socket.close()
print('发送完毕')