from multiprocessing import Pool
import time,os

def task(name):
    print(f'子进程的PID{os.getpid()},执行的是{name}')
    time.sleep(1)

if __name__ == '__main__':
    #主进程
    start=time.time()
    print('父进程执行')
    #创建进程池，进程池的个数是3
    p=Pool(3)
    for i in range(10):
        #使用非阻塞方式apply_async
        p.apply_async(func=task,args=(i,))

    p.close()#p.close()通知进程池不再向其添加新任务，‌但已经提交的任务会继续执行。‌!!进程池必须要关闭，否则会报错.
    p.join()#p.join等待所有任务完成
    print('子进程执行完毕，父进程结束')
    print(time.time()-start)


###非阻塞模式允许程序在数据未完全准备好时继续执行其他任务，‌而不是等待数据传输完成
##可能会丢包，但速度快
