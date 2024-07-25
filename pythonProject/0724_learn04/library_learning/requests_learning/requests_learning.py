import requests
import re

url='http://www.weather.com.cn/weather1d/101010100.shtml'

resp=requests.get(url)
resp.encoding='utf-8'
#print(resp.text)

city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
print(city)
weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text)
print(weather)
wd=re.findall('<span class="wd">(.*)</span>',resp.text)
print(wd)
zs=re.findall('<span class="zs">(.*)</span>',resp.text)
print(zs)

lst=[]

for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d])
print(lst)


