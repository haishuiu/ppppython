# -*- encoding: utf-8 -*-
# @ModuleName: 1234
# @Function: PyCharm
# @Author: Haishuiyu
# @Time: 2021-08-22 20:46

import re,requests,csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'}
for i in range(5):
    url = 'https://www.yuanjisong.com/consultant/allcity/python/page'+str(i+1)
    res = requests.get(url,headers=headers)
    con = res.content.decode()
    titles = re.findall(r'<div class="weui_panel_hd weui_panel_hd_adapt"><div class="topic_title">(.*?)</div><div class="topic_title">(.*?)</div><div class="topic_title">(.*?)</div></div>',con,re.S)
    a = re.findall(r'<span class="job_list_item_title ">技术能力：</span>(.?[^(\r\n)]+)<!--',con,re.S)
    prices = re.findall(r'<span class="rixin-text-jobs font-size-8 margin-r-2">(.*?)</span>',con,re.S)
    print(a)
    for title in titles:
        tit = title[0]+title[1]+title[2]
        for y,z in zip(a,prices):
            with open('12345.csv','a',newline='')as f:
                writer = csv.writer(f)
                writer.writerow([tit+'\n',str(y)+'\n',z+'元/小时\n\n'])





