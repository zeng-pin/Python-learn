from socket import socket,AF_INET,SOCK_DGRAM

send_socket=socket(AF_INET,SOCK_DGRAM)


while True:
    data=input('请输入数据,退出输入bye: ')
    if data=='bye': print('再见'); break

    ip_port=(('127.0.0.1',8888))
    send_socket.sendto(data.encode('utf-8'),ip_port)
    print('请等待客服回应')
    recv_data,addr=send_socket.recvfrom(1024)
    print('客服的回应是: ',recv_data.decode('utf-8'))

send_socket.close()