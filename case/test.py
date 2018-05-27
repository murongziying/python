#! /usr/bin/python3
import math
a = float(input("please input number a:"))
b = float(input("please input number b:"))
c = float(input("please input number c:"))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s -c))
print("this triangle area is: %f"%area)
