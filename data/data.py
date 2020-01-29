import json
import requests

def getdata1():
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


def getdata2():
    url = 'http://ncov.neeto.cn/api/realtime'
    response = requests.get(url)
    versionInfo = response.text
    # versionInfo 是接口返回的 json 格式数据

    versionInfoPython = json.loads(versionInfo)
    # json.loads 将已编码的 JSON 字符串解码为 Python 对象
    # print (versionInfoPython)

    total = versionInfoPython.get('sumInfo')
    dataList = versionInfoPython.get('provinceInfo')
    print(total)
    print(dataList)
    with open('data_1_29_list.json', 'w') as outfile:
        json.dump(dataList, outfile, ensure_ascii=False)
    with open('data_1_29_total.json', 'w') as outfile:
        json.dump(total, outfile, ensure_ascii=False)

if __name__ == '__main__':
    getdata1()
    getdata2()
