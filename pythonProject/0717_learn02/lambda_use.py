def sum(a,b):
    c=a+b
    return c

print(sum(10,20))

#匿名函数的使用
s=lambda a,b:a+b
print(s(11,22))

lst=[10,20,30,40,50]
for i in range(len(lst)):
    result=lambda x:x[i]#根据索引取值
    print(result(lst),end=' ')
    print(f'\n')

#排序的匿名函数
score=[
    {'name':'aaa','score':98},
    {'name':'bbb','score':99},
    {'name':'ccc','score':100}
]

score.sort(key=lambda x:x.get('score'),reverse=True)

for i in range(len(score)):
    print(f"score.")
