#! /usr/bin/python3
# author:linuxc
# date:2018.6.5
# application:判断数字是否为阿姆斯特朗数
# 获取用户输入的数字
num = int(input("请输入一个数字："))
# 初始化变量sum
sum1 = 0
# 指数
n = len(str(num))


# 检测
temp = num
while temp > 0:
    digit = temp % 10
    sum1 += digit ** n
    temp //= 10

# 输出结果

if num == sum1:
    print("{0}是阿姆斯特朗数".format(num))
else:
    print("{0}不是阿姆斯特朗数".format(num))
