import requests
import re

def get_html():
    url = 'http://www.weather.com.cn/weather1d/101010100.shtml'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return resp.text

def parse_html(html_str):
    city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',html_str)
    weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',html_str)
    wd=re.findall('<span class="wd">(.*)</span>',html_str)
    zs=re.findall('<span class="zs">(.*)</span>',html_str)
    lst=[]
    for a,b,c,d in zip(city,weather,wd,zs):
        lst.append([a,b,c,d])
    return lst

