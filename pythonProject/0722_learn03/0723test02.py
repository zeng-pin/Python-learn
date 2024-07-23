class Student:
    def __init__(self,name,age,gender,score):
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score

    def show(self):
        print(self.name,self.age,self.gender,self.score,end='')


n=eval(input('输入学生个数: '))
info_single=[]

for i in range(n):
    info=input()
    info_single=info.split('#')
    #print(info_single)
    stu=Student(info_single[0],info_single[1],info_single[2],info_single[3])
    stu.show()





