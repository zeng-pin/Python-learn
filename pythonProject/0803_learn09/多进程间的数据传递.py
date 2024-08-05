from  multiprocessing import Process
a=100

def add():
    print('子进程1开始执行')
    global a #声明全局变量a
    a+=30
    print('a=',a)
    print('子进程1执行完毕')
def sub():
    print('子进程2开始执行')
    global a
    a-=50
    print('a=',a)
    print('子进程2执行完毕')

if __name__ == '__main__':
    #父进程
    print('父进程开始执行')
    print('a=',a)
    #创建add子进程
    p1=Process(target=add)
    p2=Process(target=sub)
    #开始运行
    p1.start()
    p2.start()
    #对子进程进行阻塞
    p1.join()
    p2.join()
    print('父进程执行完毕')
    print('a=',a)


###由上程序得知，父进程与子进程中的变量a，保持相互独立
###若要确保进程的变量a共享要使用队列
