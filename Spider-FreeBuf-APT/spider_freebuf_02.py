import requests, json

#抓取数据
page = 1
url = "https://search.freebuf.com/search/find/?year=0&articleType=0&time=0&tabType=1&content=APT&page=" + str(page)
r = requests.get(url)
print(r.text)

#解析Json
state = json.loads(r.text)
print(state)
for n in state:
    print(n)

#获取对应的值
status = state.get('status')
data = state.get('data')
print(status)
print(data)
for n in data:
    print(n)

#获取内容
content = state.get('data').get('list')
for dic_json in content:
    for key in dic_json:
        #获取key
        print("key:", key)
        #获取value
        text = str(dic_json[key])
        #删除多余空格 换行 加粗字段<em>APT</em>
        text = text.replace(' ','')
        text = text.replace('\n','')
        text = text.replace('<em>','')
        text = text.replace('</em>','')
        print("value:", text)
    else:
        print("") #换行
