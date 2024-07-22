def get_find(s,lst):
    for item in lst:
        if s==item:
            return True
    return False


context=input('请输入文本: ')
find_contest=input('请输入要查找内容: ')
result=get_find(find_contest,context)

print('存在' if result else '不存在')


