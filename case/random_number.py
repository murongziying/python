#! /usr/bin/python3
# author:linuxc
# date:2018.5.27
# application:random number
import random
# 用random.randint(0,9)方法获取0-9的随机数
answer = random.randint(0,9)
guess = int(input("Please guess the number i want in my heart:"))
if guess == answer:
    print("You got the right answer for the first time!")
else:
    if guess > answer:
        print("It's too big!")
    else:
        print("It's too small!")
while answer != guess:
    guess = int(input("Wrong,Please retry:"))
    if guess < answer:
        print("It's too small!")
    elif guess > answer:
        print("It's too big!")
    else:
        print("Amazing")
print("Game Over ^_^")
