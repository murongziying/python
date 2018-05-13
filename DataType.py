#!/usr/bin/python3

counter = 99		#整型
mites = 3.14		#浮点型
name = 'ubuntu'		#字符串
	

print(counter)
print(mites)
print(name)
print('-----这是分界线-------')
#多个变量赋值   a=b=c=1
#同时为多个变量赋值a,b,c=1,2,'a'
#python3中有六种标准数据类型：Number(数字),String(字符),List(列表),Tuple(元组),Sets(集合),Dictionary(字典)
#其中数字类型有包括：int(整数)，float(小数)，bool(布尔)，complex(复数)
#a = b = c = 1
#print(a,b,c)
a,b,c = 1,2,'liuchao'
print(a,b,c)
print('-------这是分界线---------')
a,b,c,d = 10,9.9,False,6+7j
print(type(a),type(b),type(c),type(d))
print('-----这是分界线-----')
a = 99
isinstance(a,bool)

