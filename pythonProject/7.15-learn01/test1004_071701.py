import re

dict_name=[]
n=int(input())
for i in range(n):
    dict_name.append(input())

search=[]
for i in dict_name:
    search.append(i.split(' '))

def takenum(elem): return int(elem[2])
search.sort(key=takenum,reverse = True)

print(search[0][0],search[0][1])
print(search[n-1][0],search[n-1][1],end='')
