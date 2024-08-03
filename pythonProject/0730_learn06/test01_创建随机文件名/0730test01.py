import random
lst_kinds=['水果','烟酒','粮油','肉蛋','蔬菜']
for i in range(1,4):
    sequence='{:0>4d}'.format(i)
    random_num=random.randint(0,68719476735)   #在前面补足0如'5'———>'0005'
    random_num_16= '{:0>9}'.format(hex(random_num).upper()[2:])
    random_kindnum=random.randint(0,4)
    random_kind=lst_kinds[random_kindnum]
    file_name=sequence+'_'+random_kind+'_'+random_num_16+'.txt'
    print(file_name)
    # with open(file_name,'w+') as file:
    #      file.write('')

