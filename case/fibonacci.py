#! /usr/bin/python3
# author:linuxc
# date:2018.5.27
# application:Fabonacci function
def fib(n):
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b,a+b
    print()
print(fib(int(input('please input a number:'))))
