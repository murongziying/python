#! /usr/bin/python3
# author:linuxc
# date:2018.6.7
# application:简单的计算器

def add(x, y):
    """
    加法
    """
    return x + y
def subtract(x, y):
    """
    减法
    """
    return x -y
def multiply(x, y):
    """
    乘法
    """
    return x * y
def divide(x, y):
    """
    除法
    """
    return x / y
# 选择运算符
print("运算选项:")
print("1.加法运算")
print("2.减法运算")
print("3.乘法运算")
print("4.除法运算")

choice = input("请输入选项(1/2/3/4):")

num1 = int(input("数字一："))
num2 = int(input("数字二："))

if choice == '1':
    print("两数和是:{0}".format(add(num1, num2)))
elif choice == '2':
    print("两数差是:{0}".format(subtract(num1, num2)))
elif choice == '3':
    print("两数积是:{0}".format(multiply(num1, num2)))
elif choice == '4':
    print("两数商是:{0}".format(divide(num1, num2)))
else:
    print("请输入1/2/3/4中任意一个数字！")
