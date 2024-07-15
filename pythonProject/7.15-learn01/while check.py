num=input('input a number:')
l=len(num);flag=0;
for i in num:
    if i<'0' or i>'9':flag=1;
if flag==0:
    for i in num:
            l-=1;a=int(i);b=a*(10**l);
            print(b,end=" ");
else: print("it is not a number");