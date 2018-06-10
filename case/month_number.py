#! /usr/bin/python3
# author:linuxc
# date:2018.6.9
# application:计算每个月的天数
import calendar
year = int(input("输入年份："))
month = int(input("输入月份："))
if (year < 0) or (month < 0):
    print("请输入大于0的年月")
else:
    monthRange = calendar.monthrange(year, month)
    print(monthRange)
print("十二月份天数",calendar.mdays[12])
