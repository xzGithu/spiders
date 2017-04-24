# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    salay = scrapy.Field()
    company = scrapy.Field()
    name = scrapy.Field()
    fankui = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()

