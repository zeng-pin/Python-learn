import threading
from threading import Thread,Lock
import time
ticket=50
Lock_obj=Lock()
#使用Lock避免在线程中数据同时被调用,上锁LOCK.acquire,解锁LOCK.release
#使用Lock时使用尽量少的代码组块
def sale_ticket():
    global ticket
    for i in range(20):
        Lock_obj.acquire()#上锁
        if ticket>0:
            print(f'{threading.current_thread().name}正在出售第{ticket}张票')
            ticket-=1
        time.sleep(0.5)
        Lock_obj.release()#解锁

if __name__ == '__main__':
    for i in range(3):
        t=Thread(target=sale_ticket)
        t.start()


##使用完Lock后线程会以此进行而不是同时进行，以确保数据传输可靠性
##同时使用Lock会使运行速度降低