import os
print('获取目录的绝对路径: ',os.path.abspath('./abc.txt'))
print('判断文件是否件存在: ',os.path.exists('abc.txt'))
print('判断文件是否件存在: ',os.path.exists('aaa.txt'))

print('分割文件名与后缀名:',os.path.splitext('abc.txt'))
print('提取文件名',os.path.basename('./abc.txt'))
print('提取路径',os.path.dirname(r'G:\python-learn\pythonProject\0730_learn06\abc.txt'))
print('判断路径是否有效: ',os.path.isdir(r'G:\python-learn\pythonProject\0730_learn06'))


