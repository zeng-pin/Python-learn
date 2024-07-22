#关键字局部变量转变为全局变量

s=100
print(s)
def cacl(x,y):
    global s #关键字局部变量转变为全局变量会影响全局
    s=300
    return s+x+y
print(cacl(10,20))
print(s)



