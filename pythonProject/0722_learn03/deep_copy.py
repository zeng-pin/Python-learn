class CPU():
    pass

class Disk():
    pass

class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu=CPU()
disk=Disk()

com=Computer(cpu,disk)
com1=com#变量赋值，对象储存地址相同
print(com1,'\n',com,'\n')


import copy
com2=copy.copy(com)#浅拷贝，对象储存地址不同，子对象储存地点仍然为原有地址，源对象与拷贝对象会使用同一个子对象
print(com,'\n',com2,'\n')


com3=copy.deepcopy(com)
print(com,'\n',com3)#深拷贝，对象储存地址不同，子对象储存地点为一个新地址

