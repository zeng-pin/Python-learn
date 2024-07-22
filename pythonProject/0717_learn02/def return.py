def calc(a,b):
    c=a+b
    return c
a=5
b=6
sum=calc(a,b)
print(f'{sum}')


sum=calc(calc(a,b),7)
print(sum)



def get_sum(num):#返回多个值的函数
    s=0
    odd_sum=0
    even_sum=0
    for i in range(1,num+1):
        s+=i
        if i%2==0:even_sum+=i
        else:odd_sum+=i

    return odd_sum,even_sum,s

result=get_sum(15)
a,b,c=result #按顺序输出
print(a,b,c)