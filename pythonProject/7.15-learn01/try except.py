# try:
#     num1=int(input('enter a int: '))
#     num2=int(input('enter another int: '))
#     result=num1/num2
# except ZeroDivisionError:
#     print('除数为0')
# except ValueError:
#     print("输入格式错误")
# except BaseException:
#     print("其他错误")
# else:
#     print(f'{num1}/{num2}={result:.2f}')
# finally:
#     print('-----程序结束-----')
#
#
# try:
#     gender=input('please enter your gender: ')
#     if gender!='man' and gender!='woman':
#         raise Exception('性别只能为man或woman')
#     else:print('your gender is',gender)
# except Exception as ddd:
#     print(ddd)
