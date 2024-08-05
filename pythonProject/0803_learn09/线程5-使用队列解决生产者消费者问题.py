from queue import Queue
from threading import Thread
import time
class Producer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.queue=queue
    def run(self):
        for i in range(1,6):
            print(f'{self.name}将产品{i}放入队列')
            self.queue.put(i)
            time.sleep(1)
        print('生产者完成了所有数据的存放')
class Consumer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.queue=queue
    def run(self):
        for _ in range(5):
            value=self.queue.get()
            print(f'消费者数据{self.name}取出了{value}')

if __name__ == '__main__':
    #队列创建
    queue=Queue()
    #创建生产者进程
    p=Producer('Producer',queue)
    #创建消费者进程
    c=Consumer('Consumer',queue)

    #启动线程
    p.start()
    c.start()
    #阻塞
    p.join()
    c.join()
    print('主线程执行结束')


