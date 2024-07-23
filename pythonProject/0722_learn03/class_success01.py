class FatherA:
    def __init__(self,name):
        self.name=name

    def showA(self):
        print('A的方法')
class FatherB:
    def __init__(self,age):
        self.age=age

    def showB(self):
        print('B的方法')

class Son(FatherA,FatherB):
    def __init__(self,name,age,gender):
        FatherA.__init__(self,name)#此时要使用FatherA.__init__,而不是super.__init__,去明确父类继承
        FatherB.__init__(self,age)
        self.gender=gender

    def showB(self):   #继承父类方法重写
        print('子类Son重新后的父类方法showB')


son1=Son(name='ppp',age=19,gender='man')
print(son1.name,son1.age,son1.gender)
son1.showA()
son1.showB()