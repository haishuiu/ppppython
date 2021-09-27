# -*- encoding: utf-8 -*-
# @ModuleName: 京东图片爬虫例子
# @Function: PyCharm
# @Author: Haishuiyu
# @Time: 2021-09-07 18:17
# -*- coding: utf-8 -*
import re
import os
import urllib
import urllib3
from urllib import request
from bs4 import BeautifulSoup
from twisted.python.compat import raw_input


def craw(url,page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    soup = BeautifulSoup(html1,'lxml')
    image_list = soup.select('#J_goodsList > ul > li > div > div.p-img > a > img')
    name_list = soup.select('#J_goodsList > ul > li > div > div.p-name > a > em')
    #pricelist=soup.select('#plist > ul > li > div > div.p-price > strong')
    #print pricelist
    path = "E:/{}/".format(str(goods))
    if not os.path.exists(path):
        os.mkdir(path)
    for image_url,name in zip(image_list,name_list):
        name = name.get_text()
        image_name = path + name+".jpg"
        img_url = "http:"+str(image_url.get('data-lazy-img'))
        if img_url == 'http:None':
            img_url = "http:" + str(image_url.get('src'))
        try:
            urllib.request.urlretrieve(img_url,filename=image_name)
        except:
            continue

'''
#J_goodsList > ul > li:nth-child(1) > div > div.p-img > a > img
#plist > ul > li:nth-child(1) > div > div.p-name.p-name-type3 > a > em
#plist > ul > li:nth-child(1) > div > div.p-price > strong:nth-child(1) > i
'''

if __name__ == "__main__":
    goods = raw_input('please input the goods you want:')
    pages = input('please input the pages you want:')
    count = 0.0
    for i in range(1,int(pages+'1'),2):
        url = "https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.def.0.T06&wq=diann&page={}".format(str(goods),str(i))
        craw(url,i)
        count += 1
        print('work completed {:.2f}%'.format(count/int(pages)*100))