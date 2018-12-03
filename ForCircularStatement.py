#! /usr/bin/env python3         
# 这一行一定不能忘记，不然运行容易出错，因为./找不到命令解释器
words = ['I', 'love', 'you']
print(words)
for w in words:
    print(w)

for w in words:
    print(w, len(w))

str1 = ['opera', 'chrome', 'firefox']
for n in str1:
    print(n, len(n))
# x = str(input("please enter a string:"))
# print("the length of this character is:")
# print(len(x))
for m in str1[:]:  # [:]这个不能忘记,不然无法正常进行循环运算
    if len(m) > 6:
        str1.insert(0, m)
print(str1)
str2 = ['hi', 'liu', 'chao']
for x in str2[:]:
    if len(x) <= 2:
        str2.insert(0, x)
print(str2)
