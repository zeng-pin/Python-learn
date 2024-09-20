import threading
from threading import Thread
import time
def exm():
    for i in range(3):
        time.sleep(1)
        print(f'线程{threading.current_thread().name}正在执行{i}')


if __name__ == '__main__':
    start=time.time()
    print('主线程开始执行')
    lst=[Thread(target=exm) for i in range(2)]#列表生成式生成两个线程
    for item in lst:
        item.start()
        item.join()
    print(type(lst),type(lst[0]))
    print('共耗时:',time.time()-start)