print(bool('kkk'))
print(bool('0'))
print(bool('1'))
print(str(1))
print(int('000'))
print(float('1.11'))

s='hhh'
print(list(s))
print(tuple(s))
print(set(s))

#数学函数
a=10;b=20;c=-10
print('绝对值',abs(a),abs(c))
print('商和余数',divmod(11,5))
print(max(11,22,33),max('hello'))
print(sum((11,22,33)))
print('幂乘',pow(2,3))
print('四舍五入保留小数',round(3.66),round(3.15),round(-3.6),round(-3.1))

print(format(3.14,'20'))
print(format('hello','20'))
print(format('hello','*<20'))
print(format('hello','*>20'))
print(format('hello','*^20'))
print(eval('10+50'))#eval为去''
