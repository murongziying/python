#! /usr/bin/python3
# author:linuxc
# date:2018.5.28
# application:判断奇偶
def oddeven(n):
    if (n % 2) == 0:
        print('this number is even')
    else:
        print('this number is odd')

print(oddeven(int(input('please input a number:'))))
