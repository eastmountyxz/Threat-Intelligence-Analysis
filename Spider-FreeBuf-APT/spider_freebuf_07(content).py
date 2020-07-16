import csv
import requests, json
from lxml import etree

#请求数据
page = 1
url = "https://www.freebuf.com/160412.html"
reponse = requests.get(url).text
print(reponse)

#解析网页
html_etree = etree.HTML(reponse)
print(html_etree)
title = html_etree.xpath('//*[@class="title"]/span[1]/text()')[0]       #网站标题
print(title.strip())
author = html_etree.xpath('//*[@class="author"]/text()')                #作者
print(author)
date = html_etree.xpath('//span[@class="date"]/text()')                 #发布时间
print(date)
review = html_etree.xpath('//span[@class="review"]/text()')             #阅读量
print(review)
comment = html_etree.xpath('//span[@class="comment-num"]/text()')       #评论量
print(review)
content = html_etree.xpath('//*[@class="content-detail"]/text()')       #正文内容
print(content)


#定义CSV文件
c = open("FreeBuf-APT-detail.csv", "a+", newline = '',encoding = 'gb18030')      #写文件
writer = csv.writer(c)  
writer.writerow(['序号','标题','作者','发布时间','阅读量','评论量','正文内容'])

#获取内容
no = 1
tlist = []
tlist.append(str(no))
tlist.append(title[0])
tlist.append(author[0])
tlist.append(date[0])
tlist.append(review)
tlist.append(comment[0])
tlist.append(content)

#写入文件
writer.writerow(tlist)

#结束循环
c.close()
print("OVER!!!")
