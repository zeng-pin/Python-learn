from datetime import datetime
from datetime import timedelta

#时间的差计算
delta1=datetime(2028,10,1) - datetime(2028,5,1)
print('delta1的数据类型是',type(delta1))
print(delta1)

td1=timedelta(10,500)
print('创建一个10天的timedelta对象: ',td1)





