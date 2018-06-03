#! /usr/bin/python3
# author:linuxc
# date:2018.5.26
# application:数字求和
# 方法一
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))
sum1 = num1 + num2
print("数字 {0:0.5f} 加上数字 {1:0.5f} 等于: {2:0.5f} ".format(num1, num2 ,sum1))
# 方法二
print('sum = %0.0f'%(float(input("第一个数字："))+float(input("第二个数字："))))
