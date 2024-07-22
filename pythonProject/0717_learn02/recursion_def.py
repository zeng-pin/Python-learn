def fac(n):
    if n==1: return 1
    else: return n*fac(n-1)

print(fac(5))


def sum(n):
    if n==1 or  n==2: return 1
    else:
        return sum(n-1)+sum(n-2)

n=9;
print(sum(n))
for i in range(1,10):
    print(sum(i),end=' ')
