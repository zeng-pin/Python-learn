class Person():
    pass
class Cat():
    pass
per=Person()
c=Cat()
print(type(c),type(per))


#局部变量
class Student:
    school='welcome'
    def __init__(self,xm,age):  #xm,age是方法的参数，为局部变量作用域为整个__init__方法
        self.name=xm   #xm为局部变量,将局部变量值xm赋值给实例属性self.name
        self.age=age   #tips:实例名称与局部变量名称可以相同

    def show(self):
        print(f'我叫:{self.name},今年{self.age}岁')#实例方法的使用

    #静态方法
    @staticmethod
    def sm():
        print('静态方法不能调用实例属性和实例方法')

    #类方法
    @classmethod
    def cm(cls):
        print('类方法也不能调用实例属性和实例方法')

#调用类,创建类的对象
stu=Student(xm='ppp',age='18')
print(f'学生姓名为{stu.name},年龄为{stu.age}')
#类属性直接使用类名去调用此处为stu.name,和stu,age没有括号()

print(f'{stu.show()}')
#实例方法，用对象名调用此处为stu.show(),有括号().

stu.sm()
stu.cm()
#类方法 @classmethod 和静态方法 @staticmethod ,都直接使用类名调用

stu1=Student('aaa',20)
stu2=Student('bbb',22)
stu3=Student('ccc',25)
stu4=Student('ddd',26)

print(type(stu1))

lst=[stu1,stu2,stu3,stu4]
for i in lst:
    print(f'姓名为{i.name}，年龄为{i.age}')
