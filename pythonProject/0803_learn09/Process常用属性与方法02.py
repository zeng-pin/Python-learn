from multiprocessing import Process
import os,time

def process1(name):
    print(f'子进程PID:{os.getppid()},父进程PID:{os.getppid()}')
    time.sleep(2)

def process2(name):
    print(f'子进程PID:{os.getpid()},父进程PID{os.getppid()}')
    time.sleep(2)

if __name__ == '__main__':
    print('子进程开始运行')
    for i in range(2):
        #创建第一个子进程
        p1=Process()#若未给定参数，不会执行函数中代码，而是会调用Process中的run()方法
        #创建第二个子进程
        p2=Process(target=process2,args=('bbb',))#若指定参数，便会调用指定参数执行
        p1.start()
        p2.start()
        p1.terminate()#使用terminate直接终止进程的进行
        p2.terminate()
    print('主进程结束')