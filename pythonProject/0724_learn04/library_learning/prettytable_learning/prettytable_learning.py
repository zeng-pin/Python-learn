import prettytable as pt
#显示座位
def show_ticket(row_num):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']

    for i in range(1,row_num+1):
        lst=[f'第{i}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    return tb
def order_ticket(row_num,row,column):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(1,row_num+1):
        if int(row)==i:
            lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(column)]='已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)





if __name__ == '__main__':
    tb=show_ticket(6)
    print(tb)
    while 1:
        try:
            choose_num=input('输入想要购买的位置(格式为1,2):')
            if choose_num=='q':break;
            row, column=choose_num.split(',')
            order_ticket(6,row,column)
        except BaseException:
            print("输入格式错误")