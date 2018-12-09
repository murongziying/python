# /usr/bin/env python3
# coding=utf-8
import requests

res = requests.get("http://www.baidu.com")
savefile = open("test.html", "wb+")
savefile.write(res.content)
savefile.close()
print (res.content)