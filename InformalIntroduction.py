#!/usr/bin/env python3
# 第一行指定python解释器
# 这个是注释
print("Use Python as a calculator")
print("Number")
print("加减乘除取余运算")
print(2+2)					# 加法运算/addition operator
print(89-3*5)
print((50-4*5)/5)
print(7/3)					# 除法总是返回浮点数/division always returns a floating point number
print(11/4)					# 经典除法返回一个浮点数/classic division returns a float
print(11//4)				# 除法抛弃小数部分/floor division discards the fractional part
print(11%4)					# 取余数除法取剩下的整数部分/the % operator returns the remainder of the division 
print(2*4+3)				# result*divisor+remainder
print(2**10)				# 2的10次方/2 to the power of 10
print(10**2)				# 10的平方/10 squared
width = 10					# 宽度/width
height = 4*5				# 高度/height
area=width*height			# 面积/area
print("")
print("width=%d,height=%d,area=%d"%(width,height,area))
print("this is a %s,round rate %f,round area is %d"%("round",3.14159,9))
tax = 12.5/100
price = 100.50
amount = price * tax
print("amount=%d"%amount)
print("单双引号使用转义字符")
print("Strings")
print('"doesn\'t"')			# 单引号和双引号不能同时使用
print('doesn\'t')			# 单引号中使用单引号需要将想要显示出来的单引号进行转义
print("doesn't")			# 双引号中的单引号可以直接使用
print('"yes",he is.')		# 单引号中可以直接使用双引号
print("\"yes\",he is.")		# 双引号中使用双引号需要将想要显示出来的双引号进行转义

print('"Isn\'t,"she said.')	# \n换行
print('First line.\nSecond line.')
print('C:\some\name')		# \n换行
print(r'C:\some\name')		# \n转义字符前面加'r'可以取消转义效果

print("""
Usage:thingy [OPTIONS]
	-h
	-H hostname
""")
print(3*'Ubuntu'+'1804')	# 字符串可以进行加减乘运算
print('Ubuntu''Linux')
prefix = 'java'
prefix = 'python'			# 赋值，同一个变量，后面一个赋值会替换前一个值
print(prefix+'mangodb')		# 变量和常量之间需要用+连接
text = ('Put several strings within parentheses'
		'to have them joined together.')
print(text)					# 文本字符串

print("字符切片运算")
word = 'Python'
print('word=',word)
print('word[0]=',word[0])				# 字符串第一个字符
print('word[4]=',word[4])				# 字符串第五个字符
print('word[-1]=',word[-1])				# 字符串倒数第一个字符
print('word[-3]=',word[-3])				# 字符串倒数第三个字符
print('word[-6]=',word[-6])				# 字符串倒数第六个字符
print('word[0:2]=',word[0:2])			# 区间[1,3)内的整数，第一个字符到第三个字符之间，包含第一个字符，不包含第三个字符，也就是第一个和第二个字符。
#Py
print('word[2:5]=',word[2:5])			# 区间[3,6)内的整数，第三个字符到第六个字符之间，包含第三个字符，不包含第六个字符，也就是第三四五个字符
#tho
print('word[:2] + word[2:]=',word[:2] + word[2:])	# 区间[1,3)[3,6]内所有整数，从第一个到第三个，加上第三个到末尾，相当于word
print('word[:4] + word[4:]=',word[:4] + word[4:])	# 区间[1,5)[5,6]内所有整数，从第一个到第五个，加上第五个到末尾,相当于word

print('word[:2]=',word[:2])				# 区间[1,3)内所有整数，第一个到第三个之间
print('word[4:]=',word[4:])				# 区间[5,6]内所有整数，五个到末尾
print('word[-2:]=',word[-2:])			# 区间[-2,-1]内所有整数，倒数第二个到倒数第一个


# P  y  t  h  o  n
# 0  1  2  3  4  5
#-6 -5 -4 -3 -2 -1

print('word[4:42]=',word[4:42])			#'on'
print('word[42:]=',word[42:])			#空

print('"J" + word[1:]=','J' + word[1:])
print('word[:2] + "THON"=',word[:2] + 'THON')

print("len函数计算字符串字符个数")
s = 'linux       ubuntu'
print(len(s))				#用来计算s字符串中字符个数包含空格
# 结果s等于18

print("列表")

squares = [1,4,9,16,25]
print('squares=',squares)
print('squares[0]=',squares[0])			#squares列表中第一个字符
print('squares[-1]=',squares[-1])			#squares列表中倒数第一个字符
print('squares[-3:]=',squares[-3:])			#squares，区间[-3:-1]内所有整数，列表中倒数第一个到倒数第三个字符
print('squares[:]=',squares[:])			#squares列表中所有字符
squares1 = [36,49,64,81,100]
print('squares + squares1=',squares + squares1)	#squares+squares1中所有字符


cubes = [1,8,27,65,125]
print("修改之前的cubes")
print('cubes=',cubes)
print(4**3)
cubes[3] = 64
print("修改之后的cubes")
print('cubes=',cubes)

cubes.append(216)
cubes.append(7**3)
print("添加6的3次方和7的3次方之后的结果")
print('cubes=',cubes)



letters = ['a','b','c','d','e','f']
print('letters=',letters)
print("替换第三四五个字符")
letters[2:5] = ['C','D','E']
print(letters)
print("移除第三四五个字符")
letters[2:5] = []
print(letters)
print("清除所有字符")
letters[:] = []
print(letters)

a = ['a','b','c']
print('a=',a)				# ['a','b','c']
n = [1,2,3]
print('n',n)				# [1,2,3]
x = [a,n]
print('x=',x)				# [['a','b','c'][1,2,3]]
print('x[0]=',x[0])			# ['a','b','c']
print('x[0][1]=',x[0][1])	# b
print('x[1][1]=',x[1][1])	# 2

print("斐波那契数列")
a,b = 0,1
while b < 100:
	print(b)
	a,b = b,a+b
