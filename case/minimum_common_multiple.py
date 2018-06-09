#! /usr/bin/python3
# author:linuxc
# date:2018.6.7
# application:最小公倍数
def lcm(x, y):
    # 获取最大数
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


# 获取用户输入
num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))
lcm1 = lcm(num1, num2)
print("{0}和{1}的最小公倍数是{2}".format(num1, num2, lcm1))
