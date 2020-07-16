# coding=utf-8
import os
import csv
import time
import codecs
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver 
driver = webdriver.Chrome(chromedriver)

#访问网址
url = "https://www.freebuf.com/160412.html"
print(url)
driver.get(url)
time.sleep(2)

#网站标题
title = driver.find_element_by_xpath('//div[@class="title"]/span')
print(title.text)
#作者
author = driver.find_element_by_xpath('//div[@class="author-info"]/a[1]')
print(author.text)
#发布时间
date = driver.find_element_by_xpath('//div[@class="author-info"]/span[1]')
print(date.text)
#阅读量
review = driver.find_element_by_xpath('//div[@class="author-info"]/span[2]')
print(review.text)
#评论量
comment = driver.find_element_by_xpath('//div[@class="author-info"]/span[3]')
print(comment.text)
#正文内容
content = driver.find_elements_by_xpath('//div[@class="content-detail"]/div[1]/p')
result = ""
for n in content:
    print(n.text)
    result = result + str(n.text)

#定义CSV文件
c = open("FreeBuf-APT-detail.csv", "a+", newline = '',encoding = 'gb18030')      #写文件
writer = csv.writer(c)  
writer.writerow(['序号','标题','作者','发布时间','阅读量','评论量','正文内容'])

#获取内容
no = 1
tlist = []
tlist.append(str(no))
tlist.append(title.text)
tlist.append(author.text)
tlist.append(date.text)
tlist.append(review.text)
tlist.append(comment.text)
tlist.append(result)

#写入文件
writer.writerow(tlist)

#结束循环
c.close()
print("OVER!!!")
