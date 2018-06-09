#! /usr/bin/python3
# author:linuxc
# date:2018.6.7
# application:ASCII码与字符串转换
# 输入一个字符
ch1 = input("请输入一个字符:")
# 输入一个ASCII码
a = int(input("请输入一个ASCII码："))
print("{0}字符的ASCII码是{1}".format(ch1,ord(ch1)))
print("{0}ASCII码代表的字符是{1}".format(a,chr(a)))
