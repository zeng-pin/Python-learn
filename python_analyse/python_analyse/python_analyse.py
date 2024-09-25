def file_read(file,place):
    with open(file,'r',encoding='utf-8') as file:
        s=file.read()
        lst0=s.split('\n')
        lst=list(filter(lambda x:x!='',lst0))
        k=0
        for item in lst:
            k+=1
            if item==place : break

        lst01=lst[k:]
        return lst01

def file_write(filename,lst):
    with open(filename,'w',encoding='utf-8') as file_w:
        file_w.write('\n'.join(lst))

def clear_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            os.remove(file_path)

def insert_title(content,lst):
    lst.insert(0,content)
    return lst

if __name__ == '__main__':

    import os
    before_analyse_lst = os.listdir('./before_analyse')
    print(before_analyse_lst)

    for item in before_analyse_lst:
        filename_before='before_analyse/'+item
        lst = file_read(filename_before, 'Time/sec, Current/A')#查找内容输入
        item01=item[:-4]

        if item01[0]=='电': item01 = item01[5:]
        for j in range(len(item01)) :
            if item01[j] == '-': item01=item01[:-(len(item01)-j)];break;

        title='Time/sec,'+item01#标题输入
        lst=insert_title(title,lst)
        filename_after='after_analyse/'+item01+'.txt'
        file_write(filename_after, lst)
print('转换完成')
clear = input('输入0清空数据: ')
if clear == '0':
    clear_folder('./before_analyse')
    clear_folder('./after_analyse')
else:
    print('如需删除文件再次点击开始并输入0')



