#! /usr/bin/python3
# author:linuxc
# date:2018.6.3
# application:阶乘
n = int(input("please input a number: "))
factorial = 1
if n < 0:
    print("抱歉，负数没有阶乘")
elif n == 0:
    print("0的阶乘为1")
else:
    for i in range(1,n + 1):
        factorial = factorial * i
    print("n{0}的阶乘为{1}".format(n,factorial))
