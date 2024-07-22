class Student:
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender

    #使用 @property 修饰器，修改方法，将方法转化为属性使用
    @property
    def gender(self):
        return self.__gender


    @gender.setter#通过setter去更改其尽可读性，修改为可修改
    def gender(self,value):
        if value != 'man' and value != 'woman':
            print('性别有误，设置为默认值man')
            self.__gender='man'
        else:
            self.__gender=value


stu=Student('ppp','woman')
print(stu.name,stu.gender)#可以通过修饰来访问__gender，但不可修改
                        #此处为取值操作调用的是gender(self)
stu.gender=input('请输入更改的性别: ') #此处调用直接使用stu.gender而不是stu.__gender
                #此处为赋值操作调用的是gender(self,value)
print(stu.name,stu.gender)