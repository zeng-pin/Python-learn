class Person:
    def show(self):
        print('humanxx')
class Cat():
    def show(self):
        print('catxx')
class Dog():
    def show(self):
        print('dogxx')

def fun(obj):
    obj.show()
    pass

per=Person()
cat=Cat()
dog=Dog()
#python的多态不需要重新定义，直接包含多态,可以动态决定对象方法
fun(per)
fun(cat)
fun(dog)
