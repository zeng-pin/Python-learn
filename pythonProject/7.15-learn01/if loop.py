import random

number=-1
rannumber=random.randrange(1,101)
print(rannumber)

while number != rannumber:
    number=eval(input("input your num:"))
    if number == rannumber: print("congratuations, the number is",number)
    elif number > rannumber: print("bigger than the num")
    else: print("smaller than the num")


