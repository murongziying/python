#! /usr/bin/python3
str1 = "python"
str2 = "UBUNTU"
str3 = "    I \tlove \tyou"
print(str1.capitalize())    # 首字母大写
print(str2.casefold())      # 所有字符改为小写
print(str1.center(20))      # 将字符串居中，并使用空格填充至长度为20的新字符串
print(str2.count("U", 0, 4))        # 返回"U"出现的次数，[0,4]是计算范围，默认空时，为全选
print(str2.endswith("N", 0, 4))     # 检查字符是否以"N"结束，范围[0,4]
print(str3.expandtabs(tabsize=20))  # 将字符串中tab字符或者\t转换成空格
print(str1.find("h",0 , 6))        # 在字符串中查找字符串，并回传索引值
