#导入socket
import socket
#1.创建socket对象
socket_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2.绑定主机和IP部门
socket_obj.bind(('127.0.0.1',8888))
#3.设置最大连接数
socket_obj.listen(5)
print('--服务器启动成功--')
#4.等待客户端TCP链接
client_socket,client_addr=socket_obj.accept()#accept获得的为元组,需要进行系列解包赋值

#5.接受数据放置到info
info=client_socket.recv(1024).decode('utf-8')
while info!='bye':
    if info!='':
        print('接收到的数据是: ',info)
    #准备发送数据
    data=input('请输入需要发送的数据: ')
    #服务器回复数据
    client_socket.send(data.encode('utf-8'))
    print('发送成功')
    if data=='bye':
        break
    info=client_socket.recv(1024).decode('utf-8')

#6.关闭socket对象
client_socket.close()
socket_obj.close()