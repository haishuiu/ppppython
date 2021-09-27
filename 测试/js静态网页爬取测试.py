# -*- encoding: utf-8 -*-
# @ModuleName: js静态网页爬取测试
# @Function: PyCharm
# @Author: Haishuiyu
# @Time: 2021-09-13 16:29

import requests,os,time
from urllib import request as ur

save_path = 'C:/Users/haishuiyu/PycharmProjects/pythonProject'
headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'
}
picture_list = []
picture_name_list = []
def crwaler():

    for i in range(1300,1350):
        url = 'https://bird.ioliu.cn/v2?url=http%3A%2F%2Fwallpaper.apc.360.cn%2Findex.php%3Fc%3DWallPaper%26start%3D{}%26count%3D12%26from%3D360chrome%26a%3DgetAppsByCategory%26cid%3D26'.format(i)
        session = requests.session()
        cookies = session.cookies
        res = requests.get(url,headers=headers,cookies=cookies)
        print(res.status_code)
        res_js = res.json()
        pic_list = res_js['data']
        try:
            for pic_url in pic_list:
                img_1600_900 = pic_url['img_1600_900']
                picture_list.append(img_1600_900)
                img_name = pic_url['utag']
                picture_name_list.append(img_name)
                print(picture_list,picture_name_list)
        except:
            print('出现未知错误已跳过')
    return picture_list,picture_name_list

def download():
    isExists = os.path.exists(save_path+'NTE牛人网')
    if not isExists:
        print('文件夹创建成功')
        os.makedirs(save_path+'NTE牛人网')
    for x,y in zip(picture_list,picture_name_list):
        ur.urlretrieve(x,save_path+'NTE牛人网'+'/{}.jpg'.format(y))
        print('下载中......')
    print('一共下载{}张图片'.format(len(picture_list)))

if __name__ == "__main__":
    start = time.time()
    crwaler()
    download()
    end = time.time()
    print(end-start)
    # sum_url = len(12)
    # print('下载完成,一共下载{}张图片'.format(sum_url))



