from  socket import socket,AF_INET,SOCK_DGRAM

recv_socket=socket(AF_INET,SOCK_DGRAM)
recv_socket.bind(('127.0.0.1',8888))

while True:
    recv_data,addr=recv_socket.recvfrom(1024)
    print('接受到数据: ',recv_data.decode('utf-8'))
    if recv_data.decode('utf-8')=='bye':print('用户退出聊天'); break
    data=input('回复客户: ')
    recv_socket.sendto(data.encode('utf-8'),addr)

recv_socket.close()



