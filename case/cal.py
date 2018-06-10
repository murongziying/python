#! /usr/bin/python3
# author:linuxc
# date:2018.6.7
# application:生成日历

# 导入日历模块
import calendar

# 输入指定年月

year = int(input("输入年份："))
month = int(input("输入月份："))


# 显示日历
print(calendar.month(year, month))
