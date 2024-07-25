def my_read(filename):
    file=open(filename,'w+',encoding='utf-8')
    file.write('你好啊')#写入完成，文件的指针在最后
    file.seek(0)#将文件指针调整至最前面
    print(file.read())#读取全部
    print(file.read(2))#读取2个字符
    print(file.readline())#读取一行数据
    print(file.readline(2))#读取
    print(file.readlines())#读取全部


    file.close()

my_read('c.txt')