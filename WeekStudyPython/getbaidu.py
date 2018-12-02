# /usr/bin/python
# codeing=utf-8
import requests
res=requests.get("http://www.baidu.com")
savefile=open("test.html","w")
savefile.write(res.content)
savefile.close()