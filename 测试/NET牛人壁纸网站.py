# -*- encoding: utf-8 -*-
# @ModuleName: NET牛人壁纸网站
# @Function: PyCharm
# @Author: Haishuiyu
# @Time: 2021-09-03 21:17
import requests,re
import urllib.request
from lxml import etree
headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'
}

# def crawler():
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/'
res = requests.get(url,headers=headers)
resp = res.text
html = etree.HTML(resp)
# pics = html.xpath('//div[@calss="container-fluid"]')
pic = html.xpath('//*[@id="comments"]/ol')
print(type(pic))
# print(pic)
for p in pic:
        a = p.xpath('.//li//div[@class="comment-content"]/p/text()')
        print(a)