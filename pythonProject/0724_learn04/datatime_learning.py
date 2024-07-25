from  datetime import datetime
dt=datetime.now()
print('现在是: ',dt)
#datatime是一个类可以手动设置
dt2=datetime(2028,8,8,14,5,11)
print(dt2)

#比较dt与dt2时间可以直接比较
if dt<dt2:print(f'{dt} 小于 {dt2}')
else:print(f'{dt} 大于等于 {dt2}')

#datatime类型与字符串转化
nowdt=datetime.now()
nowdt_str=nowdt.strftime('%Y/%m/%d %H:%M:%S')
print(type(nowdt),nowdt)
print(type(nowdt_str),nowdt_str)

#同理字符串转datatime类型

str_time='2028年8月8日 20点8分'
dt3=datetime.strptime(str_time,'%Y年%m月%d日 %H点%M分')
print(type(str_time),str_time)
print(type(dt3),dt3)
