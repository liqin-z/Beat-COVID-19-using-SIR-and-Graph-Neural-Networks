import json
import requests
response = requests.get('http://cxz.moe:1314/2019-nCoV/areas')
versionInfo = response.text
# versionInfo 是接口返回的 json 格式数据

versionInfoPython = json.loads(versionInfo)
# json.loads 将已编码的 JSON 字符串解码为 Python 对象
# print (versionInfoPython)

dataList = versionInfoPython.get('data')
print(dataList)

with open('data.json', 'w') as outfile:
    json.dump(dataList, outfile, ensure_ascii=False)
