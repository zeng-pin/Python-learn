lst1=['a','b','c','d']
lst2=[10,20,30,40]
post=dict(zip(lst1,lst2))
print(post)
#print(dict(post))
#d=dict(d=10,e=20)
#print(d)
print(post.get('b'))
print(post.get('p','未找到'))
for k in post.items():
    print(k,end=' ')
print('\n')

for key,value in post.items():
    print(key,'--',value,end=' ',sep='')