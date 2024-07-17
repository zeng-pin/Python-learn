data={
    '0':'ling',
    '1':'yi',
    '2':'er',
    '3':'san',
    '4':'si',
    '5':'wu',
    '6':'liu',
    '7':'qi',
    '8':'ba',
    '9':'jiu',
}

number=input()
sum=0
for n in number:
    sum=sum+int(n)

out=''
for n in str(sum):
    out=out+data[n]+' '
print(out.rstrip(' '))
