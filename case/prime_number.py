#! /usr/bin/python3
# author:linuxc
# date:2018.6.3
# application:whether the judgment is a prime number判断一个一个数是否为质数
num = int(input("please input a ingeter number: "))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print("{0}是质数".format(num))
            print(i,'乘于',num//i,'是',num)
            break
    else:
        print(num,"是质数")
else:
    print(num,'不是质数')
