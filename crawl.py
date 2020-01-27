<<<<<<< HEAD
import json
=======
#!/usr/bin/python
#-*- coding: utf-8 -*-
# 引用 json 库用于解析 json 对象
import json
# 使用 requests 库
>>>>>>> 6fba61b449b98d92bad8244d3401e72cc5158ffe
import requests
response = requests.get('http://cxz.moe:1314/2019-nCoV/areas')
versionInfo = response.text
# versionInfo 是接口返回的 json 格式数据
<<<<<<< HEAD

versionInfoPython = json.loads(versionInfo)
# json.loads 将已编码的 JSON 字符串解码为 Python 对象
# print (versionInfoPython)

dataList = versionInfoPython.get('data')
# print(dataList)

with open('data.json', 'w') as outfile:
    json.dump(dataList, outfile, ensure_ascii=False)
=======
# json.loads 将已编码的 JSON 字符串解码为 Python 对象
versionInfoPython = json.loads(versionInfo)
# print (versionInfoPython)
dataList = versionInfoPython.get('data')
#print(dataList)

with open('data.json', 'w') as outfile:
    json.dump(dataList, outfile,ensure_ascii=False)

import pandas as pd
import numpy as np

#data=pd.read_json(dataList)


>>>>>>> 6fba61b449b98d92bad8244d3401e72cc5158ffe
