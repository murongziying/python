#! /usr/bin/python3
# author:linuxc
# date:2018.5.28
# application:判断字符串是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
# 测试字符串和数字
print(is_number('fibonacci'))	# False
print(is_number('100'))			# True
print(is_number('3.14'))		# True
print(is_number('-6.28'))		# True
print(is_number('1e3'))			# True
print(is_number('is 123'))		# False

# 测试 Unicode
# 阿拉伯语  5
print(is_number('٥'))			# True
# 泰语 2
print(is_number('๒'))			# True
# 版权号
print(is_number('©'))			# False
# 中文数字
print(is_number('四'))			# True
