#! /usr/bin/python3
x = int(input("请输入一个整数："))		           # Please enter an integer:
# 从键盘获取一个整数，且弹出提示信息
# 从键盘获取一个整数数据类型数值，如果输入非整数会提示报错信息：ValueError: invalid literal for int() with base 10: 'i'
if x < 0:										# 如果输入的X小于0,那么将0赋值给x。
    x = 0										# 将零赋值给x
    print("Please enter an positive integer")	# 负数变为零
elif x == 0:									# 否则如果x=0
    print("Zero")								# 那么就打印“Zero”
elif x == 1:									# 否则如果x=1
    print("One")								# 那么则打印“One”
else:											# 否则
	print("这是一个大于1的整数")								# 打印“more”