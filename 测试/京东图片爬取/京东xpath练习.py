# -*- encoding: utf-8 -*-
# @ModuleName: 花瓣采集网xpath练习
# @Function: PyCharm
# @Author: Haishuiyu
# @Time: 2021-09-07 14:53

import requests,os,urllib
from lxml import etree
from urllib import request as ur

headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'
}

params = {'keyword': '华为手机',
        'enc': 'utf-8',
        'suggest': '2.def.0.base',
        'wq': '华为手',
        'pvid': '509fa5dfd0c649b0913ae4bdece473ce'}

savepath = 'C:/Users/haishuiyu/PycharmProjects/pythonProject'
url_list = []

def crawl():
        url1 = 'https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&enc=utf-8&suggest=2.def.0.base&wq=%E5%8D%8E%E4%B8%BA%E6%89%8B&pvid=509fa5dfd0c649b0913ae4bdece473ce'
        res = requests.get(url1,headers=headers)
        resp = res.text
        html = etree.HTML(resp)
        pic_list = html.xpath('//*[@id="J_goodsList"]/ul')
        for pic in pic_list:
                picture = pic.xpath('.//li//img/@data-lazy-img')
                for i in picture:
                        pic_url = i.replace('//','')
                        pic_urls = pic_url.replace('/n7','/n0')
                        url = 'http://'+pic_urls
                        url_list.append(url)
                        print(url)
        return url_list


def Download():
        opener = ur.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36')]
        ur.install_opener(opener)
        isExists = os.path.exists(savepath+'京东华为手机图片')
        if not isExists:
                print('文件夹创建成功')
                os.makedirs(savepath+'京东华为手机图片')
        else:
                print('创建失败文件夹已存在')
        print('下载中......')
        # for x,i in zip(range(len(url_list)),url_list):
        #         with open('{0}.jpg'.format(x),'ab') as f:
        #                 f.write(requests.get(i,headers=headers).content)
        for i,x in zip(url_list,range(len(url_list))):
                ur.urlretrieve(i,savepath+'京东华为手机图片/{}.jpg'.format(str(0+x)))
        print('本次一共下载{}张图片'.format(len(url_list)))

crawl()
Download()
