#导入自定义my_info
import my_info
print(my_info.name)

#将my_info重命名为a
import my_info as a
a.info()

#单独导入 my_info 中的函数
from my_info import name
print(name)

#通配符 * 导入所有信息
from my_info import *
print(name)
my_info.info()#打点调用或者不打点调用都可以
info()
#同时导入多模块使用,间隔
import time,math,random

#在包中的模块导入，包被导入init文件会自动调用
import package_learning.package01 as xx
xx.info()






