#! /usr/bin/python3
# author:linuxc
# date:2018.6.3
# application:判断给定范围的质数
min1 = int(input("please input a minimum value: "))
max1 = int(input("please input a maximum value: "))
for num in range(min1,max1 + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
