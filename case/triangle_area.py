#! /usr/bin/python3
# author:linuxc
# date:2018.5.27
# application:triangle area
import math
a = float(input("please input border length a: "))
b = float(input("please input border length b: "))
c = float(input("please input border length c: "))
s = (a + b + c) / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("this triangle area is: %f"%area)
