import time
from datetime import datetime
from datetime import timedelta
if __name__ == '__main__':
    start_date = input('输入开始日期(20240725): ')
    gap_time = eval(input('输入间隔数: '))
    end_date = datetime(int(start_date[0:4]),int(start_date[4:6]),int(start_date[6:8])) + timedelta(gap_time)
    print(end_date)

