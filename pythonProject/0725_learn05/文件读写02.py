def my_write(file_place,content):#写入常规文本
    file=open(file_place,'a',encoding='utf-8')
    file.write(content)
    file.write('\n')
    file.close()

def my_write_list(file,lst):#写入一个列表
    file=open(file,'a',encoding='utf-8')
    file.writelines(lst)
    file.close()

def file_empty(file_place):#清除文件内容
    file=open(file_place,'a',encoding='utf-8')
    file.truncate(0)
    file.close()


if __name__ == '__main__':
    file_empty('b.txt')
    my_write('b.txt','aaaaa')
    my_write('b.txt','bbbb')
    my_write('b.txt',input('输入追加文字： '))
    lst=['name\t','age\t','score\n','ppp\t','22\t','100\n']
    my_write_list('b.txt',lst)