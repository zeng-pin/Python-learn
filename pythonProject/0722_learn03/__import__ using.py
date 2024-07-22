class Student():

    def __init__(self,name,age,gender):
        self._name=name #self._name是受保护，只能本类和子类访问
        self.__age=age #self.__age表示私有，只能类本身访问
        self.gender=gender #普通的实例属性，类的内部，外部，以及子类都可以访问

    def _fun1(self): # 受保护的
        print('子类本身可以访问')

    def __fun2(self): # 私有的
        print('只有定义可以访问')

    def show(self):
        self._fun1()
        self.__fun2()
        print(self._name)
        print(self.__age)

stu=Student('PPP',20,'man')
stu._fun1()
#此时self.__age不可引用

print(stu._Student__age)
stu._Student__fun2()
#可以通过以上方法访问私有属性__age和__fun2但不建议使用应该使用修饰器