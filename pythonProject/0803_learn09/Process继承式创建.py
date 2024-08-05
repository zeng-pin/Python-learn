from multiprocessing import Process
import os,time

#使用类进行继承
class SubProcess(Process):
    def __init__(self,name):
        super().__init__()#调用父类的初始化方法
        self.name=name

    def run(self):
        print(f'子进程的名称{self.name},PID：{os.getpid()},父进程的PID:{os.getppid()}')


if __name__ == '__main__':
    print('父进程开始执行')
    lst=[]
    for i in range(1,6):
        p1=SubProcess(f'这是第{i}个进程')#调用Process中的run但run被子类改写
        #启动进程
        p1.start()#此处子类SubProcess没有start方法,所以调用的是父类中的start方法
        lst.append(p1)

    for item in lst:
        item.join(2)
    print('父进程执行完毕')




