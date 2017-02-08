# -*- coding: utf-8 -*-
import scrapy
import json
from ELEProject.ELEItems import ELEItem
class ELESpider(scrapy.Spider):
    name = 'elespider' #唯一标识，启动spider时 指定名称

    allowed_domains = ['elespider.org']
    #https://mainsite-restapi.ele.me/shopping/restaurants?latitude=39.92504&longitude=116.46007&offset=100&limit=20&extras[]=activities
    start_urls = [
        'https://mainsite-restapi.ele.me/shopping/restaurants?latitude=39.92504&longitude=116.46007&offset=0&limit=100&extras[]=activities'
    ]

    def parse(self, response):

        fp = open('ele' + '.json', 'wb')
        fp.write(response.body)
        fp.close()

        jresult = json.loads(response.body)
        items = []
        for itemjson in jresult:
            name = '未知'
            recent_order_num = '未知'
            average_cost = '未知'
            if 'name' in itemjson:
                name =  itemjson['name']
            if 'recent_order_num' in itemjson:
                recent_order_num = itemjson['recent_order_num']
            if 'average_cost' in itemjson:
                average_cost = itemjson['average_cost']

            item = ELEItem(name=name,recent_order_num=recent_order_num,average_cost=average_cost)
           # item = ELEItem()
            #item.name = scrapy.Field(dict(name=itemjson['name']))
           # item.average_cost = itemjson['average_cost']
           # item.recent_order_num = itemjson['recent_order_num']
            items.append(item)



        return items