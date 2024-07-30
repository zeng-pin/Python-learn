import  json

lst=[
    {'name':'aaa','age':'18','score':80},
    {'name':'bbb','age':'20','score':90},
    {'name':'ccc','age':'22','score':100}
]

s=json.dumps(lst,ensure_ascii=False,indent=2) #ensure_ascii为了是防止中文乱码，indent增加数据缩进
print(type(s),s)#json会将数据转换为字符串

lst2=json.loads(s)#将s重新编码为Lst
print(type(lst2),lst2)

#也可以编码到文件


with open('student_json.txt','w',encoding='utf-8') as file:
    json.dump(lst,file,ensure_ascii=False,indent=2)

with open('student_json.txt','r',encoding='utf-8') as file:
    lst3=json.load(file)
    print(lst3)
#或者使用json.dumps和json.loads
# with open('student_json.txt', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(lst, ensure_ascii=False, indent=2))
#
# with open('student_json.txt', 'r', encoding='utf-8') as file:
#     lst3 = json.loads(file.read())
#     print(lst3)
