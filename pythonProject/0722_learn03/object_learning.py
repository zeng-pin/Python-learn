class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'{self.name} , {self.age}')

    #重写object中的str方法
    def __str__(self):
        return '重写str方法，得到per的属性值'
per=Person('AAA',18)
print(dir(per))
print(per)

