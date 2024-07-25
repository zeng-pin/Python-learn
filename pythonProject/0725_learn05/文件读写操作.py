def my_wirte():
    #打开文件
    file=open('a.txt','w',encoding='utf-8')
    #文件写入
    file.write('this is example')
    #文件关闭
    file.close()

def my_read():
    file=open('a.txt','r',encoding='utf-8')
    s=file.read()
    print(type(s),s)
    file.close()

if __name__ == '__main__':
    my_wirte()
    my_read()