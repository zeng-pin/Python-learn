
try:
    score=int(input('请输入分数: '))

    if score>=0 and score<=100:
        print("分数为:",score)
    else:
        raise Exception('分数不正确')

except ValueError:print('分数不正确',end='')
except Exception as wrong_num:
    print(wrong_num,end='')