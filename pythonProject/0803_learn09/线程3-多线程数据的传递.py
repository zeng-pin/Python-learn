import time
from threading import Thread
a=100
def add():
    print('加线程开始执行')
    global a
    a+=50
    print(f'a的值是:{a}')
    time.sleep(1)
    print('加线程执行结束')

def sub():
    print('减线程开始执行')
    global a
    a-=30
    print(f'a的值是:{a}')
    time.sleep(1)
    print('减线程运行结束')

if __name__ == '__main__':
    print('主线程执行')
    add=Thread(target=add)
    sub=Thread(target=sub)
    add.start()
    sub.start()
    add.join()
    sub.join()
    print('主线程执行完毕')


##多线程的全局变量a，是可以共享的
##这与进程之间的共享是相反的
##但线程的执行顺序无法确定