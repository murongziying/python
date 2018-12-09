# /usr/bin/env python3
# coding=utf-8
import test
mystr = "hello world linux and ubuntu and chrome"
a = mystr.find("linux")  # 第一次出现linux的索引号
print(a)

mylist = mystr.split(" ")
print(mylist)
for key in mylist:
    print(key)

test.printname("hello")


