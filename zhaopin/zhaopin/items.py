# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class ZhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class TencentItem(Item):
    name = Field()
    catalog = Field()
    workLocation = Field()
    recruitNumber = Field()
    detailLink = Field()
    publishTime = Field()



