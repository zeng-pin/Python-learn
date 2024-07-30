import os
with open('os_test.txt','w',encoding='utf-8') as file:
    file.write('aaabbbccc')
#删除文件
os.remove('./os_test.txt')
#重命名
#os.rename('./aa.txt','bb.txt')

#获取文件信息如时间
import time
def date_time(longtime):
    s=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(longtime))
    return s


#文件信息获取

info=os.stat('./信息获取实例.txt')
print(type(info))
print(info)
print('最后一次访问时间: ',date_time(info.st_atime))
print('文件大小是: ',info.st_size,'字节')
#启动文件
#os.startfile(r'文件路径')