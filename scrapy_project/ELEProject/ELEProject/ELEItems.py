import scrapy

class ELEItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    recent_order_num = scrapy.Field()
    average_cost = scrapy.Field()

    pass
