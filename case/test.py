#! /usr/bin/python3
year = int(input("please input a integer: "))
if (year % 4) == 0 and (year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year!")
else:
    print("It's not a leap year!")
