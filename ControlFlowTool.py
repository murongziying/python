#! /usr/bin/env python3
a = 9
if a > 0:
    print("这是个正整数")
else: 
    print("这不是整数")
# Measure some strings
# 计算words列表中每个字符串的字符长度
print('计算每个字符串长度')
words = ['cat','window','defenestrate']
for w in words:
    print(w,len(w))
print("给字符排序")
a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i,a[i])
print("在第0个位置插入字符串大于6的字符")
for w in words[:]:  #Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0,w)
        print(words)
print("1到5的链表")
for i in range(5):
    print(i)
print("5到9的链表")
for j in range(5,10):
    print(j)
print("长度为10的链表中截取从0开始的这段长度的数值并以3为等差间距")
for x in range(0,10,3):
    print(x)
print("长度为-100的数值中，从-10到-100中以-30为间距截取相应数值")
for y in range(-10,-100,-30):
    print(y)
print("计算每个字符串的字符长度")
a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i,a[i])
#将a列表用链表的形式展现出来
print("判断一个数是否是质数")
for n in range(2,10):       #n=[2,3,4,5,6,7,8,9]
    for x in range(2,n):    #x=[null,2,2,3,2,3,4,2,3,4,5,2,3,4,5,6,2,3,4,5,6,7,2,3,4,5,6,7,8]
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n,'is a prime number')
print("============Demarcation line============")
for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number",num)
        continue
    print("Found an odd number",num)
print("============Demarcation line============")
def fib(n):     #write Fibonacci series up to n
#Print a Fibonacci series up to n.
    a,b = 0,1
    while a < n:
        print(a,end='  ')
        a,b = b,a+b
    print()
fib(100)
print("============Demarcation line============")
def fib2(n):#return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)    # see below
        a,b = b,a+b
    return result
f100 = fib2(100)
print(f100)
print("============Demarcation line============")
def ask_ok(prrmt, retries=4, complaint='Yes or no,please!'):
    while True:
        ok = input(promt)
        if ok in('y','ye','yes'):
            return True
        if ok in('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)
# 这个函数可以通过几种不同的方式调用：只给出必要的参数：ask_ok('Do you really want to quit?')
# 给出一个可选的参数：ask_ok('Ok to overwrite the file?',2)
# 或者给出所有的参数：ask_ok('OK to overwrite tht file?',2,'Come on,only yes or no!')
print("============Demarcation line============")
i = 5
def f(arg=i):
    print(arg)

i=6
f()
print("============Demarcation line============")
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
# 这种情况下默认值会被调用
print("============Demarcation line============")
def f(a, L=None):
    if L is None:
        L = []
        L.append(a)
        return L
print(f(1))
print(f(2))
print(f(3))
'''这种情况下默认值不会在后续调用中累积'''
print("============Demarcation line============")
def parrot(voltage,state='a stiff',action='voom',type='Norwegian Blue'):
    print("-- This parrot wouldn't",action,end=' ')
    print("if you put",voltage,"volts through it.")
    print("-- Lovely plumage,the",type)
    print("-- It's",state,"!")
parrot(1000)                                        #1 positional argument
parrot(voltage=1000)                                #1 keyword argument
parrot(voltage=1000000,action='VOOOOOM')            #2 keyword argument
parrot(action='VOOOOOM',voltage=1000000)            #2 keyword argument
parrot('a million','bereft of life','jump')         #3 positional arguments
parrot('a thousand',state='pushing up the daisies') #1 positional,1 keyword
'''
以下几种是调用是无效的：
parrot()                    # required argument missing
parrot(voltage=5.0,'dead')  # non-keyword argument after a keyword argument
parrot(110,voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese') # unknown keyword argument
'''
print("============Demarcation line============")
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind,"?")
    print("-- I'm sorry,we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw,":",keywords[kw])
cheeseshop("Limburger","It is very runny,sir.",
            "It's really very,VERY runny,sir.",
            shopkeeper="Michael Palin",
            client="John Cleese",
            sketch="Cheese Shop Sketch")
print("============Demarcation line============")
def write_multiple_items(file,separator, *args):
	file.write(separator.join(args))
def concat(*args, sep="/"):
	return sep.join(args)
concat("earth","mars","venus")
concat("earth","mars","venus",sep=".")
print("============Demarcation line============")
list(range(3,6))		# normal call with separate arguments
args = [3,6]
list(range(*args))		# call with arguments unpacked from a list
print("============Demarcation line============")
def parrot(voltage, state='a stiff', action='voom'):
	print("-- This parrot wouldn't", action,end=' ')
	print("if you put",voltage,"volts through it.",end=' ')
	print("E's", state,"!")
d = {"voltage":"four million","state":"bleedin' demised","action":"VOOM"}
parrot(**d)
print("============Demarcation line============")
def make_incrementor(n):
	return lambda x: x + n
f = make_incrementor(42)
f(0)
f(1)
print("============Demarcation line============")
pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
print("============Demarcation line============")
def my_function():
	"""
	Do nothing, but document it.

	No, really, it doesn't do anything.
	"""
	pass
print("============Demarcation line============")
print(my_function.__doc__)

def f(ham:str, eggs:str = 'eggs') -> str:
	print("Annotations:",f.__annotations__)
	print("Arguments:", ham, eggs)
	return ham + ' and ' + eggs
f('spam')