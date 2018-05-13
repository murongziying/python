#!/usr/bin/python3
import keyword
print(keyword.kwlist)

if True:
	print("True")
else:
	print("False")


if True:
	print("Answer")
	print("True")
else:
	print("Answer")
	print("False")
	print("请输入用户名:")
	print("请输入密码:")
	print("请重试:")
# 空格和tab不能混合使用，否则无法编译。
# 多行语句表示法
'''
total = item_one + \
	item_two + \
	item_three
total = {'item_one','item_two',
}

total = ['item_three','item_four']
total = ('item_five','item_six')
'''
# 数据类型
# int(整数)
# bool(布尔)
# float(浮点数)
# complex(复数)
# String(字符串)
str='Ubuntu'

print(str)						#输出字符串
print(str[0:-1])				#输出第一个到倒数第二个之间的数字
print(str[0])					#输出字符串第一个数字
print(str[2:5])					#输出字符串第三个到第六个之间的数字
print(str[2:])					#输出第三个之后所有的数字
print(str * 2)					#str字符串乘以2
print(str + '你好')				#str字符串+“你好”
print("-----------------")
print('hello\nubuntu')			#\n表示转义字符，换行
print(r'hello\nubuntu')			#在字符串前面添加一个r，表示原始字符，不会发生转义

#等待用户输入
input('\n\n请按下enter键退出：')

import sys; x = 'ubuntu'; sys.stdout.write(x + '\n')


x='6'
y='8'
# 换行输出
print(x)
print(y)
print('-------这是分界线--------')
# 不换行输出
print(x,end=" ")
print(y,end=" ")

# import与from...import
# 在python用import或者from...import来
"""
将整个模块（somemodule）导入,格式为：import somemodule
从某个模块中导入某个函数，格式为：from somemodule import somefunction
从某个模块中导入多个函数，格式为：from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中全部函数导入，格式为：from somemodule import *
"""
import sys
print('===========python import mode============')
print('命令行参数为：')
for i in sys.argv:
	print(i)
print('\n python 路径为',sys.path)

from sys import argv,path   #导入特定成员

print('==========python from import==============')
print('path:',path)#因为导入path成员，所以此处引用是不需要加sys.path

print("--------这是分界线-------")
print('这是基本运算符')
a = 2+5
b = 9-3
c = 9/5
d = 7%3
e = 3*4
print(a,b,c,d,e)

