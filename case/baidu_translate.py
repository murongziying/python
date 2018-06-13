#! /usr/bin/python3
# coding=utf8
# author:linuxc
# date:2018.6.10
# application:百度翻译接口调用

import http.client
import hashlib
import random
import json

appid = '20180610000174405'
secretKey = 'ZJlDS_4qhBJWxkKYF4NZ'

httpClient = None
myurl = '/api/trans/vip/translate'
q = 'apple'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid + q + str(salt) + secretKey
m1 = hashlib.md5()
m1.update(sign.encode(encoding='utf-8'))
sign = m1.hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + q + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign
print(myurl)

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    # response是HTTPResponse对象
    response = httpClient.getresponse()
    print(response)
    print(response.status, response.reason)
    zh = response.read()
    zh.decode('utf-8')
    str_zh = bytes.decode(zh)
    jsonData = json.loads(str_zh)
    print(jsonData)
    print("翻译结果为：" + jsonData['trans_result'][0]['dst'])
    trans_result = open("/home/liuchao/develop/python/case/test.txt", "w")
    trans_result.write(jsonData['trans_result'][0]['dst'])
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
