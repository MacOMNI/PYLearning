# -*- coding: utf-8 -*-
import re #正则
import requests #网络交互
import os #操作系统
from bs4 import BeautifulSoup #html解析
class SpiderPictures:
    #获取所有图片
    def get_allPictures(self,_url):
        #文件保存位置
        fileLocation = os.getcwd()
        html = requests.get(url=_url).text
        soup = BeautifulSoup(html,'html.parser')
        pic_urls = soup.find_all(target='_blank')

        i=0
        for url in pic_urls:
            print( url.decode() + '\n')

            pic = requests.get(url)
            # 如果文件夹不存在，则创建一个文件夹
            if not os.path.isdir():
                os.makedirs(fileLocation)

            fp = open(fileLocation + str(i) + '.jpg', 'wb')
            fp.write(pic.content)
            # print position+each
            fp.close()
            i += 1

        return
    def save_picture(self,_imgUrl):

        return

spider = SpiderPictures()
spider.get_allPictures('https://m.umei.cc/umplus/search.php?q=%E5%88%B6%E6%9C%8D&pagesize=24')