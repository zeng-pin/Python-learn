lst=[]
while 1:
    n=input('输入商品数量：')
    if n<'0' or n>'9': print('not a num !');continue;
    break;

for i in range(int(n)):
    goods=input("input your goods :")
    lst.append(goods)

choice=[]
while 1:
    flag=0
    num=input('input your choice :')
    if num=='q':break;
    for item in lst:
        if item[0:4]==num: choice.append(item);flag=1;break;
    if not flag:print("not find item");
choice.reverse()
for i in choice:
    print(i)




