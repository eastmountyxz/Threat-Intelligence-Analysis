import csv
import requests, json

#----------------------------------------------定义CSV文件----------------------------------------------
c = open("FreeBuf-APT-all.csv", "a+", newline = '',encoding = 'gb18030')      #写文件
writer = csv.writer(c)
#url、imgUrl、title、content、time、type、name、userUrl、moneyFlag、coin、identity
writer.writerow(['序号','URL','imgRul','标题','内容简介','发布时间','类型','作者姓名','作者URL','MoeyFlag', 'coin', 'identity'])



#-----------------------------------------------抓取数据----------------------------------------------
page = 1
while page<=174:
    url = "https://search.freebuf.com/search/find/?year=0&articleType=0&time=0&tabType=1&content=APT&page=" + str(page)
    r = requests.get(url)
    print(url)

    #解析Json
    state = json.loads(r.text)
    print(state)

    #获取对应的值
    status = state.get('status')
    data = state.get('data')

    #获取内容
    content = state.get('data').get('list')
    no = 1
    for dic_json in content:
        tlist = []
        tlist.append(str(no))
        for key in dic_json:
            #获取key
            #print("key:", key)
            
            #获取value
            text = str(dic_json[key])
            #删除多余空格 换行 加粗字段<em>APT</em>
            text = text.replace(' ','')
            text = text.replace('\n','')
            text = text.replace('<em>','')
            text = text.replace('</em>','')
            #print("value:", text)
            
            #添加变量
            tlist.append(text)
        else:
            print("") #换行

        #写入文件
        writer.writerow(tlist)
        no = no + 1
        print("next content\n")
    #翻页
    page = page + 1
    
#结束循环
c.close()
print("OVER!!!")

