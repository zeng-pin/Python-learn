from multiprocessing import Pool
import os,time
def task(name):
    print(f'子进程的PID{os.getpid()},执行认为{name}')
    time.sleep(1)

if __name__ == '__main__':
    #主进程
    start=time.time()
    print('父进程执行')
    #创建进程池
    p=Pool(3)
    for i in range(10):
        #使用阻塞方式apply
        p.apply(func=task,args=(i,))

    p.close()
    p.join()
    print('子进程执行完毕，父进程结束')
    print(time.time()-start)


