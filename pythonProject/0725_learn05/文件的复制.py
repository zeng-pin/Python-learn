def copy(src,new_path):
    file1=open(src,'rb')
    file2=open(new_path,'wb')
    s=file1.read()
    file2.write(s)

    file2.close()#按栈输出先打开的先关后打开的后关
    file1.close()

if __name__ == '__main__':
    src='c.txt'
    new_path='d.txt'
    copy(src,new_path)
