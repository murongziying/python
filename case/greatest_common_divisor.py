#! /usr/bin/python3
# author:linuxc
# date:2018.6.7
# application:求两数的最大公约数
def hcf(x, y):
    """
    该函数返回两个数的最大公约数
    """
    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1,smaller + 1):
        if((x % i == 0)and(y % i == 0)):
            hcf = i

    return hcf



# 用户输入两个数字
num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))

hcf1 = hcf(num1, num2)

print("{0}和{1}最大的公约数是：{2}".format(num1, num2, hcf1))
