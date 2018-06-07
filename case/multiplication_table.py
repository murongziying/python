#! /usr/bin/python3
# author:linuxc
# date:2018.6.5
# application:乘法表
for i in range(1,10):
    for j in range(1, i + 1):
        print('{0}x{1}={2}'.format(i,j,i * j),end=' ')
    print()
