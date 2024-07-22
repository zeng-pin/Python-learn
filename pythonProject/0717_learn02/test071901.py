import random

elem=[]
for i in range(10):
    elem.append(random.randrange(1,101))
print(elem)
# print(max(elem))
elem.sort(reverse=True)
print(elem[0])

