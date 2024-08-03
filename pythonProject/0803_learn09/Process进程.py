from multiprocessing import Process
import os,time
def test():
    print(f'子进程的PIP: {os.getpid()},父进程:{os.getppid()}')
    time.sleep(1)
if __name__ == '__main__':
    print('主进程开始运行:')
    lst=[]
    for i in range(5):
        #创建子进程
        p=Process(target=test)#传入函数不加括号以参数形式传入
        #启动子进程
        p.start()
        #将启动的进出添加到列表中
        lst.append(p)
    #遍历列表的5个进程
    for item in lst:#item的类型是Process
        item.join()#通过item.join()  对主进程进行阻塞，实现先执行完子进程再执行主进程


    print('主进程执行结束')
