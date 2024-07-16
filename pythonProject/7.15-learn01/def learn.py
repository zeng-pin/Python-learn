def addnum(vartuple):

    sum=0;
    for i in vartuple:
        sum=sum+int(i)
    return (sum);

b=[]
while 1:
    a=input('input num:')
    if a=='p': break;
    elif a<'0' or a>'9' : print("wrong num");continue;
    b.append(a)
    print(b)

print('sum is:',addnum(b));


