#! /usr/bin/python3
# author:linuxc
# date:2018.5.26
# application:计算一个数的算术平方根
import cmath
# 方法一
num = float(input("please tall me you want number:"))
num_sqrt = num ** 0.5
print("the number {0} square root is: {1} ".format(num, num_sqrt))
# 方法一可以用于计算任意复数的算术平方根
# 方法二
a = float(input('please input number a:'))
b = a ** 0.5
print("a aquare root is: %f"%b)
# 方法二不能用于计算负数的算术平方根
# 方法三
num = float(input("please input a number:"))
num_sqrt = cmath.sqrt(num)
print(" {0} 的平方根是 {1:0.3f}+{2:0.3f}j".format(num, num_sqrt.real,num_sqrt.imag))
# 方法三可以用于计算任意复数算术平方根
