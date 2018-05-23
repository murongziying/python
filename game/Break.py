#! /usr/bin/python3
bingo = "python"
answer = input("我最喜欢的编程语言是什么：")
while True:
    if answer == bingo:
        break
    answer = input("不，这不是我喜欢的")
print("看来我们心有灵犀")
