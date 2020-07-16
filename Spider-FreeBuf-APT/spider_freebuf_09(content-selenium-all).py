# coding=utf-8
import os
import csv
import time
import codecs
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#文件读取
url_list = []
with open("FreeBuf-APT-all-08.csv", "r", encoding = 'gb18030') as f:
    #使用DictReader创建的reader是一个迭代器，遍历迭代器返回的数据是一个字典(有序字典)
    #返回的结果不包含行首的标题
    reader=csv.DictReader(f)
    for row in reader:
        url = row["URL"]
        url_list.append(url)
        #print("URL:", url)
        
#设置驱动
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver 
driver = webdriver.Chrome(chromedriver)

#定义CSV文件
c = open("FreeBuf-APT-detail.csv", "a+", newline = '',encoding = 'gb18030')      #写文件
writer = csv.writer(c)  
writer.writerow(['序号','标题','作者','作者URL','发布时间','阅读量','评论量','正文内容'])

#访问网址
page = 0
while page<len(url_list):
    print("页码:", page)
    url = url_list[page]
    print(url)
    driver.get(url)
    time.sleep(2)

    #网站标题
    title = driver.find_element_by_xpath('//div[@class="title"]/span')
    print(title.text)
    #作者
    author = driver.find_element_by_xpath('//div[@class="author-info"]/a[1]')
    author_url = author.get_attribute('href')
    print(author.text)
    print(author_url)
    #发布时间
    date = driver.find_element_by_xpath('//div[@class="author-info"]/span[1]')
    print(date.text)
    #阅读量
    review = driver.find_element_by_xpath('//div[@class="author-info"]/span[2]')
    print(review.text)
    #评论量 判断其是否存在
    comment = driver.find_elements_by_xpath('//div[@class="author-info"]/span[3]')
    #print(comment)
    if comment:
        com = comment[0].text
        print(com)
    else:
        com = 0
        print(com)
    #正文内容
    content = driver.find_elements_by_xpath('//div[@class="content-detail"]/div[1]/p')
    result = ""
    for n in content:
        #print(n.text)
        result = result + str(n.text)

    #获取内容
    tlist = []
    tlist.append(str(page+1))
    tlist.append(title.text)
    tlist.append(author.text)
    tlist.append(author_url)
    tlist.append(date.text)
    tlist.append(review.text)
    tlist.append(com)
    tlist.append(result)

    #写入文件
    writer.writerow(tlist)
    page = page + 1

#结束循环
c.close()
print("OVER!!!")
