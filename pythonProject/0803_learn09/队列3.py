from multiprocessing import Process,Queue
import time
a=100
def write_msg(q):
    global a
    if not q.full():
        for i in range(6):
            a-=10
            q.put(a)
            print('a入队的值:',a)

def read_msg(q):
    time.sleep(1)
    while not q.empty():
        print('出队a的值: ',q.get())

if __name__ == '__main__':
    print('父进程开始执行')
    q=Queue()#父进程创建队列，不指定参数则可接受数量无上限
    #创建入队与出队的子进程
    p1=Process(target=write_msg,args=(q,))
    p2=Process(target=read_msg,args=(q,))
    #启动子进程
    p1.start()
    p2.start()
    #阻塞子进程
    p1.join()
    p2.join()
    print('父进程执行完毕')

    