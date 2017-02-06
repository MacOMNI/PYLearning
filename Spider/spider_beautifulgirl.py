# -*- coding: utf-8 -*-
import re #正则
import requests #网络交互
import os #操作系统
from bs4 import BeautifulSoup #html解析
class SpiderPictures:
    #获取所有图片
    def get_allPictures(self,_url):
        #文件保存位置
        fileLocation = os.getcwd()+'/beautifulgirl'
        html = requests.get(url=_url).text
        soup = BeautifulSoup(html,'html.parser')
        pic_urls = soup.find_all(target='_blank')
        i = 1
        for url in pic_urls:

            pic = requests.get(url.img['src'])
            # 如果文件夹不存在，则创建一个文件夹
            if not os.path.isdir(fileLocation):
                os.makedirs(fileLocation)
                print(fileLocation)

            fp = open(fileLocation +'/'+'Beautifulgirl'+str(i) + '.jpg', 'wb')
            fp.write(pic.content)
            # print position+each
            fp.close()
            i += 1

        return


spider = SpiderPictures()
spider.get_allPictures('https://m.umei.cc/umplus/search.php?q=%E5%88%B6%E6%9C%8D&pagesize=24')