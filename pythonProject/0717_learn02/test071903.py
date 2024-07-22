def isupalpha(a):
    alpha='';b=''
    for i in a:
        print(i)
        match i:
            case i.isupper:b=i.lower();alpha+=b
            case i.islower:b=i.upper(); alpha+=b
            case _:alpha+=i
        print(b)
    return alpha

string=input('please input a string: ')
x=isupalpha(string)
print('转换大小写后为',str(x))
