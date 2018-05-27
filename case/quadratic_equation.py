#! /usr/bin/python3
# author:linuxc
# date:2018.5.26
# application:quadratic equation
import cmath
a = float(input("please input a number:"))
b = float(input("please input b number:"))
c = float(input("please input c number:"))
d = (b ** 2) - (4 * a * c)
qe1 = (-b + cmath.sqrt(d)) / (2 * a)
qe2 = (-b - cmath.sqrt(d)) / (2 * a)
if d < 0:
    print("无实数解，但是有两个复数解")
    print("solution1 = {0} = {1:0.1f}+{2:0.1f}j, solution2 = {3} = {4:0.3f}+{5:0.3f}j".format(qe1, qe1.real, qe1.imag, qe2,qe2.real, qe2.imag))
elif d == 0:
    print("有两个相同实数解")
    print("solution1 = {0} = {1:0.1f}+{2:0.1f}j, solution2 = {3} = {4:0.3f}+{5:0.3f}j".format(qe1, qe1.real, qe1.imag, qe2,qe2.real, qe2.imag))
else:
    print("有两个不同的实数解")
    print("solution1 = {0} = {1:0.1f}+{2:0.1f}j, solution2 = {3} = {4:0.3f}+{5:0.3f}j".format(qe1, qe1.real, qe1.imag, qe2,qe2.real, qe2.imag))

# noly real number solution
A = float(input('please input real number A:'))
B = float(input('please input real number B:'))
C = float(input('please input real number C:'))
D = (B ** 2) - (4 * A * C )
sol1 = (-B + cmath.sqrt(D)) / (2 * A)
sol2 = (-B - cmath.sqrt(D)) / (2 * A)
if D < 0:
    print("no real number solution")
elif D == 0:
    print("have two squal real number solution")
    print("sol1 = {0}, sol2 = {1}".format(sol1, sol2))
else:
    print("have two not squal real number solution")
    print("sol1 = {0}, sol2 = {1}".format(sol1, sol2))
