def my_write():
    lst=['aaa','bbb','ccc','ddd','eee','fff']
    with open('number_test.csv','w',encoding='utf-8') as file:
        file.write(','.join(lst))

def my_read():
    with open('number_test.csv','r',encoding='utf-8') as file:
        s=file.read()
        lst=s.split(',')
        print(lst)

##二维数组的写入
def my_table_write():
    lst=[
        ['商品名','单价','采购数'],
        ['水杯','98.5','20'],
        ['鼠标','50.5','30'],
        ['纸杯','0.5','20']
    ]
    with open('table_test.csv','w',encoding='utf-8') as file:
        for i in lst:
            item=','.join(i)
            file.write(item)
            file.write('\n')##将二维转化为一维并分割

def my_table_read():
    data=[]
    with open('table_test.csv','r',encoding='utf-8') as file:
        lst=file.readlines()##读取一整行，用行数区分二维
        #print(type(lst),lst)
        for item in lst:
            item1=item[:len(item)-1]#将列表中的\n去除
            data.append(item1.split(','))
        print(data)



if __name__ == '__main__':
    # my_write()
    # my_read()
    my_table_write()
    my_table_read()
