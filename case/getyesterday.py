#! /usr/bin/python3
# author:linuxc
# date:2018.6.10
# application:获取昨天的日期
import datetime
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    yesterday = today - oneday
    return yesterday


# 输出日期
print("昨天日期：",getYesterday())
print("今天日期：",datetime.date.today())
