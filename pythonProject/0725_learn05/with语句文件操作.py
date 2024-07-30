#使用 with open 语句可以不用file.close()关闭文件


def write_fun():
    with open('aa.txt','w',encoding='utf-8') as file:
        file.write('welcome')

def read_fun():
    with open('aa.txt','r',encoding='utf-8') as file:
        print(file.read())

def copy(src_file,target_file):
    with open(src_file,'r',encoding='utf-8') as file1:
        with open(target_file,'w',encoding='utf-8') as file2:
            file2.write(file1.read())

if __name__ == '__main__':
    write_fun()
    read_fun()
    copy('aa.txt','bb.txt')