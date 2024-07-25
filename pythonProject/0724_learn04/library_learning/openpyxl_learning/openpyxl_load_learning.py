import openpyxl


workbook=openpyxl.load_workbook('景区天气.xlsx')
sheet=workbook['景区天气.xlsx']
lst=[]

for row in sheet.rows:#sheet.row相当于在一行中
    sublist=[]
    for cell in row:
        sublist.append(cell.value)
    lst.append(sublist)

for item in  lst:
    print(item)
