#! /usr/bin/env python3
a = ['wo','ai','tangrenli']
print(a)
a.append('1314')
print(a)
# list.append(x)
# 在列表的末尾插入元素x，等同于a[len(a):] = [x]
L = ['520','1314']
a.extend(L)
print(a)
# list.extend(L)
# 将L中的全部元素插入到列表的末尾，以扩展该列表，等同于a[len(a):] = L
a.insert(4,'tangrenli')
print(a)
# list.insert(i,x)
# 将一个元素插入到指定位置。第一个参数是待插入的元素的前一个元素的位置，所以a,insert(0,x)在列表的最前边插入，而a,insert(len(a),x)等同于a.append(x)
a.remove('1314')
print(a)
# 从列表中移除第一个值为x的元素。如果没有这样的元素的话，该命令将会报错。
a.pop(2)
print(a)
# list.pop(i)
# 从列表中移除i位置后一个元素
a.pop()
print(a)
# 移除列表中最后一个元素，并且返回列表
a.clear()
print(a)
# list.clear()
# 从列表中移除所有元素，等同于del a[:]
b = ['ubuntu','suse','redhat','centos']
num1 = b.index('redhat')
print(num1)
# list.index(x)
# 返回列表中第一个值为i的元素的序号，如果没有这样的元素，该命令将会报错
num2 = b.count('suse')
print(num2)
# list.count(x)
# 返回列表中x出现的次数
b.sort()
print(b)
# list.sort()
# 对该列表进行排序
b.reverse()
print(b)
# list.reverse()
# 翻转该列表中的元素
b.copy()
print(b)
# list.copy()
# 返回该列表的一个浅拷贝，等同于a[:]

print('列表方法综合使用')
c = [55.67,555,8,5345.7,555]
print(c.count(555),c.count(55.67),c.count('ubuntu'))
c.insert(3,-20)
print(c)
c.append(555)
print(c)
num1 = c.index(555)
print(num1)
c.remove(555)
print(c)
c.reverse()
print(c)
c.sort()
print(c)
c.pop(2)
print(c)
print('将列表作为栈来使用')
stack = [3,4,5]
stack.append(6)     # 追加6
stack.append(7)     # 追加7
print(stack)
stack.pop()         # 取出7
print(stack)
stack.pop()         # 取出6
print(stack)
stack.pop()         # 取出5
print(stack)
stack.pop()         # 取出4
print(stack)
stack.pop()         # 取出3
print(stack)
print('将列表作为队列来使用')
from collections import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
print("列表推导式")
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
"""
这里会创建一个x变量，并且这个变量会在循环结束后任然存在,所以可以考虑用其他的方式创建平方数列表
"""
squares = list(map(lambda x: x**2,range(10)))
print(squares)
squares = [x**2 for x in range(10)]
print(squares)
print([(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y])
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

print(combs)
vec = [-4,-2,0,2,4]
print(vec)
# create a new list with the values doubled
[x*2 for x in vec]
print(vec)
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
print(vec)
# apply a function to all the elements
[abs(x) for x in vec]
print(vec)
# call a method on each element
freshfruit = [' banana',' loganberry','passion fruit ']
[weapon.strip() for weapon in freshfruit]
print(freshfruit)
# create a list of 2-tuples like (number,square)
print([(x,x**2) for x in range(6)])
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3],[4,5,6],[7,8,9]]
print([num for elem in vec for num in elem])
from math import pi
print([str(round(pi, i)) for i in range(1,6)])
print("嵌套列表推导式")
matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],

]
print([[row[i] for row in matrix] for i in range(4)])
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
print(list(zip(*matrix)))
print("del语句")
a = [-1,1,66,25,333,333,1234.5]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a
print("元组和序列")
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# Tuples are immytable:
# Traceback (most recent call last):
v = ([1, 2, 3], [3, 2, 1])
print(v)
empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)
print("集合")
basket = {'apple', 'orange','apple','pear','orange','banana'}
print(basket)           # show that duplicates have been removed
print('orange' in basket)
print('carbgrass' in basket)
# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)                # unique letters in a
print(a - b)            # letters in a but not in b
print(a | b)            # letters in either a or b
print(a & b)            # letters in both a and b
print(a ^ b)            # letters in a or b but not both
print('字典')
tel = {'jack' : 4098,'sape' : 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)
print(dict([('sape', 4139), ('guido', 4127),('jack', 4098)]))
print({x: x**2 for x in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4098))
print("遍历的技巧")
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
for i in reversed(range(1, 10, 2)):
    print(i)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)
print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3] < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2) < (1, 2, -1))
print((1, 2, 3) == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
