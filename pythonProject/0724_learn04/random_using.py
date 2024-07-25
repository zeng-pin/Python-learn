import random
random.seed(10)# 随机数种子
print(random.random())#[0,1)的值
print('-'*40)

print(random.randint(1,100))#[1,100]
print('-'*40)

for _ in range(1,10):
    print(random.randrange(1,10,3),end=' ')#[1,10）步长为3，即1,4,7
print('\n','-'*40)

print(random.uniform(1,100))#[a,b]随机小数
print('-'*40)

lst=[i for i in range(1,11)]
print(random.choice(lst))#在序列lst中随机挑选一个
print('-'*40)

print(lst)
random.shuffle(lst)#随机排序列表
print(lst)
