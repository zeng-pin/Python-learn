import time
now=time.time()
print(now)

obj=time.localtime()
print(obj)
print('年份',obj.tm_year)
print('月',obj.tm_mon)
print('日',obj.tm_mday)

print(time.ctime())
print(time.strftime('%Y-%m-%d',time.localtime()))
print(time.strftime('%H:%M:%S',time.localtime()))

print('%B月份的名称:',time.strftime('%B',time.localtime()))
print('$A星期的名称:',time.strftime('%A',time.localtime()))


#输入时间转化为time格式
print(time.strptime('2008-08-08','%Y-%m-%d'))
#sleep函数
#time.sleep(2)