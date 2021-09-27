# -*- encoding: utf-8 -*-
# @ModuleName: img下载测试
# @Function: PyCharm
# @Author: Haishuiyu
# @Time: 2021-08-30 19:54
from bs4 import BeautifulSoup
import requests,re,os
import urllib.request as ur
from urllib import request

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'}
url_list = []
savepath = 'C:/Users/haishuiyu/PycharmProjects/pythonProject'

def crwaler():
    print('正在获取图片URL......')
    for i in range(5):
        url = 'https://mm.enterdesk.com/dongmanmeinv/'+str(i+1)+'.html'
        res = requests.get(url,headers=headers)
        # soup = BeautifulSoup(res.text,'html.parser')
        # list = soup.find(class_='egeli_pic_m center').find_all('div',class_='egeli_pic_li')
        # for img in list:
        #     try:
        #         src = img.find('img')['src']
        #         print(src)
        #     except:
        #         pass
        soup = res.content.decode()
        img_list = re.findall(r'https://up.enterdesk.com/edpic_360_360/(.*[0-9].*|[a-z].*|[0-9].*)"',soup)
        for x in img_list:
            url_list.append(x)
    return url_list


def download():
    isExists = os.path.exists(savepath+'动漫图片')
    if not isExists:
        print('文件夹创建成功')
        os.makedirs(savepath+'动漫图片')
    else:
        print('文件夹创建失败,已存在')
    for i in url_list:
        # ur.urlretrieve('https://up.enterdesk.com/edpic_360_360/'+str(i),i.replace('/',''))
        ur.urlretrieve('https://up.enterdesk.com/edpic_360_360/'+str(i),savepath+'动漫图片'+'/'+i.replace('/',''))
        print('正在下载中...')
    print('下载完成一共下载'+str(len(url_list))+'张图片！')

crwaler()
download()
