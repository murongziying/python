#! /usr/bin/python3
import random
secret = random.randint(1,10)
print("这是一个数字游戏")
guess = int(input("请猜猜超超心里想的是什么数字："))
if guess == secret:
    print("你好厉害，一下子就猜中了")
else:
    if guess < secret:
        print("小了")
    else:
        print("大了")
while guess != secret:
    guess =int(input("哎呀猜错了哟，再试试："))
    if guess == secret:
        print("哇塞，你好棒啊！")
    elif guess > secret:
        print("大了")
    elif guess < secret:
        print("小了")
    else:
        print("哈哈，你猜不到了吧！")
print("游戏结束了哦！")
