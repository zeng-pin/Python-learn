import socket
#1.创建socket对象
client_socket=socket.socket()
#主机IP地址及端口确定
client_socket.connect(('127.0.0.1',8888))
print('-------连接已建立--------')
#向客户端发送数据
info=''
while info!='bye':
    send_data=input('请输入要发送的数据')
    client_socket.send(send_data.encode('utf-8'))
    print('发送成功')
    if send_data=='bye':
        break
    #接受数据赋值到info
    info=client_socket.recv(1024).decode('utf-8')
    print('收到服务器的响应数据:',info)

#关闭socket对象
client_socket.close()