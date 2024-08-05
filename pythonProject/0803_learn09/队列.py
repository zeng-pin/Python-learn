from multiprocessing import Queue
if __name__ == '__main__':
    #创建队列Queue(3)
    q=Queue(3)
    print('队列是否为空',q.empty())
    print('队列是否为满',q.full())
    #添加队列消息
    q.put('aaa')
    q.put('bbb')
    print('队列是否为空:',q.empty())#此时队列是不为空
    print('队列是否为满:',q.full())#此时队列是不为满

    q.put('ccc')
    print('队列是否为空:',q.empty())#此时队列是不为空
    print('队列是否为满:',q.full())#此时队列是为满
    print('队列中的信息个数: ',q.qsize())#使用qsize去确息个数

    #出队
    print(q.get())
    print('队列中的信息个数: ',q.qsize())
    #入队使用put_nowait，不管是否有空位直接进队，如果队列已满则会报错
    q.put_nowait('ddd')
    #若此时使用q.put()则不会报错，但程序会一直等待，直到队列产生空位

    print(type(q),q)
    #遍历队列元素
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())#依照先进先出出队

    print('队列中的个数',q.qsize())


