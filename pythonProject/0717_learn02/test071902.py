def isnum(a):
    sum=0;num=[]
    for i in a:
        if i.isdigit(): sum+=int(i);num.append(int(i))

    return num,sum

string=input('please input a string: ')
x=isnum(string)
print('数组为',x[0],'\n','数字和为',x[1],sep='')
