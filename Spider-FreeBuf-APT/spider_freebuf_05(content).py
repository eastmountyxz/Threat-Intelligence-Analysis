import csv
import requests, json
from lxml import etree

#请求数据
page = 1
url = "https://www.freebuf.com/160412.html"
reponse = requests.get(url).text
print(reponse)

#解析Json
html_etree = etree.HTML(reponse)
date = html_etree.xpath('//*[@class="author-info"]/span[1]/text()')
print("数组形式:",date)
print("字符形式:",date[0])


