#! /usr/bin/python3
# author:linuxc
# date:2018.5.27
# application:test function
import cmath
a = float(input('please input a number:'))
b = float(input("please input b number:"))
c = float(input("please input c number:"))
d = (b ** 2) - (4 * a * c)
if d < 0:
    print('not real number solution')
elif d == 0:
    print('have two equal solution')
    sol1 = (-b + cmath.sqrt(d)) / (2 * a) 
    sol2 = (-b - cmath.sqrt(d)) / (2 * a)
    print('the first solution = {0},the second solution = {1}'.format(sol1, sol2))
else:
    print('have two not equal solution')
    sol1 = (-b + cmath.sqrt(d)) / (2 * a) 
    sol2 = (-b - cmath.sqrt(d)) / (2 * a)
    print('the first solution = {0},the second solution = {1}'.format(sol1, sol2))
