def try1(age,name):
    print('age is '+str(age))
    print('name is '+name,end='\n\n')

try1(age=18,name='111')
try1(18,'222')


#name 设置默认值
def try2(age=20,name='2220'):
    print('age is ' + str(age))
    print('name is ' + name, end='\n\n')

try2();
try2(22,'333')

#可变参数使用*数量可调节

def fun(*para):
    print(type(para))
    for item in para:
        print(item)
fun(10,20,30)
fun(10)
fun([11,12,13])
#在调用参数时加*可将列表解包作为独立元素，如
fun(*[11,22,33,44])

#个数可变的关键字参数,赋值形式
def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'-----',value)

fun2(name='abc',age=30,height=170)#关键字参数
d={'name':'abc','age':30,'height':170}
fun2(**d)#同理此处需要系列解包使用**

