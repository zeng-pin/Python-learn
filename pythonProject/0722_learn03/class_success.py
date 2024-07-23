class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'{self.name},{self.age}')

#Student继承了Person类

# 子类继承父类
class Student(Person):
    def __init__(self,name,age,stuno):
        super().__init__(name,age)#使用super调用父类初始化方法
        self.stuno=stuno


class Doctor (Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department




stu1=Student('aaa',20,stuno='1001')
stu1.show()
print(stu1.stuno)

stu2=Doctor('bbb',22,department='China')
stu2.show()
print(stu2.department)
