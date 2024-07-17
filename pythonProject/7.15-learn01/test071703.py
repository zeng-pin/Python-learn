import re

def judge(data):
    flag = 0
    i=0; j=0;k=0;m=len(data)

    for i in range(m):
        if data[i] =='P':break;
        j=j+1
        print(j)
    for i in range(m-j):
        if data[i+j] =='T':break;
        k = k + 1
        print(k)
        if (j*k==(m-j-k+1)) \
                and (data.count('P')==1 and data.count('T')==1) :
            flag=1

    if len(data) != (data.count('P')+data.count('A')+data.count('T')):
        flag=0
    return (flag)



n=int(input())
data=[]
for i in range(n-1):
    data=input()
    if judge(data): print('YES')
    else : print('NO')

data=input()
if judge(data): print('YES',end='')
else : print('NO',end='')
