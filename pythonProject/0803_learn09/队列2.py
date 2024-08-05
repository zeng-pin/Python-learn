from multiprocessing import Queue
if __name__ == '__main__':
    q=Queue(3)
    #向队列中添加元素
    q.put('aaa')
    q.put('bbb')
    q.put('ccc')
    #put中的block为是否进行等待,timeout是等待时间timeout=2为等待2秒，2秒后任没有空位则抛出错误
    q.put('ddd',block=True,timeout=2)
    
