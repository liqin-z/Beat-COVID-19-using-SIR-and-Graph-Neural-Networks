
def getdata1():
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

    #with open('data.json', 'w') as outfile:
    #json.dump(dataList, outfile, ensure_ascii=False)


def getdata2():
    import json
    import requests
    response = requests.get('http://134.175.136.74:9081/api/province')
    versionInfo = response.text
    # versionInfo 是接口返回的 json 格式数据

    versionInfoPython = json.loads(versionInfo)
    # json.loads 将已编码的 JSON 字符串解码为 Python 对象
    # print (versionInfoPython)



def postdata():
    import json
    import requests
    headers = {'Content-Type': 'application/json'}
    data = {"province":"湖北省","all":''}
    data = json.dumps(data)
    r = requests.post("http://ncov.neeto.cn/api/", data=data,headers=headers)
    print(r.text)
    


if __name__ == '__main__':
    getdata2()

