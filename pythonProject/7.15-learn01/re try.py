import re
pattern="a|d|f"
ss='ancdefghi'
s1=re.sub(pattern,'XX',ss)
print(s1)

s2='https://www.bilibili.com/video/BV1wD4y1o7AS'
pattern2='//|/'
s1=re.split(pattern2,s2)
print(s1)

