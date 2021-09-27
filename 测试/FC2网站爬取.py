# -*- encoding: utf-8 -*-
# @ModuleName: F2C网站爬取
# @Function: PyCharm
# @Author: Haishuiyu
# @Time: 2021-09-19 19:05
import requests,re
from bs4 import BeautifulSoup
headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'
}
list_str = []
list_tag = []
list_index = []
for i in range(10):
    url = 'http://23.224.9.244/2048/thread.php?fid-3-page-{}.html'.format(i+1)
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    htmls = soup.find('div',class_='t z').find_all(class_='tal')
    for url1 in htmls:
        try:
            fc2_div = url1.find('a',class_='subject')
            fc2_div1 = url1.find('a',class_='subject')['href']
            list_tag.append(fc2_div1)
            if fc2_div is not None:
                fc2_url = re.findall(r'.*FC2.*',fc2_div.text,re.S)
                list_str.append(fc2_url)
                if list_str.index(fc2_url) == 0:
                    pass
                else:
                    list_index.append(list_str.index(fc2_url))
        except:
            pass
for i in list_index:
    print(list_str[i],'http://23.224.9.244/2048/'+list_tag[i])







