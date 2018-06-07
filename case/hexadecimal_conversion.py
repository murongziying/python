#! /usr/bin/python3
# author:linuxc
# date:2018.6.7
# application:python十进制转二进制、八进制、十六进制
# 获取一个十进制的数字
dec = int(input("输入数字："))

print("十进制数为：{0}".format(dec))
print("转换为二进制为：{0}".format(bin(dec)))
print("转换为八进制为：{0}".format(oct(dec)))
print("转换为十六进制：{0}".format(hex(dec)))

