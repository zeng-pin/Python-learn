import openpyxl
import weather_learning as weather
html_text=weather.get_html()
lst=weather.parse_html(html_text)
#print(lst)

#创建工作簿
workbook=openpyxl.Workbook()
#在excel文件中创建工作表
sheet=workbook.create_sheet('景区天气.xlsx')
#向工作表中添加数据
for item in lst:
    sheet.append(item)#一次一行

workbook.save('景区天气.xlsx')


