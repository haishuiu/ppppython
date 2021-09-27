# -*- encoding: utf-8 -*-
# @ModuleName: text问题
# @Function: PyCharm
# @Author: Haishuiyu
# @Time: 2021-09-21 17:17

import re,requests
from bs4 import BeautifulSoup

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/'

headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'
}

list1 = []
list2 = []
list3 = []

res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
htmls = soup.find(class_='widget widget_recent_entries').find('ul').find_all('li')
for urls in htmls:
    a = urls.find('a')
    list1.append(a)
    try:
        b = re.findall(r'.*[拥抱].*',a.text,re.S)
        list2.append(b)
        if list2.index(b) == 0:
            pass
        else:
            print(list2.index(b))
            c = list2.index(b)
            list3.append(c)
    except:
        pass
    # print(b)
print(list1)
print(list2)

real_url = list1[list3[0]]
print(real_url)

