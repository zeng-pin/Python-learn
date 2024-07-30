def my_read(filename):
    file=open(filename,'w+',encoding='utf-8')
    file.write('你好啊')#写入完成，文件的指针在最后
    file.seek(0)#将文件指针调整至最前面
    print(file.read())#从指针位置出发读取全部
    file.seek(0)
    print(file.read(2))#读取2个字符
    file.seek(0)
    print(file.readline())#读取一行数据
    file.seek(0)
    print(file.readline(2))#读取一行中的2个字符
    file.seek(0)
    print(file.readlines())#读取全部,一行为列表的一个元素，s为列表类型
    file.seek(0)

    file.seek(3)#将指针调整至第3个字节，即第一个字后面，因为在'utf-8'中一个中文占3个字节
    print(file.read())#从指针位置出发读取全部，读取了‘好啊

    file.close()

my_read('c.txt')