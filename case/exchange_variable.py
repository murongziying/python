#! /usr/bin/python3
# author:linuxc
# date:2018.5.27
# application:exchange variable交换变量
# method one
a = int(input("please input number a : "))
b = int(input("please input number b : "))
temp = a
a = b
b = temp
print("changed a = %d"%a)
print("changed b = %d"%b)


x = float(input("please input number x : "))
y = float(input("please input number y : "))
x,y = y,x
print("change x = {0:0.1f}".format(x))
print("change y = {0:0.2f}".format(y))
