import os

print('当前路径: ',os.getcwd())
lst=os.listdir()
print('当前路径下的目录与文件:',lst)
print('特定路径下的目录与文件',os.listdir(r'G:\python-learn\pythonProject\0725_learn05'))
#创建文件目录

os.mkdir('创建文件夹实例')
#文件夹嵌套创建
os.makedirs('./嵌套文件夹创建实例/bb/cc')

#文件夹删除
os.rmdir('./创建文件夹实例')
#嵌套文件夹删除
os.removedirs('./嵌套文件夹创建实例/bb/cc')

#改变工作路径
#os.chdir('G:\python-learn\pythonProject\0730_learn06')

