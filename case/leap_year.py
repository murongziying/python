#! /usr/bin/python3
# author:linuxc
# date:2018.5.28
# application:判断是否是闰年
while True:
    try:
        year = int(input('please input a positive integer : '))
    except ValueError:
        print('This number is not a positive integer,please reinput: ')
        continue
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        print('This is leap year!')
    else:
        print('This is not leap year!')
    break
