#! /usr/bin/python3
# author:linuxc
# date:2018.6.3
# application:列出给定数量的斐波那契数列的个数
# 用户输入
nterms = int(input("你需要几项斐波那契数列?"))
# 第一项和第二项
n1 = 0
n2 = 1
count = 2

# 判断输入的字符是否合法
if nterms <= 0:
    print("请输入一个正整数。")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1,",",n2,end=",")
    while count < nterms:
        nth = n1 + n2
        print(nth,end=",")
        # 更新值
        n1 = n2
        n2 = nth
        count += 1
