dict_tic={
    '1':'kk',
    '2':'ss',
    '3':'pp',
    '4':'oo'
}

for i in dict_tic.keys():
    print(i,end='\t')
    for j in dict_tic.get(i):
        print(j,end='')
    print(end='\t\n')

n=input('enter your choice:')
if not n in dict_tic: print('have not the ticket')
else:print('your ticket {key} is {value}'.format(key=n,value=dict_tic[n]))