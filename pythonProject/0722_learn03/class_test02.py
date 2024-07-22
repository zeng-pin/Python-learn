class Student:
    school='welcome'
    def __init__(self,xm,age):  #xm,age是方法的参数，为局部变量作用域为整个__init__方法
        self.name=xm   #xm为局部变量,将局部变量值xm赋值给实例属性self.name
        self.age=age   #tips:实例名称与局部变量名称可以相同

    def show(self):
        print(f'我叫:{self.name},今年{self.age}岁')#实例方法的使用


stu1 = Student('aaa', 20)
stu2 = Student('bbb', 22)
print(stu1.name,stu1.age)
print(stu2.name,stu2.age)
#动态绑定实例属性添加gender
stu2.gender='man'
print(stu2.gender)

#动态绑定方法此时为赋值不加()
def introduce():
    print('动态绑定方法')
    return '绑定成功'

stu2.fun=introduce()
print(stu2.fun)


