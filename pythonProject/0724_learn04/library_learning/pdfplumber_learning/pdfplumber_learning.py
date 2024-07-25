import pdfplumber
#打开pdf文件
with pdfplumber.open('xxxx.pdf') as pdf:
    for i in pdf.pages:#遍历页
        print(i.extract_text())#提取内容
        print(f'第{i.page_number}页')
