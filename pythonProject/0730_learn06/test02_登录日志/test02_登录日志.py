import json
from  datetime import datetime
# user=[
#     {'账号':'aaa','密码':'111','登录日志':''},
#     {'账号':'bbb','密码':'222','登录日志':''},
#     {'账号':'ccc','密码':'333','登录日志':''}
# ]
# with open('user_content.txt', 'w+',encoding='utf-8') as file:
#     json.dump(user,file,ensure_ascii=False,indent=2)

def login_cheak(name, password, file_place):
    flag0=0;flag1=0
    with open(file_place, 'r',encoding='utf-8') as file:
        lst = json.load(file)
    for item in lst:
        if item.get('账号')==name:
            flag0 = 1
            if item.get('密码')==password:flag1=1;break;
    return flag0,flag1

def user_date(name,file_place):
    with open(file_place,'r',encoding='utf-8') as file:
        lst = json.load(file)
        user_login_time = datetime.now()
        user_login_time_str = user_login_time.strftime('%Y/%m/%d %H:%M:%S')
        for item in lst:
            if item.get('账号') == name:
                user_login_lasttime = item['登录日志']
                item['登录日志']=user_login_time_str
                break

    with open(file_place,'w',encoding='utf-8') as file:
        json.dump(lst, file, ensure_ascii=False, indent=2)
    return user_login_lasttime



if __name__ == '__main__':
    name=input('用户名: ')
    password=input('密码: ')
    flag0,flag1=login_cheak(name,password,'user_content.txt')
    tip_num='0'
    match (flag0,flag1):
        case (0,0):
            print('用户名输入错误')
        case (0,1):
            print('用户名输入错误')
        case (1,0):
            print('密码输入错误')
        case (1,1):
            tip_num=input('输入提示数字,执行相应操作: 0,退出; 1,查看登录日志:  ')
            if tip_num == '1':
                atime = user_date(name, 'user_content.txt')
                print('用户名: ', name, '用户上次登录时间: ', atime)
        case _:
            print('请输入正确格式')
    


