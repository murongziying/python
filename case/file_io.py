#! /usr/bin/python3
# author:linuxc
# date:2018.6.9
# application:文件IO
# 写入文件
with open("test.txt","wt") as out_file:
    out_file.write("这是一段测试内容\n请查看！")

# 读取文件
with open("test.txt","rt") as in_file:
    text = in_file.read()
print(text)
