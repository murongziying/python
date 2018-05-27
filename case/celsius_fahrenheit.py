#! /usr/bin/python3
# author:linuxc
# date:2018.5.27
# application:Mutual conversion of Fahrenheit temperature in Centgrade Temperature # celsius * 1.8 = fahrenheit  - 32
# 摄氏温度与华氏温度之间的转换
cel = float(input("please input a celsius number :"))
fah = cel * 1.8 + 32
print("that hahrenheit number is :%0.1f"%fah)

fah1 = float(input("please input a hahrenheit number :"))
cel1 = (fah1-32) / 1.8
print("that celsius number is :%0.1f"%cel1)
