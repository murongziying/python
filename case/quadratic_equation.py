#! /usr/bin/python3
# author:linuxc
# date:2018.5.26
# application:二次方程求解
import cmath
import math
a = float(input("please input a number:"))
b = float(input("please input b number:"))
c = float(input("please input c number:"))
d = (b ** 2) - (4 * a * c)
qe1 = (-b + cmath.sqrt(d)) / (2 * a)
qe2 = (-b - cmath.sqrt(d)) / (2 * a)
if d < 0:
    print("无实数解，但是有两个复数解")
    print("{0} = {1:0.3f}+{2:0.3f}, {3} = {4:0.3f}+{5:0.3f}".format(qe1, qe1.real, qe1.imag, qe2, qe2.real, qe2.imag))
    print("有两个相同实数解")
    print("{0} = {1:0.3f}+{2:0.3f}, {3} = {4:0.3f}+{5:0.3f}".format(qe1, qe1.real, qe1.imag, qe2, qe2.real, qe2.imag))
else:
    print("有两个不同的实数解")
    print("{0} = {1:0.3f}+{2:0.3f}, {3} = {4:0.3f}+{5:0.3f}".format(qe1, qe1.real, qe1.imag, qe2, qe2.real, qe2.imag))
